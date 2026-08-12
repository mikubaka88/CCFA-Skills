---
name: ccf-visual-composer
description: "Own rendered visuals and visual redesign from supplied content or values: plot, beautify, lay out, generate, reconstruct, and QA paper figures, visual tables, method/architecture diagrams, icons, palettes, reference-guided layout control, and editable SVG/PDF/PPTX. Use for result-table layout, color/readability improvement, visual table redesign without changing numbers, 绘图美化, 排版, 配色, architecture diagrams, GPT Image 2 generation, reference-driven composition, explicit pure SVG, and editable reconstruction. Visual beautification remains here even for experiment results. Do not choose datasets/baselines/metrics, design evidence semantics, invent content, review the paper, rewrite prose, or convert PDFs into writing exemplars."
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

Treat image generation and editable reconstruction as two separate stages. For method, architecture, system, pipeline, framework, and illustrative scientific diagrams, use GPT Image 2 as the default first-pass renderer unless the user explicitly says not to use it. A request to create such a diagram authorizes the default image-generation stage; do not add a redundant pre-generation confirmation. After every generated image, show the raster draft and ask whether the user wants it reconstructed as editable SVG, vector PDF, editable PPTX, or a combination. Do not start reconstruction until the user agrees. Use the pure-SVG-first route only when the user explicitly rejects GPT Image 2 or explicitly asks for pure SVG/code-first output.

Classify the destination before drawing: `paper mechanism figure`, `PPT/Poster graphic`, or `README/outreach infographic`. A paper architecture request must expose the computation graph and pass `references/paper-vs-presentation-diagrams.md`; do not use slide-style stage cards, hero headings, callout dashboards, or presentation prose merely because they look polished. Presentation grammar is allowed only for an explicitly presentation-facing artifact and must be labeled accordingly.

## Core Rule

Make every visual evidence-bearing, readable, and integrated with the manuscript. Start from a visual contract, not a template. Never invent data, numbers, statistics, baselines, sample sizes, architecture modules, data flows, training signals, labels, images, captions that imply unsupported results, or official venue rules.

Preserve strong user prompts. When an architecture prompt already specifies the scientific topology, components, labels, and visual intent, keep it verbatim and append only a compact content-fit refinement. Do not replace it with a longer house-style prompt. When the input is a manuscript or sparse notes instead, extract a factual diagram specification and build the prompt from that evidence. Treat prompt length as a cost and latency surface.

Use natural title case or sentence case for ordinary English displayed inside a figure, while preserving canonical uppercase for acronyms, initialisms, and standardized technical abbreviations. For example, use `Visual Composer`, `GPT Image 2`, `Structure QA`, and `Editable SVG/PDF/PPTX`, never `VISUAL COMPOSER`, `Gpt Image 2`, `Structure Qa`, or `Editable Svg/Pdf/Pptx`. Acronyms such as `CCF`, `AI`, `GPT`, `QA`, `SVG`, `PDF`, `PPTX`, and `PNG` remain uppercase. Do not use all caps for complete ordinary-language titles, module names, legends, axes, annotations, badges, or table headers merely for emphasis.

## Modes

- `visual-contract`: define core claim, reviewer question, evidence layer, source data, panel/table map, caption role, and output constraints.
- `figure-design`: design multi-panel figures, chart families, image plates, schematics, legends, labels, color, and export specs from supplied evidence.
- `architecture-generation`: turn supplied paper/method content into a scientific diagram specification and tailored prompt; invoke GPT Image 2 as the default first-pass renderer and inspect the result.
- `pure-svg-generation`: generate diagram structure directly as SVG/code only when the user explicitly declines GPT Image 2 or explicitly requests a pure-SVG/code-first artifact; label the result and any evaluation based on it as pure SVG generation.
- `icon-system`: select one coherent public SVG family for common concepts and generate isolated custom icons only for method-specific concepts that the public family cannot express.
- `reference-layout-blueprint`: derive a content-fit wireframe from user-authorized or public scientific references without copying their exact composition, icons, or styling.
- `editable-reconstruction`: after the required post-generation confirmation, rebuild an approved architecture image as semantic SVG/PDF and/or an editable PPTX with native objects and isolated icon assets.
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
6. Normalize visible English to natural title or sentence case before plotting, prompting, or reconstruction, while preserving canonical uppercase acronyms and initialisms. Reject both all-caps ordinary phrases and incorrectly lowercased acronyms during render QA.
7. Route ordinary quantitative/result figures to deterministic, reproducible plotting code. Load `references/python-plot-recipes.md` and use `resources/python/ccfa_plot_recipes.py` as a runnable starting point. Prefer analytical plot families when the evidence calls for them: pie/donut for composition, grouped bars for categorical comparisons, volcano plots for effect-size/significance screening, correlation heatmaps for relationship matrices, and composite dashboards for multi-view analysis. If a better plot grammar is needed, load `references/plot-inspiration-map.md` and invent a new evidence-bound chart without copying external code.
8. For a method, model, system, pipeline, framework, architecture diagram, or illustrative scientific schematic, load `references/architecture-diagram-generation.md`, `references/adaptive-architecture-style.md`, `references/reference-layout-blueprint.md`, and `references/paper-vs-presentation-diagrams.md`. Freeze the delivery context, build the semantic topology, and create a low-fidelity aligned blueprint before rendering. For paper figures, map inputs, representations, operators, branches, merges, and outputs explicitly; reject a blueprint that is only a sequence of explanatory cards. Apply the prompt-specificity ladder: preserve detailed user prompts and add at most a short refinement; use full content-derived prompt construction only for manuscripts, notes, or materially incomplete prompts. Invoke the verified GPT Image 2 capability by default and inspect the raster result. If the user explicitly opts out of GPT Image 2 or requests pure SVG/code-first output, use the deterministic pure-SVG route and label it clearly. If the selected backend cannot be verified as GPT Image 2, state the limitation; do not substitute an unknown image model or silently switch to pure SVG.
9. Load `references/icon-system.md` when icons are useful. Prefer one coherent, licensed public SVG family for common concepts. Generate a custom icon only for a method-specific concept that cannot be expressed clearly with public icons or native diagram primitives; generate it as a separate asset, remove its background, inspect its edges and semantics, and never accept noisy or invented internal detail merely because it looks creative.
10. After GPT Image 2 generation, inspect the actual raster image against the diagram specification and show it to the user. Then ask the mandatory editable-deliverable question from `references/architecture-diagram-generation.md`. On agreement, use the approved raster as the aesthetic and layout reference, load `references/editable-pptx.md` for PPTX requests, and reconstruct semantic groups, native shapes, connectors, live text, and independent icon assets. Preserve useful method-specific visual assets as separately movable, background-free elements instead of flattening the full figure. Derive PDF from vector source when requested. A full-slide raster, an embedded raster inside SVG, or an auto-traced bitmap alone does not satisfy editability.
11. Load `references/figure-table-layout.md` for multi-panel composition, LaTeX float/table choices, caption/cross-reference placement, and manuscript integration.
12. Load `references/render-qa.md`; when source files exist, compile/render and inspect the actual output. When only a spec is requested, include a QA checklist and no-fabrication status.
13. Hand off to `ccf-paper-writer` for prose rewrites or narrative placement text, `ccf-integrity-auditor` for number/claim consistency, and `ccf-submission-checker` for final venue/package compliance.

## Output Contract

Return the requested artifact first. For a full visual-composition request, use this structure:

```text
Mode:
Target venue / format:
Visual contract:
Panel or table map:
Plot recipe or code path:
Architecture prompt / generation status:
Icon and asset manifest:
Reference-layout provenance:
Editable SVG/PDF/PPTX status:
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
- `references/architecture-diagram-generation.md`: architecture-content extraction, scientific prompt construction, GPT Image 2 default generation, explicit pure-SVG opt-out, post-generation editable-format question, semantic SVG/PDF/PPTX reconstruction, and architecture QA.
- `references/adaptive-architecture-style.md`: prompt-preservation ladder, compact augmentation budget, content-fit style selection, transferable scientific diagram principles, and anti-imitation checks.
- `references/icon-system.md`: public-icon selection, custom icon micro-specs, transparent asset extraction, consistency rules, licensing records, and icon QA.
- `references/reference-layout-blueprint.md`: reference selection, composition distillation, grid/alignment strategy, layout-first wireframes, and anti-imitation controls.
- `references/paper-vs-presentation-diagrams.md`: mandatory context classification and the paper-mechanism acceptance gate that prevents slide or poster layouts from being presented as conference-paper architecture figures.
- `references/editable-pptx.md`: PowerPoint editability levels, native-object reconstruction, separate icon assets, deterministic generation, packaging, and PPTX QA.
- `references/figure-table-layout.md`: multi-panel design, table design, LaTeX float placement, captions, cross-references, and manuscript integration.
- `references/render-qa.md`: render-visible QA checklist, escalation rules, and visual issue ledger.
- `resources/python/ccfa_plot_recipes.py`: runnable standard-library SVG plotting recipes for paper-ready data-analysis figures.
