# CCFA Artifact Contracts

These contracts prevent v0.4 skills from overwriting each other's work. If a user explicitly asks a skill to write outside its owner area, state the handoff risk and preserve existing artifacts.

| Artifact | Primary owner | Contract |
| --- | --- | --- |
| `ccfa.yaml` | ccf-paper-project-scaffold, ccf-pipeline-orchestrator | Most skills may read; only orchestrator/scaffold should mutate stage by default. |
| `manuscript/*.tex` | ccf-writing-skills | Review/audit skills may suggest edits but should not overwrite text without handoff. |
| `references/*.bib` | ccf-citation-auditor | ccf-literature-search may propose additions; default no-bib-edit for resubmission. |
| `experiments/results.*` | ccf-experiment-designer, user | Figure/table and integrity skills read supplied numbers only. |
| `figures/*, tables/*` | ccf-figure-table-builder | Writing skills may revise captions; do not fabricate data. |
| `reviews/*` | ccf-conference-reviewer, user | Rebuttal and ledger read real reviews. |
| `revision_ledger.*` | ccf-revision-ledger | Rebuttal may reference but not erase tracking. |
| `submission_checks/*` | ccf-submission-checker | Stores build/policy/anonymity/page readiness results. |
| `artifact/*` | ccf-artifact-reproducibility | Tracks reproducibility package and release status. |
| `talk/*` | ccf-paper-talk | Presentation outputs only; not submission evidence. |

## Default Rule

Read broadly, write narrowly. When in doubt, create a proposed patch/checklist instead of overwriting another skill's artifact.
