# Agent Guide

Use this guide when operating the CCFA family as an agent.

1. Route by primary intent, not by all possible downstream work.
2. Read only the owning skill's `SKILL.md` first.
3. If routing is ambiguous, check `ccf-common/references/skill-trigger-registry.yaml`.
4. If the task touches project state, read `ccfa.yaml` and `ccf-common/references/artifact-contracts.md`.
5. If the task names a venue, read `ccf-paper-writer/references/venue-guides/index.md` before the specific venue guide.
6. If final submission policy matters, verify the current official venue page before making final claims.
7. Use merged owner modes instead of removed helper skills: compression and talks are `ccf-paper-writer`; writing review is `ccf-paper-reviewer`; citation audit is `ccf-integrity-auditor`; result figures are `ccf-experiment-designer`; venue/artifact checks are `ccf-submission-checker`.
8. Do not let audit or review skills rewrite content unless the user explicitly asks and routing permits the handoff.
9. Use `ccf-rebuttal-writer` for response prose, reviewer-comment ledgers, and conservative resubmission planning.
