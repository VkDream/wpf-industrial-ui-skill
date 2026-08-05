# WPF 工业界面设计 Skill

这是一个面向 **.NET 10 WPF 工业桌面软件**的 Agent Skill，用于设计、实现、调整、重构和验收前端界面。

它不会为了“看起来现代”就替换项目原有架构，而是优先保留现有的：

- MVVM 与 View/ViewModel 映射；
- 导航、对话框和依赖注入方式；
- 命令、`CanExecute` 与权限门控；
- 参数 Owner、运行状态和业务合同；
- ResourceDictionary、主题、图标和多语言体系；
- 硬件、MES、安全、授权和生产能力边界。

## 适用范围

适合以下场景：

- 新建或调整 .NET 10 WPF 操作员主界面；
- 工业相机、视觉、CAD、设备状态和操作台布局；
- 参数配置、设备调试、诊断和报警界面；
- 现有 XAML 的视觉统一与增量重构；
- 检查 DPI、多语言、可访问性和完整交互状态；
- 根据截图或设计参考实现 WPF 界面。

不用于：

- WinUI、MAUI、Avalonia、Web 前端；
- 后端业务、设备 DLL、算法或数据库开发；
- 擅自引入第三方 UI 框架；
- 用界面效果冒充真实硬件、MES、安全或生产验收。

## 支持模式

| 模式 | 用途 |
|---|---|
| `DESIGN` | 输出界面结构、信息层级、布局、设计 Token 和状态合同，不修改生产文件。 |
| `IMPLEMENT` | 在现有 WPF 项目中实现明确的界面需求。 |
| `REFACTOR` | 保持功能和公共合同不变，整理视觉与 XAML 结构。 |
| `REVIEW` | 只读检查 XAML、MVVM、主题、DPI、多语言和状态覆盖。 |
| `VISUAL_QA` | 根据运行界面或截图检查布局、对齐、状态和交互问题。 |

## 环境要求

- Windows；
- WPF；
- `.NET 10`，通常为 `net10.0-windows` 或带 Windows 版本限定的 .NET 10 TargetFramework；
- 项目启用 `<UseWPF>true</UseWPF>`；
- 可选：Python 3.10+，用于运行静态审计脚本。

## 安装

### 用户级安装

将仓库复制到：

```text
%USERPROFILE%\.agents\skills\wpf-industrial-ui-design\
```

使用 Git：

```powershell
git clone https://github.com/VkDream/wpf-industrial-ui-skill.git `
  "$env:USERPROFILE\.agents\skills\wpf-industrial-ui-design"
```

### 项目级安装

将仓库放到项目的：

```text
<项目根目录>\.agents\skills\wpf-industrial-ui-design\
```

Codex 运行时真正使用的核心内容为：

```text
SKILL.md
agents/
assets/
references/
scripts/
```

仓库中的 `README.md`、`LICENSE`、示例和 GitHub Actions 只用于公开说明与维护。

## 调用示例

```text
$wpf-industrial-ui-design

读取当前 .NET 10 WPF 项目的 AGENTS.md、知识库、Shell、ViewModel、
命令、权限、导航和资源字典，增量设计并实现操作员主界面。

保持现有业务合同和 Owner，不增加第三方 UI 依赖；完成默认、悬停、
按下、禁用、焦点、选中、校验错误、加载、空态、离线、模拟和故障
等适用状态。分别报告静态检查、构建、运行、截图和人工验收证据。
```

更多话术见 [`examples/prompts.md`](examples/prompts.md)。

## 静态审计脚本

仓库包含：

```text
scripts/audit_wpf_ui.py
```

运行方式：

```powershell
python scripts/audit_wpf_ui.py C:\Path\To\Your\WpfProject
```

它会检查：

- TargetFramework 与 `UseWPF`；
- XAML XML 结构；
- WinUI 命名空间或 `x:Bind` 混入；
- 重复的资源 Key；
- View 内硬编码颜色；
- XAML 事件处理器密度；
- Resource 引用和部分布局风险。

该脚本是**启发式静态审计**，不等于编译、启动、交互或视觉验收。

## 核心设计原则

1. 项目规则优先于通用 Skill。
2. 先识别现有架构和设计系统，再修改 XAML。
3. 按操作员任务和机器状态组织界面，而不是堆叠装饰卡片。
4. 不默认安装 CommunityToolkit、Prism、Syncfusion、HandyControl、MahApps、MaterialDesign 等依赖。
5. 不把 WPF 与 WinUI 控件、命名空间或 `x:Bind` 混用。
6. 权限必须覆盖按钮、快捷键、手势、右键菜单和直接操作路径。
7. 构建成功、启动成功、截图正常和用户验收必须分开报告。
8. 模拟界面、NoHardware 或占位按钮不得被解释为真实设备能力。

## 目录结构

```text
wpf-industrial-ui-skill/
├─ SKILL.md
├─ agents/
│  └─ openai.yaml
├─ assets/
│  └─ industrial-design-tokens-template.xaml
├─ references/
│  ├─ accessibility-dpi-localization.md
│  ├─ design-system.md
│  ├─ existing-theme-adaptation.md
│  ├─ interaction-states.md
│  ├─ layout-patterns.md
│  ├─ mvvm-and-routing.md
│  ├─ net10-wpf-baseline.md
│  ├─ verification.md
│  └─ visual-quality-rubric.md
├─ scripts/
│  └─ audit_wpf_ui.py
├─ examples/
│  └─ prompts.md
├─ CHANGELOG.md
├─ LICENSE
└─ README.md
```

## 当前状态

```text
版本：v0.1.0 Preview
目标：.NET 10 WPF
状态：公开预览版，投入生产前必须结合项目规则进行审查
```

## 许可证

MIT License，详见 [`LICENSE`](LICENSE)。
