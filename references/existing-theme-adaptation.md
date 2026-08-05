# Adapting an Existing WPF Theme

Use this reference before adding tokens or shared styles to a mature application.

## Principle

One application should normally have one authoritative visual language. Map new UI needs into the existing theme rather than importing a parallel naming system, palette, and control density.

The bundled `assets/industrial-design-tokens-template.xaml` is a reference for projects without an adequate design system. It is not an instruction to merge `Ui.*` resources into every project.

## Inventory within scope

Inspect only the resources relevant to the affected screen:

- merged dictionary order;
- application and local resources;
- semantic brushes and colors;
- spacing, typography, dimensions, radii, and border thicknesses;
- base control styles and variants;
- status chips, form rows, dialog chrome, panels, viewports, and validation styles;
- hover, pressed, focus, disabled, selected, and error triggers;
- current references from the affected XAML.

Do not perform a repository-wide theme migration for a narrow page adjustment.

## Choose the smallest adaptation

Apply this order:

1. Reuse an existing semantic resource or style unchanged.
2. Compose existing resources in a view-local layout.
3. Add a focused variant `BasedOn` an authoritative base style.
4. Add a missing semantic role to the authoritative theme when several screens genuinely need it.
5. Introduce a new token layer only when the project lacks one and the user authorizes the broader change.

Avoid view-local hardcoded colors and repeated style setters. Also avoid global implicit-style changes when a named variant is sufficient.

## Semantic mapping

Map by role, not by color similarity. Typical roles include:

- application / primary / secondary / elevated surface;
- subtle / strong border;
- primary / secondary / muted / inverse text;
- primary / secondary / quiet / destructive command;
- focus and selection;
- success / information / warning / fault / offline / simulation / unavailable;
- field validation and error background;
- camera/canvas background and overlay.

If an existing key already owns a role, extend or reuse it. Do not add a differently named duplicate merely to match the template.

## Control style rules

- Preserve existing `ControlTemplate` behavior unless replacement is necessary.
- Prefer `BasedOn` for variants so focus, disabled, automation, and high-contrast behavior are inherited.
- Do not reuse a footer style for vertical action rails when its margins or alignment encode footer layout.
- Keep button hierarchy limited: one primary action per local decision area, ordinary secondary actions, quiet toolbar actions, and explicitly destructive actions.
- Add validation states to the same field styles already used by the application.

## Verification

After a shared-style change, inspect every authorized consumer, not every repository screen. Check:

- resource resolution and merge order;
- default, hover, pressed, focused, disabled, selected, and validation states;
- minimum supported size and at least one elevated DPI when authorized;
- long Simplified Chinese/Traditional Chinese/English labels when applicable;
- no unrequested color or density changes outside the intended scope.

If the contract does not permit rendering or broader consumers, keep the result pending visual review and name the unverified surfaces.

