---
name: ccf-workflow-planner
description: "Clarify complex CCF research goals, constraints, success criteria, project stages, and next-skill routing before downstream work. Use for workflow planning, task decomposition, research brief, ????, ????, ????. Do not optimize ideas, search literature, write, review, or rebut as the main output."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Workflow Planner

## Invocation Controls

**CCFA Handoff Mode: PARTIAL (Recommended).** Follow `metadata.ccf_skill_controls.handoff_question_mode` and `../ccf-common/references/handoff-modes.md`. Use `../ccf-common/references/routing.md` to keep brainstorming separate from idea optimization, idea review, literature search, experiment design, manuscript writing, compression, paper writing review, and rebuttal tasks.

Load `../ccf-common/references/task-modes.md` before deciding quick or standard mode. Use quick mode for small-scope clarification, a brief route choice, or a compact decision note. Use standard mode for complex research workflows, multi-stage plans, task decomposition, approach comparison, or reusable decision briefs.

This skill is an on-demand upstream planning skill, not a global hard gate. Do not block ordinary one-paragraph polishing, direct literature search, direct experiment design, direct compression, direct rebuttal, or a user-explicit sibling skill call.

If the user says not to use, disable, skip, or avoid a sibling skill, do not invoke or simulate that skill for the rest of the conversation. Produce a local brief and route note instead.

Treat rough ideas, manuscripts, reviews, unpublished results, and experiment plans as private user data. Load `../ccf-common/references/privacy-and-evidence.md` before browsing, using private text in a query, or making evidence/provenance claims.

## Core Rule

Turn an ambiguous research request into a decision-ready brief. Clarify what the user wants, what materials and constraints exist, what success means, which options are plausible, and which CCFA skill should run next. Do not perform the downstream research task as the main output.

This skill may discuss candidate workflows, tradeoffs, assumptions, and next actions. It must not optimize the idea, search literature, design full experiments, rewrite manuscript text, compress sections, write rebuttals, or review a paper unless the user confirms the appropriate CCFA handoff.

## Mandatory Checklist

In standard mode, complete this checklist before final output. In quick mode, run the local subset and return a compact status.

1. User goal, audience, target venue or venue family, and decision to be made are explicit or marked unknown.
2. Available inputs are inventoried: idea notes, manuscript sections, reviews, figures/tables, experiments, citations, code, timeline, and constraints.
3. Missing information is separated into must-know, useful-to-know, and safe-to-assume.
4. The task is scoped as one CCFA task, a multi-stage workflow, or too broad and needing decomposition.
5. 2-3 viable approaches are compared when the task has meaningful tradeoffs.
6. A recommended approach is stated with the reason and the main risk.
7. Privacy/evidence boundaries are stated when browsing, private manuscripts, unpublished results, or reviewer comments are involved.
8. Next CCFA skill routing is explicit and respects session denylists and handoff mode.
9. No downstream work is performed unless the user explicitly requested the downstream skill or the handoff mode allows it.

Load `references/intake-protocol.md` for goal and material intake. Load `references/approach-options.md` when comparing routes or strategies. Load `references/design-brief-template.md` when producing a decision brief.

## Workflow

1. Identify whether the user wants brainstorming itself or another CCFA task. If they directly request a concrete sibling skill task, route to the owning skill instead of forcing brainstorming.
2. Explore available context first: local files, pasted material, known target venue, existing CCFA outputs, or project notes when provided. Do not ask for information that is discoverable from the local context.
3. Load `references/intake-protocol.md` and normalize the request into goal, audience, scope, constraints, success criteria, inputs, missing information, and privacy boundary.
4. If the request spans multiple independent stages, decompose it into an ordered CCFA workflow and identify the first decision point.
5. Load `references/approach-options.md` and present 2-3 approaches only when there is a real tradeoff. Give a recommended approach first.
6. Load `references/design-brief-template.md` and produce a decision brief. If the user requested quick mode, produce a compact route note instead.
7. Follow CCFA handoff mode before transitioning to `ccf-idea-optimizer`, `ccf-idea-reviewer`, `ccf-literature-searcher`, `ccf-experiment-designer`, `ccf-paper-writer`, `ccf-paper-compressor`, `ccf-scientific-reviewer`, `ccf-writing-reviewer`, or `ccf-rebuttal-writer`.

## Output Contracts

For quick mode, return:

```text
Mode: quick
Clarified goal:
Known inputs:
Missing must-know:
Recommended next skill:
Reason:
Checks skipped:
Unresolved:
```

For standard mode, return:

```text
Mode: standard
Decision to make:
User goal and audience:
Available inputs:
Constraints:
Success criteria:
Scope diagnosis:
Approach options:
Recommended approach:
Next CCFA route:
Handoff decision:
Privacy/evidence notes:
Open questions:
Checklist status:
```

If producing a reusable research brief because the user explicitly requested a file, use the template in `references/design-brief-template.md`.

## Reference Files

Load only what is needed:

- `references/intake-protocol.md`: Use for goal, audience, input, constraint, success-criteria, and privacy intake.
- `references/approach-options.md`: Use for comparing 2-3 viable routes or strategies with tradeoffs and a recommendation.
- `references/design-brief-template.md`: Use for a final decision brief or reusable research-task brief.

If the user asks to improve a research idea, route to `ccf-idea-optimizer`. If the user asks to score or rank ideas, route to `ccf-idea-reviewer`. If the user asks to search literature, route to `ccf-literature-searcher`. If the user asks to design experiments, route to `ccf-experiment-designer`. If the user asks to write, polish, rewrite, compress, review, or rebut, route to the corresponding CCFA skill rather than keeping the task inside brainstorming.
