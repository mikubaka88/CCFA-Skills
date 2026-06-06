# Approach Options

Use this file when the user needs strategy comparison, workflow choice, or task decomposition.

## Option Rules

Present 2-3 options only when they are genuinely different. Do not pad the output with weak alternatives.

For each option, include:

```text
Option:
Best for:
What happens first:
Tradeoff:
Risk:
Next CCFA skill:
```

Lead with the recommended option unless the user asks for neutral comparison.

## Common CCFA Routes

Use these routes when they match the user's goal:

- `Clarify first`: `ccf-workflow-planner` -> owning downstream skill.
- `Idea development`: `ccf-idea-optimizer` -> optional `ccf-idea-reviewer` -> optional `ccf-literature-searcher`.
- `Idea selection`: `ccf-idea-reviewer` -> optional `ccf-literature-searcher` -> optional `ccf-idea-optimizer`.
- `Novelty grounding`: `ccf-literature-searcher` -> `ccf-idea-optimizer` or `ccf-paper-writer`.
- `Experiment story`: `ccf-experiment-designer` -> `ccf-paper-writer`.
- `Manuscript improvement`: `ccf-paper-writer` -> `ccf-scientific-reviewer` -> `ccf-writing-reviewer` or `ccf-paper-writer` or `ccf-paper-compressor`.
- `Page limit`: `ccf-paper-compressor` -> optional `ccf-paper-writer`.
- `Post-review response`: `ccf-rebuttal-writer` -> optional writing or experiment handoff.

## Recommendation Criteria

Choose the recommended route by:

1. user's immediate decision,
2. strongest missing input,
3. privacy and evidence constraints,
4. whether novelty or results are current/uncertain,
5. whether the output should be a reusable file,
6. session denylists and handoff mode.

Do not recommend literature search when the immediate need is local text polishing. Do not recommend writing before the idea, evidence, or results are stable enough to support the claims.

## Too-Broad Decomposition

When the request mixes independent workstreams, split it into ordered stages:

```text
Stage:
Owner skill:
Input needed:
Output produced:
Handoff condition:
```

Stop at the first stage unless the user explicitly asks for the full workflow brief.
