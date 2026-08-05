# Accessibility, DPI, Localization, and Visual Robustness

## Keyboard and focus

- define logical tab order;
- ensure core workflows are possible without a mouse;
- preserve visible focus;
- use access keys when the product convention supports them;
- set default and cancel behavior for dialogs;
- return focus predictably after dialogs, navigation, and validation failures.

## UI Automation

Add meaningful `AutomationProperties.Name`, `HelpText`, and stable identifiers for icon-only, custom, canvas, and non-obvious controls. Do not duplicate noisy names on purely decorative elements.

## Contrast and semantics

- do not rely on color alone;
- use icon, label, border, pattern, or state text;
- verify text/background contrast;
- test high-contrast/contrast themes when the deployment environment requires them;
- do not suppress system high-contrast behavior without an approved replacement.

## DPI and resizing

Test practical combinations:

- 100%, 125%, 150%, 200%;
- primary supported resolution;
- minimum supported window size;
- maximized and restored window;
- multi-monitor movement when applicable.

Check:

- clipped text;
- fixed-size controls that cannot accommodate translation;
- pixel-snapping and blurry lines/icons;
- incorrect popup/dialog placement;
- canvas scaling and coordinate overlays;
- minimum-size access to critical actions.

## Localization

For Simplified Chinese, Traditional Chinese, and English:

- use resource keys rather than embedded text;
- allow natural text expansion;
- avoid constructing sentences from fragments;
- define wrapping/trimming/tooltips intentionally;
- keep units and numbers locale-aware where required;
- check accelerator/access-key collisions;
- preserve domain terminology contracts.

Do not shrink all text to solve one translation overflow. Fix layout, width policy, or wording first.

## Icons

- use the project's existing icon set and visual language;
- choose vector assets where practical;
- align icon size and optical weight;
- pair unfamiliar/destructive icons with text;
- verify light/dark/high-contrast behavior;
- do not replace approved icons merely for stylistic uniformity.
