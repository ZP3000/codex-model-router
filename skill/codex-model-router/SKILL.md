---
name: codex-model-router
description: Route multi-step Codex work between Sol Extra High and Luna Max for automatic model selection, and honor explicit Sol/Luna routing requests when model delegation is available.
---

# Codex model router

Use this skill at the beginning of a multi-step task when model choice or delegation can improve the work, or when the user explicitly asks for Sol, Luna, or a model handoff. Automatic selection is allowed; it does not force delegation for every prompt. Do not delegate a simple task merely to demonstrate routing.

## Fixed profiles

| Profile | model | reasoning_effort |
| --- | --- | --- |
| Sol Extra High | `gpt-5.6-sol` | `xhigh` |
| Luna Max | `gpt-5.6-luna` | `max` |

Use the exact profile values above when the runtime supports them. Do not silently substitute another model or reasoning setting.

In field form: Sol Extra High uses `model: gpt-5.6-sol` and `reasoning_effort: xhigh`; Luna Max uses `model: gpt-5.6-luna` and `reasoning_effort: max`.

## Decision and execution workflow

1. At task start, decide whether a new judgment could materially change the task direction. Use Sol Extra High only for task framing and decomposition, a consequential plan or method choice, a complex mechanism, research gap, core scientific, algorithmic, or methodological judgment, a genuinely difficult evidence or logic conflict, a direction correction after execution, or a stage/final core review.
2. Once the direction is clear, hand execution to Luna Max. Luna is the default for post-search organization, screening, deduplication, extraction, multi-file or multi-result integration, structured writing under an established logic, tables and format conversion, scripts, batch file work, rule-based analysis, citation and archive cleanup, and delivery formatting.
3. A large corpus, many files, long context, or many steps does not by itself justify Sol. Ask whether the work needs a new high-impact judgment or only follows an existing rule.
4. If a new contradiction or direction-level problem appears, use Sol again only when it cannot be resolved by applying the established rules. After the decision, return to Luna immediately.
5. If a core review is needed, Sol reviews the logic, evidence chain, reliability of conclusions, and material omissions. Luna then applies the approved corrections and completes the handoff.

## Required handoff

Every Sol-to-Luna handoff must be compact and structured with:

- goal;
- core conclusion or decision;
- key constraints;
- execution steps; and
- unresolved questions.

Avoid having both models repeat the same reading or reasoning. Sol decides what to do and why; Luna carries out the settled work.

Do not use Sol merely because it is stronger, for mechanical list organization, deduplication, or format conversion, to repeat a settled decision, for reassurance, to reread raw material that Luna has already sufficiently organized, or to remain on Sol when no new key problem exists.

## Runtime boundaries

- Switch or delegate only when the current runtime supports delegation and the user/system instructions authorize it. If delegation is unavailable, continue with the available runtime and disclose that the exact route was not applied; never claim a switch that did not happen.
- If an exact profile is unavailable, disclose the limitation and follow higher-priority instructions. Do not present an approximate model as `gpt-5.6-sol` or `gpt-5.6-luna`.
- Preserve the user's requested scope and permissions. A route choice does not grant permission for external writes, messages, or other side effects.

## Source-policy reference

For an audit, an implementation comparison, or a question about the originating Chinese policy, read [the normalized source policy](references/source-policy.zh-CN.md). Do not load that reference on every ordinary invocation; the operational rules above are the routine entrypoint.
