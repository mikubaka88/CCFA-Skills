# Skill Self-Tests

The current runtime surface has 16 skills. These smoke prompts check routing for the Attention/ICLR closed-loop demo.

| Prompt intent | Expected skill | Demo evidence |
| --- | --- | --- |
| Create an ICLR-style paper workspace for the Transformer idea. | `ccf-project-scaffolder` | `ccfa.yaml`, `paper/iclr2026_conference.sty`. |
| Plan the workflow from source reading to rebuttal. | `ccf-pipeline-orchestrator` | `02-iclr-closed-loop-skill-run.md`. |
| Turn the source paper into a reusable idea brief. | `ccf-idea-optimizer` | `01-idea-document.md`. |
| Score the idea's ICLR risk before writing. | `ccf-idea-reviewer` | `03-idea-review.md`. |
| Search or list related-work targets. | `ccf-literature-searcher` | `02-iclr-closed-loop-skill-run.md`, Related Work in TeX. |
| Design WMT evidence tables and ablation plan. | `ccf-experiment-designer` | `official-data.md`, `result-tables.md`, TeX experiment section. |
| Generate paper-ready SVG plots from verified result data. | `ccf-visual-composer` | `visual-composer/plot_demo.py`, `visual-composer/figures/*.svg`. |
| Draft and optimize the full ICLR manuscript. | `ccf-paper-writer` | `03-writing-draft.md`, `paper/attention_iclr_submission.tex`. |
| Review writing and scientific quality. | `ccf-paper-reviewer` | `04-review-and-rebuttal.md`. |
| Check claims, numbers, and citations. | `ccf-integrity-auditor` | `04-review-and-rebuttal.md` integrity table. |
| Check ICLR format/package/artifact readiness. | `ccf-submission-checker` | `05-submission-check.md`. |
| Draft response and revision ledger. | `ccf-rebuttal-writer` | `04-review-and-rebuttal.md` rebuttal section. |
| Check shared routing and artifact contracts. | `ccf-common` | `02-iclr-closed-loop-skill-run.md`, `06-family-self-audit.md`. |
| Maintain skills/docs/SVG/release quality. | `ccf-skill-forger` | writer policy updates and family self-audit. |

Conflict checks:

- "润色并保持 LaTeX 格式" routes to `ccf-paper-writer`, not `ccf-paper-reviewer`.
- "完整审稿/评分" routes to `ccf-paper-reviewer`, not `ccf-paper-writer`.
- "引用是否真实支撑 claim" routes to `ccf-integrity-auditor`, not `ccf-literature-searcher`.
- "ICLR page limit / anonymity / build" routes to `ccf-submission-checker`, not writer.
