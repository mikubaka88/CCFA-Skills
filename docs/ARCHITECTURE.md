# CCFA Architecture

CCFA is a CCF paper-project workflow family. Its job is not to make one large all-purpose skill, but to keep each research stage explicit enough that another agent can route, audit, and hand off without ambiguity.

## Layers

| Layer | Skills |
| --- | --- |
| Project | `ccf-project-scaffolder`, `ccf-pipeline-orchestrator` |
| Planning | `ccf-workflow-planner` |
| Ideation | `ccf-idea-optimizer`, `ccf-idea-reviewer` |
| Evidence | `ccf-literature-searcher`, `ccf-experiment-designer` |
| Manuscript | `ccf-paper-writer`, `ccf-paper-compressor` |
| Review | `ccf-scientific-reviewer`, `ccf-writing-reviewer` |
| Audit | `ccf-integrity-auditor`, `ccf-citation-auditor` |
| Output | `ccf-figure-table-builder`, `ccf-artifact-packager` |
| Submission | `ccf-venue-format-guide`, `ccf-submission-checker` |
| Post-review | `ccf-rebuttal-writer`, `ccf-resubmission-adapter`, `ccf-paper-presenter` |
| Governance | `ccf-common`, `ccf-skill-forger` |

## Relationship Model

The family has three linked tracks:

1. Project track: `ccf-project-scaffolder` creates the workspace, and `ccf-pipeline-orchestrator` maintains stage/gate state in `ccfa.yaml`.
2. Research track: planning -> idea -> literature -> experiments -> writing -> compression -> review.
3. Assurance and output track: integrity/citation audits, figures/tables, artifacts, venue format, submission checks, rebuttal, resubmission, and presentation.

## Design References

ARS, nature-skills, and ARIS are workflow references, not authoritative venue or review sources. CCFA adopts their useful decomposition and automation ideas, but keeps stricter boundaries:

- Discovery and verification are separate: `ccf-literature-searcher` finds new work, while `ccf-citation-auditor` verifies existing citations.
- Review types are separate: `ccf-scientific-reviewer`, `ccf-writing-reviewer`, and `ccf-integrity-auditor` answer different questions.
- Venue rules are separate from content: `ccf-venue-format-guide` handles format requirements, while `ccf-paper-writer` handles manuscript text.
- Post-review tracking is merged: `ccf-rebuttal-writer` owns both response wording and revision ledger tracking.

## Naming Migration

| Old name | Current name | Reason |
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

## Source Of Truth

`SKILL.md` is authoritative. `docs/SKILLS_CATALOG.md`, `ccf-common/references/routing.md`, and `ccf-common/references/skill-trigger-registry.yaml` are audit indexes.
