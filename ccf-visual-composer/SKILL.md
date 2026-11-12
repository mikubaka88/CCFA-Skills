---
name: ccf-visual-composer
description: "Render and redesign scientific figures, visual tables, and method/architecture diagrams from supplied content, including biological data. Use for 绘图美化, 多面板分析图, 定量与消融可视化, 排版, 配色, GPT Image 2 generation, pure SVG, and editable SVG/PDF/PPTX. Preserve values and topology. Experiment evidence design belongs to ccf-experiment-designer; manuscript rewriting and PDF-to-writing exemplars are separate."
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

Reuse canonical paths and one stable task directory, normally `ccfa-workfiles/<purpose>/<artifact-id>/`. Update current artifacts in place, preserve inputs, and check UTF-8/Chinese text. Apply [artifact-contracts.md](../ccf-common/references/artifact-contracts.md) when writing files.

## Collaboration Contract

Apply [ccf-humanization](../ccf-humanization/SKILL.md) first, then [ccf-common](../ccf-common/SKILL.md), once. Reuse their active rules and valid prerequisites at handoffs. Integrate only a needed contribution through [routing.md](../ccf-common/references/routing.md); no duplicate intake or reports.

## Invocation Controls

**CCFA Handoff Mode: PARTIAL (Recommended).** Preserve `metadata.ccf_skill_controls` and Common's [handoff modes](../ccf-common/references/handoff-modes.md). User-specified tools, formats and existing authoring sources take priority.

| Current artifact | Preferred route |
| --- | --- |
| New method, architecture or flow diagram | Generate a complete composition with GPT Image from the supplied science and actual reference images. Let the model arrange groups, proportions, illustrations and typography together. Straight lines, alignment and readable labels are quality requirements, not reasons by themselves to build a Python skeleton. |
| Numerical analysis, ablation, benchmark or biological data | Use Python and supplied data. Compose supported elements into one coherent analysis unit; preserve exact values and statistics. |
| Method figure containing quantitative plots | Preserve code-rendered numeric marks, axes and labels; use image generation for the surrounding scientific illustration without redrawing results. |
| Existing raster / code / native editable figure | Edit its current authoring source through the host's relevant workflow; refresh affected exports. A local edit does not restart concept generation. |
| Explicit code route, exact geometric tolerances, or requested editable output | Use appropriate code/native authoring. An unspecified editability request prefers native PPTX; SVG requires an explicit SVG request. |

Deliver PNG by default. Follow host image instructions and use an available authorized alternative if image generation is unavailable. Numerical reproducibility does not imply a need to reconstruct every diagram in code.

## Preserve The User's Visual Requirements

- Preserve scientific modules, typed connections, labels, equations, values, units and uncertainty. Resolve a material data/topology gap with its owner; do not invent content to finish the layout.
- Fit the actual paper slot, with compact meaningful groups, aligned peers, short clear connections and legible text. Use the reference's visual hierarchy; allow content-fit asymmetry and adequate connector clearance. No default square, mandatory grid, equal-width boxes or prescribed orientation. Honor explicit pixel/gap requirements; otherwise leave detailed placement to the renderer.
- Use Times New Roman by default or selected Comic Sans MS, subject to user/venue overrides. Bold titles, legends and axis/colorbar labels and ticks. Method headings stand out; body labels and equations keep a restrained hierarchy. Use coherent semantic colors, lighter bar/box fills and substantial darker same-hue outlines; dense points and heatmaps keep their own encoding.
- Build information density from article-specific relationships: density + conditional region + state/weighted shares; quantile boxes + tail whiskers + a quantile curve; or bars + same-unit trends + supplied ranges. Labels alone do not add analysis. Keep additional views when their scientific questions or domains require them.
- Preserve sample IDs or an explicit matched-order contract; equal lengths do not prove pairing. Match units, shared scales, entity colors and actual observation times. Retain all required reference elements and keep Chinese/math glyphs readable.

## Workflow

1. Reuse the current paper, data, references and decisions. Establish the scientific message, essential content, final size and requested formats internally; save one compact source record only when useful. Missing visual preferences are routine design choices, not a new intake form.
2. Select the route above. For a new data composition, classify input data and chart type independently with `resources/python/ccfa_figure_library.py route`, then inspect only selected candidates and their `element_plan`. Reuse source data through existing bindings. Primitives/extracted panels are components, and original templates and reference pairs remain available. For equally suitable choices, use the library's automatic selection without asking for a seed or forcing usage balance.
3. For image generation, attach useful authorized references and identify their roles. Preserve a good user prompt; append only missing refinements. Otherwise send the supported content/connections, reference roles, and a short finish request. Keep exact science; omit duplicated inventories, whole skill text, speculative warnings and pixel-by-pixel prescriptions unless the task needs them. Start with one complete candidate; additional designs follow the request or effective `figure_variants` preference.
4. Inspect the actual result once at final size for scientific fidelity and visual quality: topology/values/text, grouping, alignment, information density, contrast and readable spacing. Verify required source-to-target paths rather than inferring connections from proximity. Group related defects in one region into one local correction, preserve accepted content, and recheck its attached connections afterward. Code edits rerender their affected source; raster edits follow host image instructions. If the same defect survives two corrections, change the relevant strategy rather than repeating the same attempt.
5. Deliver the figure and requested formats with necessary reusable sources. Editable delivery uses live native objects, not a whole embedded raster. Keep one current source/prompt and preview, remove task-created disposable files, and preserve inputs and required examples. No automatic SVG, editable rebuild, QA ledger or second generation pass.

## Modes And Selective References

The entry above is sufficient for a straightforward generation. Load only detail needed for the current decision; do not read the table as a checklist.

| Mode | Load when needed |
| --- | --- |
| `visual-contract` | [visual-contract.md](references/visual-contract.md): unresolved scientific encodings, complex composition or cross-panel consistency. |
| `architecture-generation` | [architecture-diagram-generation.md](references/architecture-diagram-generation.md): complex topology, prompt examples, code authoring or reconstruction. |
| `reference-layout-blueprint` | [reference-layout-blueprint.md](references/reference-layout-blueprint.md): an ambiguous reference role or detailed reconstruction. [adaptive-architecture-style.md](references/adaptive-architecture-style.md): a missing visual direction; an adequate supplied reference needs no preset search. |
| `figure-design`, `python-plotting` | [figure-design-library.md](references/figure-design-library.md): routing/bindings/linked layouts; [python-plot-recipes.md](references/python-plot-recipes.md): selected renderer; [figure-examples.md](references/figure-examples.md): requested examples/paper cards. |
| `pure-svg-generation`, `editable-reconstruction` | Explicit format request: [editable-pptx.md](references/editable-pptx.md) or architecture reference's semantic reconstruction. Preserve existing editable sources. |
| `icon-system` | [icon-system.md](references/icon-system.md): an unmet reusable asset or licensing decision, not a compulsory icon-extraction pass. |
| `table-design`, `layout-integration` | [figure-table-layout.md](references/figure-table-layout.md): table or manuscript integration. |
| `render-qa` | [render-qa.md](references/render-qa.md): a relevant unresolved defect or requested format check. |

Use [palette-and-accessibility.md](references/palette-and-accessibility.md) for a palette/accessibility decision. Return the artifact first, with concise provenance and actual checks; keep process instructions out of the figure and do not repeat the full prompt unless requested.
