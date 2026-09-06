# codex-model-router

Route multi-step Codex work between a small number of deliberate Sol decisions and a larger amount of Luna execution. The package preserves the originating policy while adding an installable Codex Skill with explicit runtime boundaries.

[中文版说明](README.zh-CN.md)

## Features

- Uses exact, auditable model profiles for Sol Extra High and Luna Max.
- Selects a route at the start of a multi-step task and honors explicit Sol/Luna requests.
- Keeps Sol for direction-changing judgment, correction, and core review.
- Makes Luna the default for settled execution, extraction, integration, writing, scripting, batch work, and formatting.
- Requires a structured Sol-to-Luna handoff and discloses unavailable runtime capabilities.
- Allows implicit invocation without claiming that the Skill is loaded for every prompt.

## Route matrix

| Profile | Model | `reasoning_effort` | Primary use |
| --- | --- | --- | --- |
| Sol Extra High | `gpt-5.6-sol` | `xhigh` | Task framing, consequential decisions, direction correction, and core review |
| Luna Max | `gpt-5.6-luna` | `max` | Settled execution, organization, analysis, writing, scripts, batch work, and delivery |

Large workloads do not automatically require Sol: volume, file count, context length, and step count are not substitutes for a new high-impact judgment.

## Installation

Install the Skill directly from GitHub with the Codex Skill installer. If the repository is private, first ensure Git/GitHub credentials are configured; installer auto mode will use an available access method:

```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py --repo ZP3000/codex-model-router --path skill/codex-model-router
```

Windows PowerShell:

```powershell
$installer = Join-Path $env:USERPROFILE ".codex\skills\.system\skill-installer\scripts\install-skill-from-github.py"
python $installer --repo ZP3000/codex-model-router --path skill/codex-model-router
```

Start a new turn or restart Codex after installation. The Skill is globally installed and eligible for implicit invocation; it is not guaranteed to be loaded for every prompt.

## Automatic and explicit invocation

For a multi-step task, the Skill may be selected automatically to choose an appropriate route. For a direct request, invoke it explicitly:

```text
Use $codex-model-router to route this multi-step task; use Sol for initial direction and Luna for execution.
```

You can also state the desired profile in the task. The exact model switch occurs only when delegation is authorized and supported by the current runtime. If a profile is unavailable, the limitation must be disclosed; an agent must never pretend that a switch happened.

## Runtime boundaries

- Sol is reserved for startup planning, consequential method or evidence decisions, direction-level correction, and stage/final core review.
- Luna is the default once the direction is settled, including search-result organization, extraction, integration, established-logic writing, data processing, scripts, batch operations, analysis under fixed rules, and formatting.
- Every Sol-to-Luna handoff contains the goal, core conclusion, key constraints, execution steps, and unresolved questions.
- A route does not grant permission for external writes, messages, or other side effects.

## Project structure

```text
skill/codex-model-router/
├── SKILL.md
├── agents/openai.yaml
└── references/source-policy.zh-CN.md
tests/validate_skill.py
```

The Chinese source policy is a reference for audits and implementation comparisons; routine invocations use the concise `SKILL.md` entrypoint.

## Validation

From the repository root:

```bash
python tests/validate_skill.py
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skill/codex-model-router
```

The first command checks package invariants without third-party dependencies. The second is the standard Codex Skill scaffold validator.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the local validation and pull-request expectations. Changes should preserve the two exact model mappings, the runtime disclosure boundary, and the Sol-to-Luna workflow.

## License

This project is released under the [MIT License](LICENSE).
