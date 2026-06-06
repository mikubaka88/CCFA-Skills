# 06 - CCFA Family Self-Audit From This Demo

Owner: `ccf-skill-forger` with `ccf-common`.

This audit is based on running the Attention/ICLR closed-loop demo and comparing `ccf-paper-writer` with the external `Research-Paper-Writing-Skills` repository.

## Problems Found And Fixed

| Problem | Evidence in old behavior | Fix applied |
| --- | --- | --- |
| Writer output was too report-shaped. | Full writing tasks could end as mode/status/checklist text. | `task-modes.md` and `ccf-paper-writer` now require artifact-first output. |
| Demo was too short. | It had abstract, storyline, and notes, but not a full paper. | Added a 6-page compiling ICLR LaTeX manuscript. |
| Full-paper requests were underspecified. | Writer did not explicitly require full sections. | Writer now requires Abstract, Introduction, Background/Related Work, Method, Experiments, Limitations, Conclusion, References, and Appendix/checklist placeholders when appropriate. |
| Section-writing patterns were weaker than Master-cai's guide. | CCFA had general section modules but fewer abstract/intro/method pattern variants. | Added `research-writing-patterns.md` with abstract, introduction, related-work, method, experiment, conclusion, and exemplar-mode rules. |
| ICLR venue guide had an incorrect anonymity assumption. | It said ICLR OpenReview submissions were not anonymous. | Updated guide and index to ICLR 2026 double-blind basics and page-limit basics. |
| Demo did not show source-paper writing mode. | It summarized the paper but did not map original writing pattern to the generated draft. | `00-original-paper-reading.md` and `03-writing-draft.md` now include source-mode preservation tables. |

## Remaining Family Issues

| Issue | Severity | Why it matters | Proposed future work |
| --- | --- | --- | --- |
| Venue guides are still migrated legacy material with uneven freshness. | High | Wrong venue rules can produce invalid TeX or anonymity behavior. | Add official-source verification scripts for top venues and mark stale guides more visibly. |
| ICLR template package is only a `.sty`, not a full official sample project. | Medium | Scaffolder may need to create a fuller template with `references.bib`, appendix, and checklist files. | Add venue-specific scaffold assets for ICLR, NeurIPS, CVPR, ICML, ACL. |
| Related-work search is simulated in the demo. | Medium | A real current ICLR submission requires current literature and modern baselines. | Add a live-search demo variant or a cached verified literature-search folder. |
| Artifact/reproducibility remains checklist-only. | Medium | Submission quality depends on real code/data/env files. | Add a demo artifact package skeleton with README, env, seeds, and data preprocessing notes. |
| Full ablation values are not fully copied from the original paper. | Medium | Reviewers need component causality, not just a plan. | Add a verified ablation table artifact sourced from the official paper. |
| SVG diagrams were not regenerated for the ICLR demo change. | Low | Main architecture diagrams still say demo-attention but may not mention ICLR. | Update generated demo SVG labels after the content stabilizes. |
| No automated LaTeX build check in CI yet. | Medium | Demo TeX can regress silently. | Add a CI job that compiles demo papers when TeX is available, or a lightweight syntax check otherwise. |
| Output-density rule is policy-level, not yet tested with smoke prompts. | Medium | Skills may still produce short outputs if the agent ignores policy. | Add smoke tests for "完整文章", "完整闭环", "详细 review", and "只润色保持格式". |

## Comparison With Master-cai Repository

| Capability | Master-cai writing skill | CCFA after this update |
| --- | --- | --- |
| Section-specific guides | Strong Abstract/Intro/Method/Experiments/Conclusion guides. | Added comparable section patterns plus venue/project governance. |
| Example bank | Many local examples and sentence-logic templates. | Uses exemplar cards and now explicitly extracts source-paper writing modes without copying text. |
| Flow check | Reverse outline and paragraph-flow questions. | Covered in section modules and writing checklists; still needs more smoke tests. |
| Claim-evidence map | Explicit for Abstract/Introduction. | Present in writer, reviewer, and integrity auditor; stronger artifact ownership. |
| Full workflow | Mainly writing-focused. | Broader loop: idea, literature, experiments, writing, review, integrity, submission, rebuttal, maintenance. |
| Venue LaTeX | Not the central focus. | Venue guide branch and scaffold/submission integration. |

Conclusion: CCFA is broader and more governed, but it needed Master-cai-style writing granularity and denser artifact-first output. This update adds those missing controls while keeping CCFA's venue, audit, and closed-loop structure.
