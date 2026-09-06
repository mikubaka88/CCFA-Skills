---
name: ccf-idea-reviewer
description: "Assess research ideas for value, novelty, insight, and mechanism. Use for 思路审核, 靠谱吗, 值得做吗, 创新够不够, idea review, scoring, and ranking; no numeric-score request is needed. Default to concept-only review without experiment assessment, including ideas extracted from manuscripts. Developing an idea belongs to ccf-idea-optimizer; evaluating manuscript evidence or writing belongs to ccf-paper-reviewer."
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

**CCFA Handoff Mode: PARTIAL (Recommended).** Follow `metadata.ccf_skill_controls.handoff_question_mode`, `../ccf-common/references/handoff-modes.md`, and `../ccf-common/references/task-modes.md`. Infer assessment from the requested judgment; an exact skill name, review keyword, or numeric score is unnecessary. A rough idea can still receive a serious concept assessment.

Choose by the object of judgment, not file type: a PDF supplied for “只看核心思路” remains idea review. Use `ccf-idea-optimizer` for requested development and `ccf-paper-reviewer` for manuscript evidence, scientific completeness, writing, or version readiness. Execute an explicitly combined review/development task through its respective owners without another permission round.

## Core Rule

Judge problem importance, novelty against closest work, conceptual insight, mechanism coherence, elegance, and audience fit. Default to concept-only scope. Do not grade experiments, demand baselines/ablations/results, assess implementation resources, or lower the verdict because research is unfinished. Add experiment or feasibility assessment only when the user requests that extension, keeping it separate from the concept score.

Distinguish a logical contradiction from an untested hypothesis. A meaningful claim can be assessed before experimental validation. Separate concept quality, development potential, and confidence; do not turn uncertain novelty into demonstrated overlap or submission readiness into idea quality.

Every consequential criticism identifies the affected idea statement or assumption, its inspected basis, its significance, and the smallest repair. Do not fabricate prior art, results, reviewer agreement, or acceptance probability. Use `abandon` only after identifying why no meaningful formulation or plausible rescue remains.

## Workflow

1. Identify the requested judgment, concept, audience, available sources, and any explicit scope extension. Reuse conversation context; ask only for a missing decision that changes the assessment. Do not ask for experimental materials merely to start idea review.
2. Load `references/strict-idea-review.md` for report selection and assessment, including qualitative judgments. Normalize problem → gap → insight → mechanism; keep experimental planning outside default intake.
3. Ground decisive novelty claims through public-safe retrieval under `../ccf-common/references/privacy-and-evidence.md`, unless browsing is forbidden. Reuse prior verified sources and record searched, partially searched, supplied-only, or unsearched coverage. Inspect relevant primary-source content before claiming overlap.
4. Assess distinct conceptual perspectives using `references/expert-panel.md`; combine duplicate issues under stable IDs. Experiment reviewers are optional for a requested extension. Use independent calls only if permitted and useful, and label single-agent perspectives honestly.
5. For standard scoring, load `references/rubric.md`, `references/calibration.md`, and `../ccf-common/references/review-output-standards.md`. Use the six conceptual dimensions and assessed-weight coverage. Honor no-score requests with qualitative judgments; low confidence is not a low score.
6. Distinguish decisive conceptual flaws from repairable gaps and unanswered questions. Compare multiple ideas under a common scope and rubric. Re-review changed assumptions and unresolved concerns without imposing new experiment criteria.
7. Deliver the detailed report from `strict-idea-review.md` by default; use its brief version only for an explicit brevity request or restrictive user format. Put requested optimization or experiment work in its own authorized deliverable.

## Output Contract

Use the concept-review structure defined in `references/strict-idea-review.md`; do not substitute a generic coaching response or manuscript acceptance report. State the conceptual verdict, prior-art delta, anchored concerns, applicable scorecard, development potential, confidence, and concrete refinements without repeating the same criticism. A rough seed, short prompt, or no-score request does not select brief output or authorize experiment assessment.

For an explicitly requested brief judgment, use the template's five blocks and retain the same concept-only boundary. No forced scores or experimental checklist. Recommendations remain `accept-to-develop`, `revise`, `pivot-with-rescue-route`, `abandon`, or `needs-literature-search`.

## References

- `references/strict-idea-review.md`: standard report structure, grounding, and scope.
- `references/rubric.md`, `references/calibration.md`: concept dimensions, weights, coverage, and decision conditions.
- `references/expert-panel.md`: distinct conceptual perspectives and optional requested extensions.
- `references/source-notes.md`: public provenance and reuse boundaries.
- `../ccf-common/references/review-output-standards.md`: evidence, scoring, and concern continuity.

For file outputs, follow `../ccf-common/references/artifact-contracts.md`: reuse the established report path, keep intermediate files under one stable task directory, and update current files in place. Load this policy only when writing files and it is not already in context.
