# CCFA Architecture

CCFA is a paper-project workflow family, not a loose collection of unrelated writing prompts. The current 17-skill architecture has one owner per responsibility area, a first-priority humanization overlay, and `ccfa.yaml` plus explicit artifact contracts to keep stages connected.

![Architecture](../assets/ccfa-skills-architecture.svg)

## Core Model

The family has four layers:

| Layer | Purpose | Skills |
| --- | --- | --- |
| First family preflight | Before every skill, keep communication direct and evidence-faithful; apply detailed prose/experiment modes when relevant. | `ccf-humanization` |
| Research production chain | Move a paper project from project setup to rebuttal. | `ccf-project-scaffolder`, `ccf-pipeline-orchestrator`, `ccf-idea-optimizer`, `ccf-idea-reviewer`, `ccf-literature-monitor`, `ccf-literature-searcher`, `ccf-experiment-designer`, `ccf-visual-composer`, `ccf-paper-to-exemplar`, `ccf-paper-writer`, `ccf-paper-reviewer`, `ccf-integrity-auditor`, `ccf-submission-checker`, `ccf-rebuttal-writer` |
| Shared family preflight | After Humanization and before every specialist, establish scope, routing, prerequisites, evidence, and artifact controls. | `ccf-common` |
| Family maintenance | Maintain skills, docs, generated SVGs, validation, and releases. | `ccf-skill-forger` |

Compose work around requested outcomes and their prerequisites. One owner integrates each artifact; other skills contribute necessary grounding, scientific checks, and specialist output without requiring separate user requests. Reuse applicable evidence and select dependencies by their effect on the result. Typical paths include:

```text
idea judgment: closest-work grounding when missing -> concept review
substantial writing: evidence/citation grounding -> writer -> affected review -> verified revision
review + revision: reviewer -> writer -> affected checks, retaining resolved concerns
new scientific figure: data/topology prerequisites -> visual composer -> render QA
existing figure label update: reuse scientific inputs -> source edit -> affected exports

Every path begins with Humanization -> Common -> specialist work.
Reuse active preflight rules at handoffs; detailed editing is task-dependent.
Scaffolding, orchestration, monitoring, exemplars, and submission checks
are selected when requested or necessary for a concrete deliverable.
```

Rebuttal owns response structure and ledger discipline; requested manuscript edits belong to `ccf-paper-writer`. Contributors return evidence and findings to the integrating owner, who resolves conflicts and verifies affected results. Return to upstream work when a dependency changes. Finish when requested outputs and applicable prerequisites/checks are complete, or explicitly identify the dependent result that remains incomplete. Role boundaries prevent responsibility confusion without preventing collaboration.

## Working Files And Incremental Execution

The file contract is the first instruction section in every runtime skill. Preserve explicit paths and this artifact's existing mappings/task folder. When none exist, generated working files use `ccfa-workfiles/<purpose>/<artifact-id>/`, such as `figures/method-overview/` or `reviews/paper-short-title/` beneath that root. Create source/assets/cache/build subdirectories only as needed. Names describe the task and content; the same artifact keeps its directory across skill transitions. Ordinary updates replace the current generated file, while raw observations, required comparison baselines, submitted packages, and requested history remain evidence. Clean only verified disposable files created by the task.

An existing editable figure is updated from its authoring source and only affected requested formats are re-exported. A single current specification holds scientific labels, topology, layout, asset provenance, and useful QA state. Local changes do not require a new concept image or duplicate manifests. Failed exports remain explicitly incomplete while the last usable artifact is preserved.

Reference loading follows the current mode. Reuse sources/checks only while their version, assumptions, coverage, and freshness support the decision. Pass the concrete question, prerequisite status, evidence anchors, paths, and completion condition. Internal checks return findings without another intake form or full report; requested reviews keep their templates and evidence coverage. Token efficiency comes from eliminating duplicate work and irrelevant context while completing necessary prerequisites. Conditional dependency routes live in `ccf-common/references/routing.md`, execution guidance in `task-modes.md`, handoffs in `handoff-modes.md`, and file placement in `artifact-contracts.md` under that shared reference directory.

## Artifact State

`ccfa.yaml` records the project state:

- `version`
- `project`
- `target_venue`
- `stage`
- `artifacts`
- `claims`
- `experiments`
- `reviews`
- `revision_ledger`
- `submission_checks`

The file is not meant to contain the whole paper. It is a routing and status spine. Concrete outputs still live in manuscript, review, evidence, experiment, submission, artifact, and rebuttal files.

![Artifact contract](../assets/ccfa-skills-artifacts.svg)

## Owner Boundaries

The family intentionally merged helper skills into owner modes. `ccf-visual-composer` carries a small self-contained Python SVG plotting recipe library for reproducible data figures and an architecture-diagram workflow: content-derived prompt, authorized image generation, draft inspection, and semantic SVG/vector-PDF reconstruction when requested. Existing authorization covers the required stages; optional extra formats remain optional.

| Capability | Owner | Boundary |
| --- | --- | --- |
| Humanization and publication-faithfulness | `ccf-humanization` | First preflight for every CCFA skill, including planning, review, and visuals. Preserve rigorous criticism and facts; apply detailed editing only to authorized prose and relevant experiment work. |
| Workflow planning | `ccf-pipeline-orchestrator` | Coordinates stages; does not write, search, review, or rebut. |
| Literature monitoring | `ccf-literature-monitor` | Tracks recent papers, venue feeds, labs, and competitors; deep retrieval stays with literature search. |
| Compression and presentations | `ccf-paper-writer` | Changes manuscript-derived text; does not judge acceptance risk. |
| Exemplar extraction | `ccf-paper-to-exemplar` | Converts PDFs into writing pattern cards; does not draft or review manuscripts. |
| Writing review | `ccf-paper-reviewer` | Diagnoses writing and format-facing risk; does not rewrite unless handed back to writer. |
| Citation audit | `ccf-integrity-auditor` | Checks existing citations; broad discovery stays with literature search. |
| Result evidence and specs | `ccf-experiment-designer` | Uses real results; never invents numbers. |
| Publication visuals | `ccf-visual-composer` | Owns reproducible data plots plus research method/architecture diagrams, GPT Image 2-first generation, post-generation editable SVG/PDF/PPTX reconstruction, explicit pure-SVG opt-out, palettes, captions, manuscript integration, and render QA. |
| Venue format and artifacts | `ccf-submission-checker` | Checks package readiness; content polishing stays with writer. |
| Resubmission adaptation | `ccf-rebuttal-writer` | Maintains response/ledger logic; manuscript edits route back to writer. |
| Docs SVGs | `ccf-skill-forger` | Repository maintenance only; research figures/tables stay with experiment designer and visual composer. |

![Review boundaries](../assets/ccfa-skills-review-boundaries.svg)

## Venue Branch

Venue-specific LaTeX and policy notes are reference material:

```text
ccf-paper-writer/references/venue-guides/index.md
ccf-paper-writer/references/venue-guides/<venue>.md
```

Use `ccf-paper-writer` for venue-aware manuscript text and page-budget-aware drafting. Use `ccf-submission-checker` for final page limits, anonymity, PDF metadata, camera-ready checks, and package readiness. If a from-scratch writing request names a venue, writer reads the venue guide and length budget first; if no venue is named or the guide is missing, writer falls back to the NeurIPS template. Writer expands substantive omissions and compresses overlength drafts before final submission checks; page fill alone does not justify padding or repeated compile loops.

## Source Of Truth

`SKILL.md` is authoritative for runtime behavior. These files are public indexes and audit aids:

- [SKILLS_CATALOG.md](SKILLS_CATALOG.md)
- [NAMING_AND_MERGE_AUDIT.md](NAMING_AND_MERGE_AUDIT.md)
- `ccf-common/references/routing.md`
- `ccf-common/references/skill-trigger-registry.yaml`
- `ccf-common/references/artifact-contracts.md`
