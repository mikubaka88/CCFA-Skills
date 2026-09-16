---
name: ccf-paper-writer
description: "Draft, revise, polish, compress, or presentation-adapt CCF manuscript prose. Use for 写作, 润色论文, 改写, 压缩论文, abstracts, sections, slides, and rewrites based on reviews. Preserve supplied evidence and format. Assessment without rewriting belongs to ccf-paper-reviewer; rebuttal belongs to ccf-rebuttal-writer."
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

Before writing, resolve the canonical output and one stable working directory per task/artifact. Reuse explicit or established task paths; otherwise use project-root `ccfa-workfiles/<purpose>/<artifact-id>/`, with `source/`, `assets/`, `cache/`, and `build/` only as needed. Update current files in place; do not scatter intermediates or create iteration copies. Preserve inputs and required evidence; clean only verified disposable files created by this task. Use UTF-8 text I/O and check Chinese text after saving or rendering. For file work, apply [artifact-contracts.md](../ccf-common/references/artifact-contracts.md) and reuse the same paths across skill transitions.

## Collaboration Contract

Before specialist execution, read and apply [ccf-humanization](../ccf-humanization/SKILL.md) first, then [ccf-common](../ccf-common/SKILL.md). At every handoff, reuse their applicable active rules or refresh missing/changed ones. Both preflights are required even without prose; detailed editing, experiment, and maintenance modes run only when relevant.

Keep one integrating owner and actively use other skills to resolve missing prerequisites or check material findings. Reuse applicable evidence; do not skip necessary groundwork to save tokens. Before finalizing, integrate contributions and verify affected results. Follow the conditional [cooperation routes](../ccf-common/references/routing.md); avoid unrelated stages and duplicate reports.

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
| `draft` manuscript | Complete evidence-bound manuscript | Venue guide, `references/length-budget-policy.md`, `references/storyline-blueprint.md`, and relevant section/checklist references. |
| `compress` | Shortened source text preserving meaning and numbers | `references/compression-rules.md`. |
| `presentation` | Slides/poster/talk/Q&A prose from supplied research | Applicable presentation guidance in `references/section-modules.md` and the source paper. |

An abstract, caption, synopsis, paragraph edit, or exact JSON response does not require venue guides, full exemplars, reviewer panels, or length planning by default. Load matched exemplar cards from `references/exemplars/index.md` only for a requested style adaptation or a full manuscript that benefits from them. Never copy exemplar wording or technical content.

## Workflow

1. Identify the requested mode, output format, evidence, and target length from the conversation and supplied files. Infer routine choices; ask only for a missing decision that changes the research claim, deliverable, or feasibility. Continue independent work while that decision is pending.
2. For an authorized edit to an existing manuscript, revise that file in place and preserve Markdown/LaTeX sections, commands, citations, labels, equations, and float environments unless restructuring is requested. Follow `../ccf-common/references/artifact-contracts.md`; create no dated or `v2` copies for an ordinary iteration. Supplying a file for inspection alone does not authorize rewriting it.
3. For a full submission manuscript, read `references/venue-guides/index.md` and the matched guide, then establish a section budget using `references/length-budget-policy.md`. If no venue or guide is available, use the existing NeurIPS guide/template as a disclosed drafting assumption. `references/output-style-policy.md` controls ambiguous format choices. Current final policy requires official verification; local guides can support a provisional draft.
4. Organize the scientific argument. For a substantial introduction or full manuscript, use `references/storyline-blueprint.md`; for bounded prose, directly connect problem, insight, mechanism, evidence, and implication. Keep material scope where it changes interpretation. Do not generate a reviewer-risk register or multi-expert tournament for ordinary writing.
5. Resolve evidence prerequisites before asserting dependent claims. When literature is needed, load `references/citation-workflow.md`, use `ccf-literature-searcher` for missing sources, and update the bibliography without changing unrelated keys. Use `ccf-integrity-auditor` for unresolved citation-support or numerical conflicts. Reuse applicable verified evidence. For supplied-evidence-only or no-browsing tasks, preserve provided citations and keep unsupported claims provisional without inventing entries.
6. Draft the requested artifact. Use `references/research-writing-patterns.md`, the relevant `references/section-modules.md` passages, and applicable `references/writing-checklists.md` checks for substantial writing only. A full paper includes all scientifically relevant and venue-required sections, with explicit `TBD` placeholders for unavailable evidence. Keep methods, setups, and analyses substantive; never pad with generic caution, assumed modules, or imaginary results.
7. For reported experimental comparisons, consult `../ccf-humanization/references/experiment-discipline.md` when method identity or protocol matters. Use supplied design specifications for a proposed method and cited evidence for prior work; do not demand runnable checkpoints or full experimental confirmation to perform a text edit.
8. For a full LaTeX manuscript with an available engine, compile and inspect page count, errors, references, and affected layouts. Fix concrete issues, expand actual explanatory gaps, and compress excess content. Put auxiliary files, build logs, and current previews under the established build directory or chosen task working directory; export the requested PDF to its canonical path only after a successful build. Preserve existing relative includes and build configuration. Recompile after relevant changes; if another pass makes no substantive progress, revise the approach or report the exact remaining issue. Do not loop to fill pages or chase harmless warnings. Leave final venue compliance to `ccf-submission-checker` when requested or necessary.
9. Check the resulting prose once with Humanization's sentence decisions. For a full section or paper, run `scripts/check_prose_quality.py` when available. Inspect defensive-language candidates in context; fix real problems and retain justified scientific language. Use `--strict` only when a strict lint report is requested, not as a universal publication gate. Rerun only for changed content or unresolved findings.
10. For a substantial draft or changes to argument/evidence, use `ccf-paper-reviewer` to check the affected claim-evidence links, coherence, and unresolved review findings unless these checks already cover the current text. Integrate corrections within the authorized writing scope and verify them; no separate full review report or acceptance score is required. A local wording edit uses local checks. If missing evidence needs a new research decision, leave the affected claim unresolved and continue supported work. Deliver after applicable prerequisites and checks, without starting unrelated downstream outputs.

## Output Contract

Return the actual revised text, manuscript, compressed passage, or presentation prose first in the user's format. Ordinary local edits need no mode/status/next-skill block. For full manuscript files, report their paths, substantive changes, relevant validation, and concrete unresolved evidence. Exact schemas stay exact.

A complete draft contains the requested scientific sections at appropriate depth; it may remain evidence-incomplete. Distinguish draft completion from submission readiness. Do not label unknown results as observations or claim measured score improvements from a prose revision.

## References

Load selectively by the modes above:

- `references/output-style-policy.md`, `references/length-budget-policy.md`: source-format preservation and manuscript budgeting.
- `references/venue-guides/index.md`, `references/exemplars/index.md`: target venue and selected style moves.
- `references/storyline-blueprint.md`, `references/section-modules.md`, `references/research-writing-patterns.md`: scientific organization and section writing.
- `references/citation-workflow.md`: verified citation insertion.
- `references/prose-quality-guardrails.md`, `references/writing-checklists.md`, `scripts/check_prose_quality.py`: semantic prose review and supporting diagnostics.
- `references/compression-rules.md`: evidence-preserving compression.
- `references/table-style-guide.md`: existing LaTeX table source guidance; visual redesign belongs to `ccf-visual-composer`.
- `references/score-lifting-loop.md`, `references/expert-review-loop.md`: applying actual reviewer deductions when that work is requested.
- `../ccf-common/references/review-output-standards.md`: conditional scores and frozen review standards, only for requested review-related outputs.
