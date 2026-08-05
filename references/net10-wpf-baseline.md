# .NET 10 WPF Baseline

Use this reference before making framework-level choices.

## Project detection

A normal .NET 10 WPF executable project uses a Windows target and WPF enablement, for example:

```xml
<PropertyGroup>
  <OutputType>WinExe</OutputType>
  <TargetFramework>net10.0-windows</TargetFramework>
  <UseWPF>true</UseWPF>
</PropertyGroup>
```

A project may use a Windows-version-qualified target. Preserve the existing target unless migration is explicitly requested.

## Native Fluent theme

WPF on modern .NET includes a native Fluent theme and `ThemeMode` support. In .NET 10, Fluent styling continues to receive fixes and broader control coverage, but it should not be treated as a complete design system for an industrial product.

Possible application-level use:

```xml
<Application
    x:Class="Example.App"
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    ThemeMode="System">
</Application>
```

Or merge the native resource dictionary when that matches the project baseline:

```xml
<ResourceDictionary Source="pack://application:,,,/PresentationFramework.Fluent;component/Themes/Fluent.xaml" />
```

Do not switch a mature application's theme mechanism merely because this API exists. Test custom templates and third-party controls before adopting it.

## WPF versus WinUI guard

WPF uses:

```xml
xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
```

Do not introduce:

- `Microsoft.UI.Xaml` namespaces;
- WinUI-only `x:Bind` assumptions;
- `NavigationView`, `InfoBar`, `TeachingTip`, `SelectorBar`, `TabView`, or other WinUI-only controls unless a WPF library already provides an approved equivalent;
- WinUI window-sizing or AppWindow code.

Use WinUI design ideas only as interaction and visual principles, then map them to actual WPF controls and project components.

## MVVM Toolkit

`CommunityToolkit.Mvvm` is framework-agnostic and suitable for WPF, but it is optional. Use it only when already present or explicitly approved. Do not migrate hand-written, Prism, ReactiveUI, or project-specific MVVM infrastructure solely for stylistic consistency.

## Build baseline

Prefer project-authoritative commands. Typical fallback:

```text
dotnet restore <solution-or-project>
dotnet build <solution-or-project> -c Debug --no-restore
dotnet test <solution-or-test-project> -c Debug --no-build
```

Do not restore or download packages when the task forbids network access or dependency changes. In that case, use existing assets and report the blocker precisely.

## Source references

- Microsoft Learn: What's new in WPF for .NET 10
- Microsoft Learn: WPF styles and templates / Fluent theme
- Microsoft Learn: CommunityToolkit.Mvvm introduction
