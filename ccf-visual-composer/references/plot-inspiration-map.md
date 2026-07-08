# Plot Inspiration Map

This map records design ideas to borrow conceptually from widely used open-source visualization projects. Use `../ccf-common/references/source-registry.yaml` as the source of truth for URLs and verification dates.

## Useful Ideas To Borrow

| Source family | Design ideas worth adapting | CCFA implementation direction |
| --- | --- | --- |
| Matplotlib gallery | Broad plot taxonomy, explicit source-code examples, tight control over axes and artists. | Keep a broad recipe catalog and expose low-level SVG primitives for custom plots. |
| Seaborn examples | Statistical defaults, distribution summaries, grids, small multiples. | Provide ridgelines, small multiples, and semantic grouping defaults. |
| Plotly Python | Interactive thinking, hover-ready data structure, dashboard composition. | Keep data records explicit and make demo dashboards easy to extend, even when static SVG is the output. |
| Bokeh gallery | Linked views, exploratory dashboards, web-native composition. | Encourage multi-panel analytical views when a single chart hides structure. |
| Altair/Vega-Lite | Declarative grammar: data, mark, encoding, transform. | Ask for data shape, mark type, encoding, and transform before coding a custom chart. |
| Plotnine/ggplot | Grammar-of-graphics layering and theme discipline. | Separate data, scale, marks, labels, and theme in recipes. |
| Python Graph Gallery | Chart-type taxonomy and examples grouped by analytical purpose. | Route users by evidence shape: compare, distribute, relate, rank, change, compose. |
| Scientific Visualization book | Publication-quality layout, spacing, annotation, and typographic restraint. | Prefer direct labels, whitespace discipline, and vector exports over decorative effects. |
| SciencePlots/LovelyPlots | Paper-ready style sheets and editable scientific figures. | Keep palettes, font, SVG editability, and LaTeX integration as first-class concerns. |

## CCFA Creative Boundaries

- Do not limit output to common bar/line/scatter charts when the evidence suggests richer structure.
- Do not use novelty as decoration; unusual plot grammars must answer a reviewer question.
- Use animation or interactivity only for exploration or demos, not for static paper evidence unless the venue supports it.
- Prefer a boring chart with honest evidence over a beautiful chart that exaggerates.

## Chart Grammar Menu

Use this menu to invent new charts:

| Evidence shape | Candidate grammars |
| --- | --- |
| One headline metric per model | Lollipop, dot plot, ranked strip, annotated benchmark tile. |
| Many models x many datasets | Heatmap, clustered matrix, table-figure hybrid, small multiples. |
| Before/after or base/big | Slopegraph, paired dots, ratio strips, delta ladder. |
| Runs/seeds/samples | Ridgeline, violin/box hybrid, uncertainty ribbons, raincloud. |
| Time or scale trends | Small multiples, direct-labeled line families, horizon strips. |
| Mechanism path or pipeline | Annotated flow, layered schematic, evidence-linked block diagram. |
| Multiple quality dimensions | Radar only for secondary summary; prefer parallel coordinates or scorecard when exact comparison matters. |
