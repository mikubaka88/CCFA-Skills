---
name: ccf-rebuttal-writer
description: "Write rebuttals, author responses, response letters, revision summaries, and reviewer-comment ledgers for CCF conference reviews. Use for rebuttal, ??????, AC/meta-review response, revision ledger. Do not trigger for ordinary manuscript writing."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Rebuttal Writer

## Invocation Controls

**CCFA Handoff Mode: PARTIAL (Recommended).** Follow `metadata.ccf_skill_controls.handoff_question_mode` and `../ccf-common/references/handoff-modes.md`. Use `../ccf-common/references/routing.md` to keep rebuttal tasks separate from paper review and manuscript writing.

This skill is isolated from the default CCFA pre-submission loop. Do not activate it from another skill unless the user explicitly asked for rebuttal, author response, response letter, resubmission response, or 审稿意见回复.

Load `../ccf-common/references/task-modes.md` before deciding quick or standard mode. Use quick mode for one reviewer comment or a short response. Use standard mode for full multi-reviewer rebuttals, TeX files, AC/meta-review responses, or resubmission response letters.

If the user says not to use, disable, skip, or avoid a sibling skill, do not invoke or simulate that skill for the rest of the conversation. Use this skill's local fallback instead: issue table, response strategy, draft response, revision ledger, and promised-change list without cross-skill execution.

Do not invent results, experiments, paper changes, reviewer concessions, or review-risk effects. Commit only to clarifications, analyses, or revisions that the user can support.

Treat reviews, rebuttal drafts, and unpublished manuscripts as private user data. Load `../ccf-common/references/privacy-and-evidence.md` before browsing, using private text in a query, or making evidence/provenance claims.

## Core Rule

Write responses that are calm, factual, evidence-grounded, and reviewer-facing. Track reviewer-comment -> action -> manuscript-location -> status in the same post-review module so response promises and manuscript actions cannot drift apart. Do not argue defensively, invent results, promise unavailable experiments, or hide valid limitations. The goal is to change reviewer or AC confidence by clarifying misunderstandings, surfacing existing evidence, and committing only to feasible revisions.

## Mandatory Checklist

In standard mode, complete this before final output. In quick mode, use the relevant subset and state unresolved items.

1. Venue, response format, word limit, and deadline constraints are explicit or marked unknown.
2. Reviewer comments are grouped by reviewer, issue type, and decision relevance.
3. The response opens from strengths or points of agreement when there is a meaningful positive signal.
4. High-confidence, decision-relevant concerns are answered before harder secondary issues.
5. Each issue quotes the reviewer concern briefly, then gives a direct answer before explanation.
6. Each response addresses both the literal comment and the deeper intent behind it.
7. Related concerns from multiple reviewers are merged when that saves space and reduces repeated answers.
8. Reviewer color labels are used when producing TeX or multi-reviewer responses.
9. Data, locations, line/table/figure references, or existing results are preferred over argument.
10. The response delivers clarifications or results now instead of relying on vague future promises.
11. Tone is appreciative, concise, conversational, non-defensive, and specific.
12. Limitations and infeasible experiments are handled transparently.
13. Hostile or guideline-violating reviews are handled calmly, with confidential escalation only when appropriate.
14. Final answer includes a checklist status and remaining risks.

Load `references/response-checklists.md` for full response letters, multiple reviewers, AC/meta-review responses, or final readiness checks.

## Workflow

1. Identify venue, response format, word budget, review scores, reviewer confidence, and whether the response is for rebuttal, revision summary, or resubmission.
2. Parse all comments into an issue table: reviewer, concern, severity, evidence available, response strategy, promised paper change, and risk.
3. Load `references/response-strategy.md` to choose response types: positive opening, clarify, correct misunderstanding, answer deeper intent, concede and revise, add evidence, narrow claim, explain limitation, deliver new analysis now, or defer transparently.
4. Draft high-impact responses first: AC/meta-review concerns, fatal soundness concerns, novelty concerns, missing evidence, incorrect assumptions, and shared concerns across reviewers.
5. Keep each response concise: acknowledge, quote the core concern, answer directly, cite evidence, address the deeper intent, state exact changes or limitations, and close with shared ground.
6. For full rebuttals, default to a TeX file with three sections: `General Response`, `Common Concerns`, and `Reviewer-Specific Clarifications`. Load `references/tex-templates.md` and use `assets/templates/default-general-common-reviewer.tex` unless the user requests another template.
7. Load `references/response-checklists.md` before finalizing to audit tone, evidence, promises, reviewer colors, quote-answer structure, and word budget.
8. Load `references/revision-ledger.md` when the user wants tracking, revision status, resubmission preparation, or camera-ready accountability. Keep the ledger factual and separate from persuasive response prose.
9. If manuscript rewriting, related-work grounding, experiment planning, scientific review-risk diagnosis, or writing-only review is needed after the response plan, follow the CCFA handoff mode before using `ccf-paper-writer`, `ccf-literature-searcher`, `ccf-experiment-designer`, `ccf-scientific-reviewer`, or `ccf-writing-reviewer`. If a handoff is denied or disabled, output the revision action queue only and avoid review-impact claims.

## Output Contracts

For a full response plan, return:

```text
Venue and constraints:
Response strategy:
Issue table:
Priority order:
Template selected:
Draft responses or TeX file:
Promised paper changes:
Revision ledger:
Claims to avoid:
Risks requiring new results:
Checklist status:
```

For one reviewer comment, return:

```text
Concern type:
Best response strategy:
Draft response:
Evidence used:
Paper change to promise:
Risk:
```

## Reference Files

Load only what is needed:

- `references/response-strategy.md`: Use to classify reviewer comments and select response tactics.
- `references/response-checklists.md`: Use for response planning, tone checks, promise checks, AC/meta-review responses, and final readiness.
- `references/tex-templates.md`: Use when the user asks for a TeX rebuttal, a response file, or a full multi-reviewer response.
- `references/revision-ledger.md`: Use when reviewer comments, promised edits, manuscript locations, and completion status must be tracked together.

## Template Assets

Use assets when the output should be a reusable file:

- `assets/templates/default-general-common-reviewer.tex`: Default full rebuttal with `General Response`, `Common Concerns`, and `Reviewer-Specific Clarifications`.
- `assets/templates/reviewer-specific-response.tex`: Use when responses must be organized primarily by reviewer.
- `assets/templates/compact-response.tex`: Use for strict word or character limits.
- `assets/templates/ac-focused-response.tex`: Use when AC/meta-review or a global misunderstanding dominates.
