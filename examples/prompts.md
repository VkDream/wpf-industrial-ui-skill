# 调用话术示例

## 1. 创建操作员主界面

```text
$wpf-industrial-ui-design

读取当前 .NET 10 WPF 项目的规则、知识库、Shell、ViewModel、命令、
权限和资源字典。设计并实现视觉优先的操作员工作区：主区域为相机或
工艺画布，旁边放置高频操作台，持续显示机器状态、当前步骤、报警和
模拟/离线边界。保持现有路由、Owner 和命令，不新增第三方 UI 依赖。
```

## 2. 只读评审现有界面

```text
$wpf-industrial-ui-design

以 REVIEW 模式只读检查当前 WPF 界面。重点检查信息层级、对齐、资源复用、
Binding、Command、权限、加载/空态/错误/离线/故障状态、DPI、多语言、
硬编码颜色和事件处理器。不要修改文件，按 P0/P1/P2 输出问题和依据。
```

## 3. 增量重构配置页

```text
$wpf-industrial-ui-design

以 REFACTOR 模式整理机器配置界面。保持 ViewModel、命令、保存格式、
参数 Owner 和导航不变；统一间距、字号、标签、输入控件、校验提示和
Apply/Revert/Dirty 状态。不要重写 Shell，不添加 UI 框架。
```

## 4. 根据截图实现

```text
$wpf-industrial-ui-design

根据提供的截图调整当前 .NET 10 WPF 页面。先测量区域比例、间距、对齐、
字号和控件状态，再增量修改 XAML。完成构建后用同尺寸截图比较，至少迭代
一次；截图只作为视觉证据，不代替功能和用户验收。
```

## 5. 工业 UI 静态审计

```text
$wpf-industrial-ui-design

运行 scripts/audit_wpf_ui.py 对已授权的 WPF 项目范围做静态审计，解释每条
告警是否真实适用。不得把脚本通过解释为构建、运行或 GUI 验收通过。
```
