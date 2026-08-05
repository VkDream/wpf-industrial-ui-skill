# MVVM, Binding, Commands, and Routing

## Adapt, do not replace

First identify whether the project uses:

- hand-written `INotifyPropertyChanged` and `ICommand`;
- CommunityToolkit.Mvvm;
- Prism;
- ReactiveUI;
- Caliburn.Micro;
- a custom framework.

Use its established patterns. Framework migration is a separate task.

## View responsibilities

Views may contain:

- layout and visual composition;
- bindings, templates, styles, triggers, and visual states;
- view-only focus, selection, drag, resize, and coordinate behavior;
- minimal lifecycle glue when the existing project requires it.

Views must not own:

- production decisions;
- device or MES calls;
- recipe persistence;
- authorization policy;
- alarm state transitions;
- long-running business workflows.

## Command contract

For each command verify:

- the authoritative owner;
- `CanExecute` conditions;
- permission and runtime state gates;
- reentrancy/concurrency behavior;
- cancellation;
- progress and error projection;
- whether the same action appears in menu, toolbar, context menu, keyboard shortcut, or direct manipulation.

All entry points for the same action should converge on the same command or application contract.

## Binding contract

- editing values normally use TwoWay binding and an intentional source update trigger;
- status projections normally use OneWay;
- static labels/content use localization resources, not ViewModel duplication;
- use `FallbackValue` and `TargetNullValue` only when they express a real UI contract;
- investigate binding warnings rather than hiding them;
- avoid converters that contain business logic or expensive work;
- prefer typed ViewModel properties and state projections over converter chains.

## Validation

Use the project's existing validation mechanism. Common options include:

- `INotifyDataErrorInfo`;
- validation rules;
- ViewModel error collections;
- domain result projections.

Show errors near fields and, for long forms, in a summary. Keep Apply/Save command gating consistent with visible errors.

## Navigation

Preserve the existing route mechanism:

- `ContentControl` + DataTemplates;
- custom view locator;
- `Frame`/Page navigation;
- tab/workspace model;
- window/dialog service;
- Prism regions.

Do not add a second navigation stack. Preserve route IDs and back/close behavior.

## Resource architecture

- preserve merged-dictionary order;
- avoid duplicate keys;
- use `BasedOn` deliberately;
- use `DynamicResource` where runtime theme switching requires it;
- use `StaticResource` for stable local references when appropriate;
- do not replace implicit base styles unintentionally;
- test custom controls after changing global implicit styles.

## Performance

- virtualize large collections;
- batch UI-thread updates;
- avoid creating brushes, geometries, and templates repeatedly;
- freeze reusable Freezables when safe;
- move expensive transformation out of converters and property getters;
- avoid event subscriptions that outlive views/ViewModels; use disposal or weak patterns consistent with the project.
