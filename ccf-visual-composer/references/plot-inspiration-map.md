# Plot Inspiration Map

This map records design ideas to borrow conceptually from open-source visualization projects. Use `../../ccf-common/references/source-registry.yaml` as the source of truth for URLs and verification dates. Load a source only for an unresolved choice; these are optional references, not default dependencies.

## Useful Ideas To Borrow

| Source family | Design ideas worth adapting | CCFA implementation direction |
| --- | --- | --- |
| Matplotlib gallery | Broad plot taxonomy, explicit source-code examples, tight control over axes and artists. | Keep the standalone SVG recipes and use the analytical panel library for editable multi-panel figures. |
| Seaborn examples | Statistical defaults, distribution summaries, grids, small multiples. | Provide ridgelines, small multiples, and semantic grouping defaults. |
| Plotly Python | Interactive thinking, hover-ready data structure, dashboard composition. | Keep data records explicit and make demo dashboards easy to extend, even when static SVG is the output. |
| Bokeh gallery | Linked views, exploratory dashboards, web-native composition. | Encourage multi-panel analytical views when a single chart hides structure. |
| Altair/Vega-Lite | Declarative grammar: data, mark, encoding, transform. | Ask for data shape, mark type, encoding, and transform before coding a custom chart. |
| Plotnine/ggplot | Grammar-of-graphics layering and theme discipline. | Separate data, scale, marks, labels, and theme in recipes. |
| Python Graph Gallery | Chart-type taxonomy and examples grouped by analytical purpose. | Route users by evidence shape: compare, distribute, relate, rank, change, compose. |
| Scientific Visualization book | Publication-quality layout, spacing, annotation, and typographic restraint. | Prefer direct labels, whitespace discipline, and vector exports over decorative effects. |
| SciencePlots/LovelyPlots | Paper-ready style sheets and editable scientific figures. | Keep palettes, font, SVG editability, and LaTeX integration as first-class concerns. |
| ComplexHeatmap | Related matrices and annotations share entity order and group boundaries. | Join by stable IDs, retain common ordering, and use shared normalization only for comparable quantities. |
| patchwork | Align data areas, collect shared legends, respect fixed-aspect panels. | Plan plot rectangles separately from label margins; let flexible panels absorb spare space. |
| Scientific Inkscape | Resize figures while preserving typographic and stroke dimensions. | Bind font sizes to final physical width, then reflow panels without shrinking labels. |
| Bioicons | Editable scientific objects from biology and chemistry. | Retrieve a fitting SVG only when needed, inspect individual license/attribution, and normalize visual weight. |
| PaperVizAgent | Plan content, render, and revise from specific visual feedback. | Distinguish scientific fidelity from visual quality in one inspection; repair named regions and keep optional extra generation/review gated. |
| AstraDraw | Reusable editable elements and local modification. | Reuse project-approved components, stable object IDs, and their topology before drawing new assets. |

## Meaning-Indexed Design Library

Use `resources/python/ccfa_figure_library.py route` for a new chart choice and `explain <kind>` for a selected grammar. The [design-library guide](figure-design-library.md) connects 43 chart grammars, 16 analytical purposes and 16 fusion plans. It describes why each view makes a relationship legible, which data it requires, what it can obscure, and how it can share a figure with complementary views. Read only the returned candidates, relevant card and necessary implementation signatures.

`resources/figure-library/studies.json` contains 78 design cards from 43 papers: 75 newly inspected figure records plus 3 reused visual records. Cards distinguish the observed composition, its rationale, required fields, fusion opportunities, caveats, and Python panel plan. Query one card with `studies --id <study-id>`; use `reproduce <study-id> --demo` for an explicitly simulated design adaptation. Reconstructing an analytical arrangement does not reproduce the paper's numerical results. Source IDs resolve to the shared source registry; original paper artwork is not bundled.

The separate compressed metadata inventory contains 54,890 records across 18 declared coverage entries for the 2025–2026 publication years. Query `resources/python/ccfa_figure_corpus.py --coverage` for available editions, tracks and gaps; use bounded title queries when discovering another useful paper. A metadata record is not a figure-inspection record. The bundled inventory covers the listed conference proceedings and declared Nature AI-related journal scopes rather than every AI-related article across all Nature journals.

Keep scientific fit ahead of novelty in appearance. The router first matches meaning and data fields, then can use a seed and task-owned accepted-use history to spread choices among equally suitable alternatives. Do not rotate charts during a local edit. Fusion preserves observation correspondence, denominators, scales and category identity; a visually similar matrix, composition or distribution with a different denominator is not an interchangeable panel.

## Earlier Inspected Paper Figures

Load this section when choosing a panel arrangement. The nine papers below were checked on 2026-10-30. Figure links, original-paper URLs and award checks live in the central registry under the listed IDs; no routine task needs to fetch all of them. The bundled Python implementations are original, and their demos use explicitly labeled synthetic data. These are analytical relationships to adapt, not replicas of the papers' layouts, results or artwork.

| Functional arrangement | Inspected reference and registry ID | Relationship to carry into a template |
| --- | --- | --- |
| Overview with aligned benchmarks | AlphaFold 3, Nature 2024, Fig. 1; `alphafold3-figure-layout` | Examples, comparable quantitative panels and a mechanism strip form a clear hierarchy. Use in `mechanism_overview` and `benchmark_atlas`; preserve metric definitions even when several axes share a numeric range. |
| Perturbation and representation atlas | scGPT, Nature Methods 2024, Figs. 3 and 4; `scgpt-figure-layout` | Combine a few related distributions, embeddings and matrices; keep category colors and entity order consistent. Use in `representation_diagnostics` and `biological_atlas`, with fewer labels than the original dense panels. |
| Prediction and subgroup diagnostics | scFoundation, Nature Methods 2024, Fig. 3; `scfoundation-figure-layout` | Pair prediction-versus-observation views with ranked or subgroup effects. Use in `calibration_errors` and `paired_effects`; draw reference lines and statistics from the supplied data. |
| Paired cases beside performance curves | Cellpose3, Nature Methods 2025, Fig. 2; `cellpose3-figure-layout` | Keep corresponding observations aligned and method colors stable across cases and curves. Apply to `paired_effects` and `scaling_robustness`; supplied image crops can occupy a separate custom panel without changing sample correspondence or scale. |
| Scaling and resource frontiers | VAR, NeurIPS 2024 main-track Best Paper, Figs. 5 and 6; `neurips-2024-var` | Align small multiples; distinguish observations, fitted trends and Pareto envelopes by line treatment. Use in `scaling_robustness` and `benchmark_atlas`; fit only when the data and model justify it. |
| Heterogeneity behind an average ranking | PRISM, NeurIPS 2024 Datasets and Benchmarks Best Paper, Fig. 4; `prism-figure-layout` | Coordinate uncertainty and subgroup comparisons through stable entity identity and aligned rows. Use in `paired_effects` and `benchmark_atlas`; highlight a few comparisons instead of repeating every short label. |

The two award claims are checked against `neurips-2024-best-paper-awards`. The Nature papers are figure references, with no best-paper claim. `ablation_interactions` adds an original factorial-ablation arrangement; it is not attributed to any one paper.

### Recent Distribution and Dynamics Analyses

| Functional arrangement | Inspected reference and registry ID | Relationship to carry into a template |
| --- | --- | --- |
| Aligned comparisons, local statistics and time | The Flexibility Trap, ICML 2026 Outstanding Paper, Figs. 3, 7 and 9; `icml-2026-flexibility-trap-figures` | A model-by-task grid, category bars with a global reference, and wall-time trajectories separate general trends from local differences. Carry this organization into `sensitivity_dynamics` and `scaling_robustness`, with explicit time units. |
| Distributions beside a controlled sweep | LLMs Get Lost In Multi-Turn Conversation, ICLR 2026 Outstanding Paper, Fig. 6; `iclr-2026-lost-conversation-figures` | Define the interval before comparing aligned model/condition summaries and a gradual perturbation sweep. Use the relationship in `sensitivity_dynamics`; show the median, interval and upper quantile distinctly, without inheriting the original's dense numeric annotations. |
| Overall distribution and category differences | Artificial Hivemind, NeurIPS 2025 Best Paper, Figs. 7 and 8; `neurips-2025-hivemind-figures` | Connect an overall distribution to selected category breakdowns, then combine box summaries with visible observations. Use in `sensitivity_dynamics` and `paired_effects`; preserve the category denominator and stable ordering. |

Awards are checked against `icml-2026-awards`, `iclr-2026-outstanding-blog` and `neurips-2025-best-paper-awards`. Figure observations refer to the inspected paper versions recorded in the registry, independently of award descriptions.

The `sensitivity_dynamics` arrangement comes directly from a user-provided figure reference: density plus rank-bin summaries, followed by state evolution plus category composition. It supports four panels together or two paired figures. Its `density_map`, `binned_summary` and `category_comparison` primitives preserve shared observations, thresholds, rank-bin membership and entity colors. Compute state shares and P95 from the supplied observations; define the denominator and interval meaning. The three recent papers inform distribution/quantile and category combinations; none is claimed to contain this same hexbin layout. The reference image, paper artwork and reported data are not bundled.

For implementation details, load only the needed source: `matplotlib-constrained-layout` for panel alignment, `matplotlib-fonts` for glyph handling, and `nature-panel-export` / `nature-figure-specifications` / `nature-final-lines` for the corresponding Nature production target. Palette values and their attribution are covered in [palette-and-accessibility.md](palette-and-accessibility.md), including `ggsci-palettes` and `tol-color-schemes`. Journal-associated palettes are optional choices, not journal requirements.

## CCFA Creative Boundaries

- Do not limit output to common bar/line/scatter charts when the evidence suggests richer structure.
- Use an unusual plot grammar when it explains a scientific relationship more clearly; a new appearance alone does not justify extra panels.
- Use animation or interactivity only for exploration or demos, not for static paper evidence unless the venue supports it.
- Prefer a boring chart with honest evidence over a beautiful chart that exaggerates.

## Chart Grammar Menu

Use this menu to invent new charts:

| Evidence shape | Candidate grammars |
| --- | --- |
| One headline metric per model | Lollipop, dot plot, ranked strip, annotated benchmark tile. |
| Composition or category share | Donut, waffle, stacked bar, mosaic tile; prefer bars when exact comparison matters. |
| Categorical comparison | Grouped bar, diverging bar, interval bar, Cleveland dot plot. |
| Many models x many datasets | Heatmap, clustered matrix, table-figure hybrid, small multiples. |
| Before/after or base/big | Slopegraph, paired dots, ratio strips, delta ladder. |
| Runs/seeds/samples | Ridgeline, violin/box hybrid, uncertainty ribbons, raincloud. |
| Effect-size screening | Volcano plot, MA plot, ranked hit map, thresholded scatter. |
| Relationship matrix | Correlation heatmap, pair grid, clustered heatmap, annotated matrix. |
| Time or scale trends | Small multiples, direct-labeled line families, horizon strips. |
| Mechanism path or pipeline | Annotated flow, layered schematic, evidence-linked block diagram. |
| Multi-view analysis | Coordinated panels selected for the actual question; shared entity encodings and appropriate common scales. |
| Multiple quality dimensions | Radar only for secondary summary; prefer parallel coordinates or scorecard when exact comparison matters. |
