# codex-model-router

将多步骤 Codex 任务路由为少量 Sol 决策和大量 Luna 执行。本项目保留源策略，并将其封装为可安装的 Codex Skill，同时明确运行时能力边界。

[English README](README.md)

## 特性

- 使用可审计的 Sol Extra High 与 Luna Max 精确模型配置。
- 在多步骤任务开始时选择路由，也响应用户明确提出的 Sol/Luna 路由要求。
- Sol 仅负责改变方向的判断、纠偏和核心审核。
- 方向确定后，Luna 默认负责整理、抽取、整合、既定逻辑写作、脚本、批处理、按规则分析和格式收尾。
- Sol 到 Luna 的交接必须包含结构化执行信息，并披露运行时能力限制。
- 允许隐式调用，但不声称每个提示都会加载此 Skill。

## 路由矩阵

| 配置 | 模型 | `reasoning_effort` | 主要用途 |
| --- | --- | --- | --- |
| Sol Extra High | `gpt-5.6-sol` | `xhigh` | 任务启动、关键决策、方向纠偏和核心审核 |
| Luna Max | `gpt-5.6-luna` | `max` | 已确定方向下的执行、整理、分析、写作、脚本、批处理和交付 |

任务量大、文件多、上下文长或步骤多，并不单独构成使用 Sol 的理由；关键在于是否出现新的高影响方向判断。

## 安装

直接从 GitHub 使用 Codex Skill 安装器安装。如果仓库是 private，请先确保 Git/GitHub 凭据已配置；安装器 auto 模式会按可用方式访问：

```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py --repo ZP3000/codex-model-router --path skill/codex-model-router
```

Windows PowerShell：

```powershell
$installer = Join-Path $env:USERPROFILE ".codex\skills\.system\skill-installer\scripts\install-skill-from-github.py"
python $installer --repo ZP3000/codex-model-router --path skill/codex-model-router
```

安装后请开始下一轮对话或重启 Codex。Skill 会被全局安装并允许隐式调用，但不保证每次提示都会强制加载。

## 自动与显式调用

多步骤任务可以自动选择此 Skill 来决定路由；也可以显式调用：

```text
Use $codex-model-router to route this multi-step task; use Sol for initial direction and Luna for execution.
```

只有当前运行时支持委派且获得授权时，才实际切换精确模型。模型不可用时必须披露限制，不能伪称已经切换。

## 运行时边界

- Sol 仅用于任务启动规划、关键方案或证据判断、方向级纠偏，以及阶段/最终核心审核。
- 方向确定后，Luna 默认负责检索结果整理、抽取、整合、既定逻辑写作、数据处理、脚本、批量操作、按固定规则分析和格式工作。
- 每次 Sol 到 Luna 的交接都要包含目标、核心结论、关键约束、执行步骤和未解决问题。
- 路由选择不会额外授予外部写入、发送消息或其他副作用的权限。

## 项目结构

```text
skill/codex-model-router/
├── SKILL.md
├── agents/openai.yaml
└── references/source-policy.zh-CN.md
tests/validate_skill.py
```

中文源策略仅在审计或实现对照时阅读；日常调用使用精炼的 `SKILL.md` 入口。

## 验证

在仓库根目录执行：

```bash
python tests/validate_skill.py
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skill/codex-model-router
```

第一条命令不依赖第三方包，检查项目实质不变量；第二条是 Codex Skill 标准结构验证器。

## 贡献

请参阅 [CONTRIBUTING.md](CONTRIBUTING.md)。修改时应保持两个精确模型映射、运行时披露边界和 Sol 到 Luna 的工作流。

## 许可证

本项目采用 [MIT License](LICENSE)。
