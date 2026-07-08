# Python Plot Recipes

Use `resources/python/ccfa_plot_recipes.py` when the user wants concrete Python plotting code, a runnable demo, or a starting point for a paper figure. The bundled recipes are original CCFA code. They are inspired by public visualization galleries and libraries, but they do not copy external code.

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

1. Start from the visual contract: claim, reviewer question, source data, and intended placement.
2. Pick a recipe by evidence shape, not by aesthetics.
3. Keep the proposed method color stable across all generated figures.
4. Use typographic hierarchy: large title, strong panel titles, compact axis text, and direct labels for the main evidence.
5. Use direct labels whenever possible; do not make reviewers decode a legend for the main message.
6. For composite figures, combine 2-5 coordinated panels only when each panel answers a distinct reviewer question.
7. If the recipe does not fit the evidence, compose a new one using the same primitives: canvas, axis, direct labels, semantic palette, and source note.
8. Save source data next to generated figures or name the upstream file in the caption.

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
- Constraint: what the visual refuses to claim.

## Composite Dashboard Rules

Use a composite figure when a single chart would hide the analysis structure. A useful composite dashboard usually combines:

- one composition view, such as donut or stacked bars;
- one categorical comparison, such as grouped bars;
- one relationship view, such as correlation heatmap or scatter;
- one discovery/screening view, such as volcano or ranked hits.

Keep the figure publishable:

- Use one shared title and a clear panel title for every subfigure.
- Keep each panel visually independent; do not force all panels into one color scale.
- Use different but harmonious palettes across panels.
- Avoid shrinking text below readability; use fewer panels if labels become fragile.

## External-Inspiration Boundary

Public galleries are inspiration, not source material to paste. Borrow ideas such as direct labeling, small multiples, density summaries, grammar-of-graphics layering, and publication style defaults. Do not copy source code, datasets, proprietary examples, or distinctive layout compositions.
