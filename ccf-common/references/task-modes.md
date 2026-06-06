# CCFA Task Modes

Use this file to decide how much checklist and audit work a CCFA skill should run for the current request.

## Mode Values

**standard** is the default for substantial work:

- whole-paper planning, review, or rewriting,
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

1. If the user explicitly says quick, fast, 简单检查, 快速润色, quick polish, or "不用完整 checklist", use quick mode unless the task is high-stakes or broad enough to require standard.
2. If the user says standard, full, final, submission-ready, checklist-audit, score-risk, 全面检查, 投稿前, or wants a reusable folder/file, use standard mode.
3. If the user gives only one paragraph for polishing, default to quick mode.
4. If the user gives a full section, manuscript, review set, literature search, or experiment plan, default to standard mode.
5. Safety rules never become quick: do not invent evidence or results, do not expose private text in searches without authorization, preserve idea scope unless authorized, and apply source-quality exclusions in literature search.

## Output Flexibility

For non-review skills, the user's requested output shape wins over the skill's default report shape. If the user asks for LaTeX, Markdown, a table, a direct rewrite, a short answer, a file, Chinese prose, English prose, or a specific section structure, produce that format first and put internal checks behind it.

Review-related skills may keep stricter fixed formats because their value is diagnosis, scoring, and traceable criticism. `ccf-paper-reviewer`, `ccf-idea-reviewer`, and integrity/submission gate checks should remain more structured than writing, search, planning, or experiment-design outputs.

For editing, polishing, compression, and local revision, preserve the user's existing format and markup unless the user explicitly asks for restructuring. Do not convert LaTeX into a checklist report, Markdown into a different outline, or a paragraph into a table just because the skill has a template.

When a non-review task is under-specified, proceed with reasonable assumptions and ask at most a small number of targeted questions as optional suggestions. Do not block ordinary writing or planning work merely because a full checklist cannot be completed.

## Minimal Status

Every CCFA skill may include mode in final output when checklist strictness affects reliability:

```text
Mode:
Checks run:
Checks skipped:
Unresolved risks:
```
