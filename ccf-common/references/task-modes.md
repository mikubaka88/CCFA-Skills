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
- substantial multi-deliverable workflows; a small artifact remains quick even if another skill will later read it.

Run the skill's full mandatory checklist internally. Surface skipped items only when the user asked for an audit, the task is review-related, or the omission changes the reliability of the answer.

**quick** is for narrow local work:

- one paragraph or one small subsection polish,
- one local compression pass,
- a small literature sanity scan,
- one experiment-table sketch,
- a quick idea-risk note,
- a short reviewer-risk note.

Quick mode does not require the full mandatory checklist. Run the local subset only. Idea and manuscript reviewers select detailed/brief presentation through their report templates: narrow scope alone does not request brevity. For other skills, keep quick output short. Use a compact status only when it helps the user understand risk:

```text
Mode: quick
Local checks: venue/style, factual preservation, claim-evidence, no invented evidence
Skipped standard checks: full paper storyline, full reviewer simulation, full source audit
Unresolved:
```

## Mode Selection

1. If the requested deliverable is exploration, brainstorming, direction discovery, rescue, or development, use exploratory mode. A rough input does not override a request to judge whether the idea is worthwhile, novel, or logically sound; those requests use idea review even without scores.
2. If the user explicitly asks for quick or narrow work, preserve that scope. Do the relevant accuracy checks; name a material coverage limit instead of silently escalating to full review.
3. If the user says standard, full, final, submission-ready, checklist-audit, score-risk, 全面检查, or 投稿前, use standard mode. Creating a small reusable file alone does not require the full workflow.
4. If the user gives only one paragraph for polishing, default to quick mode.
5. If the user gives a full section, manuscript, review set, literature search, or experiment plan, default to standard mode, except early idea/literature scouting should stay exploratory until the user asks for a hard decision.
6. Safety rules never become quick or exploratory: do not invent evidence or results, do not expose private text in searches without authorization, preserve idea scope unless authorized, and apply source-quality exclusions in literature search.

## Output Flexibility

For non-review skills, the user's requested output shape wins over the skill's default report shape. If the user asks for LaTeX, Markdown, a table, a direct rewrite, a short answer, a file, Chinese prose, English prose, or a specific section structure, produce that format first and put internal checks behind it.

Review-related skills use structured evidence, scoring, and traceable criticism when applicable, while honoring an explicit user schema or concise requested format. `ccf-paper-reviewer`, `ccf-idea-reviewer`, and integrity/submission gate checks should remain more structured than writing, search, planning, or experiment-design outputs.

For `ccf-idea-reviewer`, separate concept quality, development potential, and confidence. Experimental completion and publication readiness are outside default concept review; do not require experimental material or penalize its absence. Assess experiments or execution feasibility only as a requested extension. Use `abandon` only when no meaningful central claim or plausible reformulation remains after a concrete rescue attempt.

For broad requests such as "完整流程", "完整文章", "详细报告", "用所有 skills", "full paper", "full review", or "closed loop", do not return fragments. Produce complete artifacts with enough concrete content to be useful: full drafts rather than abstract-only samples, filled tables rather than headings only, reviewer comments with evidence rather than generic risks, and handoff packets that name files, claims, blockers, and next actions.

For submission-style manuscript requests, "complete" also means length-aware. The writing owner should establish the target venue's page/word budget, use the budget to allocate substantive content, fill actual explanatory gaps, and compress overfilled drafts. Page occupancy alone does not justify padding, invented method detail, or an unbounded compile loop.

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
6. The argument flow is clear: problem -> reason -> consequence -> action, or scientific question -> mechanism or observation -> supported interpretation.
7. No generic filler remains where a concrete location, artifact, or action is required.

## Minimal Status

Every CCFA skill may include mode in final output when checklist strictness affects reliability:

```text
Mode:
Checks run:
Checks skipped:
Unresolved risks:
```

## Execution And Context

Keep the active goal, requested artifacts, authorization, evidence locations, completed work, and next action available across long tasks. Reuse existing `ccfa.yaml`, canonical reports, and handoff fields when persistence is needed; do not create extra process files for a short task or a no-new-files request. New user messages usually steer the active task: update the affected requirements, preserve valid completed work, answer a side question briefly, and resume. Replace the goal only when the user cancels it or asks for an incompatible task.

Load the owner's entry and only the reference sections needed for this mode. Treat a reference list as navigation, not a read-all checklist. Reuse shared policy already in context; reload when the file changed or the relevant rule was lost in compaction. Read source ranges located by search before loading a whole PDF extraction, library, venue guide, or report. A full scientific review or complete exemplar analysis still requires coverage of the relevant full source, read in coherent sections.

Use one representation of each fact: a source table, current specification, or existing report. Link to it in downstream work instead of copying full abstracts, tool logs, manuscript passages, and prior reports into every handoff. Give tools the smallest sufficient input and request targeted output; show counts, relevant rows, errors, and locations before raw dumps. Do not truncate evidence needed to assess a claim or silently lower requested coverage.

For a revision, inspect the changed passage, panel, data series, or issue plus its affected dependencies. Reuse unchanged source verification, chart layout, bibliography, and established scientific context. Broaden the check when a changed premise affects the whole artifact. A new source version or changed evidence invalidates dependent conclusions; a color or spelling edit does not.

When durable context is needed, update the existing report/specification with the active goal, constraints, current paths, verified findings, unresolved decisions, and next action. After compaction, recover that compact state and inspect referenced material as needed; do not re-extract or rescore unchanged inputs by default. Keep generated files under `artifact-contracts.md`; token reduction must not create a second uncontrolled set of context files. Return file links and a concise change report when files are the deliverable, unless the user also requests the full content in the conversation.

Batch independent read-only searches and checks when the host supports it. Keep dependent decisions, shared-file edits, and approvals sequential. If the host permits subagents, delegate only bounded independent work that improves coverage or elapsed time while the owner has useful work to do. Give each delegate the relevant inputs, output contract, and write boundary; integrate evidence before concluding. Do not claim independent reviewers when using role perspectives in a single pass. Small local edits do not need delegation.

Validate the requested outcome and changed paths. After relevant checks pass, repeat them only for a new change, failure, or unresolved concern. A missing tool limits the dependent verification, not unrelated authorized work. Distinguish not checked from failed. Do not fabricate verification or claim a running background task unless a real scheduler or job exists.

## GPT-6 Adaptation

The GPT-6 Astra guidance consulted on 2026-09-05 emphasizes authorization-aware follow-through, clear skill priority, explicit delegation conditions, direct writing, and proportionate verification. These execution rules remain portable to other supported agents. Keep model choice and reasoning effort in the host; compare effort on representative tasks rather than pinning every skill to a maximum. Skills do not enable API async execution, caching, compaction, or mid-turn steering by declaring them in Markdown. Use only capabilities actually exposed by the host. Official provenance is recorded with the skill-authoring sources in `source-registry.yaml`.
