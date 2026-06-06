# CCFA Skill Smoke Tests For This Demo

The current runtime surface has 13 skills. This table shows the expected route for the same Attention/NeurIPS scenario.

| Prompt | Expected owner | Demo location | Boundary |
| --- | --- | --- | --- |
| Create a NeurIPS-style paper workspace for the Transformer idea. | `ccf-project-scaffolder` | `ccfa.yaml` | Creates state; does not invent content. |
| Plan the workflow from original paper reading to rebuttal. | `ccf-pipeline-orchestrator` | `02-neurips-skill-run.md` | Routes and gates only. |
| Turn the original paper's attention-only direction into an idea brief. | `ccf-idea-optimizer` | `01-idea-document.md` | Shapes the idea; does not score alternatives. |
| Score the idea's likely NeurIPS risk. | `ccf-idea-reviewer` | `02-neurips-skill-run.md` | Scores idea; does not polish the paper. |
| Search or list related-work targets. | `ccf-literature-searcher` | `02-neurips-skill-run.md` | Finds new work; does not audit fixed citations. |
| Design WMT experiments and build result tables from official values. | `ccf-experiment-designer` | `result-tables.md` | Uses real values only. |
| Draft, polish, compress, or make a talk outline. | `ccf-paper-writer` | `03-writing-draft.md` | Writes text; does not review or rebut. |
| Run scientific and writing review. | `ccf-paper-reviewer` | `04-review-and-rebuttal.md` | Diagnoses; does not rewrite. |
| Audit claims, numbers, and citations. | `ccf-integrity-auditor` | `04-review-and-rebuttal.md` | Checks support; does not search broadly. |
| Check NeurIPS format/package/artifact readiness. | `ccf-submission-checker` | `05-submission-check.md` | Checks package; does not polish. |
| Draft rebuttal and revision ledger. | `ccf-rebuttal-writer` | `04-review-and-rebuttal.md` | Responds to reviews; not ordinary writing. |
| Check shared routing and artifact contracts. | `ccf-common` | all files | Governance only. |
| Maintain this demo's docs and SVGs. | `ccf-skill-forger` | `tools/build_ccfa_diagrams.py`, assets | Maintenance only. |
