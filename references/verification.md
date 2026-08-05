# WPF UI Verification Matrix

## Evidence levels

| Level | Proves | Does not prove |
|---|---|---|
| Static XAML/resource audit | XML validity, obvious key/namespace/style problems | runtime bindings, layout, interaction |
| Build | compilation and resource generation | launch health, visual correctness |
| Unit/ViewModel tests | tested commands, validation, state projections | rendered UI and actual navigation |
| Launch smoke | executable starts in the tested environment | complete workflow or visual acceptance |
| Interaction test | exercised commands/routes/states | all DPI/locales/real integrations |
| Screenshot review | appearance at captured state/size | hidden states, command correctness |
| User visual review | reviewer accepts presented appearance | hardware/MES/safety/production validation |

## Static checks

When the project contract permits a read-only heuristic scan and Python 3.10+ is available, run it against the authorized WPF project or view root:

```text
python scripts/audit_wpf_ui.py <wpf-project-or-authorized-view-root>
```

Do not point it at a drive root, user profile, broad evidence tree, or unrelated repository content. Use repeated `--include` and `--exclude` globs when the allowlist is narrower. Generated, dependency, build, test-result, backup, and evidence directories are excluded by default.

Review all warnings. Typical findings:

- target framework mismatch;
- `UseWPF` missing;
- malformed XAML;
- WinUI namespace or `x:Bind` in WPF;
- duplicate resource keys;
- hardcoded colors outside theme/resources;
- event-handler-heavy views;
- ordinary UI laid out with Canvas;
- unreviewed third-party XAML assemblies.

The script is bounded and intentionally heuristic. Its `HEURISTIC_STATIC_SCAN_*` result describes only the inventory process. It is not an XAML compiler, build, render, GUI review, or CI authority. Do not use `--strict` until project-specific false positives and scope have been reviewed.

## Build and test

Use only project-authoritative commands allowed by the current contract. Honor compile/test counts and failure-stop rules. Record configuration and exact result. Do not call a targeted test a full regression.

## Runtime binding review

Capture WPF binding warnings in Debug where practical. Verify:

- no broken binding paths in affected views;
- no missing resources or template exceptions;
- commands enable/disable as expected;
- no UI-thread exceptions;
- localization resources resolve.

## Visual review set

When rendering is authorized, start with a baseline and capture the modified screen at the same size, DPI, state, and locale. Inspect at least the applicable subset of:

- normal state;
- loading/empty/error or the relevant non-happy state;
- minimum supported size;
- primary production resolution;
- at least one elevated DPI where practical;
- each required language at its riskiest screen;
- permission/read-only state;
- simulation/offline/unavailable state if applicable.

Perform at least one comparison-and-adjust iteration for visual implementation. If launch or screenshot capture is forbidden or unavailable, state that visual evidence is pending instead of widening the task.

## Visual defect classes

- P0: critical command inaccessible, misleading safety/capability state, destructive action ambiguity;
- P1: clipped/overlapped critical content, broken navigation, unreadable fault/status, severe DPI/localization failure;
- P2: inconsistent spacing/style/state, moderate hierarchy or alignment defect;
- P3: polish issue with no workflow impact.

## Closeout boundary

Use `PENDING_USER_VISUAL_REVIEW` when a human acceptance step is required and has not occurred. Do not substitute an agent-generated screenshot summary for the user's approval.

Project-specific result codes and independent-review gates always override generic skill result codes.
