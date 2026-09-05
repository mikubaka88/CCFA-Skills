---
name: ccf-visual-composer
description: "Render and redesign CCF figures, visual tables, and method/architecture diagrams from supplied content. Use for 绘图美化, 排版, 配色, GPT Image 2 generation, pure SVG, and editable SVG/PDF/PPTX. Preserve values and topology. Experiment evidence design belongs to ccf-experiment-designer; manuscript rewriting and PDF-to-writing exemplars are separate."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Visual Composer

## Invocation Controls

**CCFA Handoff Mode: PARTIAL (Recommended).** Follow `metadata.ccf_skill_controls.handoff_question_mode`, `../ccf-common/references/handoff-modes.md`, and `../ccf-common/references/task-modes.md`. Reuse shared rules already in context.

For a new scientific method or architecture concept, GPT Image 2 remains the default first-pass renderer unless the user requests pure SVG/code-first output or opts out. Use the verified host capability and its privacy/image instructions. Do not label an unknown backend as GPT Image 2. Existing authorization covers necessary generation and requested reconstruction; offer extra formats only when outside the request.

## Core Rule

Create readable visuals from supplied content. Preserve values, units, uncertainty, exact labels, method modules, and typed connections. Quantitative plots use reproducible code. Missing data or topology requires the relevant evidence owner; do not invent it to complete a composition. Preserve scientific terminology and canonical uppercase acronyms; use natural case for ordinary labels.

Classify the destination as paper mechanism figure, presentation/poster, or README/outreach. Paper figures show representations and computation. Choose visual grammar from the method, not a fixed stage-card template.

## Modes And Selective References

Read only the relevant sections below. A local edit starts from the existing source and applicable QA; it does not reload the complete generation workflow.

| Mode | Use and reference |
| --- | --- |
| `visual-contract` | Non-trivial content/evidence/output decisions: `references/visual-contract.md`. |
| `figure-design`, `python-plotting` | Numerical plots: select from `references/python-plot-recipes.md`, then import the needed recipe from `resources/python/ccfa_plot_recipes.py`; read implementation only to debug or adapt it. `references/plot-inspiration-map.md` is optional for an unresolved chart choice. |
| `architecture-generation` | New concept: `references/architecture-diagram-generation.md`; paper-specific grammar only from `references/paper-vs-presentation-diagrams.md`. |
| `pure-svg-generation` | Explicit deterministic route: use the supported topology and vector authoring source directly. |
| `editable-reconstruction` | Semantic reconstruction sections in `references/architecture-diagram-generation.md`; load `references/editable-pptx.md` only for PPTX. |
| `reference-layout-blueprint` | Supplied reference composition: `references/reference-layout-blueprint.md`; use `references/adaptive-architecture-style.md` when prompt refinement is needed. |
| `icon-system` | Native primitives, reusable licensed icons, or necessary custom assets: `references/icon-system.md`. |
| `table-design`, `layout-integration` | Supplied values, panel/float/caption placement: `references/figure-table-layout.md`. |
| `render-qa` | Inspect the requested formats using the relevant checks in `references/render-qa.md`. |

Use `references/palette-and-accessibility.md` only when choosing or changing color semantics. Reuse an established palette and icon family when they remain suitable.

## Workflow

1. Resolve the requested artifact, existing source, final size, destination, formats, and scientific takeaway. For file work, read `../ccf-common/references/artifact-contracts.md` once and resolve canonical output and working paths before rendering. Keep unrelated figures in separate stable working directories; honor existing project paths.
2. Reuse an existing specification or form the relevant visual-contract fields internally. One specification holds topology, exact labels, data locations, layout, style, and required provenance. Do not save separate overlapping contracts, prompt drafts, wireframes, icon manifests, and QA logs by default. A minor edit needs only the requested change and its dependencies.
3. Select the smallest rendering route that completes the task. A new architecture concept uses the default image workflow. For an existing SVG, PPTX, or plot script, directly edit that authoring source and export affected requested formats; do not run a new raster concept pass for a label, color, spacing, data, or export change. Raster edits follow the host image-editing workflow and use the existing image as reference.
4. Preserve a detailed user prompt and add only missing content or a compact style refinement. Reuse approved topology, layout tokens, and assets. Start with one complete candidate unless alternatives are requested. Search new visual references or generate custom icons only to resolve a specific unmet need.
5. Inspect the draft. Correct local vector/native text and layout directly during authorized reconstruction; reserve raster regeneration for material composition/topology failures or a requested new visual direction. If two attempts fail to fix the same defect, diagnose the cause and change the relevant strategy. Never stop merely at an attempt count while a feasible correction remains.
6. Build requested editable outputs as semantic groups, live text, shapes, and typed connectors. Do not embed a whole raster and claim editability. Keep unavoidable raster assets separate and describe their actual editability. Generate downstream PDF/PPTX from the canonical authoring source without lossy round trips; retain only necessary reusable source and assets.
7. Check changed outputs at intended size for data/topology, labels, clipping, contrast, fonts, and requested editability. Render affected pages/slides first; perform a broader check only when a changed shared style or layout affects them. Save one current preview under the working build directory. Do not repeatedly reopen unchanged previews or regenerate already satisfactory outputs for marginal stylistic alternatives.
8. Finish the requested deliverable and check file placement, current exports, and disposable temporary files. New data/protocol decisions belong to `ccf-experiment-designer`, manuscript prose to `ccf-paper-writer`, and claim mismatches to `ccf-integrity-auditor`; keep unaffected authorized work moving.

## Output Contract

Deliver the requested visual and necessary editable source/formats first. A specification-only request needs no render. Return canonical paths, useful provenance, actual QA results, and material editability limits. Keep the full prompt, specification, and inventory in one reusable source record only when needed or requested; do not also repeat them in the final answer. Preserve explicit exact-output requests.
