---
name: ccf-conference-writing-reviewer
description: "Detailed writing-only reviewer for CCF-A/target-venue manuscripts: paragraph-by-paragraph writing critique, writing logic, LaTeX/format audit, claim-evidence presentation, consistency, contribution display, figure/table narration, and reviewer-facing communication risks. Use only when the user explicitly asks for writing review, 逐段写作评审, LaTeX or format checking, paper logic, wording consistency, abstract/introduction/storyline presentation, figure/table narration, or concrete writing revision actions; 中文触发: 写作评审, 逐段写作评审, 论文格式检查, LaTeX检查, 全文一致性, 行文逻辑, 论文规范性, 投稿前写作审查, 论文展示优势. Do not use for full scientific paper review, 模拟审稿, 完整审稿, AC评审, meta-review, or paper scoring."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Conference Writing Reviewer

## Invocation Controls

**CCFA Handoff Mode: PARTIAL (Recommended).** Follow `metadata.ccf_skill_controls.handoff_question_mode` and `../ccf-common/references/handoff-modes.md`. Use `../ccf-common/references/routing.md` to keep writing review separate from idea scoring, literature search, experiment design, full scientific paper review, manuscript rewriting, compression, and rebuttal tasks.

Load `../ccf-common/references/task-modes.md` before deciding quick or standard mode. Use quick mode for a short section-level writing risk note, one paragraph, abstract, or introduction scan. Use standard mode for writing-focused manuscript review, paragraph-by-paragraph writing review, LaTeX/format audit, consistency audit, or concrete writing revision planning.

Use this skill only when the user explicitly asks for writing, presentation, LaTeX, format, paragraph logic, or consistency review. If the user asks for complete paper review, simulated reviewers, AC/meta-review, scientific scoring, novelty/soundness/evidence review, or acceptance-risk diagnosis, route to `ccf-conference-reviewer`.

If the user says not to use, disable, skip, or avoid a sibling skill, do not invoke or simulate that skill for the rest of the conversation. Use this skill's local fallback instead: writing diagnosis, format audit, and revision action queue without cross-skill execution.

Do not invent results, citations, experiments, reviewer consensus, score changes, or acceptance probability. Conditional writing-risk effects must be grounded in the manuscript or in explicitly proposed edits.

Treat manuscripts, appendices, reviews, and unpublished results as private user data. Load `../ccf-common/references/privacy-and-evidence.md` before browsing, using private text in a query, or making evidence/provenance claims.

## Core Rule

Review like a strict paper-writing reviewer who has read the manuscript closely. The primary job is not to judge scientific acceptance; it is to find where the writing fails to make the contribution legible, convincing, consistent, and venue-compliant.

Every material issue must be anchored to a section, paragraph ID, line number, TeX command, figure/table, equation, claim, or missing evidence path. Do not write generic advice such as "improve clarity", "strengthen motivation", "add details", or "polish language" unless it is followed by the exact location, why a reviewer would be confused, and the concrete edit.

## Mandatory Review Checklist

In standard mode, complete this checklist before final output. In quick mode, run the local subset and return a compact status.

1. Venue, year, track, paper type, manuscript scope, and assumptions are explicit.
2. The reading scope is stated: abstract only, section, main paper, full paper, appendix, TeX source, or pasted text.
3. The manuscript is segmented into sections and paragraph IDs when enough text is available.
4. Paragraph-level issues are reported for all high-impact paragraphs: abstract, introduction, contribution list, method overview, main result paragraphs, limitations, and conclusion.
5. Global storyline, motivation, contribution display, and section order are audited.
6. Claim-evidence presentation is audited for major claims; scientific truth is not re-scored here.
7. Terminology, notation, dataset/model names, and contribution wording are checked for consistency.
8. Figures, tables, captions, equations, algorithms, and result narration are checked when present.
9. LaTeX/format compliance is checked when source, snippets, or venue rules are available.
10. Every material weakness is converted into a concrete writing or format revision action.
11. Optional transitions to `ccf-writing-skills`, `ccf-paper-compressor`, `ccf-experiment-designer`, `ccf-literature-search`, or `ccf-conference-reviewer` follow CCFA handoff mode. Rebuttal is used only when explicitly requested.

Load `references/writing-review-rubric.md` for writing-risk review. Load `references/paragraph-review-protocol.md` for writing-focused paragraph review. Load `references/latex-format-audit.md` for TeX, format, template, citation, figure/table, or equation checks.

## Workflow

1. Identify venue, track, field, paper type, manuscript state, and the user's goal: writing review, paragraph-by-paragraph writing review, LaTeX/format audit, consistency audit, story diagnosis, or writing revision planning. If the venue is unknown, use a generic strict CS conference writing lens and state that assumption.
2. If the user asks for the latest venue policy, page limit, template rule, anonymity rule, or current-year formatting rule, verify the official venue page before applying a venue-specific rule.
3. If local `.tex` files are available, inspect source structure with fast search before reviewing. Do not claim compilation unless a build was actually run.
4. Read the manuscript in passes:
   - Pass 1: title, abstract, introduction, contribution list, headings, figures/tables, conclusion; identify the intended story and contribution promise.
   - Pass 2: paragraph-by-paragraph writing review of high-impact sections; assign IDs and diagnose role, takeaway, logic, evidence presentation, and edit action.
   - Pass 3: terminology/notation consistency, figure/table narration, related-work positioning as writing, and limitation placement.
   - Pass 4: LaTeX/format/template/citation/reference audit when source or venue constraints are available.
5. Load `references/writing-review-rubric.md` and score only writing/presentation dimensions. If the user asks for acceptance-style scoring or scientific review, follow CCFA handoff mode before switching to `ccf-conference-reviewer`.
6. Load `references/paragraph-review-protocol.md` and produce a paragraph table for standard mode. For long manuscripts, prioritize high-impact paragraphs and group low-risk paragraphs with IDs.
7. Load `references/latex-format-audit.md` when format, TeX, references, figures/tables, equations, or venue compliance matter.
8. Convert every issue into an action using `references/revision-actions.md`. Classify each action as writing-fixable, structure-fixable, claim-qualification, citation/positioning, figure/table, LaTeX/format, compression, or accepted-limitation.
9. Follow the CCFA handoff mode before offering the action queue to `ccf-writing-skills`, `ccf-paper-compressor`, `ccf-experiment-designer`, `ccf-literature-search`, or `ccf-conference-reviewer`. If denied, output the queue only.

## Output Contracts

For a full writing review, return:

```text
Writing verdict:
Venue and assumptions:
Reading scope:
Global storyline diagnosis:
Contribution presentation:
Paragraph-by-paragraph table:
Claim-evidence presentation audit:
Consistency audit:
Figure/table/equation/caption audit:
LaTeX and format audit:
High-priority writing actions:
Section-level edit plan:
Claims to weaken, move, or support:
What not to change:
Optional next-module decision:
Checklist status:
```

For quick mode or a short section, return:

```text
Quick writing verdict:
Main reviewer confusion:
Top local issues:
Exact edit instructions:
Risk if left unfixed:
Checklist status:
```

For LaTeX/format review, return:

```text
Format verdict:
Source/compilation status:
Blocking compliance issues:
LaTeX/source issues:
Citation/reference issues:
Figure/table/caption issues:
Notation/equation issues:
Concrete fixes:
```

## Coordination With Writing Skills

When this skill is explicitly used with `ccf-writing-skills`, or the user confirms the optional module transition, act as the diagnostic reviewer and let `ccf-writing-skills` perform rewrites. If writing is denied, provide the same concrete action queue to the user without invoking the writing skill:

```text
Location:
Issue:
Reviewer confusion:
Required edit:
Evidence or wording support needed:
Where to revise:
Risk-reduction condition:
Status:
```

## Reference Files

Load only what is needed:

- `references/writing-review-rubric.md`: Use for writing/presentation dimensions, anti-filler deduction format, and writing-only boundaries.
- `references/paragraph-review-protocol.md`: Use for paragraph IDs, paragraph tables, and 逐段写作评审.
- `references/latex-format-audit.md`: Use for TeX source, format, template, citation, figure/table, equation, and compilation-status checks.
- `references/revision-actions.md`: Use to turn writing deductions into concrete revision actions and closed-loop risk reduction.
- `references/review-checklists.md`: Use to prevent omissions in full writing review, format audit, and writing revision planning.
- `references/source-notes.md`: Use when source provenance, official-policy checks, or method rationale matters.

If the user's task is complete scientific paper review, simulated reviewers, AC/meta-review, or paper scoring, follow the CCFA handoff mode before switching to `ccf-conference-reviewer`. If the user's task is post-review communication rather than manuscript writing review, switch to `ccf-conference-paper-rebuttal` only when the user explicitly requests rebuttal, author response, response letter, resubmission response, or 审稿意见回复. If the user asks to score an early idea rather than a manuscript, follow the CCFA handoff mode before switching to `ccf-idea-reviewer`; if not confirmed, provide only a scope warning.


## v0.4 Venue Guide Boundary

For LaTeX/page/anonymity/template checks, read `../ccf-writing-skills/references/venue-guides/index.md` and the specific venue guide if present. This skill may diagnose format and writing-presentation risks, but it must not rewrite manuscript content unless the user asks for writing revision and routing allows handoff to `ccf-writing-skills`.
