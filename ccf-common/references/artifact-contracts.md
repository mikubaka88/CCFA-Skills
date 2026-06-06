# CCFA Artifact Contracts

These contracts prevent CCFA skills from overwriting each other's work. Read broadly, write narrowly.

| Artifact | Primary owner | Contract |
| --- | --- | --- |
| `ccfa.yaml` | `ccf-project-scaffolder`, `ccf-pipeline-orchestrator` | Scaffold creates it; orchestrator updates stage/gate state. Other skills may read and propose updates. |
| `manuscript/*.tex` | `ccf-paper-writer` | Review and audit skills suggest edits; writing changes route back to paper writer unless user explicitly authorizes otherwise. |
| `references/*.bib` | `ccf-citation-auditor` | Citation auditor verifies existing entries; literature searcher proposes new candidates. |
| `experiments/results.*` | user, `ccf-experiment-designer` | Figure/table and integrity skills read supplied numbers only. |
| `figures/*`, `tables/*` | `ccf-figure-table-builder` | Captions may route through paper writer; data must be real. |
| `reviews/*` | `ccf-scientific-reviewer`, user | Rebuttal writer reads real reviews and maintains response ledger. |
| `reviews/revision-ledger.md` | `ccf-rebuttal-writer` | Tracks reviewer comment -> response promise -> manuscript action -> status. |
| `submission/*` | `ccf-submission-checker` | Stores build, anonymity, page, metadata, and policy readiness results. |
| `artifact/*` | `ccf-artifact-packager` | Tracks code/data/model release and reproducibility package status. |
| `talk/*` | `ccf-paper-presenter` | Presentation outputs only; not submission evidence. |
| governance docs | `ccf-common`, `ccf-skill-forger` | Routing, naming, trigger registry, source registry, validation, and diagrams. |
