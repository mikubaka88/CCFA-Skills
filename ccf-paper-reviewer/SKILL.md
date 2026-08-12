---
name: ccf-paper-reviewer
description: "Own assessment-only manuscript deliverables without rewriting: full scientific review, scoring, reviewer reports, issue diagnosis, AC/meta-review, readiness judgment, writing/format review, and cross-version comparison. Use for full review, scientific review, do not rewrite, assessment-only, paper review, score drift, moving-target review, 完整审稿, 不要改写, 模拟审稿, 论文评分, 版本对比, 复审一致性, 写作评审, LaTeX检查. Requests for revised or polished prose, including rewrite based on reviews with no new review, belong to ccf-paper-writer; rebuttals belong to ccf-rebuttal-writer; visual/table styling belongs to ccf-visual-composer."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Paper Reviewer

## Invocation Controls

**CCFA Handoff Mode: PARTIAL (Recommended).** Follow `metadata.ccf_skill_controls.handoff_question_mode`, `../ccf-common/references/handoff-modes.md`, and `../ccf-common/references/task-modes.md`.

Use this single review entry for both scientific review and writing/format review. Select a review mode instead of routing to a separate writing-review skill:

- `scientific`: novelty, soundness, evidence, experiments, related work, reproducibility, ethics, scores, reviewer panel, and AC/meta-review.
- `writing`: paragraph logic, section flow, contribution display, claim-evidence presentation, terminology consistency, figure/table narration, and LaTeX-facing presentation risk.
- `full`: scientific + writing + format + revision-action synthesis.
- `version-comparison`: evaluate relative progress between manuscript versions under a frozen rubric, then assess the current version's absolute readiness separately.

Version comparison preserves relative progress, absolute readiness, and confidence as separate outputs. Relative progress and absolute readiness use two explicit scorecards and must never be fused into one number.

Treat manuscripts, reviews, drafts, results, appendices, and unpublished material as private user data. Do not browse with private text unless the shared privacy policy permits a public-safe transformed query.

Load `../ccf-common/references/review-output-standards.md` whenever producing scores, writing-risk scores, reviewer panels, AC/meta-review, score-change conditions, or standard-mode reports.

## Core Rule

Act as a strict but fair reviewer and AC. Produce decision-relevant findings, not prose rewrites. Do not rewrite manuscript prose. Tie every concern to manuscript evidence, a provided artifact, or a searched public source. Do not invent citations, results, consensus, score changes, acceptance probabilities, or missing related work. Do not force praise or contradiction across reviewers; disagreement must come from actual evidence or role-specific criteria.

Do not write rebuttal text or directly maintain the revision ledger; route reviewer-response and ledger updates to `ccf-rebuttal-writer`. Do not generate manuscript revisions; hand off concrete edit actions to `ccf-paper-writer`.

## Workflow

1. Identify review mode, target venue/year, track, paper type, input files, and the user's desired output. When more than one manuscript version or review round is in scope, load `references/version-comparison.md` before scoring.
2. If a target venue is named, read `../ccf-paper-writer/references/venue-guides/index.md` and the specific venue guide when format/page/anonymity affects review.
3. Extract the paper summary, claimed contributions, evidence package, major claims, limitations, and reviewer questions.
4. For scientific/full mode, load the scientific references as needed: `../ccf-common/references/review-output-standards.md`, `references/review-workflow.md`, `references/universal-review-rubric.md`, `references/venue-review-styles.md`, `references/reviewer-panel.md`, `references/calibration-and-rank.md`, and `references/desk-checks.md`.
5. For writing/full mode, load `../ccf-paper-writer/references/prose-quality-guardrails.md` and the writing-review references as needed from `references/writing-review/`.
6. Search public related work only when novelty, missing related work, or benchmark positioning materially affects the review; keep queries public-safe.
7. Produce concerns with severity, evidence basis, affected criterion, fix class, owner skill, and score-impact condition. Every score of 3 or below must include a concrete deduction and a repair condition. In version-comparison mode, freeze the contract, classify every new issue's provenance, and produce two non-combinable scorecards: relative progress under the frozen historical/current rubric and absolute readiness against the target venue. Report confidence separately.
8. For standard scientific/full mode, write or overwrite the canonical Markdown report in `ccfa-review-reports/` when a local paper path exists; otherwise return the report in the current context. Follow `../ccf-common/references/artifact-contracts.md`; do not make a dated report per iteration.

## Output Contracts

For standard review:

```text
Mode:
Venue and assumptions:
Paper summary:
Likely stance and calibrated score:
Quantitative scorecard:
Top strengths:
Major/fatal concerns:
Writing and presentation concerns:
Format/venue concerns:
Multi-reviewer panel:
Concern-to-action table:
Recommended next CCFA owner:
Checks run:
Unresolved or unverified:
Output self-check:
```

For quick review:

```text
Mode:
Likely stance:
Top concerns:
Immediate fixes:
Missing checks:
Next owner:
```

For version comparison:

```text
Frozen comparison contract:
Relative-progress scorecard:
  Historical / current / delta / weight by dimension:
  Weighted progress delta and classification:
Issue ledger changes and provenance:
Traceable score decreases:
Absolute-readiness scorecard:
  Current dimension scores:
  Overall score or stance and threshold:
  Remaining blocking evidence:
Confidence and comparability:
Next owner:
```

## Reference Files

- `references/review-workflow.md`: scientific review process.
- `references/fixed-output-format.md`: fixed report format.
- `references/universal-review-rubric.md`: scientific dimensions and claim-evidence audit.
- `references/venue-review-styles.md`: venue-family expectations.
- `references/reviewer-panel.md`: simulated reviewers and AC/meta-review.
- `references/calibration-and-rank.md`: scores, ranks, and confidence.
- `references/version-comparison.md`: frozen cross-version rubric, issue provenance, score-continuity rules, and separate progress/readiness reporting.
- `scripts/validate_version_comparison.py`: deterministic validation of a structured comparison contract and its score changes.
- `references/desk-checks.md`: desk and policy checks.
- `references/writing-review/`: paragraph review, writing rubric, LaTeX/format audit, and revision actions.
- `../ccf-paper-writer/references/prose-quality-guardrails.md`: prose anti-patterns and cohesion checks for writing review.
- `../ccf-common/references/review-output-standards.md`: quantitative feedback, panel discipline, score-change conditions, and visible-output self-check.
