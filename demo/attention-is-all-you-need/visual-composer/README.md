# Visual Composer Demo

Owner: `ccf-visual-composer`

This demo renders paper-style SVG figures from the verified values in `../artifacts/official-data.md`. It uses `ccf-visual-composer/resources/python/ccfa_plot_recipes.py`, which is a standard-library-only recipe library bundled with the skill.

## Run

```bash
python demo/attention-is-all-you-need/visual-composer/plot_demo.py
```

Generated files:

```text
visual-composer/figures/translation_bleu_lollipop.svg
visual-composer/figures/training_schedule_slopegraph.svg
visual-composer/figures/configuration_ratio_heatmap.svg
visual-composer/figures/base_big_small_multiples.svg
```

## Visual Contract

```text
Core claim: Transformer big reports strong official headline BLEU while scaling model/training configuration relative to base.
Reviewer question: Which official values support the demo's result and configuration narrative?
Evidence layer: main result + configuration/schedule support.
Source data: ../artifacts/official-data.md.
Statistics/uncertainty: none supplied in the official extract; no uncertainty is invented.
Output format: editable SVG.
```

## No-Fabrication Status

- BLEU values, step time, steps, duration, model dimensions, heads, and dropout come from `../artifacts/official-data.md`.
- Ratio and normalized panels are derived from those official values and labeled as ratios or normalized units.
- The demo does not add external baseline scores, seeds, or uncertainty intervals.
