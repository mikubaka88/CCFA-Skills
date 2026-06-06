# TeX Templates

Use this file when the user asks for a rebuttal TeX file, author-response TeX, response-letter template, or a full multi-reviewer response.

## Default Selection

Use `assets/templates/default-general-common-reviewer.tex` by default for full rebuttals. It contains:

- `General Response`
- `Common Concerns`
- `Reviewer-Specific Clarifications`

This default is best when the user provides multiple reviews and wants a balanced response that starts from strengths, merges shared issues, and then gives reviewer-specific clarifications.

## Template Choices

- `assets/templates/default-general-common-reviewer.tex`: Default. Use for most full rebuttals.
- `assets/templates/reviewer-specific-response.tex`: Use when the venue expects responses organized by reviewer or each reviewer has distinct concerns.
- `assets/templates/compact-response.tex`: Use when there is a strict word or character budget.
- `assets/templates/ac-focused-response.tex`: Use when AC/meta-review concerns, global misunderstanding, or one decisive issue dominates.

## Required TeX Features

Templates should include:

- reviewer color macros,
- concise reviewer quote blocks,
- direct answer blocks,
- evidence blocks with line/table/figure references,
- common-concern merging,
- self-contained acronyms and experimental settings,
- transparent limitation language.

## Filling Rules

1. Replace reviewer labels with the actual reviewer IDs used by the venue.
2. Quote only the core concern.
3. Put the direct answer before background.
4. Use bold emphasis only for decisive answers, evidence, and limitations.
5. Cite paper locations such as Section, Table, Figure, Appendix, or line number when available.
6. Include newly completed analyses or results in the rebuttal text instead of only promising them.
7. Keep reviewer-specific answers short when a common concern already answers the main issue.
