# Output Style Policy

Use this reference when the requested writing output could conflict with the default CCFA reporting shape.

## Priority Order

1. User-requested final format.
2. Original source format for edit/polish/compression tasks.
3. Target venue LaTeX format for from-scratch manuscript tasks.
4. NeurIPS LaTeX fallback when the target venue is absent, unknown, or has no local guide.
5. Compact risk/status note only after the main writing output.

## Edit And Polish

Preserve existing structure unless the user asks for restructuring:

- LaTeX commands, environments, labels, citations, equations, comments, and section hierarchy.
- Markdown headings, tables, lists, code fences, and links.
- Paragraph count and section order when the request is "polish", "润色", "改写但不改结构", or "keep format".

If a sentence contains an unsupported claim, either soften it in place or add a short note after the revised text. Do not turn a polish request into a long review report.

## From Idea To Manuscript

When the user has only an idea and asks to write a paper:

1. Search `venue-guides/index.md` for the target venue.
2. Read the specific venue guide when it exists.
3. Draft a LaTeX manuscript using that venue's template conventions.
4. If the venue guide is missing or no venue is named, draft with the NeurIPS template path `ccf-latex-templates/NeurIPS/neurips_2026.tex`.
5. Use `TBD` for missing results, citations, figures, or implementation details.

Do not block the draft because final venue policy may be stale. State the freshness risk briefly and route final compliance to `ccf-submission-checker`.

## Flexible Suggestions

For non-review writing work, suggestions may be phrased as optional questions instead of hard blockers. Example:

```text
可以把本文定位成 benchmark + architecture paper 吗？这样 novelty 压力会小一些，但需要更强的 dataset/protocol 说明。
```

Use hard blockers only for fabricated evidence, privacy risk, incompatible user constraints, or impossible format requirements.
