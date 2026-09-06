# Contributing

Thanks for helping improve `codex-model-router`.

## Before opening a pull request

- Keep the Skill scoped to model routing and the Sol-to-Luna workflow.
- Preserve the exact profile values: `gpt-5.6-sol` with `xhigh`, and `gpt-5.6-luna` with `max`.
- Do not claim a model switch when the runtime cannot perform delegation.
- Keep the normalized Chinese source policy aligned with the originating policy when changing operational rules.
- Do not add credentials, private data, or invented contact details.

Run the local checks from the repository root:

```bash
python tests/validate_skill.py
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skill/codex-model-router
```

Pull requests should explain the behavioral or documentation change and include the validation result. Keep unrelated formatting churn out of the change.
