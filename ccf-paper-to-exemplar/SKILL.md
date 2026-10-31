---
name: ccf-paper-to-exemplar
description: "Distill supplied paper PDFs into writing exemplar cards and register a requested personal library. Use for PDF to writing exemplar, 写作范例, and reusable paper-writing patterns. Preserve attribution; transfer argument structure and selected language conventions without copying scientific claims. Figure reconstruction, manuscript drafting, and review have separate owners."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# Paper-to-Exemplar

## Family File Contract

Before file work, reuse canonical paths and one task/artifact working directory; default to project-root `ccfa-workfiles/<purpose>/<artifact-id>/`. Update in place, preserve inputs, and use UTF-8 with Chinese-text checks. Apply [artifact-contracts.md](../ccf-common/references/artifact-contracts.md) for naming, ownership, and task-created cleanup; handoffs inherit these paths.

## Collaboration Contract

Before specialist execution, read and apply [ccf-humanization](../ccf-humanization/SKILL.md) first, then [ccf-common](../ccf-common/SKILL.md). At every handoff, reuse their applicable active rules or refresh missing/changed ones. Both preflights are required even without prose; detailed editing, experiment, and maintenance modes run only when relevant.

Integrate necessary specialist contributions under one owner; reuse valid prerequisites and verify affected results. Follow the [cooperation routes](../ccf-common/references/routing.md) without duplicate reports.

## Scope And Shared Controls

Distill supplied paper PDFs into reusable writing patterns, preserving source attribution and scientific meaning. This skill owns exemplar cards; manuscript drafting belongs to `ccf-paper-writer`, visual reconstruction to `ccf-visual-composer`, and scientific review to `ccf-paper-reviewer`.

Follow `../ccf-common/references/handoff-modes.md`, `../ccf-common/references/task-modes.md`, and `../ccf-common/references/artifact-contracts.md`. Resolve existing card/library and cache paths before writing. Preserve no-new-files requests by editing a named existing card or returning the analysis in context. Conversion alone does not authorize global library/default changes.

## Workflow

1. Identify PDF paths, source versions, desired writing patterns, optional venue, and authorized destination. Reuse a completed card and extraction when they match the same source and requested scope; a new source version requires checking the affected analysis.
2. If extraction is needed, run `scripts/convert.py` with explicit `--output-dir`, `--full-text`, and `--full-text-dir` pointing to the chosen working cache. For a new project, the shared default is `ccfa-workfiles/exemplars/<source-id>/`, with extraction in `cache/`; preserve established paths. The converter preserves existing cards and creates only missing skeletons. `--full-text-dir` is optional; omitting it preserves the legacy output layout. Python with `pymupdf` is required for extraction, not for reusing a valid existing card.
3. Check extraction success and page markers. Analyze the relevant full source in coherent sections; use search and targeted ranges for a local card update. Inspect actual PDF pages when equations, figures, or reading order affect interpretation. Do not substitute an abstract-only analysis for a full-paper exemplar or treat empty extraction as complete.
4. Recover how the source explains its science, using `../ccf-paper-writer/references/exemplar-style-analysis.md`. For relevant passages, inspect the scientific subject, main verb, definition placement, sentence relationships, and paragraph progression as well as the overall organization. Distinguish the source's observations from its interpretation and preserve meaningful uncertainty. Do not replace this reading with a generic introduction outline or infer quality from awards.
5. Fill or revise the existing card in place using the established headings: Story Pattern, Abstract Moves, Introduction Moves, Method Moves, Evidence Moves, Citation Patterns, Reusable Techniques, and Do-Not-Copy Boundary. Anchor source observations to pages, sections, or identifiable paragraphs; label adaptation advice separately. Verify claimed section or paragraph counts rather than inferring them from extraction matches. Describe selected techniques with their scientific purpose, not fixed sentence templates. When language adaptation is requested, include source-grounded sentence, transition, punctuation, or rhythm observations under Reusable Techniques. No new profile file or corpus quota is needed. Preserve attribution and distinguish source paraphrases, short quotations, and original hypothetical examples.
6. When library registration is requested, use `../ccf-paper-writer/references/exemplars/cards/` or the user's existing library and update `../ccf-paper-writer/references/exemplars/index.md` without duplicate entries. Preserve unrelated cards; a matching filename alone does not prove the same source. Keep raw extraction in the working cache, outside the reusable card library.
7. Update `../ccf-paper-writer/references/custom-format/default-user-format.md` only when default selection is requested. A venue-only request can select an existing relevant card through the index instead of extracting another PDF. Load `../ccf-paper-writer/references/venue-guides/index.md` only when venue-family classification is unclear.
8. Verify the card's source descriptions against the relevant original passages, including claimed organization and language examples. Completed cards have no `[ANALYZE]` or `[MANUAL]` placeholders; advice is identifiable as advice and source references are accurate. Return the canonical card paths and useful writing patterns; report actual registration/default changes only when performed. Do not echo the full PDF extraction or add generic next-action menus.

## Writer Handoff

Pass the selected card path, source identity/version, relevant original-passage locations, and observed writing moves. The writer reuses matched originals for substantive drafting and expression repair; a local edit does not automatically load default or venue card bundles. For full manuscripts or explicit style adaptation, select from `../ccf-paper-writer/references/exemplars/index.md` and load only matching sections/cards. Preserve existing user defaults without treating them as mandatory reading for every writing request.
