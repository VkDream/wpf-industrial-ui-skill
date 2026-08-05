# Interaction and State Coverage

## Universal control states

For each reusable interactive control, inspect:

- normal;
- pointer over;
- pressed;
- disabled;
- keyboard focused;
- selected/current;
- validation error;
- busy/in progress.

Do not remove visible focus merely for appearance.

## Screen states

Data-driven and operational screens should deliberately cover applicable states:

- initial/loading;
- loaded/normal;
- empty/no selection;
- validation blocked;
- warning;
- fault/error;
- disconnected/offline;
- stale data;
- permission denied/read-only;
- simulation/NoHardware;
- capability unavailable/waiting for integration;
- partial availability;
- shutdown/disposed.

Do not represent all of these with one generic red banner.

## Feedback hierarchy

Use the least disruptive surface that still matches the decision:

- inline hint/status for passive information;
- field validation for input problems;
- status bar/banner for ongoing system state;
- non-modal notification for completed background actions;
- modal confirmation for blocking, destructive, or irreversible decisions;
- dedicated fault/alarm surface for operational faults.

## Destructive actions

Confirmation should state:

- the exact action verb;
- affected item/job/product/configuration;
- whether it is reversible;
- consequences;
- primary action and Cancel.

Avoid vague OK/Cancel when a verb such as Delete, Discard, Reset, Stop, or Abort is available.

## Busy and reentrancy

- disable or gate duplicate execution when unsupported;
- show progress when the user would otherwise think the command failed;
- support cancel only when the underlying operation can honor it;
- do not leave a control permanently disabled after failure;
- preserve fault details for diagnostics.

## Permission

A permission rule applies to:

- visible buttons;
- menu and toolbar items;
- keyboard shortcuts;
- context menus;
- double-click and drag gestures;
- direct canvas editing;
- command invocation from other views.

The View may hide or disable affordances, but the authoritative command/service must still enforce permission.
