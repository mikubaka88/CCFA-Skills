# CCFA Task Modes

Use this file to decide how much checklist and audit work a CCFA skill should run for the current request.

## Mode Values

**exploratory** is for early research direction discovery and repeated back-and-forth ideation:

- finding possible directions from a broad topic,
- shaping a weak or vague seed before it is ready to score,
- literature scouting for opportunity maps rather than final novelty gates,
- comparing possible problem framings without making an investment decision,
- asking "这个方向还能怎么做", "有没有可救路线", "找两个方向", "先别否定，帮我发散".

Run enough checks to avoid fabrication and obvious dead ends, but do not apply submission-ready review gates as visible verdicts. The output should preserve optionality: candidate reframings, nearest prior-art risks, open gaps, minimum viable research questions, and the next evidence needed to decide. Use `low confidence` or `needs-search` for uncertainty; do not convert uncertainty into rejection.

**standard** is the default for substantial work:

- whole-paper planning, review, or rewriting,
- venue-aware full-manuscript drafting with page/word budget,
- full idea optimization or scoring,
- literature search that informs novelty, Related Work, Introduction, or experiment design,
- full experiment design,
- full-section or paper-length compression,
- rebuttal plans, TeX files, or multi-reviewer responses,
- any workflow that will feed another CCFA module.

Run the skill's full mandatory checklist internally. Surface skipped items only when the user asked for an audit, the task is review-related, or the omission changes the reliability of the answer.

**quick** is for narrow local work:

- one paragraph or one small subsection polish,
- one local compression pass,
- a small literature sanity scan,
- one experiment-table sketch,
- a quick idea-risk note,
- a short reviewer-risk note.

Quick mode does not require the full mandatory checklist. Run the local subset only and keep the visible output short. Use a compact status only when it helps the user understand risk:

```text
Mode: quick
Local checks: venue/style, factual preservation, claim-evidence, no invented evidence
Skipped standard checks: full paper storyline, full reviewer simulation, full source audit
Unresolved:
```

## Mode Selection

1. If the user asks to explore, brainstorm, find directions, rescue a direction, try variants, or says the idea is rough, use exploratory mode unless they explicitly ask for strict scoring.
2. If the user explicitly says quick, fast, 简单检查, 快速润色, quick polish, or "不用完整 checklist", use quick mode unless the task is high-stakes or broad enough to require standard.
3. If the user says standard, full, final, submission-ready, checklist-audit, score-risk, 全面检查, 投稿前, or wants a reusable folder/file, use standard mode.
4. If the user gives only one paragraph for polishing, default to quick mode.
5. If the user gives a full section, manuscript, review set, literature search, or experiment plan, default to standard mode, except early idea/literature scouting should stay exploratory until the user asks for a hard decision.
6. Safety rules never become quick or exploratory: do not invent evidence or results, do not expose private text in searches without authorization, preserve idea scope unless authorized, and apply source-quality exclusions in literature search.

## Output Flexibility

For non-review skills, the user's requested output shape wins over the skill's default report shape. If the user asks for LaTeX, Markdown, a table, a direct rewrite, a short answer, a file, Chinese prose, English prose, or a specific section structure, produce that format first and put internal checks behind it.

Review-related skills may keep stricter fixed formats because their value is diagnosis, scoring, and traceable criticism. `ccf-paper-reviewer`, `ccf-idea-reviewer`, and integrity/submission gate checks should remain more structured than writing, search, planning, or experiment-design outputs.

When `ccf-idea-reviewer` is used on an early seed, separate `current conference readiness` from `development potential`. A low current score means the seed is not ready, not that the direction is dead. Use `abandon` only when the idea has no testable claim and no plausible reformulation after at least one concrete rescue attempt.

For broad requests such as "完整流程", "完整文章", "详细报告", "用所有 skills", "full paper", "full review", or "closed loop", do not return fragments. Produce complete artifacts with enough concrete content to be useful: full drafts rather than abstract-only samples, filled tables rather than headings only, reviewer comments with evidence rather than generic risks, and handoff packets that name files, claims, blockers, and next actions.

For submission-style manuscript requests, "complete" also means length-aware. The writing owner should establish the target venue's page/word budget, aim near that budget, expand underfilled drafts with evidence-bound content, and compress overfilled drafts before final/submission checks.

For editing, polishing, compression, and local revision, preserve the user's existing format and markup unless the user explicitly asks for restructuring. Do not convert LaTeX into a checklist report, Markdown into a different outline, or a paragraph into a table just because the skill has a template.

When a non-review task is under-specified, proceed with reasonable assumptions and ask at most a small number of targeted questions as optional suggestions. Do not block ordinary writing or planning work merely because a full checklist cannot be completed.

## Information Density

Visible output should maximize useful information and minimize boilerplate. Avoid long disclaimers, repeated "what this is not" lists, vague praise, generic next steps, and empty section headings. Every paragraph, bullet, or table row should contain at least one of: a concrete claim, a specific edit, an evidence link, a named artifact, a decision, a blocker, a quantified value, or an actionable question.

## Output Quality Gate

Before returning a visible artifact, every CCFA skill should do one quick self-read:

1. The answer follows the requested or promised output format.
2. Headings, bullets, and tables are complete and in a logical order.
3. Review and audit outputs include concrete evidence, severity, score or pass/fail status, and action conditions where applicable.
4. Writing outputs preserve the user's source format unless restructuring was requested.
5. Chinese and English punctuation are used consistently; mixed punctuation is allowed only when required by code, LaTeX, citations, or filenames.
6. The argument flow is clear: problem -> reason -> consequence -> action, or broader claim -> evidence -> limitation -> next step.
7. No generic filler remains where a concrete location, artifact, or action is required.

## Minimal Status

Every CCFA skill may include mode in final output when checklist strictness affects reliability:

```text
Mode:
Checks run:
Checks skipped:
Unresolved risks:
```
