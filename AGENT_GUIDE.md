# Agent Guide

Use this guide when operating the CCFA family as an agent.

1. Route by primary intent, not by all possible downstream work.
2. Read only the owning skill's `SKILL.md` first.
3. If routing is ambiguous, check `ccf-common/references/skill-trigger-registry.yaml`.
4. If the task touches project state, read `ccfa.yaml` and `ccf-common/references/artifact-contracts.md`.
5. If the task names a venue, read `ccf-paper-writer/references/venue-guides/index.md` before the specific venue guide.
6. For `ccf-paper-writer`, preserve the user's requested output shape. Polishing keeps the original Markdown/LaTeX structure; from-scratch manuscript requests use the target venue guide first and NeurIPS LaTeX fallback when the venue is absent or unspecified.
7. For broad requests, produce dense artifacts rather than fragments. A full-paper request should yield a full manuscript; a closed-loop demo should yield concrete files, reviews, audits, and rebuttal text.
8. If final submission policy matters, verify the current official venue page before making final claims.
9. Use merged owner modes instead of removed helper skills: compression and talks are `ccf-paper-writer`; writing review is `ccf-paper-reviewer`; citation audit is `ccf-integrity-auditor`; result evidence/specs are `ccf-experiment-designer`; publication figure/table layout, Python plotting code, palette, captions, and render QA are `ccf-visual-composer`; venue/artifact checks are `ccf-submission-checker`.
10. Do not let audit or review skills rewrite content unless the user explicitly asks and routing permits the handoff.
11. Use `ccf-rebuttal-writer` for response prose, reviewer-comment ledgers, and conservative resubmission planning.
12. For early idea work, default to exploration before judgment. Route "找方向", "还能怎么做", "这个方向怎么救", and repeated rough-direction discussion to `ccf-idea-optimizer`; use `ccf-idea-reviewer` only when the user explicitly asks for scoring, ranking, or strict selection.
13. For idea-stage literature search, return an opportunity map. Do not let related work alone kill a direction unless the same problem, mechanism, setting, and evidence path are already covered and no credible rescue route remains.
14. For from-scratch submission manuscripts, `ccf-paper-writer` must establish a venue page/word budget before drafting. A short idea should become a full submission-shaped manuscript with `TBD` evidence placeholders; underfilled drafts are expanded, overfilled drafts are compressed by the writer before `ccf-submission-checker` finalizes page compliance.
15. Route "竞品监控", "新论文追踪", "最近有没有类似 idea", and recurring arXiv/OpenReview/venue watch tasks to `ccf-literature-monitor`; route broad related-work, benchmark, dataset, and opportunity-map searches to `ccf-literature-searcher`.
16. Review-style outputs should include quantified scores, confidence, evidence basis, score-change conditions, and independent multi-reviewer panel notes in standard mode.
17. Route figure/table layout, Python plotting code, creative data-analysis plots, palette choice, panel maps, caption placement, float order, visual cross-references, and manuscript visual integration to `ccf-visual-composer`; keep missing data, baselines, metrics, and experiment design with `ccf-experiment-designer`.
