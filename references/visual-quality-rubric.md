# Industrial WPF Visual Quality Rubric

Use this reference for every UI creation, restyle, or visual adjustment. Judge the rendered hierarchy and task flow, not merely whether the XAML is valid.

## 1. Establish a measurable baseline

Before editing, record the available evidence:

- current screenshot or live render and its window size;
- user-supplied reference image and which parts are authoritative;
- primary operator task and the one visually dominant region;
- major alignment lines, panel proportions, and current density;
- current normal, disabled, empty, error, and permission states;
- project theme resources already used by the affected screen.

Do not infer exact colors, dimensions, device capabilities, or interaction contracts from a screenshot when the source does not establish them.

## 2. Hierarchy

A good screen should be readable in three passes:

1. page identity, machine/process state, and primary action;
2. active work area and current step or selection;
3. secondary parameters, metadata, and diagnostics.

Check:

- one region is visibly dominant for the primary task;
- primary, secondary, quiet, and destructive actions are not styled equally;
- labels, values, units, hints, and status text have distinct roles;
- unavailable actions do not form an undifferentiated wall of gray buttons;
- warnings and faults are prominent without turning normal information into alarm color.

## 3. Alignment and spacing

Use a 4 DIP grid unless the project defines another system.

- Reuse a small set of gaps such as 4, 8, 12, 16, 24, and 32 DIP.
- Align repeated labels, fields, units, action edges, and section headings.
- Avoid accidental double spacing caused by both control margins and spacer rows.
- Keep panel padding consistent within the same hierarchy level.
- Use whitespace to group related content; do not put every group inside an identical card.
- Fixed widths require a reason such as stable numeric entry, known units, or an approved minimum window.

Misaligned button edges, drifting unit columns, and uneven card padding are P2 defects even when the screen still functions.

## 4. Density and card restraint

Industrial desktop UI should be compact enough for scanning but not cramped.

- Prefer flat sections, separators, headings, or subtle surface changes inside an already bounded panel.
- Avoid card-in-card nesting unless elevation or ownership genuinely changes.
- Preserve space for camera, canvas, drawing, process, and data-grid surfaces.
- Collapse or defer low-frequency help instead of shrinking the primary work area.
- Keep high-frequency controls near the feedback they affect.

## 5. Reusable composition patterns

### Parameter row

Use a stable label / editor / unit-or-hint grid. Let the editor column grow when the window grows. Show validation beside the affected field and keep Save/Apply gating consistent with it.

### Dialog

Use a clear title, bounded content, optional validation/status strip, and a stable footer. One action is primary. Cancel remains reachable through button and keyboard when the contract allows it.

### Vertical action group

Use a style designed for a vertical rail; do not reuse a horizontal footer-button style that adds left-only margins. Align all action edges and distinguish the next valid action from unavailable future steps.

### Process or calibration steps

Show step label, state, concise evidence, and contextual action. Use current/completed/blocked/unavailable states rather than several identical cards containing identical disabled buttons.

### Status chip

Pair color with text or icon. Use stable semantic roles such as normal, information, warning, fault, offline, simulation, and unavailable. Do not expose provider, owner, JSON, DLL, or internal mode names in normal UI unless operators need them.

### Camera or canvas empty state

Keep the viewport visually dominant. Use a restrained overlay with a concise state and next action. Do not present fixed acquisition size, local imagery, or simulated content as proof of camera model, FOV, calibration, SDK connection, or production capability.

## 6. Typography and icons

- Use the project's approved fonts and a small deliberate type scale.
- Avoid oversized empty-state text and tiny low-contrast operational text.
- Keep section headings visually quieter than the page title.
- Use the project's icon family; align optical weight and size.
- Pair unfamiliar or destructive icons with labels.

## 7. State polish

Inspect applicable states individually:

- hover, pressed, keyboard focus, default and disabled;
- selected/current;
- validation error;
- loading/busy;
- empty/no selection;
- offline, stale, simulation, unavailable, permission denied, and fault.

Disabled content must remain legible. Focus must remain visible. Status must not rely on color alone.

## 8. Visual comparison loop

When GUI evidence is authorized:

1. Capture the baseline at an explicit size, DPI, state, and locale.
2. Implement the smallest coherent UI change.
3. Capture the same state at the same size and DPI.
4. Compare hierarchy, alignment, density, clipping, wrapping, action prominence, and state clarity.
5. Correct at least one observed defect or explicitly record that no material defect was found.
6. Retain user or designated-reviewer acceptance as a separate gate.

When GUI evidence is not authorized or available, report the visual result as pending. Static inspection and automated tests cannot close this loop.

