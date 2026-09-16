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

## Family File Contract

Before writing, resolve the canonical output and one stable working directory per task/artifact. Reuse explicit or established task paths; otherwise use project-root `ccfa-workfiles/<purpose>/<artifact-id>/`, with `source/`, `assets/`, `cache/`, and `build/` only as needed. Update current files in place; do not scatter intermediates or create iteration copies. Preserve inputs and required evidence; clean only verified disposable files created by this task. Use UTF-8 text I/O and check Chinese text after saving or rendering. For file work, apply [artifact-contracts.md](../ccf-common/references/artifact-contracts.md) and reuse the same paths across skill transitions.

## Collaboration Contract

Before specialist execution, read and apply [ccf-humanization](../ccf-humanization/SKILL.md) first, then [ccf-common](../ccf-common/SKILL.md). At every handoff, reuse their applicable active rules or refresh missing/changed ones. Both preflights are required even without prose; detailed editing, experiment, and maintenance modes run only when relevant.

Keep one integrating owner and actively use other skills to resolve missing prerequisites or check material findings. Reuse applicable evidence; do not skip necessary groundwork to save tokens. Before finalizing, integrate contributions and verify affected results. Follow the conditional [cooperation routes](../ccf-common/references/routing.md); avoid unrelated stages and duplicate reports.

## Invocation Controls

**CCFA Handoff Mode: PARTIAL (Recommended).** Follow `metadata.ccf_skill_controls.handoff_question_mode`, `../ccf-common/references/handoff-modes.md`, and `../ccf-common/references/task-modes.md`. Reuse shared rules already in context.

For a new scientific method or architecture concept, GPT Image 2 remains the default first-pass renderer unless the user requests pure SVG/code-first output or opts out. Use the verified host capability and its privacy/image instructions. Do not label an unknown backend as GPT Image 2. Existing authorization covers necessary generation and requested reconstruction; offer extra formats only when outside the request.

## Core Rule

Create readable visuals from supplied content. Preserve values, units, uncertainty, exact labels, method modules, and typed connections. Quantitative plots use reproducible code. Missing data or topology requires the relevant evidence owner; do not invent it to complete a composition. Preserve scientific terminology and canonical uppercase acronyms; use natural case for ordinary labels.

Classify the destination as paper mechanism figure, presentation/poster, or README/outreach. Paper figures show representations and computation. Choose visual grammar from the method, not a fixed stage-card template.

For new compositions, use `references/visual-contract.md`: a compact content-fit canvas, shared alignment anchors, scaled gaps, and typography checked at final size. Do not default to a square or force a fixed aspect ratio. Times New Roman is the default; Comic Sans MS serves a requested comic treatment, subject to user/venue typography. For a new visual direction, choose one functional preset from `references/adaptive-architecture-style.md`. Inspect supplied references, allocate space by explanatory importance, and keep only necessary labels/numbers.

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
2. Resolve scientific prerequisites before rendering dependent content: source values, units, metric meaning, topology, and intended message. Use `ccf-experiment-designer` for unresolved result semantics, the method's owner for topology, or `ccf-integrity-auditor` for source conflicts; integrate their evidence without inventing missing content. Reuse one specification for topology, labels, data locations, layout, style, and provenance. Do not save overlapping contracts, prompt drafts, wireframes, or QA logs. A minor edit reuses unchanged prerequisites and checks only affected dependencies.
3. Select the smallest rendering route that completes the task. A new architecture concept uses the default image workflow. For an existing SVG, PPTX, or plot script, directly edit that authoring source and export affected requested formats; do not run a new raster concept pass for a label, color, spacing, data, or export change. Raster edits follow the host image-editing workflow and use the existing image as reference.
4. Preserve a detailed user prompt and add missing constraints once. For a full redesign, include the reference roles, layout geometry, text inventory, typography, and palette needed to make it concrete; do not truncate these to an arbitrary word limit. Reuse approved topology, layout tokens, and assets. Start with one complete candidate unless alternatives are requested. Search or generate assets only to resolve a specific unmet need.
5. Inspect the draft against the layout and scientific contract. Correct vector/native text and geometry during requested reconstruction; for raster delivery, use a targeted image edit for text, spacing, or illustration defects and preserve accepted regions. If two attempts fail to fix the same defect, diagnose the cause and change the relevant strategy. Never stop merely at an attempt count while a feasible correction remains.
6. Build requested editable outputs as semantic groups, live text, shapes, and typed connectors. Do not embed a whole raster and claim editability. Keep unavoidable raster assets separate and describe their actual editability. Generate downstream PDF/PPTX from the canonical authoring source without lossy round trips; retain only necessary reusable source and assets.
7. Check changed outputs for data/topology, whole-figure compactness, shared edges/baselines, final-size text, clipping, contrast, and requested editability. A local edit also checks attached connectors and protected regions. Render affected pages/slides first; broaden only when a changed shared style/layout affects them. Save one current preview under the working build directory; reuse satisfactory inspections.
8. Finish the requested deliverable and check file placement, current exports, and disposable temporary files. New data/protocol decisions belong to `ccf-experiment-designer`, manuscript prose to `ccf-paper-writer`, and claim mismatches to `ccf-integrity-auditor`; keep unaffected authorized work moving.

## Output Contract

Deliver the requested visual and necessary editable source/formats first. A specification-only request needs no render. Return canonical paths, useful provenance, actual QA results, and material editability limits. Keep the full prompt, specification, and inventory in one reusable source record only when needed or requested; do not also repeat them in the final answer. Preserve explicit exact-output requests.
