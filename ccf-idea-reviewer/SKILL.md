---
name: ccf-idea-reviewer
description: "Assess, score, rank, and compare early CCF research ideas when judgment is explicitly requested. Use for idea评分, 选题排名, 严格评审, and acceptance-potential triage. Ground novelty in prior work. Unscored brainstorming and idea development belong to ccf-idea-optimizer; full manuscripts belong to ccf-paper-reviewer."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Idea Reviewer

## Invocation Controls

**CCFA Handoff Mode: PARTIAL (Recommended).** Follow `metadata.ccf_skill_controls.handoff_question_mode`, `../ccf-common/references/handoff-modes.md`, and `../ccf-common/references/task-modes.md`. Use this skill for explicitly requested idea assessment, scoring, ranking, or strict selection. Development without scoring belongs to `ccf-idea-optimizer`.

## Core Rule

Judge the research problem and mechanism against the closest relevant work and required evidence. Every material criticism names the affected claim, its basis, why it matters, and a concrete repair or pivot condition. Separate current conference readiness, development potential, and confidence. Unknown novelty is not proven novelty or automatic rejection.

Do not review prose, rewrite a manuscript, fabricate prior art/results, simulate reviewer consensus, or promise acceptance probabilities. Use `abandon` only when there is no testable central claim or plausible reformulation after a concrete rescue attempt.

## Workflow

1. Identify the requested judgment, venue/family, field, maturity, and available evidence. Normalize each idea into problem, gap, insight, mechanism, expected evidence, and constraints. Ask only when a missing decision changes the verdict; otherwise label the assumption and proceed.
2. For standard scoring, load `references/strict-idea-review.md` and ground the closest work through public-safe retrieval under `../ccf-common/references/privacy-and-evidence.md`. Necessary literature verification is part of the requested assessment unless browsing is forbidden. Mark source coverage as searched, partially searched, supplied-only, or unsearched.
3. Build the closest-work comparison and state what remains after subtracting prior art. Verify current official venue criteria when their exact year/track affects the judgment. Do not score from search snippets.
4. Use `references/expert-panel.md` and `../ccf-common/references/review-output-standards.md` for the relevant field, method, experiment, venue, and prior-art perspectives. Independent subagents are optional when permitted and useful; a single-pass role analysis must not be described as independent empirical agreement. Do not force praise, disagreement, or rejection.
5. Load `references/rubric.md` and `references/calibration.md` for requested numeric scoring. Apply the dimensions and weights consistently; mark non-applicable criteria with reasons and follow the calibration rule. Scores of 3 or below need a deduction, evidence basis, and repair condition. Confidence stays separate.
6. Separate fatal concerns from repairable gaps. For each non-develop recommendation, identify the smallest credible change in problem framing, mechanism, grounding, evidence, feasibility, or venue. In multiple-idea ranking, apply the same rubric and evidence standard across candidates.
7. Deliver the requested score/ranking and concrete actions. Perform optimization or full experiment design only when included in the request; otherwise provide a concise optional next step. Honor skill denylists without simulating a denied workflow.

## Output Contracts

For standard scoring, put the verdict/ranking first, followed by the closest-work delta, scorecard, confidence, decisive concerns with evidence, role-specific findings, and repair/score-change conditions. Avoid repeating the same concern in several boilerplate sections. Preserve an explicit user schema or concise format.

For quick triage, give the strongest ingredient, main evidenced risks, novelty confidence, development potential, and next deciding evidence. Do not present a quick scan as a full literature-backed review.

Recommendations remain `accept-to-develop`, `revise`, `pivot-with-rescue-route`, `abandon`, or `needs-literature-search`. Conditional score movement is diagnostic, never a promised reviewer response.

## References

- `references/strict-idea-review.md`: closest-work subtraction and strict criteria.
- `references/expert-panel.md`: perspective-specific assessment.
- `references/rubric.md`, `references/calibration.md`: dimensions, anchors, weighting, and recommendations.
- `references/source-notes.md`: provenance and official criteria.
- `../ccf-common/references/review-output-standards.md`: confidence, panel discipline, and score-change conditions.

For file outputs, follow `../ccf-common/references/artifact-contracts.md`: resolve existing project paths first, keep generated working files under one stable task/artifact directory, and update canonical files in place. Load this shared policy only when files are written and it is not already in context.
