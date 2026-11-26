---
name: ccf-paper-to-exemplar
description: "Distill supplied papers or selected passages into reusable writing exemplar cards, register requested project/personal libraries, and save explicitly selected default exemplars. Use for PDF to writing exemplar, 提炼写作范例, 建立个人范例库, and 设置默认范例. Ordinary drafting and one-time reference learning stay with ccf-paper-writer; figure reconstruction and scientific review have separate owners."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# Paper-to-Exemplar

## Preflight And Ownership

Apply [ccf-humanization](../ccf-humanization/SKILL.md) first, then [ccf-common](../ccf-common/SKILL.md); reuse applicable active rules at handoffs. Both remain required. Handoff mode is **PARTIAL**, under Common's [handoff rules](../ccf-common/references/handoff-modes.md).

Own reusable writing cards and requested library registration. Manuscript prose and one-time learning from a reference stay with `ccf-paper-writer`; do not make card extraction a prerequisite for ordinary writing. Visual reconstruction and scientific review retain their separate owners. Preserve attribution and the source's actual scientific meaning.

For files, use [artifact-contracts.md](../ccf-common/references/artifact-contracts.md). Reuse the existing card/source/cache and update in place; the new-task default is `ccfa-workfiles/exemplars/<source-id>/`. A no-new-files request can return the analysis in context. Reading or converting a paper does not authorize library registration or preference changes.

## Workflow

1. Identify the source/version, writing question and requested coverage: passage, section or whole paper. Reuse a matching completed analysis. An introduction paragraph needs its relevant context, not a forced full-paper audit; a full-paper request still requires reading coherent sections rather than extrapolating from the abstract.
2. Read an existing original-text extraction directly. Only when PDF extraction is needed, run `scripts/convert.py` with explicit `--output-dir`, `--full-text`, and `--full-text-dir` in the chosen task directory. `--section introduction` or another selected function creates a scoped skeleton; repeat the option when useful. Omit it for the compatible whole-paper skeleton. The converter extracts text and creates unfinished cards; it does not perform the analysis. It preserves existing cards. `pymupdf` is needed only for PDF extraction.
3. Check source locations and extraction quality. Inspect actual PDF pages when reading order, equations or figures affect interpretation. Use [exemplar-style-analysis.md](../ccf-paper-writer/references/exemplar-style-analysis.md) to recover the scientific subject, operations, sentence relationships and paragraph progression. Judge the passage itself; awards do not establish a writing technique.
4. For a whole-paper card, retain all eight established sections: Story Pattern, Abstract Moves, Introduction Moves, Method Moves, Evidence Moves, Citation Patterns, Reusable Techniques and Do-Not-Copy Boundary. Read and anchor the relevant source throughout; evidence can be a proof, analysis, observation or experiment as the paper actually uses it. For passage/section coverage, write the relevant observed moves plus Reusable Techniques and Do-Not-Copy Boundary, omitting unexamined sections. Record the original source/version and page, section or paragraph anchors; distinguish observed writing from adaptation advice. Preserve source-grounded language observations without imposing sentence templates, paragraph counts or a corpus quota. Completed cards have no `[ANALYZE]` or `[MANUAL]` placeholders.
5. Register only when requested, using `scripts/personal_library.py`. Project registration uses `<project>/.ccfa/exemplars/library.json`; explicit `--scope user` uses `$CODEX_HOME/ccfa/exemplars/library.json` or `~/.codex/ccfa/exemplars/library.json`. Registration references the existing completed card and original source without copying the PDF. Preserve their stable paths. Built-in cards, index and default format are maintained as package resources, not personal data; change them only during an explicitly authorized family-maintenance task.
6. When the user explicitly selects default exemplars, save the registered IDs with `set-default` in the requested project or personal scope. Preserve other defaults when no change is requested. A project without an explicit selection inherits personal defaults; a project selection overrides them. The existing built-in custom format can still be explicitly selected, without editing its installed file to store private preferences.
7. Check the resulting source descriptions against the original passages. Return the canonical card and useful techniques; mention registration/default changes only if performed. Do not echo a full extraction or create a compulsory analysis report during drafting.

## Personal Library Commands

Use the actual source/version, locations and writing functions. Registration rejects unfinished skeletons, updates the same ID without duplicate rows, and requires a new ID or explicit `--replace-source` to assign an existing ID to another paper.

```bash
python ccf-paper-to-exemplar/scripts/personal_library.py register --project . --id paper-a-motivation --card ccfa-workfiles/exemplars/paper-a/source/card.md --source ccfa-workfiles/exemplars/paper-a/cache/original.full.md --source-id paper-a --source-version accepted --location "Section 1 paragraph 2" --function motivation --coverage passage
python ccf-paper-to-exemplar/scripts/personal_library.py query --project . --function motivation
python ccf-paper-to-exemplar/scripts/personal_library.py set-default --project . --id paper-a-motivation
```

`query` reads registry metadata and file stats, not paper/card contents, and creates no files. It first matches the writing question/functions, then prioritizes matching defaults; a default does not make an unrelated card relevant. Results retain card/source paths, version, locations, function, coverage and `is_default`; `defaults_scope` identifies project selection or personal inheritance. Changed or missing files are excluded until their analysis is checked and registered again. `--query` searches metadata, and `--limit` controls returned candidates, not how many papers the writer must use. Ordinary registration never changes writing defaults. `set-default --id` may be repeated for multiple exemplars; `--clear` explicitly selects none, while project `--inherit` restores personal inheritance. Personal selection requires explicit `--scope user`.

## Writer Handoff

Pass the selected card path, original source/version, relevant passage locations, coverage and observed moves. The writer reads the matched original passage before adaptation; a card is navigation, not original prose. Personal-library metadata can supplement [the built-in index](../ccf-paper-writer/references/exemplars/index.md) without loading every card or changing defaults. Ordinary one-time reference use stays in the writer's current context and creates no library entry.
