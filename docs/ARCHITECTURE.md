# CCFA Architecture

CCFA is a paper-project workflow family, not a loose collection of unrelated writing prompts. The current 17-skill architecture has one owner per responsibility area, a first-priority humanization overlay, and `ccfa.yaml` plus explicit artifact contracts to keep stages connected.

![Architecture](../assets/ccfa-skills-architecture.svg)

## Core Model

The family has four layers:

| Layer | Purpose | Skills |
| --- | --- | --- |
| Priority humanization overlay | Keep publication prose direct and evidence-faithful alongside its content owner; remove empty defenses and retain meaningful uncertainty. | `ccf-humanization` |
| Research production chain | Move a paper project from project setup to rebuttal. | `ccf-project-scaffolder`, `ccf-pipeline-orchestrator`, `ccf-idea-optimizer`, `ccf-idea-reviewer`, `ccf-literature-monitor`, `ccf-literature-searcher`, `ccf-experiment-designer`, `ccf-visual-composer`, `ccf-paper-to-exemplar`, `ccf-paper-writer`, `ccf-paper-reviewer`, `ccf-integrity-auditor`, `ccf-submission-checker`, `ccf-rebuttal-writer` |
| Shared state and policy | Keep routing, evidence, privacy, source registry, and artifact ownership consistent. | `ccf-common` |
| Family maintenance | Maintain skills, docs, generated SVGs, validation, and releases. | `ccf-skill-forger` |

The main chain is:

```text
publication-prose preflight: recover scientific content and remove empty defenses

scaffold -> orchestrate -> optimize idea -> review idea
         -> monitor recent literature -> search literature
         -> design experiments -> compose visuals -> optional exemplar extraction
         -> write manuscript -> review manuscript -> audit integrity
         -> check submission -> rebuttal / ledger / resubmission
```

The rebuttal stage can loop back to writing, experiments, integrity audit, or submission checks. This is why rebuttal is not a dead-end output skill; it owns response structure and ledger discipline, while actual manuscript edits go back to `ccf-paper-writer`.

## Working Files And Incremental Execution

Preserve explicit paths, existing project mappings, and established folders. When none exist, generated working files use `output/<task>/<artifact-id>/`, with source/assets/cache/build subdirectories created only when needed. One stable ID separates each figure or search topic; ordinary updates replace the current generated artifact. Raw observations, required review baselines, submitted packages, and requested history remain evidence.

An existing editable figure is updated from its authoring source and only affected requested formats are re-exported. A single current specification holds scientific labels, topology, layout, asset provenance, and useful QA state. Local changes do not require a new concept image or duplicate manifests. Failed exports remain explicitly incomplete while the last usable artifact is preserved.

Reference loading follows the current mode. Reuse verified sources and extracted text when still applicable; send paths and changed evidence across handoffs. Complete assessments retain their required evidence coverage. Shared execution rules live in `ccf-common/references/task-modes.md`; file lifetimes and placement live in `ccf-common/references/artifact-contracts.md`.

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
| Humanization and publication-faithfulness | `ccf-humanization` | Runs alongside publication writing; removes rhetorical defenses, preserves scientific facts, and raises only concrete unresolved decisions. Raw plans and assessment-only work do not load it by default. |
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
