---
name: ccf-paper-reviewer
description: "Review CCF/target-venue manuscripts end to end: scientific novelty, soundness, evidence, simulated reviewers, AC/meta-review, score risk, writing logic, paragraph clarity, LaTeX/format presentation, and reviewer-facing revision actions. Use for paper review, scientific review, writing review, format review, 审稿, 模拟审稿, 论文评分, 写作评审, 逐段评审, LaTeX检查. Do not rewrite the manuscript as the main task and do not write rebuttals."
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

Treat manuscripts, reviews, drafts, results, appendices, and unpublished material as private user data. Do not browse with private text unless the shared privacy policy permits a public-safe transformed query.

## Core Rule

Act as a strict but fair reviewer and AC. Produce decision-relevant findings, not prose rewrites. Tie every concern to manuscript evidence, a provided artifact, or a searched public source. Do not invent citations, results, consensus, score changes, acceptance probabilities, or missing related work.

Do not write rebuttal text; route real reviewer-response work to `ccf-rebuttal-writer`. Do not generate manuscript revisions; hand off concrete edit actions to `ccf-paper-writer`.

## Workflow

1. Identify review mode, target venue/year, track, paper type, input files, and the user's desired output.
2. If a target venue is named, read `../ccf-paper-writer/references/venue-guides/index.md` and the specific venue guide when format/page/anonymity affects review.
3. Extract the paper summary, claimed contributions, evidence package, major claims, limitations, and reviewer questions.
4. For scientific/full mode, load the scientific references as needed: `references/review-workflow.md`, `references/universal-review-rubric.md`, `references/venue-review-styles.md`, `references/reviewer-panel.md`, `references/calibration-and-rank.md`, and `references/desk-checks.md`.
5. For writing/full mode, load the writing-review references as needed from `references/writing-review/`.
6. Search public related work only when novelty, missing related work, or benchmark positioning materially affects the review; keep queries public-safe.
7. Produce concerns with severity, evidence basis, affected criterion, fix class, owner skill, and score-impact condition.
8. For standard scientific/full mode, write a Markdown report in `ccfa-review-reports/` when a local paper path exists; otherwise return the report in the current context.

## Output Contracts

For standard review:

```text
Mode:
Venue and assumptions:
Paper summary:
Likely stance and calibrated score:
Top strengths:
Major/fatal concerns:
Writing and presentation concerns:
Format/venue concerns:
Concern-to-action table:
Recommended next CCFA owner:
Checks run:
Unresolved or unverified:
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

## Reference Files

- `references/review-workflow.md`: scientific review process.
- `references/fixed-output-format.md`: fixed report format.
- `references/universal-review-rubric.md`: scientific dimensions and claim-evidence audit.
- `references/venue-review-styles.md`: venue-family expectations.
- `references/reviewer-panel.md`: simulated reviewers and AC/meta-review.
- `references/calibration-and-rank.md`: scores, ranks, and confidence.
- `references/desk-checks.md`: desk and policy checks.
- `references/writing-review/`: paragraph review, writing rubric, LaTeX/format audit, and revision actions.
