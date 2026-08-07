---
name: ccf-visual-composer
description: "Compose, generate, reconstruct, and QA publication-grade CCF paper visuals: data-analysis figures, tables, method/architecture diagrams, scientific schematics, captions, palettes, panel maps, Python plotting code, and editable SVG/PDF deliverables. Use for figure/table layout, visual QA, palette selection, LaTeX placement, multi-panel design, creative data visualization, architecture diagrams, pipeline/system/model diagrams, GPT Image 2 (gptimage2 / gpt-image-2) prompt design and confirmed generation, vector reconstruction, source-data traceability, and manuscript visual integration. Do not design experiments, invent results or components, write manuscript prose as the main task, or perform final submission compliance."
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

**CCFA Handoff Mode: PARTIAL (Recommended).** Follow `metadata.ccf_skill_controls.handoff_question_mode` and `../ccf-common/references/handoff-modes.md`.

Treat external image generation and editable-vector reconstruction as two separate user-authorized actions. Before an architecture-diagram image call, show the content-derived prompt and ask explicitly whether to invoke GPT Image 2, unless the user already authorized that exact call in the current request. After every generated architecture image, ask whether the user wants an editable SVG/PDF version. Do not start reconstruction until the user agrees.

## Core Rule

Make every visual evidence-bearing, readable, and integrated with the manuscript. Start from a visual contract, not a template. Never invent data, numbers, statistics, baselines, sample sizes, architecture modules, data flows, training signals, labels, images, captions that imply unsupported results, or official venue rules.

Apply title case to every English word displayed inside a figure: capitalize only the first letter and keep the remaining letters lowercase. For example, use `Visual Composer`, `Gpt Image 2`, and `Editable Svg/Pdf`, never `VISUAL COMPOSER`, `GPT IMAGE 2`, or `EDITABLE SVG/PDF`. Do not render English words in all caps in titles, module labels, legends, axes, annotations, badges, tables, or generated-image prompts. Preserve canonical spelling in manuscript prose, captions, filenames, and source metadata when scientific identifiers require it; the title-case rule governs visible text inside the image unless the user explicitly overrides it.

## Modes

- `visual-contract`: define core claim, reviewer question, evidence layer, source data, panel/table map, caption role, and output constraints.
- `figure-design`: design multi-panel figures, chart families, image plates, schematics, legends, labels, color, and export specs from supplied evidence.
- `architecture-generation`: turn supplied paper/method content into a scientific diagram specification and tailored prompt; after explicit confirmation, invoke GPT Image 2 through the available image-generation capability and inspect the result.
- `editable-reconstruction`: after the required post-generation confirmation, rebuild an approved architecture image as semantic, editable SVG and export a vector PDF when requested.
- `python-plotting`: write or adapt Python plotting code using bundled recipes, standard-library SVG output, analytical chart recipes, composite dashboards, or optional libraries available in the user's environment.
- `table-design`: design publication tables, numeric precision, grouping, ordering, notes, width strategy, and LaTeX table structure from supplied values.
- `layout-integration`: place figures/tables near first discussion, align captions/cross-references, choose single-column/full-width floats, and keep visuals connected to text.
- `render-qa`: compile or render when files exist; inspect clipping, overlap, float order, font, contrast, rasterization, and source-data traceability.

## Workflow

1. Identify target venue/family, manuscript context, supplied data/results or method content, artifact type, output format, and whether the user wants creation, redesign, or QA.
2. Load `../ccf-common/references/task-modes.md` and `../ccf-common/references/privacy-and-evidence.md` when the task touches manuscript files, private results, or project artifacts.
3. If claims, evidence, source data, or result values are missing, mark the gap and hand off to `ccf-experiment-designer`; do not fill the gap by invention. If architecture topology, labels, or method content are missing, inspect the user-authorized project sources or ask a targeted question instead of inventing modules.
4. Load `references/visual-contract.md` and write the visual contract before changing layout or style.
5. Load `references/palette-and-accessibility.md` before choosing colors; prefer accessible scientific palettes and semantic consistency over decorative color.
6. Normalize the visible English text inventory to title case before plotting, prompting, or reconstruction. Reject all-caps image text during render QA and correct it before delivery.
7. Route ordinary quantitative/result figures to deterministic, reproducible plotting code. Load `references/python-plot-recipes.md` and use `resources/python/ccfa_plot_recipes.py` as a runnable starting point. Prefer analytical plot families when the evidence calls for them: pie/donut for composition, grouped bars for categorical comparisons, volcano plots for effect-size/significance screening, correlation heatmaps for relationship matrices, and composite dashboards for multi-view analysis. If a better plot grammar is needed, load `references/plot-inspiration-map.md` and invent a new evidence-bound chart without copying external code.
8. For a method, model, system, pipeline, framework, or architecture diagram, load `references/architecture-diagram-generation.md`. Build a content-grounded diagram specification and generation prompt first. Show the prompt and obtain the required GPT Image 2 confirmation before the external call; if the selected backend cannot be verified as GPT Image 2, state that limitation and do not mislabel the backend.
9. After generation, inspect the actual image against the diagram specification. Then ask the mandatory editable-deliverable question from `references/architecture-diagram-generation.md`. On agreement, reconstruct semantic groups, shapes, connectors, and live text as SVG; derive PDF from the vector source. Embedding or auto-tracing the raster alone does not satisfy editability.
10. Load `references/figure-table-layout.md` for multi-panel composition, LaTeX float/table choices, caption/cross-reference placement, and manuscript integration.
11. Load `references/render-qa.md`; when source files exist, compile/render and inspect the actual output. When only a spec is requested, include a QA checklist and no-fabrication status.
12. Hand off to `ccf-paper-writer` for prose rewrites or narrative placement text, `ccf-integrity-auditor` for number/claim consistency, and `ccf-submission-checker` for final venue/package compliance.

## Output Contract

Return the requested artifact first. For a full visual-composition request, use this structure:

```text
Mode:
Target venue / format:
Visual contract:
Panel or table map:
Plot recipe or code path:
Architecture prompt / generation status:
Editable SVG/PDF status:
Palette and accessibility:
LaTeX / manuscript placement:
Caption and cross-reference plan:
Render QA ledger:
Missing evidence or data:
No-fabrication status:
Next CCFA owner:
```

## References

- `references/visual-contract.md`: figure/table contract, evidence hierarchy, panel map, source-data traceability, and anti-loop state files.
- `references/palette-and-accessibility.md`: top-journal/scientific palettes, color-vision safety, print/grayscale checks, and semantic color rules.
- `references/python-plot-recipes.md`: bundled Python recipe library, chart-selection rules, and custom plot invention prompt.
- `references/plot-inspiration-map.md`: conceptual map from open-source visualization projects to CCFA-native plotting decisions.
- `references/architecture-diagram-generation.md`: architecture-content extraction, scientific prompt construction, GPT Image 2 confirmation gate, post-generation editable-format question, semantic SVG/PDF reconstruction, and architecture QA.
- `references/figure-table-layout.md`: multi-panel design, table design, LaTeX float placement, captions, cross-references, and manuscript integration.
- `references/render-qa.md`: render-visible QA checklist, escalation rules, and visual issue ledger.
- `resources/python/ccfa_plot_recipes.py`: runnable standard-library SVG plotting recipes for paper-ready data-analysis figures.
