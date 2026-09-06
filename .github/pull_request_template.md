## Summary

<!-- What changed, and why? Keep the scope focused. -->

## Validation

- [ ] `python tests/validate_skill.py`
- [ ] `python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skill/codex-model-router`

## Compatibility review

- [ ] The exact Sol mapping remains `gpt-5.6-sol` + `xhigh`.
- [ ] The exact Luna mapping remains `gpt-5.6-luna` + `max`.
- [ ] Runtime limitations are disclosed; no unsupported switch is presented as successful.
- [ ] The Chinese source policy and the operational Skill remain semantically aligned.

## Checklist

- [ ] I removed credentials and private data.
- [ ] I added or updated documentation for user-visible behavior.
- [ ] I kept unrelated formatting churn out of this pull request.
