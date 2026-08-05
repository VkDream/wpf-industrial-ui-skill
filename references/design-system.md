# Industrial WPF Design System

## Principle

Use semantic tokens and restrained visual hierarchy. Industrial UI must remain readable under long sessions, variable lighting, dense information, alarms, and localization pressure.

## Resource layers

Recommended merge order, adapted to the existing project:

1. primitive values: colors, doubles, thicknesses, corner radii;
2. semantic brushes and typography;
3. control base styles;
4. control variants and states;
5. view-specific resources;
6. runtime theme override when supported.

Avoid cyclic DynamicResource graphs and duplicate keys across dictionaries.

## Semantic roles

At minimum define:

- application background;
- primary and secondary surfaces;
- elevated/floating surface;
- subtle and strong borders;
- primary, secondary, muted, and inverse text;
- primary command and hover/pressed states;
- secondary command;
- selection and focus;
- success, warning, fault, information, offline, simulation, disabled;
- validation error and field error background;
- canvas/camera/drawing background and overlay roles.

Name by purpose, not hue.

## Typography

Use a small deliberate scale. Example roles:

- window/title: 20–24 DIP;
- page title: 18–22 DIP;
- section title: 15–18 DIP;
- body/control: 13–15 DIP;
- compact metadata: 12–13 DIP;
- critical status: chosen by hierarchy, not arbitrary enlargement.

Use installed fonts that cover required Chinese and Latin glyphs. Preserve project font policy.

## Spacing and density

Use a 4 DIP base grid. Typical values: 4, 8, 12, 16, 24, 32.

- High-frequency operator buttons need larger targets and clearer grouping.
- Configuration pages can be denser but must retain scan lines and alignment.
- Avoid excessive card margins that reduce usable workspace.
- Do not use a single spacing value everywhere; distinguish inline, group, section, and page spacing.

## Control variants

Define purposeful variants rather than styling each instance:

- primary action;
- secondary action;
- quiet/toolbar action;
- destructive action;
- emergency/safety-adjacent display-only treatment;
- selected navigation item;
- status badge;
- data-entry field;
- read-only value field;
- operation tile or command cluster.

Each variant needs default, hover, pressed, disabled, focus, and selected/error states as applicable.

## Native Fluent theme

The native WPF Fluent theme can provide a base control appearance on .NET 10. Treat it as a platform layer, not the product's complete identity. Override through semantic resources and lightweight styles before replacing standard ControlTemplates.

## Anti-patterns

- hardcoded colors in view XAML;
- large gradients and decorative glow around normal data;
- every group presented as an identical rounded card;
- color-only alarms;
- tiny gray text for operationally important state;
- white-on-blue buttons for every action, destroying hierarchy;
- custom templates for standard controls without keyboard, focus, DPI, automation, and high-contrast coverage;
- copying web/mobile spacing into a dense desktop operator console;
- using icons without visible labels for unfamiliar or destructive actions.
