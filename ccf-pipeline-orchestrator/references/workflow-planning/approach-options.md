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

- `Clarify first`: `ccf-pipeline-orchestrator` -> owning downstream skill.
- `Idea development`: `ccf-idea-optimizer` integrates the idea. Use `ccf-literature-searcher` before consequential novelty claims when relevant verified sources are missing; use `ccf-idea-reviewer` for an unresolved conceptual judgment when needed.
- `Idea selection`: `ccf-idea-reviewer` integrates the assessment, with missing decisive prior art resolved by `ccf-literature-searcher` before the dependent verdict. Requested development then belongs to `ccf-idea-optimizer`.
- `Novelty grounding`: `ccf-literature-searcher` -> `ccf-idea-optimizer` or `ccf-paper-writer`.
- `Experiment story`: `ccf-experiment-designer` -> `ccf-paper-writer`.
- `Manuscript improvement`: `ccf-paper-writer` directly for requested edits; `ccf-paper-reviewer` -> `ccf-paper-writer` when both assessment and revision are requested. Do not insert a review cycle into ordinary polishing.
- `Page limit`: `ccf-paper-writer` compression mode.
- `Post-review response`: `ccf-rebuttal-writer` -> optional writing or experiment handoff.

## Recommendation Criteria

Choose the recommended route by:

1. user's immediate decision,
2. strongest missing input,
3. privacy and evidence constraints,
4. whether novelty or results are current/uncertain,
5. whether the output should be a reusable file,
6. session denylists and handoff mode.

A minor local correction needs no fresh literature search. Substantive expression rewriting follows the effective writing-reference preference, reusing matching originals and applicable prior searches. Draft the supported content when requested, including a results-pending manuscript; keep unavailable outcomes and unsettled claims explicit instead of waiting for the whole study to finish.

## Too-Broad Decomposition

When the request mixes independent workstreams, split it into ordered stages:

```text
Stage:
Owner skill:
Input needed:
Output produced:
Handoff condition:
```

For a planning-only request, return the requested stage plan without executing it. For authorized multi-stage work, complete each requested stage and integrate helper results; do not stop at the first skill boundary or expand into optional stages. Use the shared continuity/return contract in `../../../ccf-common/references/handoff-modes.md`.
