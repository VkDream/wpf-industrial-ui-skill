# WPF Industrial UI Skill

[![Validate](https://github.com/VkDream/wpf-industrial-ui-skill/actions/workflows/validate.yml/badge.svg)](https://github.com/VkDream/wpf-industrial-ui-skill/actions/workflows/validate.yml)

面向 **.NET 10 WPF 工业桌面软件**的 Agent Skill，用于设计、实现、重构、评审和视觉验收前端界面，同时保留现有项目的 MVVM、导航、命令、权限、参数 Owner、资源字典与外部能力边界。

This repository contains an Agent Skill for designing, implementing, refactoring, reviewing, and visually validating **industrial .NET 10 WPF** user interfaces without replacing an existing application's architecture merely to modernize its appearance.

## Why this skill exists

通用 WPF 指南通常只覆盖 XAML、Binding 和 MVVM；通用 UI 生成器则经常强制指定控件库、导航框架或自动安装依赖。本 Skill 重点解决存量工业项目中的实际约束：

- detect and preserve the existing WPF architecture;
- design around operator tasks and machine state;
- keep visual polish separate from real hardware, MES, safety, licensing, and production capability;
- centralize semantic resources and complete interaction states;
- validate static XAML, build, runtime, screenshots, and user acceptance as different evidence levels;
- avoid adding CommunityToolkit, Prism, Syncfusion, HandyControl, MahApps, MaterialDesign, or other packages unless already authoritative or explicitly approved.

## Target

- WPF on `.NET 10` (`net10.0-windows` or a Windows-version-qualified .NET 10 target)
- Existing or new industrial desktop applications
- Codex-compatible Agent Skill layout
- Windows development environments

The skill does **not** convert WPF projects to WinUI, MAUI, Avalonia, or web UI.

## Modes

| Mode | Purpose |
|---|---|
| `DESIGN` | Define screen architecture, hierarchy, layout, tokens, and state contracts without changing production files. |
| `IMPLEMENT` | Implement an approved UI change in the existing WPF project. |
| `REFACTOR` | Improve visual consistency and maintainability while preserving behavior and public contracts. |
| `REVIEW` | Perform a read-only XAML, MVVM, design-system, DPI, localization, and state audit. |
| `VISUAL_QA` | Review screenshots or a running UI while keeping implementation and user-acceptance evidence separate. |

## Installation

### User-level Codex skill

Copy this repository, or only the runtime skill files, to:

```text
%USERPROFILE%\.agents\skills\wpf-industrial-ui-design\
```

### Project-level skill

```text
<repository-root>\.agents\skills\wpf-industrial-ui-design\
```

The runtime skill package contains `SKILL.md`, `agents/`, `assets/`, `references/`, and `scripts/`. Repository-only files such as this README and GitHub workflow are excluded from the generated ZIP.

## Usage

```text
$wpf-industrial-ui-design

Inspect the existing .NET 10 WPF project, preserve its MVVM, navigation,
commands, permissions, resource hierarchy, and capability boundaries,
then redesign and implement the operator workspace. Do not add third-party
UI dependencies. Validate static XAML, build, runtime, visual states, DPI,
localization, and remaining user-review gates separately.
```

更多示例见 [`examples/prompts.md`](examples/prompts.md)。

## Static audit

The included audit is conservative. It checks project targets, `UseWPF`, XML validity, WinUI namespace leakage, duplicate resource keys, hardcoded colors, event-handler density, resource references, and selected layout risks. It does not compile or render the application.

```powershell
python scripts/audit_wpf_ui.py C:\Path\To\Your\WpfRepository
```

JSON output:

```powershell
python scripts/audit_wpf_ui.py C:\Path\To\Your\WpfRepository --json
```

## Validate and package

```powershell
python scripts/validate_skill.py
python scripts/package_skill.py
```

The package command writes:

```text
dist/wpf-industrial-ui-design.zip
```

The generated ZIP intentionally contains no `README.md`.

## Repository structure

```text
.
├─ SKILL.md
├─ agents/
│  └─ openai.yaml
├─ assets/
│  └─ industrial-design-tokens-template.xaml
├─ references/
├─ scripts/
│  ├─ audit_wpf_ui.py
│  ├─ package_skill.py
│  └─ validate_skill.py
├─ examples/
├─ .github/workflows/validate.yml
├─ CHANGELOG.md
├─ LICENSE
└─ README.md
```

## Scope and evidence boundaries

A clean build does not prove runtime behavior. A successful launch does not prove interaction completeness. A screenshot does not prove command wiring. A polished device panel does not prove real hardware, MES, safety, or production readiness. The skill requires these evidence levels to be reported separately.

## Status

`v0.1.0 Preview`

Tested as a reusable skill package and static-audit workflow. Review all generated or modified production UI before deployment.

## Influences

This is an original synthesis. Design and workflow concepts were reviewed from public WPF, WinUI, shell, and UI-builder skills; framework-specific source code and proprietary control assets are not included. Details are recorded in [`references/source-influences.md`](references/source-influences.md).

## License

MIT — see [`LICENSE`](LICENSE).
