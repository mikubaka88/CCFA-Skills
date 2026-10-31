---
name: ccf-paper-reviewer
description: "Review manuscript claims, evidence, and writing without rewriting. Use for 文章审核, 审稿, 稿件有什么硬伤, 结论站得住吗, 投稿成熟度, writing review, and version comparison. Return a structured scientific or writing review; scores need not be explicitly requested. Concept-only judgment belongs to ccf-idea-reviewer even with a full PDF; requested prose edits belong to ccf-paper-writer."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Paper Reviewer

## Preflight And Ownership

Apply [ccf-humanization](../ccf-humanization/SKILL.md) first, then [ccf-common](../ccf-common/SKILL.md); reuse applicable active rules at handoffs. Both remain required. Handoff mode is **PARTIAL**, governed by metadata and Common's [handoff rules](../ccf-common/references/handoff-modes.md).

Assess manuscript claims, support and writing without rewriting. A concept-only question belongs to `ccf-idea-reviewer`, even with a full PDF; requested prose edits belong to `ccf-paper-writer`, and responses/revision ledgers to `ccf-rebuttal-writer`. Do not invent citations, results, missing related work, consensus, score movement or acceptance probabilities. Keep private manuscripts and reviews within the authorized boundary; use public-safe transformed queries under [privacy-and-evidence.md](../ccf-common/references/privacy-and-evidence.md).

Before file work follow [artifact-contracts.md](../ccf-common/references/artifact-contracts.md): reuse canonical paths and one stable task directory, default `ccfa-workfiles/<purpose>/<artifact-id>/`, preserve inputs, update in place, and check UTF-8/Chinese text. A bounded internal check returns findings to its integrating owner without another full report.

## Review Modes And References

| Mode | Assessment and relevant guidance |
| --- | --- |
| `scientific` | Novelty, significance, soundness and the paper's actual evidence, appropriate to contribution type. Use [review-workflow.md](references/review-workflow.md), [universal-review-rubric.md](references/universal-review-rubric.md) and [reviewer-panel.md](references/reviewer-panel.md) as needed. |
| `writing` | Paragraph logic, section flow, terminology, contribution display, claim presentation, captions and LaTeX-facing risks. Use relevant [prose guardrails](../ccf-paper-writer/references/prose-quality-guardrails.md) and `references/writing-review/`; no scientific acceptance score or automatic new experiments. |
| `full` | Scientific plus writing/format checks and consolidated action priorities. |
| `version-comparison` | Read [version-comparison.md](references/version-comparison.md) before scoring. Freeze the comparison contract; keep relative progress and absolute readiness as separate scorecards, with confidence separate from both. |

For scores, panels, AC/meta-review, change conditions, or standard reports, load [review-output-standards.md](../ccf-common/references/review-output-standards.md). [calibration-and-rank.md](references/calibration-and-rank.md) is the sole generic seven-dimension rubric; use a verified venue form when applicable. [venue-review-styles.md](references/venue-review-styles.md) and [desk-checks.md](references/desk-checks.md) apply to consequential venue decisions. Verify current official year/track rules rather than treating legacy guides as final policy; ICLR 2027 review needs its ICLR guidance and AI-use distinction between author pre-review and official assignment.

Identify the draft phase. Internal alignment checks of content-first or results-pending drafts assess explanation and consistency, with absent empirical adequacy `not assessed`; no invented acceptance score, imposed page limit or experiment campaign. Unsupported empirical assertions remain findings. A requested full submission review still reports real evidence incompleteness under its normal rubric. [materials-to-manuscript.md](../ccf-paper-writer/references/materials-to-manuscript.md) defines the draft contract.

## Evidence And Findings

Read the supplied scientific work and relevant dependencies at the requested coverage; filenames and excerpts do not establish whole-paper inspection. Reconstruct contributions, claims and support before judgment. Anchor concerns to actual locations. For every major/critical concern, inspect the strongest supplied passage or appendix that could answer it; record the countercheck and withdraw or narrow refuted criticism. Separate confirmed flaw, unsupported claim, clarification and missing input. Do not force praise, disagreement, or a concern quota.

Resolve consequential gaps through `ccf-literature-searcher` for closest work/benchmarks, `ccf-integrity-auditor` for numerical/citation-support conflicts, or `ccf-experiment-designer` for protocol interpretation. Reuse checks and respect no-browsing/supplied-evidence limits. Review does not authorize manuscript edits or new experiments. A low score needs its deduction and repair condition; confidence and inspected coverage are distinct from quality.

## Optional Independent Expert

[plain-expert-review.md](references/plain-expert-review.md) implements the existing `independent_review` switch as one fresh-context GPT-6 specialist reading, not an extra layer. `off` adds none automatically; `auto` requires a consequential unresolved judgment or useful requested pre-submission check; `on` favors a relevant substantial scientific/full pass when valuable. Explicit requests override the switch for this task without saving changes. Writing-only does not automatically invoke scientific expertise; concept-only stays with the idea owner.

`scripts/prepare_expert_review.py` prepares a source-bound neutral request, never a model call. Pass scope/question, exclusions, material locations and actual execution identity; withhold main-review conclusions, scores, generation history and other candidates. Preserve user model/effort choices and mandatory preflights. Missing GPT-6 or genuine fresh-context support limits only this extra pass. Record actual model, settings and inspected coverage; never claim a human or official reviewer. Verify returned evidence, merge duplicate concerns under stable IDs, and integrate once without votes, repeated full reviews or indefinite debate. Reuse requires matching inputs, guidance, actual runtime/options and coverage.

## Report Contract

For a user-requested report read [fixed-output-format.md](references/fixed-output-format.md): detailed by default, fourteen sections for scientific/full, nine for writing, five only for explicit brief/restrictive output. Narrow scope, a short prompt, or no-score request does not select brief output or broaden the assessment. Honor an explicit venue/user schema. Use the template's typed findings, stable concern IDs and bracketed references; keep one canonical explanation and scorecard rather than a report per role. Preserve historical dimensions/weights for relative comparisons and assess current readiness separately.

For standard scientific/full review with local paper and authorized file output, reuse the established report or the canonical Markdown file in `ccfa-review-reports/`; otherwise return it in context. Follow [review-workflow.md](references/review-workflow.md) for filename/location rules; no dated report per rerun. Validate saved default-format reports with `scripts/validate_version_comparison.py --report`; structural validation does not prove scientific correctness.

Internal contributions return inspected scope, located findings, resolved/open concern IDs and completion conditions, without inheriting a full report or panel. For a [writing context packet](../ccf-paper-writer/references/writing-execution.md), inspect necessary dependencies and preserve declared excerpt/section coverage. Return findings without applying manuscript patches; the writer owns authorized integration.
