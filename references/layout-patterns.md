# WPF Industrial Layout Patterns

Choose one primary silhouette and compose secondary patterns. Do not combine every pattern on one screen.

## 1. Operator console

Recommended regions:

- top: application identity, mode, connection, user/permission, global alarms;
- center-left or center: dominant live camera, drawing, process, or machine visualization;
- adjacent operation console: Start, Pause/Hold, Resume, Stop, Reset, material handling, current job;
- contextual secondary area: recipe, selection, short diagnostics, or current step;
- bottom/status strip: machine state, coordinates, cycle state, alarm summary, simulation marker.

Rules:

- keep high-frequency actions near the primary visual feedback;
- do not place production controls in a distant global toolbar merely for symmetry;
- hide or collapse secondary configuration rather than shrinking the hero surface;
- emergency and destructive concepts must be visually distinct and semantically accurate.

## 2. Configuration workspace

Recommended regions:

- stable category navigation;
- page title and scope/owner description;
- editable form organized by domain;
- validation summary and dirty-state marker;
- Apply, Revert, and optional Restore Defaults in a stable footer or command area.

Rules:

- drafts must be visually distinguishable from applied runtime values when the domain uses both;
- switching category/product/machine must handle dirty-state protection;
- input units, ranges, defaults, source, and permissions must be explicit;
- avoid one enormous scrolling form when categories have distinct owners.

## 3. Diagnostics and commissioning

Recommended regions:

- device/category tree or segmented navigation;
- immutable current snapshot;
- controlled command area;
- raw/normalized status and fault detail;
- evidence/log view;
- simulation, disconnected, and permission banners.

Rules:

- display-only status and write commands must not look identical;
- Force/Override/Test actions require permission, state gate, audit, and clear active indication;
- stale timestamps and disconnected data must remain visible.

## 4. Dashboard

Prioritize exceptions and next actions:

- health summary;
- active fault and blocked work;
- current job/recipe/production state;
- trends only when their time base and source are clear;
- drill-down routes.

Avoid an undifferentiated grid of equal cards.

## 5. CAD, drawing, vision, or document workspace

- content fills most of the window;
- tools are grouped by mode/context;
- layer/properties panels are secondary and resizable;
- status/coordinate/zoom information is compact;
- direct manipulation is governed by the same permissions and dirty-state rules as command buttons.

## 6. Modal workflow

Use for bounded decisions or edits, not general navigation.

- explicit title and affected object;
- focused content;
- primary verb and Cancel;
- validation before close;
- destructive confirmations include object identity and effect;
- preserve keyboard default/cancel behavior.

## Responsive desktop behavior

WPF desktop design should define behavior bands rather than imitate responsive web pages:

- full layout;
- compact width with secondary panes collapsed or moved to tabs/drawers;
- minimum supported width with all critical actions still reachable;
- optional multi-monitor/large-canvas mode.

Do not silently hide required commands at small sizes. Provide overflow or an alternate route.
