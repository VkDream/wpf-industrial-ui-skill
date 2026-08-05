#!/usr/bin/env python3
"""Bounded heuristic inventory for .NET WPF UI source.

Requires Python 3.10 or newer and uses only the standard library. The script is
read-only. It does not build, run, render, or visually approve the application.
"""

from __future__ import annotations

import argparse
from collections import Counter
import fnmatch
import io
import json
import os
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET


MIN_PYTHON = (3, 10)
XAML_NS = "http://schemas.microsoft.com/winfx/2006/xaml/presentation"
X_NS = "http://schemas.microsoft.com/winfx/2006/xaml"
XKEY = f"{{{X_NS}}}Key"

DEFAULT_EXCLUDED_DIRS = {
    ".git",
    ".vs",
    ".idea",
    "bin",
    "obj",
    "node_modules",
    "packages",
    "artifacts",
    "testresults",
    "coverage",
    "backups",
    "backup",
    "evidence",
}

EVENT_ATTRS = {
    "Click",
    "Loaded",
    "Unloaded",
    "SelectionChanged",
    "TextChanged",
    "Checked",
    "Unchecked",
    "KeyDown",
    "KeyUp",
    "MouseDown",
    "MouseUp",
    "PreviewMouseDown",
    "PreviewMouseUp",
    "Drop",
    "DragOver",
    "Closing",
}

COLOR_RE = re.compile(r"#(?:[0-9A-Fa-f]{8}|[0-9A-Fa-f]{6}|[0-9A-Fa-f]{4}|[0-9A-Fa-f]{3})\b")
RESOURCE_RE = re.compile(r"\{(?:StaticResource|DynamicResource)\s+([^},\s]+)")
DOCTYPE_RE = re.compile(r"<!\s*(?:DOCTYPE|ENTITY)\b", re.IGNORECASE)
DISCLAIMER = (
    "Heuristic source inventory only: the application was not built, run, "
    "rendered, or accepted by the user."
)


def local_name(name: str) -> str:
    return name.rsplit("}", 1)[-1]


def add_finding(
    result: dict,
    severity: str,
    code: str,
    message: str,
    path: str | None = None,
    line: int | None = None,
) -> None:
    result[severity].append(
        {
            "code": code,
            "path": path,
            "line": line,
            "message": message,
        }
    )


def first_line(lines: list[str], *tokens: str) -> int | None:
    for number, line in enumerate(lines, start=1):
        if all(token in line for token in tokens):
            return number
    return None


def is_resource_path(path: Path) -> bool:
    parts = {part.casefold() for part in path.parts}
    return bool(parts & {"resources", "resource", "themes", "theme", "styles", "style", "assets"})


def matches_any(path: Path, patterns: list[str]) -> bool:
    normalized = path.as_posix().casefold()
    name = path.name.casefold()
    return any(
        fnmatch.fnmatch(normalized, pattern.casefold())
        or fnmatch.fnmatch(name, pattern.casefold())
        for pattern in patterns
    )


def should_exclude(relative: Path, custom_patterns: list[str]) -> bool:
    if any(part.casefold() in DEFAULT_EXCLUDED_DIRS for part in relative.parts):
        return True
    return matches_any(relative, custom_patterns)


def collect_source_files(
    root: Path,
    custom_excludes: list[str],
    includes: list[str],
    max_files: int,
) -> tuple[list[Path], list[str]]:
    files: list[Path] = []
    errors: list[str] = []

    def onerror(exc: OSError) -> None:
        errors.append(str(exc))

    for current, dirs, names in os.walk(root, topdown=True, followlinks=False, onerror=onerror):
        current_path = Path(current)
        kept_dirs: list[str] = []
        for directory in dirs:
            candidate = current_path / directory
            try:
                relative = candidate.relative_to(root)
            except ValueError:
                continue
            if not should_exclude(relative, custom_excludes):
                kept_dirs.append(directory)
        dirs[:] = kept_dirs

        for name in names:
            suffix = Path(name).suffix.casefold()
            if suffix not in {".xaml", ".csproj"}:
                continue
            candidate = current_path / name
            try:
                relative = candidate.relative_to(root)
            except ValueError:
                continue
            if should_exclude(relative, custom_excludes):
                continue
            if includes and not matches_any(relative, includes):
                continue
            files.append(candidate)
            if len(files) > max_files:
                raise RuntimeError(
                    f"File limit exceeded ({max_files}); narrow the root/include patterns "
                    "or raise --max-files deliberately."
                )

    files.sort(key=lambda path: path.as_posix().casefold())
    return files, errors


class ReadBudget:
    def __init__(self, max_file_bytes: int, max_total_bytes: int) -> None:
        self.max_file_bytes = max_file_bytes
        self.max_total_bytes = max_total_bytes
        self.total_bytes = 0

    def read_text(self, path: Path) -> tuple[str | None, str | None]:
        try:
            size = path.stat().st_size
        except OSError as exc:
            return None, f"Could not stat file: {exc}"
        if size > self.max_file_bytes:
            return None, f"File exceeds --max-file-bytes ({size} > {self.max_file_bytes})"
        if self.total_bytes + size > self.max_total_bytes:
            return None, (
                "Total read limit would be exceeded "
                f"({self.total_bytes + size} > {self.max_total_bytes})"
            )
        try:
            raw = path.read_text(encoding="utf-8-sig")
        except UnicodeDecodeError:
            return None, "File is not UTF-8/UTF-8-BOM"
        except OSError as exc:
            return None, f"Could not read file: {exc}"
        self.total_bytes += size
        return raw, None


def text_of_first(root: ET.Element, name: str) -> str | None:
    for element in root.iter():
        if local_name(element.tag) == name and element.text:
            return element.text.strip()
    return None


def namespace_values(raw: str) -> list[tuple[str, str]]:
    values: list[tuple[str, str]] = []
    for _event, item in ET.iterparse(io.StringIO(raw), events=("start-ns",)):
        prefix, value = item
        values.append((prefix or "(default)", value))
    return values


def duplicate_keys_by_scope(root: ET.Element) -> list[str]:
    duplicates: set[str] = set()
    for element in root.iter():
        name = local_name(element.tag)
        if name != "ResourceDictionary" and not name.endswith(".Resources"):
            continue
        keys = Counter(
            child.attrib[XKEY]
            for child in list(element)
            if child.attrib.get(XKEY)
        )
        duplicates.update(key for key, count in keys.items() if count > 1)
    return sorted(duplicates)


def colors_outside_resource_scopes(
    root: ET.Element,
    relative: Path,
    lines: list[str],
) -> list[tuple[int | None, str]]:
    if is_resource_path(relative):
        return []
    found: list[tuple[int | None, str]] = []

    def visit(element: ET.Element, in_resource_scope: bool) -> None:
        name = local_name(element.tag)
        scoped = in_resource_scope or name == "ResourceDictionary" or name.endswith(".Resources")
        if not scoped:
            values = list(element.attrib.values())
            if element.text:
                values.append(element.text)
            for value in values:
                if not isinstance(value, str):
                    continue
                for color in COLOR_RE.findall(value):
                    found.append((first_line(lines, color), color))
        for child in list(element):
            visit(child, scoped)

    visit(root, False)
    return found


def audit(root_path: Path, args: argparse.Namespace) -> dict:
    result = {
        "root": str(root_path),
        "projects": [],
        "xaml_files": 0,
        "errors": [],
        "warnings": [],
        "notes": [],
        "metrics": {},
        "disclaimer": DISCLAIMER,
    }

    try:
        source_files, walk_errors = collect_source_files(
            root_path,
            args.exclude,
            args.include,
            args.max_files,
        )
    except RuntimeError as exc:
        add_finding(result, "errors", "WPF001", str(exc))
        return result

    for message in walk_errors:
        add_finding(result, "warnings", "WPF002", f"Directory enumeration issue: {message}")

    budget = ReadBudget(args.max_file_bytes, args.max_total_bytes)
    csproj_files = [path for path in source_files if path.suffix.casefold() == ".csproj"]
    xaml_files = [path for path in source_files if path.suffix.casefold() == ".xaml"]
    wpf_projects = 0

    for project in csproj_files:
        relative = project.relative_to(root_path)
        raw, error = budget.read_text(project)
        if error:
            add_finding(result, "warnings", "WPF010", error, str(relative))
            continue
        assert raw is not None
        if DOCTYPE_RE.search(raw):
            add_finding(
                result,
                "errors",
                "WPF011",
                "DOCTYPE/ENTITY is not accepted by this local source scanner.",
                str(relative),
            )
            continue
        try:
            project_root = ET.fromstring(raw)
        except ET.ParseError as exc:
            add_finding(result, "errors", "WPF012", f"Malformed project XML: {exc}", str(relative))
            continue

        tfm = text_of_first(project_root, "TargetFramework")
        tfms = text_of_first(project_root, "TargetFrameworks")
        use_wpf = text_of_first(project_root, "UseWPF")
        is_wpf = (use_wpf or "").casefold() == "true"
        wpf_projects += int(is_wpf)
        project_info = {
            "path": str(relative),
            "target_framework": tfm,
            "target_frameworks": tfms,
            "use_wpf": use_wpf,
            "is_wpf": is_wpf,
        }
        result["projects"].append(project_info)
        targets = ";".join(value for value in (tfm, tfms) if value)
        if is_wpf and "net10.0-windows" not in targets:
            add_finding(
                result,
                "warnings",
                "WPF013",
                "WPF project is not visibly targeting net10.0-windows; imported or conditional MSBuild properties are not evaluated.",
                str(relative),
            )
        if not is_wpf and project.name.casefold().endswith("wpf.csproj"):
            add_finding(
                result,
                "warnings",
                "WPF014",
                "Project name suggests WPF but a literal UseWPF=true was not found; imported properties are not evaluated.",
                str(relative),
            )

    if not csproj_files:
        add_finding(result, "notes", "WPF015", "No .csproj files found in the bounded scan set.")
    elif wpf_projects == 0:
        add_finding(result, "notes", "WPF016", "No literal UseWPF=true was found; imported MSBuild properties are not evaluated.")

    all_defined_keys: Counter[str] = Counter()
    all_resource_refs: Counter[str] = Counter()
    first_resource_ref: dict[str, tuple[str, int | None]] = {}
    third_party_xmlns: Counter[str] = Counter()
    event_count = 0
    hardcoded_color_count = 0
    canvas_count = 0

    for xaml in xaml_files:
        relative = xaml.relative_to(root_path)
        raw, error = budget.read_text(xaml)
        if error:
            add_finding(result, "warnings", "WPF020", error, str(relative))
            continue
        assert raw is not None
        lines = raw.splitlines()
        if DOCTYPE_RE.search(raw):
            add_finding(
                result,
                "errors",
                "WPF021",
                "DOCTYPE/ENTITY is not accepted by this local source scanner.",
                str(relative),
            )
            continue
        try:
            namespaces = namespace_values(raw)
            root = ET.fromstring(raw)
        except ET.ParseError as exc:
            add_finding(result, "errors", "WPF022", f"Malformed XAML XML: {exc}", str(relative))
            continue

        if any("Microsoft.UI.Xaml" in value or value.startswith("using:Microsoft.UI") for _, value in namespaces):
            add_finding(result, "errors", "WPF023", "WinUI namespace detected in WPF XAML.", str(relative))

        for prefix, value in namespaces:
            if "assembly=" in value and not value.endswith("assembly=PresentationFramework"):
                third_party_xmlns[f"{prefix}={value}"] += 1

        if not root.tag.startswith("{" + XAML_NS + "}") and local_name(root.tag) != "ResourceDictionary":
            add_finding(
                result,
                "warnings",
                "WPF024",
                f"Unexpected root namespace for WPF XAML: {root.tag}",
                str(relative),
            )

        duplicates = duplicate_keys_by_scope(root)
        if duplicates:
            add_finding(
                result,
                "warnings",
                "WPF025",
                "Duplicate x:Key in the same parsed resource scope: " + ", ".join(duplicates),
                str(relative),
            )

        color_locations = colors_outside_resource_scopes(root, relative, lines)
        if color_locations:
            hardcoded_color_count += len(color_locations)
            sample = ", ".join(f"{value}@{line}" for line, value in color_locations[:5])
            add_finding(
                result,
                "warnings",
                "WPF026",
                f"Hardcoded color literal(s) outside a theme/resource path: {sample}",
                str(relative),
                color_locations[0][0],
            )

        for element in root.iter():
            key = element.attrib.get(XKEY)
            if key:
                all_defined_keys[key] += 1
            element_name = local_name(element.tag)
            if element_name == "Canvas":
                canvas_count += 1
            for attr_name, attr_value in element.attrib.items():
                attr_local = local_name(attr_name)
                if isinstance(attr_value, str) and "{x:Bind" in attr_value:
                    add_finding(
                        result,
                        "errors",
                        "WPF027",
                        "WinUI-style x:Bind detected in WPF XAML.",
                        str(relative),
                        first_line(lines, "x:Bind"),
                    )
                if attr_local == "CompileBindings":
                    add_finding(
                        result,
                        "warnings",
                        "WPF028",
                        "Non-standard WPF x:CompileBindings marker detected.",
                        str(relative),
                        first_line(lines, "CompileBindings"),
                    )
                if attr_local in EVENT_ATTRS and attr_value and "{Binding" not in attr_value:
                    event_count += 1
                    add_finding(
                        result,
                        "notes",
                        "WPF029",
                        f"XAML event handler {attr_local}=\"{attr_value}\"; confirm it is view-only behavior.",
                        str(relative),
                        first_line(lines, attr_local, attr_value),
                    )
                if isinstance(attr_value, str):
                    for resource_key in RESOURCE_RE.findall(attr_value):
                        normalized_key = resource_key.strip()
                        all_resource_refs[normalized_key] += 1
                        first_resource_ref.setdefault(
                            normalized_key,
                            (str(relative), first_line(lines, normalized_key)),
                        )

    ignored_resource_prefixes = (
        "{x:Type",
        "{x:Static",
        "x:Type",
        "x:Static",
        "System",
        "MaterialDesign",
        "MahApps",
        "Fluent",
    )
    unresolved = [
        (key, count)
        for key, count in all_resource_refs.items()
        if key not in all_defined_keys and not key.startswith(ignored_resource_prefixes)
    ]
    for key, count in sorted(unresolved, key=lambda item: (-item[1], item[0]))[:25]:
        path, line = first_resource_ref[key]
        add_finding(
            result,
            "notes",
            "WPF030",
            f"Resource key is not defined in the bounded scan set: {key} ({count} reference(s)); it may be framework, generated, package, or externally merged.",
            path,
            line,
        )

    if canvas_count:
        add_finding(
            result,
            "notes",
            "WPF031",
            f"Canvas elements found: {canvas_count}; review only ordinary-form uses, not drawing/camera/overlay surfaces.",
        )
    if third_party_xmlns:
        summary = "; ".join(f"{key} ({count})" for key, count in third_party_xmlns.most_common(20))
        add_finding(
            result,
            "notes",
            "WPF032",
            "Assembly-qualified XAML namespaces found; project-local namespaces are expected, external dependencies need authorization review: " + summary,
        )

    result["xaml_files"] = len(xaml_files)
    result["metrics"] = {
        "scanned_files": len(source_files),
        "read_bytes": budget.total_bytes,
        "csproj_files": len(csproj_files),
        "wpf_projects": wpf_projects,
        "xaml_files": len(xaml_files),
        "defined_resource_keys": len(all_defined_keys),
        "resource_references": sum(all_resource_refs.values()),
        "xaml_event_handler_attributes": event_count,
        "hardcoded_color_literals_outside_resource_paths": hardcoded_color_count,
        "canvas_elements_for_contextual_review": canvas_count,
        "assembly_qualified_xmlns": sum(third_party_xmlns.values()),
    }
    return result


def result_code(result: dict) -> str:
    if result["errors"]:
        return "HEURISTIC_STATIC_SCAN_ERROR"
    if result["warnings"] or result["notes"]:
        return "HEURISTIC_STATIC_SCAN_FINDINGS_PRESENT"
    return "HEURISTIC_STATIC_SCAN_NO_FINDINGS"


def print_findings(heading: str, findings: list[dict]) -> None:
    print(f"\n{heading} ({len(findings)})")
    for item in findings:
        location = ""
        if item["path"]:
            location = item["path"]
            if item["line"]:
                location += f":{item['line']}"
            location += " - "
        print(f"- [{item['code']}] {location}{item['message']}")


def main() -> int:
    if sys.version_info < MIN_PYTHON:
        print("ERROR: Python 3.10 or newer is required.", file=sys.stderr)
        return 2

    parser = argparse.ArgumentParser(description="Bounded heuristic inventory for .NET 10 WPF UI source")
    parser.add_argument("root", type=Path, help="Authorized WPF project or view root")
    parser.add_argument("--json", action="store_true", help="Emit JSON")
    parser.add_argument("--strict", action="store_true", help="Return 1 when warnings are present; use only after project-specific review")
    parser.add_argument("--exclude", action="append", default=[], help="Additional relative-path or name glob to exclude; repeatable")
    parser.add_argument("--include", action="append", default=[], help="Relative-path or file-name glob to include; repeatable")
    parser.add_argument("--max-files", type=int, default=5000, help="Maximum .csproj + .xaml files (default: 5000)")
    parser.add_argument("--max-file-bytes", type=int, default=2 * 1024 * 1024, help="Maximum bytes per file (default: 2 MiB)")
    parser.add_argument("--max-total-bytes", type=int, default=64 * 1024 * 1024, help="Maximum total bytes read (default: 64 MiB)")
    parser.add_argument("--allow-broad-root", action="store_true", help="Permit a filesystem or user-profile root; use deliberately")
    args = parser.parse_args()

    if args.max_files <= 0 or args.max_file_bytes <= 0 or args.max_total_bytes <= 0:
        parser.error("scan limits must be positive")

    try:
        root = args.root.resolve(strict=True)
    except OSError as exc:
        print(f"ERROR: root cannot be resolved: {args.root}: {exc}", file=sys.stderr)
        return 2
    if not root.is_dir():
        print(f"ERROR: root is not a directory: {root}", file=sys.stderr)
        return 2

    home = Path.home().resolve()
    is_filesystem_root = root.parent == root
    is_user_profile_root = root == home
    if (is_filesystem_root or is_user_profile_root) and not args.allow_broad_root:
        print(
            "ERROR: refusing a filesystem/user-profile root. Select the WPF project or authorized view root, "
            "or pass --allow-broad-root deliberately.",
            file=sys.stderr,
        )
        return 2

    result = audit(root, args)
    code = result_code(result)
    result["result"] = code

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print("WPF UI HEURISTIC STATIC INVENTORY")
        print(f"Root: {result['root']}")
        for key, value in result["metrics"].items():
            print(f"  {key}: {value}")
        print_findings("ERRORS", result["errors"])
        print_findings("WARNINGS", result["warnings"])
        print_findings("NOTES", result["notes"])
        print(f"\nRESULT: {code}")
        print(f"BOUNDARY: {DISCLAIMER}")

    if result["errors"]:
        return 1
    if args.strict and result["warnings"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
