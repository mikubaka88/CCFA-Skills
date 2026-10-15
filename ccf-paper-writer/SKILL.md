---
name: ccf-paper-writer
description: "Draft, revise, polish, compress, or presentation-adapt CCF manuscript prose. Use for 写作, 润色论文, research documents to complete papers, 完整初稿, 实验留空, 改写, 压缩论文, abstracts, sections, and slides. Draft content before fitting pages; preserve evidence and format. Assessment without rewriting belongs to ccf-paper-reviewer; rebuttal belongs to ccf-rebuttal-writer."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Paper Writer

## Family File Contract

Before file work, reuse canonical paths and one task/artifact working directory; default to project-root `ccfa-workfiles/<purpose>/<artifact-id>/`. Update in place, preserve inputs, and use UTF-8 with Chinese-text checks. Apply [artifact-contracts.md](../ccf-common/references/artifact-contracts.md) for naming, ownership, and task-created cleanup; handoffs inherit these paths.

## Collaboration Contract

Before specialist execution, read and apply [ccf-humanization](../ccf-humanization/SKILL.md) first, then [ccf-common](../ccf-common/SKILL.md). At every handoff, reuse their applicable active rules or refresh missing/changed ones. Both preflights are required even without prose; detailed editing, experiment, and maintenance modes run only when relevant.

Integrate necessary specialist contributions under one owner; reuse valid prerequisites and verify affected results. Follow the [cooperation routes](../ccf-common/references/routing.md) without duplicate reports.

## Invocation Controls

**CCFA Handoff Mode: PARTIAL (Recommended).** Follow `metadata.ccf_skill_controls.handoff_question_mode`, `../ccf-common/references/handoff-modes.md`, and `../ccf-common/references/task-modes.md`. User scope and existing authorization govern execution; preserve plan-only, no-browsing, exact-output, and no-new-files requests.

This skill owns manuscript text, compression, and presentation prose. Preserve the supplied problem, method mechanism, experimental setting, numbers, citation keys, and conclusion unless a research change is authorized. A requested revision authorizes ordinary accurate wording edits and necessary local checks.

Run `ccf-humanization` as the first manuscript-facing preflight. Read `../ccf-humanization/references/humanization-policy.md` and `references/prose-quality-guardrails.md`. These guide direct scientific writing; they do not start a separate review or a confirmation loop.

## Writing Standard

Write from the contribution: what problem matters, why the mechanism addresses it, what the evidence establishes, and what follows. Replace reviewer-facing reassurance, apologetic novelty claims, repeated caveats, denial-led positioning, and stacked hedges with their scientific payload. Delete sentences with no payload. Do not add a limitations sentence to each paragraph, abstract, caption, or conclusion by habit.

Keep meaningful uncertainty, known negative results, necessary assumptions, fair-comparison constraints, and mandatory disclosures in direct academic prose. Do not write that a method is confirmed, approved, or publication-ready. Explain the actual method and relevant configuration. A missing result stays missing; a proposed study is not a completed experiment. Never guess citations or insert invented measurements to complete a draft.

Use the humanization policy as the single source for punctuation and pattern thresholds. Natural writing is a semantic editing task; passing a phrase checker does not establish quality. Keep scientifically necessary terms, negation, and hedging even when a heuristic flags them.

## Modes And Reference Loading

| Mode | Deliverable | References beyond the shared prose policy |
| --- | --- | --- |
| `polish` | Revised paragraph or local passage in its source format | None unless a factual, citation, or explicit style question requires one. |
| `draft` section | Requested section with a coherent scientific argument | The relevant part of `references/section-modules.md`; citation workflow only when literature support is needed. |
| `draft` manuscript | Complete content-first manuscript, including a results-pending draft when requested | `references/materials-to-manuscript.md`, `references/storyline-blueprint.md`, and relevant section/checklist references. Read a venue guide for a requested format, not to impose an initial page budget. |
| `submission-fit` | A complete, aligned draft fitted to a specified venue or length | Venue guide, `references/length-budget-policy.md`, and `references/compression-rules.md`; verify current official rules for final compliance. |
| `compress` | Shortened source text preserving meaning and numbers | `references/compression-rules.md`. |
| `presentation` | Slides/poster/talk/Q&A prose from supplied research | Applicable presentation guidance in `references/section-modules.md` and the source paper. |

An abstract, caption, synopsis, paragraph edit, or exact JSON response does not require venue guides, full exemplars, reviewer panels, or length planning by default. Load matched exemplar cards from `references/exemplars/index.md` only for a requested style adaptation or a full manuscript that benefits from them. Never copy exemplar wording or technical content.

## Workflow

1. Identify the requested mode, output format, evidence, and target length from the conversation and supplied files. Infer routine choices; ask only for a missing decision that changes the research claim, deliverable, or feasibility. Continue independent work while that decision is pending.
2. For an authorized edit to an existing manuscript, revise that file in place and preserve Markdown/LaTeX sections, commands, citations, labels, equations, and float environments unless restructuring is requested. Follow `../ccf-common/references/artifact-contracts.md`; create no dated or `v2` copies for an ordinary iteration. Supplying a file for inspection alone does not authorize rewriting it.
3. For a new manuscript from research documents, use `references/materials-to-manuscript.md`. Draft substantive content without a page quota, check scientific and textual alignment, then fit length only when requested. Naming a venue alone does not trigger compression. An explicit submission-ready or fixed-length request includes fitting after the content check in the same task. Read `references/venue-guides/index.md` and the matched guide for template conventions; use `references/length-budget-policy.md` only in the fitting phase. Preserve a supplied template or requested format. For new LaTeX without a usable target template, NeurIPS is a disclosed format fallback, not a scientific or length requirement. `references/output-style-policy.md` governs format choices.
4. Organize the scientific argument. For a substantial introduction or full manuscript, use `references/storyline-blueprint.md`; for bounded prose, directly connect problem, insight, mechanism, evidence, and implication. Keep material scope where it changes interpretation. Do not generate a reviewer-risk register or multi-expert tournament for ordinary writing.
5. Resolve evidence prerequisites before asserting dependent claims. When literature is needed, load `references/citation-workflow.md`, use `ccf-literature-searcher` for missing sources, and update the bibliography without changing unrelated keys. Use `ccf-integrity-auditor` for unresolved citation-support or numerical conflicts. Reuse applicable verified evidence. For supplied-evidence-only or no-browsing tasks, preserve provided citations and keep unsupported claims provisional without inventing entries.
6. Draft substantive sections and supporting appendices using `references/section-modules.md` and applicable `references/writing-checklists.md` checks. Load `references/research-writing-patterns.md` only when alternative writing patterns or exemplar adaptation are useful. `references/materials-to-manuscript.md` owns result-status handling: preserve supplied results, leave missing values and dependent analysis blank, and honor an explicitly deferred experiment section. Do not invent mechanisms or pad with cautionary text.
7. For reported experimental comparisons, consult `../ccf-humanization/references/experiment-discipline.md` when method identity or protocol matters. Use supplied design specifications for a proposed method and cited evidence for prior work; do not demand runnable checkpoints or full experimental confirmation to perform a text edit.
8. For a full LaTeX manuscript with an available engine, compile and inspect errors, references, and affected layouts. Fix overflow and missing references in every phase; page count is informational during content-first drafting. Fit length only in `submission-fit` or explicitly requested compression. Put build artifacts under the established working directory and export the requested PDF only after a successful build. Preserve relative includes and build configuration. Recompile after relevant changes; do not loop to fill pages or chase harmless warnings. Leave final venue compliance to `ccf-submission-checker` when requested or necessary.
9. Check the resulting argument once with the cohesion repairs in `references/prose-quality-guardrails.md`, then apply Humanization's sentence decisions and verify that factual meaning survived revision. For a full section or paper, run `scripts/check_prose_quality.py` when available. Inspect candidates in context; fix real problems and retain justified scientific language. Use `--strict` only when a strict lint report is requested, not as a universal publication gate. Rerun only for changed content or unresolved findings.
10. For a substantial draft or changes to argument/evidence, use `ccf-paper-reviewer` to check the affected links and coherence unless already covered. Carry the drafting phase and intentionally missing evidence into the check. A results-pending draft needs a writing/alignment check, not an invented acceptance score or an automatic new-experiment campaign. Unsupported empirical assertions still require correction. Integrate authorized fixes and verify affected passages; a local edit uses local checks. Deliver the requested artifact and concrete unresolved decisions without unrelated downstream outputs.

## Output Contract

Return the actual revised text, manuscript, compressed passage, or presentation prose first in the user's format. Ordinary local edits need no mode/status/next-skill block. For full manuscript files, report their paths, substantive changes, relevant validation, and concrete unresolved evidence. Exact schemas stay exact.

A complete draft contains the requested scientific sections at appropriate depth; it may remain evidence-incomplete. Distinguish draft completion from submission readiness. Do not label unknown results as observations or claim measured score improvements from a prose revision.

## References

Load selectively by the modes above. Maintain phase/result rules in `materials-to-manuscript.md`, section responsibilities in `section-modules.md`, citation rules in `citation-workflow.md`, and fitting rules in `length-budget-policy.md`; other references apply them without duplicating the full policy.

- `references/materials-to-manuscript.md`: research-document intake, complete initial drafts, results-pending writing, and alignment before compression.
- `references/output-style-policy.md`, `references/length-budget-policy.md`: source-format preservation and later manuscript fitting.
- `references/venue-guides/index.md`, `references/exemplars/index.md`: target venue and selected style moves.
- `references/storyline-blueprint.md`, `references/section-modules.md`, `references/research-writing-patterns.md`: scientific organization and section writing.
- `references/citation-workflow.md`: verified citation insertion.
- `references/prose-quality-guardrails.md`, `references/writing-checklists.md`, `scripts/check_prose_quality.py`: semantic prose review and supporting diagnostics.
- `references/compression-rules.md`: evidence-preserving compression.
- `references/table-style-guide.md`: existing LaTeX table source guidance; visual redesign belongs to `ccf-visual-composer`.
- `references/score-lifting-loop.md`, `references/expert-review-loop.md`: applying actual reviewer deductions when that work is requested.
- `../ccf-common/references/review-output-standards.md`: conditional scores and frozen review standards, only for requested review-related outputs.
