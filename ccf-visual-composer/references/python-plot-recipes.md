# Python Plot Recipes

Use `resources/python/ccfa_plot_recipes.py` for runnable numerical plots across fields, including biological data. Reuse an existing plotting pipeline when suitable; the bundled SVG recipes give a standard-library starting point without installing a new plotting framework.

## Recipe Library Contract

The bundled library must remain:

- Self-contained: standard library only, so demos run in bare environments.
- Editable: exports SVG text and shapes rather than raster-only images.
- Evidence-bound: consumes supplied data only.
- Themeable: palettes and layout can be adapted without changing chart logic.
- Portable: recipes can be translated into Matplotlib, Seaborn, Plotly, Altair, Bokeh, or Plotnine when those dependencies exist.

## Available Recipes

| Recipe | Best for | Avoid when |
| --- | --- | --- |
| `lollipop_rank` | Headline metric comparison, benchmark result ranking, compact bar replacement. | Differences are tiny and uncertainty dominates. |
| `slopegraph` | Paired changes such as base vs big, before vs after, old vs new. | Metrics are on unrelated scales without clear normalization or labels. |
| `heatmap_matrix` | Dense model/config/dataset matrices and table-to-visual summaries. | Exact numeric lookup is more important than pattern reading. |
| `donut_chart` | Composition, proportions, dataset/source split, error taxonomy, or budget allocation. | Exact comparison between many categories is the main task; use bars instead. |
| `grouped_bar_chart` | Categorical comparisons across methods, datasets, ablations, cohorts, or settings. | Too many groups make labels unreadable; use small multiples or heatmaps. |
| `volcano_plot` | Effect-size versus significance screening, feature/gene/module discovery, or large ablation scans. | P-values, effect sizes, or thresholds are not supplied. |
| `correlation_heatmap` | Metric-feature relationships, module interactions, dataset correlations, or diagnostic matrices. | The sample size is too small or correlation is not meaningful for the data type. |
| `ridgeline_density` | Seed distributions, sample distributions, uncertainty, repeated-run behavior. | The paper only has one value per group. |
| `small_multiple_lines` | Trends across datasets, scales, ablations, or time. | Panels do not share a comparable visual grammar. |
| `radial_scorecard` | Multi-criterion profile summaries for exploratory or slide visuals. | The figure is the main scientific evidence; radial charts can overstate shape differences. |

## How To Adapt

1. Reuse the relevant visual contract: scientific question, supplied data, intended size, and placement. Import a selected recipe; read only its signature or implementation when needed. Do not load the full library or rebuild an existing plotting pipeline for a local change.
2. Pick a recipe by evidence shape, not by aesthetics.
3. Keep the proposed method color stable across related figures. Existing palettes remain available; `ccfa_gem`, `ccfa_nocturne`, `ccfa_ceramic`, `ccfa_orchid`, `ccfa_arctic`, `ccfa_wine`, and `ccfa_ink` expose the established showcase alternatives. See `palette-and-accessibility.md` only when choosing or changing color roles.
4. Set `Theme(paper_width_in=<final width>, min_font_pt=<minimum label size>)` for paper delivery; leaving `paper_width_in=None` preserves the legacy pixel canvas for previews. To keep stroke widths in physical points across different design resolutions, add `stroke_unit="pt"`; this requires `paper_width_in` and interprets Canvas stroke widths as points. The default `stroke_unit="viewbox"` preserves existing drawing-unit widths. Use `visual-contract.md` for the physical type scale. `Theme` defaults to Times New Roman with CJK fallbacks; a requested comic treatment can use `Theme(font="Comic Sans MS, Microsoft YaHei, sans-serif", ...)`. Reflow labels after sizing; the font floor alone cannot prevent overlap. Pass `title=""` when the caption already supplies the title.
5. Use natural title or sentence case for ordinary visible English, while preserving canonical uppercase acronyms and initialisms such as `CCF`, `AI`, `QA`, `SVG`, and `PDF`. Never use all caps for complete ordinary-language titles, panel names, legends, axes, annotations, badges, or table headers; use font weight, size, color, or spacing for emphasis instead.
6. Use short direct labels where they help identify the main comparison; collect shared legends when repeated entities would otherwise repeat labels.
7. Add a panel when it explains part of the scientific question. Choose panel count and chart types from the evidence; a composition view, correlation matrix, or screening plot is not a required dashboard ingredient.
8. If the recipe does not fit the evidence, compose a new one using the same primitives: canvas, axis, direct labels, semantic palette, and source note.
9. Read the canonical upstream data by path instead of copying the dataset into each figure folder. Keep authoring code, reusable assets, and build previews at the paths resolved by the shared artifact contract. Save each requested export at its canonical destination and update it in place. Reuse one data load and theme for a figure batch; regenerate only affected panels/exports after a local change.

## Custom Plot Invention Prompt

When inventing a new plot, fill this before coding:

```text
Scientific question:
Data shape:
Primary comparison:
Secondary structure:
What the viewer should notice first:
What must not be visually exaggerated:
Required labels/units:
Candidate grammar:
Why a standard chart is insufficient:
Accessibility checks:
```

Then design a plot grammar:

- Anchor: the first visual object the reader should inspect.
- Contrast: color, alignment, slope, position, or grouping.
- Context: uncertainty, baseline, scale, or source note.
- Scope: the evaluated settings and statistical meaning needed to interpret the visual.

## Composite Dashboard Rules

Use `figure-table-layout.md` for composition. Give each panel a scientific role and use only necessary panel labels/headings; the manuscript caption often replaces an internal figure title.

- Align related matrices/annotation strips by unique entity IDs before plotting, then reuse one order and group split. The library validates shapes and labels; it does not join or cluster source tables. Missing observations need explicit handling in the authoring code, not fabricated zeros.
- Reuse one entity-to-color map and one legend for matching meanings. Comparable heatmaps share `ColorNorm` and a palette; separate quantities retain labeled scales. Do not rotate palettes solely because a panel is new.
- `small_multiple_lines` shares x/y ranges by default. Supply panel `x_unit`/`y_unit` labels; conflicting declared units reject shared axes. Use `share_x=False` or `share_y=False` only when that dimension is not comparable, keeping free-scale markings and per-panel ranges visible.
- A supplied `entity` identifies the same method across panels and produces one shared legend entry. Use `show_legend=False` when a composition already provides that legend. A panel may use `title=""` if its `entity` is supplied and the surrounding composition explains its role.
- Align actual plot areas, account for tick-label margins, and preserve fixed spatial/image aspect ratios. When assembling exported panels at a new width, restore their physical typography/stroke sizes; do not simply shrink the whole SVG and call its original font setting sufficient.

## Runnable Controls

From the repository root, these synthetic values demonstrate the API only. Replace them with the existing source-data loader for scientific use. The examples return SVG strings in memory and do not scatter demo files.

```python
import sys
sys.path.insert(0, "ccf-visual-composer/resources/python")
from ccfa_plot_recipes import (
    ColorNorm, PALETTES, Theme, heatmap_matrix, small_multiple_lines, volcano_plot,
)

theme = Theme(width=900, height=520, paper_width_in=7.0, min_font_pt=9.0)
# Both matrices have the same IDs, units and transformation, already aligned.
matrix_theme = Theme(width=900, height=280, paper_width_in=7.0, min_font_pt=9.0)
rows, cols = ["Gene A", "Gene B"], ["Control", "Treatment"]
norm = ColorNorm(-2.0, 2.0, center=0.0)
matrices = ([[0.2, 1.0], [-1.0, 0.8]], [[0.4, 1.5], [-0.5, 1.2]])
heatmaps = [heatmap_matrix(
    values, rows, cols, title="", theme=matrix_theme, norm=norm,
    palette=PALETTES["diverging_cork"], show_values=False,
    colorbar_label="Log2 fold change",
) for values in matrices]

# One method keeps its color; the 100-fold magnitude difference stays visible.
trends = small_multiple_lines([
    {"title": "Dataset A", "entity": "Method A", "x": [1, 2, 3], "y": [1, 2, 3],
     "x_unit": "Step", "y_unit": "ms"},
    {"title": "Dataset B", "entity": "Method A", "x": [1, 2, 3], "y": [100, 200, 300],
     "x_unit": "Step", "y_unit": "ms"},
], title="", theme=theme, share_x=True, share_y=True,
   entity_colors={"Method A": "#0072B2"})

# Supply already computed statistics; the renderer performs no correction.
screen = volcano_plot([
    {"gene": "Gene A", "log2_fc": 1.4, "q": 0.01},
    {"gene": "Gene B", "log2_fc": -0.4, "q": 0.30},
], "log2_fc", "q", "gene", title="", statistic="q", theme=theme)
```

Use `save_svg(svg, canonical_path)` only for a requested export, at the path established by the artifact contract. Invalid dimensions, non-finite values, probabilities outside `[0, 1]`, and correlations outside `[-1, 1]` are errors to resolve from source data. A zero p/q value needs an explicit, justified `zero_floor` for display; the plot labels that floor, and positive values retain their actual magnitudes. Do not relabel raw p values as adjusted p or q values. `ColorNorm` rejects values outside its stated bounds, so extend a shared range from all relevant data instead of silently saturating it.

For combined heatmaps, `show_colorbar=False` suppresses a repeated colorbar only when the assembled figure retains one for that same normalization, palette, and unit. Independent exports keep their own colorbars. These controls add local computation, not model calls; broader library adoption or a new dependency is optional.

## External-Inspiration Boundary

Public galleries are inspiration, not source material to paste. Borrow ideas such as direct labeling, small multiples, density summaries, grammar-of-graphics layering, and publication style defaults. Do not copy source code, datasets, proprietary examples, or distinctive layout compositions.
