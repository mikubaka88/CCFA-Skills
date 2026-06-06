# Naming And Merge Audit

Date: 2026-06-06

## Naming Rule

Runtime skills now follow a single naming style:

```text
ccf-<object>-<role/action>
```

Examples: `ccf-paper-writer`, `ccf-scientific-reviewer`, `ccf-citation-auditor`, `ccf-project-scaffolder`.

`ccf-common` is the only exception because it is not a user-facing workflow skill; it is the shared governance module.

## Merged Skill

`ccf-revision-ledger` was merged into `ccf-rebuttal-writer`. The reason is practical: a revision ledger is only useful when tied to reviewer comments, response promises, manuscript locations, and post-review status. Keeping it as a separate runtime skill created a likely trigger conflict with rebuttal and response-letter prompts.

The ledger template now lives at:

```text
ccf-rebuttal-writer/references/revision-ledger.md
```

## Renamed Skills

| Old name | Current name | Decision |
| --- | --- | --- |
| `ccf-brainstorming` | `ccf-workflow-planner` | Clearer role name; avoids overlap with generic brainstorming. |
| `ccf-literature-search` | `ccf-literature-searcher` | Aligns with role/action naming. |
| `ccf-writing-skills` | `ccf-paper-writer` | Replaces plural family-style name with a single owning role. |
| `ccf-conference-reviewer` | `ccf-scientific-reviewer` | Names the review type, not the venue layer. |
| `ccf-conference-writing-reviewer` | `ccf-writing-reviewer` | Keeps writing review distinct from scientific review. |
| `ccf-conference-paper-rebuttal` | `ccf-rebuttal-writer` | Names the output responsibility. |
| `ccf-conference-guides` | `ccf-venue-format-guide` | Clarifies it handles venue format only. |
| `ccf-paper-project-scaffold` | `ccf-project-scaffolder` | Aligns with role/action naming. |
| `ccf-artifact-reproducibility` | `ccf-artifact-packager` | Clarifies owned artifact output. |
| `ccf-revision-ledger` | `merged into ccf-rebuttal-writer` | Ledger tracking is part of post-review response accountability. |
| `ccf-paper-talk` | `ccf-paper-presenter` | Clarifies presentation ownership. |
| `ccf-forge-skills` | `ccf-skill-forger` | Avoids plural skill-family wording. |

## Non-Merges

- `ccf-venue-format-guide` and `ccf-submission-checker` remain separate: one answers requirements, the other checks real files.
- `ccf-literature-searcher` and `ccf-citation-auditor` remain separate: one discovers new literature, the other verifies existing citations.
- `ccf-scientific-reviewer`, `ccf-writing-reviewer`, and `ccf-integrity-auditor` remain separate: they review different evidence surfaces.
- `ccf-project-scaffolder` and `ccf-pipeline-orchestrator` remain separate: creation and orchestration are different lifecycle responsibilities.
