---
name: ccf-visual-composer
description: "Compose, polish, generate, and QA publication-grade CCF paper figures, tables, captions, palettes, panel maps, Python plotting code, and manuscript visual layout integration from supplied data/results. Use for figure/table layout, visual QA, palette selection, LaTeX figure/table placement, multi-panel design, creative data visualization, data-analysis plots, pie/donut charts, bar charts, volcano plots, correlation heatmaps, composite dashboards, source-data traceability, and making visuals fit naturally in the paper. Do not design experiments, invent results, write manuscript prose as the main task, or perform final submission compliance."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Visual Composer

## Core Rule

Make figures and tables evidence-bearing, readable, and integrated with the manuscript. Start from a visual contract, not a template. Never invent data, numbers, statistics, baselines, sample sizes, images, captions that imply unsupported results, or official venue rules.

## Modes

- `visual-contract`: define core claim, reviewer question, evidence layer, source data, panel/table map, caption role, and output constraints.
- `figure-design`: design multi-panel figures, chart families, image plates, schematics, legends, labels, color, and export specs from supplied evidence.
- `python-plotting`: write or adapt Python plotting code using bundled recipes, standard-library SVG output, analytical chart recipes, composite dashboards, or optional libraries available in the user's environment.
- `table-design`: design publication tables, numeric precision, grouping, ordering, notes, width strategy, and LaTeX table structure from supplied values.
- `layout-integration`: place figures/tables near first discussion, align captions/cross-references, choose single-column/full-width floats, and keep visuals connected to text.
- `render-qa`: compile or render when files exist; inspect clipping, overlap, float order, font, contrast, rasterization, and source-data traceability.

## Workflow

1. Identify target venue/family, manuscript context, supplied data/results, artifact type, output format, and whether the user wants creation, redesign, or QA.
2. Load `../ccf-common/references/task-modes.md` and `../ccf-common/references/privacy-and-evidence.md` when the task touches manuscript files, private results, or project artifacts.
3. If claims, evidence, source data, or result values are missing, mark the gap and hand off to `ccf-experiment-designer`; do not fill the gap by invention.
4. Load `references/visual-contract.md` and write the visual contract before changing layout or style.
5. Load `references/palette-and-accessibility.md` before choosing colors; prefer accessible scientific palettes and semantic consistency over decorative color.
6. For plotting-code requests, load `references/python-plot-recipes.md` and use `resources/python/ccfa_plot_recipes.py` as a runnable starting point. Prefer analytical plot families when the evidence calls for them: pie/donut for composition, grouped bars for categorical comparisons, volcano plots for effect-size/significance screening, correlation heatmaps for relationship matrices, and composite dashboards for multi-view analysis. If a better plot grammar is needed, load `references/plot-inspiration-map.md` and invent a new evidence-bound chart without copying external code.
7. Load `references/figure-table-layout.md` for multi-panel composition, LaTeX float/table choices, caption/cross-reference placement, and manuscript integration.
8. Load `references/render-qa.md`; when source files exist, compile/render and inspect the actual output. When only a spec is requested, include a QA checklist and no-fabrication status.
9. Hand off to `ccf-paper-writer` for prose rewrites or narrative placement text, `ccf-integrity-auditor` for number/claim consistency, and `ccf-submission-checker` for final venue/package compliance.

## Output Contract

Return the requested artifact first. For a full visual-composition request, use this structure:

```text
Mode:
Target venue / format:
Visual contract:
Panel or table map:
Plot recipe or code path:
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
- `references/figure-table-layout.md`: multi-panel design, table design, LaTeX float placement, captions, cross-references, and manuscript integration.
- `references/render-qa.md`: render-visible QA checklist, escalation rules, and visual issue ledger.
- `resources/python/ccfa_plot_recipes.py`: runnable standard-library SVG plotting recipes for paper-ready data-analysis figures.
