# Naming And Merge Audit

The current v0.7 line keeps CCFA runtime skills small while adding one explicit visual-publication owner with bundled plotting recipes. The goal is not to remove capability, but to remove trigger ambiguity. A user should be able to choose one owner for a request without guessing among small helper skills.

## Current Runtime Surface

| Stage | Runtime skill |
| --- | --- |
| Setup | `ccf-project-scaffolder` |
| Planning | `ccf-pipeline-orchestrator` |
| Idea | `ccf-idea-optimizer`, `ccf-idea-reviewer` |
| Evidence | `ccf-literature-monitor`, `ccf-literature-searcher`, `ccf-experiment-designer`, `ccf-visual-composer` |
| Manuscript | `ccf-paper-writer` |
| Review | `ccf-paper-reviewer` |
| Audit | `ccf-integrity-auditor` |
| Submission | `ccf-submission-checker` |
| Post-review | `ccf-rebuttal-writer` |
| Governance | `ccf-common`, `ccf-skill-forger` |

## Merge Decisions

| Removed runtime entry | New owner | Reason | Boundary after merge |
| --- | --- | --- | --- |
| `ccf-workflow-planner` | `ccf-pipeline-orchestrator` | Both owned task planning, routing, and gate selection. | Orchestrator plans only; it does not perform downstream work. |
| `ccf-paper-compressor` | `ccf-paper-writer` | Compression edits manuscript text and must share writing evidence safeguards. | Writer may compress, but cannot change claims/results. |
| `ccf-writing-reviewer` | `ccf-paper-reviewer` | Writing review is a review mode over the same manuscript. | Reviewer diagnoses; writer edits. |
| `ccf-citation-auditor` | `ccf-integrity-auditor` | Citation verification is part of evidence integrity. | Integrity audits existing citations; literature search finds new papers. |
| `ccf-figure-table-builder` | `ccf-experiment-designer`, then `ccf-visual-composer` | Result content depends on real experiment values; publication visuals and plotting code need a separate layout/QA owner. | Experiment designer owns evidence and values; visual composer owns Python plotting recipes, palette, panel/table layout, captions, manuscript integration, and render QA. |
| `ccf-artifact-packager` | `ccf-submission-checker` | Artifact readiness is part of submission readiness. | Submission checker audits package/artifact; it does not promise unavailable releases. |
| `ccf-venue-format-guide` | `ccf-submission-checker` | Venue format lookup is a submission gate. | Paper writer reads venue references for text; submission checker owns compliance. |
| `ccf-resubmission-adapter` | `ccf-rebuttal-writer` | Resubmission is post-review response and revision planning. | Rebuttal writer defaults to no new experiments/bib changes unless authorized. |
| `ccf-paper-presenter` | `ccf-paper-writer` | Slides, posters, talk scripts, and Q&A are paper-derived writing outputs. | Presentation output does not replace submission review. |
| `ccf-doc-diagram-designer` | `ccf-skill-forger` | Repository docs SVGs are maintenance artifacts. | Skill forger updates generator and screenshot-QAs diagrams. |

## Install Policy

Install only the 16 current runtime skills. Do not copy merged helper names into `$CODEX_HOME/skills`. If an older local install still has those helper directories, remove them before installing the current family to avoid trigger collisions. `ccf-literature-monitor`, `ccf-visual-composer`, and `ccf-paper-to-exemplar` are current runtime entries, not merged helper names.

## Demo Policy

The demo must use the current 16 runtime skills. Merged abilities still appear in the demo as modes:

- compression and talk output inside `ccf-paper-writer`
- source-format-preserving polish and venue-aware LaTeX drafting inside `ccf-paper-writer`
- result evidence/specs inside `ccf-experiment-designer`
- publication visual layout, palette, and render QA inside `ccf-visual-composer`
- citation audit inside `ccf-integrity-auditor`
- venue and artifact checks inside `ccf-submission-checker`
- resubmission notes inside `ccf-rebuttal-writer`
- documentation diagrams inside `ccf-skill-forger`
