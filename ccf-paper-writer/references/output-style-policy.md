# Output Style Policy

Use this reference when the requested writing output could conflict with the default CCFA reporting shape.

## Priority Order

1. User-requested final format.
2. Original source format for edit/polish/compression tasks.
3. Target venue LaTeX format for from-scratch manuscript tasks.
4. Target venue length/page budget for full-manuscript tasks.
5. NeurIPS LaTeX fallback when the target venue is absent, unknown, or has no local guide.
6. Compact risk/status note only after the main writing output.

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
4. Establish a page/word budget from `length-budget-policy.md`; for submission-style drafts, aim near the venue limit rather than producing a short skeleton.
5. If the venue guide is missing or no venue is named, draft with the NeurIPS template path `ccf-latex-templates/NeurIPS/neurips_2026.tex`.
6. Use `TBD` for missing results, citations, figures, or implementation details.
7. For "完整文章", "full paper", "from scratch", or "投稿", include all normal paper parts for the target venue: abstract, introduction, background/related work or preliminaries, method, experiments, analysis/ablation, limitations, ethics/reproducibility if relevant, conclusion, references, and appendix/checklist placeholders when expected.

If the first draft is substantially below the venue budget, expand with useful missing content before declaring it complete. If it exceeds the budget, run compression locally because compression is owned by `ccf-paper-writer`.

Do not block the draft because final venue policy may be stale. State the freshness risk briefly and route final compliance to `ccf-submission-checker`.

## Information-Dense Writing

Do not use the main answer for generic process narration. The first visible artifact should be the draft, revised text, table, review response, or file path requested by the user. Keep notes short and concrete:

- name the exact unsupported claim,
- name the missing evidence or file,
- name the section affected,
- name the next owner only when a handoff is useful.

For full workflow demos, every skill should leave a concrete artifact rather than a one-line description.

## Citation Format Rules

Every manuscript must follow these citation formatting rules:

1. **Natural weaving:** Citations appear as part of the narrative. The claim precedes the citation bracket. A sentence should make sense if the brackets were removed.

2. **No author-name subjects:** Do not use `Author et al. [N]` as the grammatical subject of a sentence. Use the method name, the finding, or the paradigm as the subject: "Self-attention [1]..." not "Vaswani et al. [1]..."

3. **Group with purpose:** When citing multiple works, group them by what they share: "Contrastive objectives [9,10,11]" rather than dumping "Several works [1,2,3,4,5,6,7,8] have studied this."

4. **One citation per claim:** Do not repeat the same citation in consecutive sentences. If two sentences draw on the same source, merge them or rephrase.

5. **Bib file as source of truth:** Every `\cite{}` key must exist in the project `.bib` file. Never write a citation from memory.

6. **No bold labels:** Do not use `\textbf{Concept:}` or `\textit{Label:}` as paragraph scaffolding. Write prose paragraphs with topic sentences and logical flow. The only exceptions are venue-mandated section headings or checklist items.

7. **Citation density:** Check per-section minimums from `references/citation-workflow.md`. An AI/ML/CV/NLP paper with fewer than25 total references is under-cited. Count them before calling a draft complete.

## Flexible Suggestions

For non-review writing work, suggestions may be phrased as optional questions instead of hard blockers. Example:

```text
可以把本文定位成 benchmark + architecture paper 吗？这样 novelty 压力会小一些，但需要更强的 dataset/protocol 说明。
```

Use hard blockers only for fabricated evidence, privacy risk, incompatible user constraints, or impossible format requirements.
