# Python Plot Recipes

Use `resources/python/ccfa_plot_recipes.py` for runnable numerical plots across fields, including biological data. Reuse an existing plotting pipeline when suitable; the bundled SVG recipes give a standard-library starting point without installing a new plotting framework.

## Recipe Library Contract

The original `ccfa_plot_recipes.py` library must remain:

- Self-contained: standard library only, so demos run in bare environments.
- Editable: exports SVG text and shapes rather than raster-only images.
- Evidence-bound: consumes supplied data only.
- Themeable: palettes and layout can be adapted without changing chart logic.
- Portable: recipes can be translated into Matplotlib, Seaborn, Plotly, Altair, Bokeh, or Plotnine when those dependencies exist.

## Multi-Panel Python Templates

For a new analytical composition, use the semantic router below; reuse an already suitable template or project script. `resources/python/ccfa_analysis_templates.py` provides nine complete layouts, while `ccfa_figure_library.py` composes selected panels. These routes need NumPy/Matplotlib; do not install them for an existing SVG-only task. Use the target environment's existing compatible packages. No model call is needed to rerun a saved specification.

### Choose By Meaning, Then Compose

The meaning-indexed library combines the existing 13 panel types and 30 additional components into **43 selectable chart grammars**, organized by **16 analytical purposes** with **16 fusion plans**. Use the [design-library guide](figure-design-library.md) for question-to-chart decisions, data requirements, interpretation boundaries, paper design cards and examples. The registry is a local lookup resource, not material to load in full into every prompt.

```bash
python ccf-visual-composer/resources/python/ccfa_figure_library.py route "分布与长尾"
python ccf-visual-composer/resources/python/ccfa_figure_library.py explain ecdf
python ccf-visual-composer/resources/python/ccfa_figure_library.py demo --fusion paired_benefit --out ccfa-workfiles/figures/paired-effect/build/figure
python ccf-visual-composer/resources/python/ccfa_figure_library.py compose --spec path/to/figure-data.json --out ccfa-workfiles/figures/analysis/build/figure
```

Routing starts with the current paper: its claim, section, observation unit, data relationships and figure size. A compact `route --brief path/to/figure-brief.json` can reuse that context; a direct question remains sufficient for a simple figure. Declared unpaired data excludes paired views, missing intervals exclude interval-based views, and a folding state axis retains checkpoint order. Randomness is automatic only among equally suitable candidates; users do not set a seed, and global usage balance never outranks article fit. Task-owned `--history` is optional. Record accepted choices only; later edits retain the selected specification and concrete data.

`explain <kind>` returns the design rationale, required fields, misuse cautions and fusion role. A fusion plan connects analytical roles rather than filling a panel quota: for example, matched changes, baseline-dependent benefit and agreement can share one figure only when their observations and units support those views. Reuse entity IDs/colors, state denominator and uncertainty meaning, align comparable axes, and keep unrelated scales distinct. The binned group-composition component preserves literal bin positions and widths so it can share an x axis with counts; its empty bins remain unknown, not fabricated zeros.

`studies --id <study-id>` reads one inspected paper design card; `reproduce <study-id> --demo --out <base-path>` creates an explicitly simulated Python adaptation of its analytical arrangement. `--data <path>` uses supplied study data instead. The corpus command searches **54,890 paper metadata records** across the declared 2025–2026 inventories:

```bash
python ccf-visual-composer/resources/python/ccfa_figure_corpus.py --query calibration --venue ICLR --year 2025 --limit 3
```

Inventory coverage and inspected figures are tracked separately: **78 design cards from 43 papers**, including **75 newly inspected cards and 3 reused visual records**, document actual design observations. `ccfa_figure_corpus.py --coverage` lists the 18 coverage records, publication gaps and listing scope. Metadata search does not imply a paper's figures were inspected or reproduced. Use the selected paper only when a missing design question warrants reading it, not as a compulsory batch retrieval.

Exports retain the specification, editable Python authoring source and available vector/preview outputs at one canonical base path. `compose --spec` consumes supplied panel data and never falls back to demo values. Explicit demo exports identify their synthetic numbers; paper values or original artwork are not bundled. Keep original-paper attribution in the central source registry and selected design cards.

The **43 single-axis grammars** also work with **three linked layouts** in `ccfa_figure_layouts.py`: `joint_marginals` shares supplied observations and bin edges with central and marginal views; `aligned_tracks` shares positions while retaining each track's units; `matrix_slices` extracts the selected row/column from the same response grid. They are coordinated layouts, not three additional single-axis grammars. Use `layout <kind> --demo --out <base>` for explicit simulated examples, or `compose --spec` with actual supplied values.

`compose --spec` can resolve declared CSV/TSV/JSON records through `data_sources`, one panel/layout `table` selection, and column/group/matrix bindings. It never guesses an aggregation, fills missing matrix cells, or generates samples. All columns in a selected table preserve the same filtered and ordered rows; duplicate matrix cells require an explicit upstream aggregate. Paired grouped samples require `groups.pair_by` to align unique, shared subject IDs, or an explicit `groups.matched_order: true` contract for already aligned anonymous rows. Equal lengths alone do not establish a pairing. Ordinary unpaired groups and already matched arrays keep their existing API. Input files join the export protection list.

The [preserved example table](figure-examples.md) includes the original nine templates and the user-requested density/perturbation and dynamics/category pairs alongside paper studies. List or render one without searching the whole library:

```bash
python ccf-visual-composer/resources/python/ccfa_figure_library.py examples --category reference
python ccf-visual-composer/resources/python/ccfa_figure_library.py example reference:sensitivity-pair --demo --out ccfa-workfiles/figures/sensitivity-pair/build/figure
python ccf-visual-composer/resources/python/ccfa_figure_library.py example reference:dynamics-pair --demo --out ccfa-workfiles/figures/dynamics-pair/build/figure
```

| Template | Analytical composition |
| --- | --- |
| `mechanism_overview` | Compact mechanism strip, growth curve, repeated-run intervals, resource trade-off and gain map. |
| `benchmark_atlas` | Cross-task matrix, repeated runs, sample distributions, cost and data efficiency. |
| `ablation_interactions` | Aligned component settings and scores, changes from the full model, interactions and training curves. |
| `scaling_robustness` | Six curve panels for scale, noise, missing observations, latency and capacity. |
| `representation_diagnostics` | Supplied embedding coordinates, probe scores, attention, correlation and neighborhood agreement. |
| `biological_atlas` | Cell groups, expression, effect-size screening and activity/prevalence dot matrix. |
| `paired_effects` | Matched observations, paired differences, subgroup intervals and time response. |
| `calibration_errors` | Reliability, confidence counts, residuals, confusion, error distributions and failure categories. |
| `sensitivity_dynamics` | Hexbin density with a threshold share, boxplots with a computed percentile, state evolution and category bars/lines on one scale. |

The layouts are starting points, not required panel inventories. Remove or replace irrelevant panels in the authoring script; never manufacture results to fill a slot. For a bespoke layout, import the needed functions from `ccfa_analysis_panels.py`. Preserve their data checks while changing geometry. All entity IDs and display labels must correspond to the supplied data.

From the repository root:

```bash
python ccf-visual-composer/resources/python/ccfa_analysis_templates.py --demo all --out ccfa-workfiles/figures/analysis-demo
```

This explicit legacy demo generates labeled synthetic data for the nine preserved templates. It saves one `source/demo-data.json`, current SVG/PDF/PNG exports under `figures/`, and one `manifest.json` with export paths and basic QA. Repeat the same command to update these files in place. `--palette-showcase` uses different palettes for these independent examples only. Related figures normally keep one palette and an explicit entity-to-color mapping.

For a paper's two-panel combination, replace `--demo all` with `--demo sensitivity_dynamics --panel-pair sensitivity` (density + box/percentile), or `--panel-pair dynamics` (temporal states + category shares). Omit `--panel-pair` for all four panels. Keep a distinct artifact ID for each retained figure. The Python API accepts the same selection in `data["panel_pair"]`; it needs only the selected pair's data. These are separate views of the supplied analyses, not invented extra experiments.

To use real data, take the matching object structure from `source/demo-data.json`, replace it with actual inputs, remove its synthetic `_meta`, and pass that JSON by path. Inputs can be a single template object or a dictionary keyed by template name. Missing inputs are errors, never a request to generate numbers:

```bash
python ccf-visual-composer/resources/python/ccfa_analysis_templates.py --template benchmark_atlas --data path/to/analysis-data.json --out ccfa-workfiles/figures/main-analysis --palette npg --width-mm 183 --font-size 8.5
```

For Python integration:

```python
from ccfa_analysis_templates import render_template
from ccfa_analysis_panels import save_figure
fig = render_template("benchmark_atlas", supplied_data, palette="npg", width_mm=183)
save_figure(fig, canonical_figure_path, protected_paths=(source_data_path,))
```

The module directory must be on Python's import path, as in the legacy example below. Use one data loader and one figure style for a batch. Read the selected builder/schema only, not all demo arrays. The CLI is a convenience entry point; existing project scripts can call the components without adopting its directory layout.

### Data And Layout Details

- `methods` contains unique ordered IDs; `entity_colors` can supply an ID-to-hex map. `series[].method`, comparison labels and related panels reuse those IDs. Group identities in embeddings have their own order and map. Do not infer a pairing from unordered rows.
- Bounds are supplied lower/upper values in the original metric, not guessed error lengths. State SD, SE, CI, sample count and aggregation in the caption. The synthetic example's repeated-run bars use one sample SD; paired subgroup intervals use an explicitly computed bootstrap 95% CI. The renderer does not convert one into the other.
- `paired_effects` checks that supplied differences equal the second matched group minus the first. Confusion/count panels consume counts; rates need an explicitly relabeled custom panel. A correlation matrix stays within [-1, 1]. A generic heatmap may show missing cells distinctly instead of filling zeros.
- Embeddings consume coordinates: they neither calculate UMAP/t-SNE nor establish separation significance. Demo coordinates are synthetic. Volcano plots consume supplied p/q statistics and correction labels; zero probabilities need an explicit justified display floor. Gene/pathway names alone do not establish a biological interpretation.
- Composite density plots count the actual input samples; a logarithmic colorbar represents counts, not a probability density estimate. The threshold fraction and selected percentile are computed from supplied observations. Box bodies show median/IQR with 1.5-IQR whiskers and visible outliers, while the overlaid line is the named percentile. Preserve the grouping rule and sample identity when linking panels. Percentage panels need their denominator/aggregation in the caption; overlapping state criteria need not sum to 100. An under-curve fill is visual emphasis, not an uncertainty band. Prefer one scale for bars and lines of the same quantity; adding a second axis requires a real unit difference.
- Set dimensions in mm and type in pt before export; default width is 183 mm and font size 8.5 pt, with content-dependent height. A composition's top-level `font_size` reaches panels, preserved templates and all linked layouts, including the primary axes, ticks and legends. There is no square constraint. `--font serif` uses Times New Roman when present, `sans` and `comic` are available. CJK fallbacks recognize Windows fonts, native macOS PingFang/Songti SC/TC and Noto/Source Han families; a minimal Linux environment needs an installed CJK font, for example Noto Sans CJK. Export refuses missing glyphs, and the release Chinese-text check must run rather than skip. Exact venue typography overrides these defaults when requested.
- Use shared alignment within each analytical row, short panel titles, room for axis labels, one legend per meaning and restrained cell annotations. Adjust spans before shrinking type. Comparable matrices share normalization; different metrics retain separate labeled scales. The current full-page presets are double-column examples, not layouts to squeeze unchanged into a single column.
- SVG retains live text and vector marks; PDF embeds fonts; PNG is a preview. Basic export QA checks missing glyphs and canvas bounds. Inspect actual output for overlaps, cramped labels and misleading visual scales. Reuse the existing scientific/visual checks in `render-qa.md`.

## Available SVG Recipes

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

Use inspected papers and public galleries to understand why an analytical arrangement works. Rebuild the selected relationship with the bundled original Python code and supplied data, or label an explicit synthetic demonstration. Preserve source attribution and the distinction between a design reconstruction and a reproduction of reported results. Reuse appropriately licensed external code only under its actual license; do not copy paper artwork or substitute invented values for the original results.
