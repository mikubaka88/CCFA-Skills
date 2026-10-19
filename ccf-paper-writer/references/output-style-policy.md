# Output Style Policy

Use this reference when the requested writing output could conflict with the default CCFA reporting shape.

## Priority Order

1. User-requested final format.
2. `ccf-humanization` direct-academic and warning-non-injection policy.
3. Original source format for edit/polish/compression tasks.
4. Target venue LaTeX format for from-scratch manuscript tasks.
5. Content-first drafting followed by alignment; venue length/page budget only during requested fitting.
6. NeurIPS format fallback for a new LaTeX manuscript when no usable target template is specified. Preserve requested Markdown, custom formats, and supplied templates; a missing local venue guide does not override them.
7. A compact note after the main writing output only for a remaining unresolved scientific decision or material evidence gap that needs the user's decision; never inject workflow warnings into the artifact.

## Edit And Polish

Preserve existing structure unless the user asks for restructuring:

- LaTeX commands, environments, labels, citations, equations, comments, and section hierarchy.
- Markdown headings, tables, lists, code fences, and links.
- Paragraph count and section order when the request is "polish", "润色", "改写但不改结构", or "keep format".

If a sentence overstates supplied evidence, revise it accurately within the authorized edit. Preserve verified negative results, assumptions, and comparison constraints as direct scientific content in the relevant passage. Only a remaining decision that requires unknown evidence or a change to the research claim warrants a short external note; identify that decision and continue unaffected work. Do not turn ordinary factual qualification into a warning or a polish request into a long review report.

## Canonical Revision Files

Use one canonical path for each requested manuscript or writing deliverable. Ordinary iterations overwrite that file in place. Do not create version-suffixed, dated, timestamped, `revised`, `new`, or `final-final` copies unless the user explicitly requests snapshots or multiple alternatives. Keep rollback in version control. Do not save prompt drafts, critique passes, or failed rewrites beside the manuscript. Immutable submissions, user-provided source versions, and raw experiment records remain separate when preservation is scientifically or externally required.

## From Idea To Manuscript

Follow `materials-to-manuscript.md` for content-first drafting, result status, alignment, and the transition to page fitting. Use the requested format and venue template conventions; a NeurIPS template can be a disclosed fallback, not an initial page constraint. Resolve policy freshness and missing inputs through the relevant owner when needed, and route final compliance to `ccf-submission-checker`. Surface only material unresolved choices; do not append routine freshness or missing-input warnings to every draft.

## Information-Dense Writing

Do not use the main answer for generic process narration. The first visible artifact should be the draft, revised text, table, review response, or file path requested by the user. When a decision remains, keep its note short and concrete:

- name the exact unsupported claim,
- name the missing evidence or file,
- name the section affected,
- name the next owner only when a handoff is useful.

For full workflow demos, produce the requested concrete artifacts. Several skills may improve the same canonical artifact; do not require a separate process file from each skill.

## Citation Format Rules

Use `citation-workflow.md` as the source for attribution, verified entries, citation placement, and coverage. Preserve the project's citation style and keys. Prose emphasis follows `prose-quality-guardrails.md`; it is not a separate citation requirement.

## Flexible Suggestions

For non-review writing work, ask about a concrete unresolved fact or research choice when it changes the requested text. Base the question on supplied material; do not propose a new paper type merely to reduce perceived novelty pressure. Example:

```text
材料中把数据集分别写成“已完成标注”和“正在标注”。目前是哪一种状态？我会先完成不依赖该状态的段落。
```

Use hard blockers only for fabricated evidence, privacy risk, incompatible user constraints, or impossible format requirements.
