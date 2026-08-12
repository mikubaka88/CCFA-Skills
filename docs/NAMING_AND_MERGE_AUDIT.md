# Naming And Merge Audit

The current v0.8 line keeps the established 17-skill architecture while adding a first-priority humanization preflight and extending the explicit visual-publication owner with scientific architecture generation and editable reconstruction. The goal is not to add a parallel lifecycle, but to keep trigger ownership clear across the existing paper-project chain.

## Current Runtime Surface

| Stage | Runtime skill |
| --- | --- |
| Priority preflight | `ccf-humanization` |
| Setup | `ccf-project-scaffolder` |
| Planning | `ccf-pipeline-orchestrator` |
| Idea | `ccf-idea-optimizer`, `ccf-idea-reviewer` |
| Evidence | `ccf-literature-monitor`, `ccf-literature-searcher`, `ccf-experiment-designer`, `ccf-visual-composer` |
| Exemplar ingestion | `ccf-paper-to-exemplar` |
| Manuscript | `ccf-paper-writer` |
| Review | `ccf-paper-reviewer` |
| Audit | `ccf-integrity-auditor` |
| Submission | `ccf-submission-checker` |
| Post-review | `ccf-rebuttal-writer` |
| Governance | `ccf-common`, `ccf-skill-forger` |

The table contains all 17 runtime skills. No runtime skill is currently redundant enough to delete safely.

## Ambiguity And Conflict Audit

| Boundary | Canonical decision | Why both owners remain |
| --- | --- | --- |
| `ccf-paper-writer` vs `ccf-paper-reviewer` | Writer edits manuscript text and applies supplied findings. Reviewer owns simulated reviewers, formal scores, AC/meta-review, and cross-version judgment. | Editing and independent judgment require different evidence and mutation boundaries. |
| Relative progress vs absolute readiness | Version comparison keeps a frozen historical/current progress scorecard and a separate current-version venue-readiness scorecard. Confidence is reported separately; the scores are never combined. | A paper may improve without becoming acceptance-ready. The two questions must not share one aggregate score. |
| `ccf-humanization` vs prose guardrails | Humanization is the single source for defensive-writing and measurable pattern thresholds. Prose guardrails own cohesion, section logic, and academic expression and reference the shared thresholds. | Centralizing thresholds prevents numerical drift while retaining the v0.7 writing-quality layer. |
| `ccf-paper-to-exemplar` vs `ccf-paper-writer` | Exemplar skill ingests and distills user-provided PDFs; writer consumes selected cards and authors text. | PDF conversion is a library-maintenance mutation, not ordinary manuscript writing. |
| `ccf-literature-monitor` vs `ccf-literature-searcher` | Monitor owns recurring, time-bounded watch reports; searcher owns deep retrieval and screening for a concrete research question. | Recurrence and deep evidence retrieval have different persistence and freshness contracts. |
| `ccf-experiment-designer` vs `ccf-visual-composer` | Experiment designer owns values, protocols, metrics, and evidence meaning. Visual composer owns composition, icons, rendering, and editable reconstruction. | The visual owner must not invent experiment content. |
| `ccf-project-scaffolder` vs `ccf-pipeline-orchestrator` | Scaffolder creates the workspace and initial state; orchestrator updates stages and gates. | Initial filesystem mutation is distinct from continuing coordination. |
| `ccf-common` vs `ccf-skill-forger` | Common owns shared runtime governance contracts. Skill forger changes skills, docs, manifests, validators, and releases. | A shared policy module is not the same as the maintenance operator. |
| Generated intermediates vs evidence history | Necessary skill-generated intermediates use one canonical path and are overwritten on the next iteration. User inputs, raw measurements, submissions, monitoring history, and required audit evidence are not deleted by this rule. | This prevents duplicate attempts without destroying evidence or user-managed history. |

## v0.7 Constraint Compatibility

The v0.7 writing-quality guardrails, multi-expert storyline construction, quantitative feedback discipline, and publication-visual owner remain active. The current family narrows their ownership without removing them:

- multi-expert storyline generation remains a writer planning aid for full manuscripts and explicit narrative work;
- formal reviewer simulation and scoring route to `ccf-paper-reviewer`, avoiding a second reviewer inside the writer;
- defensive-writing and measurable prose thresholds route to `ccf-humanization`, while writer guardrails retain cohesion and section-level academic quality;
- the v0.7 criterion score, overall stance, and confidence fields remain valid; cross-version work adds two separate scorecards rather than replacing those fields;
- necessary generated intermediates remain allowed, but repeated generations overwrite the canonical path unless the user requests named alternatives or snapshots.

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

Install only the 17 current runtime skills. Do not copy merged helper names into `$CODEX_HOME/skills`. If an older local install still has those helper directories, remove them before installing the current family to avoid trigger collisions. `ccf-humanization`, `ccf-literature-monitor`, `ccf-visual-composer`, and `ccf-paper-to-exemplar` are current runtime entries, not merged helper names.

## Demo Policy

The demo must use the current 17 runtime skills. Merged abilities still appear in the demo as modes:

- compression and talk output inside `ccf-paper-writer`
- source-format-preserving polish and venue-aware LaTeX drafting inside `ccf-paper-writer`
- result evidence/specs inside `ccf-experiment-designer`
- publication visual layout, palette, and render QA inside `ccf-visual-composer`
- citation audit inside `ccf-integrity-auditor`
- venue and artifact checks inside `ccf-submission-checker`
- resubmission notes inside `ccf-rebuttal-writer`
- documentation diagrams inside `ccf-skill-forger`
