---
name: wpf-industrial-ui-design
description: >-
  Use only for .NET 10 WPF UI/XAML creation, modification, restyling, adjustment, or
  screenshot implementation. Exclude backend/C#/DLL/tests/docs, non-WPF, and read-only UI
  questions. Also use when explicitly invoked as $wpf-industrial-ui-design.
  Preserve MVVM, navigation, commands, permissions, ownership, localization, resource
  architecture, project contracts, and evidence boundaries while producing task-first
  industrial desktop interfaces.
---

# .NET 10 WPF Industrial UI Design

Create or improve production-oriented WPF front ends without replacing the application's existing contracts merely to make the screen look modern. Treat the interface as an operational projection of commands, permissions, runtime state, configuration ownership, and evidence—not as an isolated XAML composition.

## Core contract

1. **Obey the project contract first.** Current user instructions, local `AGENTS.md`, project knowledge-base rules, exact file allowlists, Git restrictions, build/test budgets, stop conditions, and project result codes override this generic skill. This skill grants no edit, build, test, GUI, hardware, production, release, or review authority by itself.
2. **Read project knowledge before project UI work.** Follow the repository's physical startup chain and knowledge-base entry order before inspecting or modifying the real project. Loading this skill never replaces that step.
3. **Target .NET 10 WPF.** Confirm the actual WPF project, target framework, Windows target, and `UseWPF` before editing. Do not silently downgrade, retarget, or mix WPF with WinUI namespaces and patterns.
4. **Preserve the existing architecture.** Detect the current MVVM implementation, View/ViewModel mapping, navigation, dialogs, DI, commands, permissions, themes, localization, custom controls, and third-party libraries within the authorized scope. Adapt to them unless the user explicitly authorizes a migration.
5. **Design from operator tasks.** Establish the primary task, high-frequency actions, critical status, secondary configuration, and failure recovery before choosing panels or controls.
6. **Separate design from capability.** A polished button, device badge, alarm panel, or animation must not imply that hardware, MES, safety, licensing, production, or other external capability is implemented or verified.
7. **Adapt the existing design system.** Prefer the project's authoritative theme and semantic resources. Do not introduce a parallel token namespace merely because this skill includes a template.
8. **Keep business logic out of views.** Prefer bindings and commands. Code-behind is allowed only for view-specific behavior that cannot reasonably be expressed through XAML, attached behavior, or an existing service contract.
9. **Do not introduce dependencies by default.** Do not install or add CommunityToolkit.Mvvm, Prism, Syncfusion, MaterialDesign, HandyControl, MahApps, FluentWPF, or any other package unless it is already authoritative in the project or the user explicitly approves it.
10. **Implement every relevant interaction state.** Cover default, pointer-over, pressed, disabled, focus, selected, validation error, loading, empty, offline, stale, simulation, permission denied, unavailable capability, and fault states as applicable.
11. **Close the visual loop.** For visual implementation, inspect the current render/reference when available, implement against measurable hierarchy and alignment, then compare a same-size render or screenshot and iterate at least once when GUI evidence is authorized. If rendering is forbidden or unavailable, stop at pending visual review.
12. **Validate in layers.** Static XAML and resource checks, build, automated tests, launch, interaction, screenshot/visual inspection, independent review, and user acceptance are different evidence levels. Report them separately.
13. **Prefer incremental change.** Preserve existing commands, owners, route IDs, automation IDs, localization keys, public ViewModel contracts, and manually approved layouts. Do not rebuild the shell unless shell replacement is the requested task.

## Authority discovery

When accessible and not prohibited:

1. Read the applicable physical `AGENTS.md` / `AGENTS.override.md` chain.
2. Identify the repository root and the actual WPF startup project.
3. Read the project's governance rules and current `START_HERE.md` entry when the project uses a knowledge base. Read its current head and physical EOF when required by local rules.
4. Inspect only the files and neighboring contracts needed for the requested UI change. A narrow allowlist outranks the broad inventory suggestions in this skill.
5. Treat current user instructions and project-specific rules as higher authority than this generic skill.
6. Do not run Git, builds, tests, Release, a GUI, full-suite scans, hardware, production services, or customer-data access unless the current project contract explicitly authorizes them.

If an authority source is unavailable, continue from accessible repository evidence and declare the gap. Do not invent its content.

## Invocation modes

Determine the mode before making changes:

- `DESIGN`: produce a concrete screen architecture, information hierarchy, layout contract, design tokens, and state specification; do not modify production files unless asked.
- `IMPLEMENT`: implement an approved screen or UI change in the existing project.
- `REFACTOR`: improve visual consistency or maintainability while preserving behavior and public contracts.
- `REVIEW`: perform a read-only UI/XAML/MVVM/design-system audit and report prioritized findings.
- `VISUAL_QA`: launch or inspect supplied screenshots, compare them against the UI contract, and report visual/interaction defects without claiming implementation success from images alone.

Default to `IMPLEMENT` only when the user explicitly asks to change the project. Otherwise use `DESIGN` or `REVIEW` according to intent.

The automatic trigger is intentionally narrower than these modes: use `REVIEW` or `VISUAL_QA` only when the skill was explicitly named or the review is part of an authorized UI creation/modification task.

## Phase 0 — Establish the UI contract

Record internally:

- target project and target framework;
- requested mode and affected screens;
- primary user role and primary task;
- high-frequency commands and safety/destructive commands;
- required status and feedback;
- current navigation and ownership contracts;
- minimum supported window size and DPI assumptions;
- localization languages and longest-content risks;
- existing visual baseline or supplied reference images;
- prohibited dependencies and integration gates;
- acceptance evidence required this round.

Ask a question only when a missing choice would materially change the layout, target screen, interaction contract, or permitted dependencies. Otherwise preserve existing project choices and document assumptions.

## Phase 1 — Detect the .NET 10 WPF baseline

Confirm:

- a WPF project exists;
- `TargetFramework` is `net10.0-windows` or a compatible Windows-version-qualified .NET 10 target;
- `UseWPF` is enabled;
- WPF XML namespace is used, not `Microsoft.UI.Xaml`;
- existing package and framework choices;
- whether the application uses the native WPF Fluent theme, custom resources, third-party themes, or a hybrid;
- whether the current navigation is `ContentControl`, `Frame`, tabs, multiple windows, dialogs, or a custom host;
- whether MVVM is hand-written, CommunityToolkit-based, Prism-based, ReactiveUI-based, or project-specific.

Read `references/net10-wpf-baseline.md` before changing theme or framework-level behavior.

The optional audit script requires Python 3.10 or newer. Run it only against the authorized WPF project or view root, never a drive root or unrelated repository tree:

```text
python scripts/audit_wpf_ui.py <wpf-project-or-authorized-view-root>
```

Treat its output as a heuristic inventory, not a build, XAML compiler, visual PASS, or failure-closing gate. Use `--strict` only when the project contract permits it and project-specific exceptions are already reviewed.

## Phase 2 — Inventory existing UI contracts

Build a compact UI inventory before editing:

- shell regions and routes;
- View → ViewModel mapping;
- commands and `CanExecute` sources;
- permission/role gates, including keyboard and gesture paths;
- dialogs, confirmations, notifications, and status projections;
- ResourceDictionary merge order;
- semantic brushes, styles, templates, icons, fonts, spacing, and sizes;
- loading, empty, error, offline, simulation, and fault states;
- localized strings and text expansion pressure;
- custom controls, attached behaviors, converters, and code-behind handlers;
- large collections and virtualization requirements;
- current screenshots and known visual defects.

Do not replace an existing navigation or MVVM mechanism merely because another GitHub skill uses a different one.

## Phase 3 — Choose the application silhouette

Select the closest layout family before writing XAML. Read `references/layout-patterns.md` and `references/visual-quality-rubric.md`.

Typical industrial WPF silhouettes:

- **Operator console:** dominant camera/canvas/process surface, adjacent high-frequency operation console, persistent machine/status strip, contextual secondary panels.
- **Engineering/configuration workspace:** stable category navigation, editable content area, validation summary, explicit Apply/Revert, dirty-state protection.
- **Diagnostics/commissioning:** device tree or category rail, status snapshots, controlled commands, logs and evidence area, permission and simulation markers.
- **Dashboard/overview:** health and production summary, exceptions first, drill-down routes; not a wall of equal cards.
- **Document/CAD editor:** content-dominant canvas, lightweight chrome, contextual tools, layers/properties in secondary panes.
- **Modal workflow:** one decision or bounded edit, explicit primary/cancel actions, no hidden navigation.

Do not default every application to a left navigation rail. Choose the silhouette that matches the task.

## Phase 4 — Freeze the design system before broad XAML changes

Read `references/design-system.md` and `references/existing-theme-adaptation.md`.

Only when the project lacks an approved design system, use the included industrial light baseline as a starting point:

```text
assets/industrial-design-tokens-template.xaml
```

Do not copy it blindly. If an authoritative theme already exists, map the needed concepts into its resource names and styles instead of creating a second `Ui.*` system.

Freeze or preserve:

- semantic color roles, including surfaces, borders, text, accent, status, selection, validation, and disabled states;
- type scale and weights;
- spacing grid and control density;
- minimum hit targets and high-frequency command sizing;
- corner radius, border thickness, focus treatment, and elevation policy;
- icon source and sizing rules;
- light/dark/high-contrast policy;
- animation and transition policy;
- localization and text-wrapping rules.

For the default industrial light direction, prefer a white/light-neutral workspace with restrained blue emphasis, clear borders, high information density, and unambiguous status colors. Do not turn every panel into a decorative card.

## Phase 5 — Design interaction and state coverage

Read `references/interaction-states.md`.

For every interactive control or operational feature, specify:

- action owner and command;
- enabled/disabled conditions;
- permission behavior;
- busy/reentrancy behavior;
- confirmation requirement;
- cancellation and timeout behavior;
- success, warning, and failure feedback;
- simulation/NoHardware/unavailable presentation;
- keyboard access, focus order, tooltip/help, and automation name;
- localized label and compact alternative when space is constrained.

Rules for industrial/safety-adjacent UI:

- Separate Start, Feed Hold/Pause, Resume, Controlled Stop, Abort, Reset, Clear Alarm, and E-stop concepts when the domain distinguishes them.
- Do not render a software E-stop as proof of a safety chain.
- Destructive or irreversible actions require identity/context in the confirmation message.
- Disabled controls must expose why they are disabled when the reason matters operationally.
- Permission must govern commands, shortcuts, gestures, drag operations, context menus, and direct manipulation—not just button visibility.
- A placeholder control must show `Unavailable`, `Waiting for integration`, `Simulation`, or the project's authoritative wording.

## Phase 6 — Implement incrementally

Read `references/mvvm-and-routing.md`.

Implementation order:

1. Add or update semantic tokens and shared styles.
2. Build or adjust focused reusable controls only when existing controls/styles cannot express the contract.
3. Update the affected view structure.
4. Wire to existing ViewModel properties, commands, validation, and state projections.
5. Add view-only behavior with attached behaviors or minimal code-behind when justified.
6. Preserve route, command, permission, owner, localization, and automation identities.
7. Add or update design-time data without coupling production code to the designer.
8. Add targeted tests for ViewModels, command gates, navigation, validation, and state mapping.

### XAML rules

- Use WPF `{Binding}` and WPF resource semantics. Do not copy WinUI `x:Bind`, `NavigationView`, `InfoBar`, `TeachingTip`, or Microsoft.UI namespaces into WPF.
- Prefer `Grid`, `DockPanel`, and purposeful nested layouts over absolute positioning. `Canvas` is appropriate for drawing, CAD, overlay, and coordinate surfaces—not ordinary form layout.
- Use `Auto` and `*` sizing deliberately; fixed dimensions require a UI contract reason.
- Keep collection controls virtualized when data volume can grow.
- Avoid nesting a scrolling collection in an unconstrained outer `ScrollViewer`.
- Use semantic resource names such as `Ui.Brush.Surface`, `Ui.Brush.Command.Primary`, and `Ui.Brush.Status.Fault`; do not name by hue alone.
- Keep view files readable. Extract repeated layouts into DataTemplates, styles, or focused controls, not arbitrary abstraction layers.
- Keep XAML event handlers exceptional and auditable.

### MVVM rules

- The ViewModel must not hold `Window`, `Control`, `DispatcherObject`, or vendor-device UI objects unless the project already defines and justifies such a contract.
- Async commands must prevent accidental reentrancy or explicitly support concurrency.
- Bound mutable values must notify correctly.
- Validation must be represented in both command gating and visible field/summary feedback where appropriate.
- Do not create a God ViewModel. Compose focused child ViewModels or projections while preserving the existing architecture.
- Do not create a new navigation service, dialog service, or messenger when an authoritative one already exists.

## Phase 7 — Accessibility, DPI, localization, and performance

Read `references/accessibility-dpi-localization.md`.

Minimum checks:

- keyboard-only completion of core workflows;
- visible focus indication and logical tab order;
- `AutomationProperties.Name` / `HelpText` / stable IDs for non-obvious controls;
- text labels are not replaced solely by placeholders or color;
- status is not communicated by color alone;
- scaling at 100%, 125%, 150%, and 200% where practical;
- minimum-window behavior and no clipped critical commands;
- Simplified Chinese, Traditional Chinese, and English expansion where applicable;
- virtualization and bounded rendering for large lists/logs;
- frozen/reused brushes and geometries where performance matters;
- no heavy computation in converters or UI-thread command bodies;
- no high-frequency per-item Dispatcher calls.

## Phase 8 — Validate in evidence layers

Read `references/verification.md`.

Execute the applicable layers in order:

1. **Static:** XML/XAML parse, project target, resource keys, namespace purity, duplicate styles/keys, hardcoded visual constants, suspicious handlers, binding-path review.
2. **Build:** build the affected .NET 10 WPF project using the project's authoritative command and configuration.
3. **Automated tests:** run targeted tests, then the applicable full suite.
4. **Launch:** start the intended executable/configuration and verify it remains healthy for the defined smoke interval.
5. **Interaction:** exercise navigation, commands, permission gates, validation, loading/error/empty/offline states, resizing, and localization paths.
6. **Visual:** when authorized, capture or inspect before/after screenshots at the same window size, DPI, state, and locale. Correct clipping, overlap, visual hierarchy, inconsistent states, icon/text alignment, density defects, and obvious regressions; perform at least one compare-and-adjust iteration for visual implementation.
7. **User acceptance:** retain `PENDING_USER_VISUAL_REVIEW` until the user or designated reviewer confirms the rendered interface when that confirmation is required.

A successful build is not visual approval. A screenshot is not interaction proof. A NoHardware screen is not real-device validation.

If launch or screenshot capture is outside the current contract, do not manufacture visual evidence or widen scope. Complete the permitted static/automated work and report `PENDING_USER_VISUAL_REVIEW` or the project's equivalent.

## Phase 9 — Closeout

Report:

1. mode and affected screens;
2. project/target framework detected;
3. design contract and silhouette selected;
4. files changed;
5. design tokens/styles/controls added or changed;
6. bindings, commands, routes, permissions, and owners preserved or intentionally changed;
7. static audit result;
8. build and test commands/results;
9. launch/interaction evidence;
10. visual evidence and reviewed resolutions/DPI/locales;
11. unresolved visual, dependency, hardware, or integration boundaries;
12. project-authoritative result code; use the generic codes below only when the project contract does not define one.

Result codes:

- `WPF_NET10_UI_DESIGN_SPEC_READY`
- `WPF_NET10_UI_IMPLEMENTATION_PASS`
- `WPF_NET10_UI_IMPLEMENTATION_PASS_PENDING_VISUAL_REVIEW`
- `WPF_NET10_UI_REFACTOR_PASS`
- `WPF_NET10_UI_REVIEW_FINDINGS`
- `WPF_NET10_UI_VISUAL_QA_PASS`
- `WPF_NET10_UI_BLOCKED_PROJECT_CONTRACT`
- `WPF_NET10_UI_BLOCKED_DEPENDENCY_APPROVAL`
- `WPF_NET10_UI_BUILD_OR_TEST_FAIL`
- `WPF_NET10_UI_VISUAL_REVIEW_FAIL`
- `WPF_NET10_UI_INSUFFICIENT_EVIDENCE`

Never replace, upgrade, or reinterpret a project-specific result code with one of these generic codes.

## Hard prohibitions

Do not:

- convert WPF to WinUI/MAUI/Avalonia as a side effect;
- add packages or license keys without authorization;
- rewrite the shell, routing, or MVVM framework without explicit scope;
- replace real project icons with arbitrary generated icon sets without approval;
- hide capability gaps behind polished controls;
- claim GUI pass from static XAML review;
- claim real hardware, MES, safety, or production readiness from UI behavior;
- fabricate screenshots, interaction evidence, binding logs, or DPI results;
- delete existing user changes merely to normalize style;
- perform unrelated backend or device implementation under a UI task;
- skip the project's knowledge-base startup because this skill was loaded;
- scan the whole repository when a file or screen allowlist is narrower;
- exceed an authorized build/test count or continue after a contractual hard stop;
- create a second theme/token system alongside an existing authoritative one;
- claim independent review PASS or user GUI PASS from self-review or automation.
