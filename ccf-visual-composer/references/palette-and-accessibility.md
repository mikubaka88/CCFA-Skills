# Palette And Accessibility

Color is evidence encoding, not decoration. Choose palettes that remain legible under color-vision variation, grayscale printing, small conference columns, and projector compression.

## Default Palette Policy

- Categorical evidence default: Okabe-Ito Color Universal Design; keep existing approved mappings. For method illustrations, use the established CCFA palette or a content-fit variant below.
- Alternative categorical set: ggsci NPG when its series remain distinguishable at final size.
- Sequential and diverging maps: prefer perceptually uniform scientific colour maps such as batlow, lajolla, tokyo, oslo, vik, roma, broc, or cork.
- Discrete alternatives: use ColorBrewer families that pass colorblind/print checks.
- Avoid rainbow/jet for new numerical encodings of ordered quantities; preserve actual supplied image/depth data and approved template mappings.

## Recommended Hex Sets

Okabe-Ito qualitative:

```text
#E69F00 #56B4E9 #009E73 #F0E442 #0072B2 #D55E00 #CC79A7 #000000
```

ggsci NPG qualitative:

```text
#E64B35 #4DBBD5 #00A087 #3C5488 #F39B7F #8491B4 #91D1C2 #DC0000 #7E6148 #B09C85
```

Neutral manuscript support:

```text
#222222 #666666 #A6A6A6 #D9D9D9 #F2F2F2
```

## Additional Scientific Palettes

Select these through the existing `PALETTES` dictionary in `resources/python/ccfa_plot_recipes.py`; both Python plotting paths share it. Each row is a categorical set, with the source order preserved. The journal names identify ggsci's palette names, not an official journal requirement or endorsement. Choose for the data and final reading size; a palette name alone does not make a figure compliant with a journal.

| Palette key | Hex sequence | Suggested use and constraint |
| --- | --- | --- |
| `aaas` | `#3B4992` `#EE0000` `#008B45` `#631879` `#008280` `#BB0021` `#5F559B` `#A20056` `#808180` `#1B1919` | Saturated method comparisons and compact condition panels; similar dark colors need markers or direct labels. |
| `nejm` | `#BC3C29` `#0072B5` `#E18727` `#20854E` `#7876B1` `#6F99AD` `#FFDC91` `#EE4C97` | Cohort distributions, paired outcomes, and ablations with warm/cool separation; the pale yellow is best as a fill with a visible outline. |
| `lancet` | `#00468B` `#ED0000` `#42B540` `#0099B4` `#925E9F` `#FDAF91` `#AD002A` `#ADB6B6` `#1B1919` | Distinct condition highlights and grouped response panels; the red/green pair must carry a second visual distinction. |
| `jco` | `#0073C2` `#EFC000` `#868686` `#CD534C` `#7AA6DC` `#003C67` `#8F7700` `#3B3B3B` `#A73030` `#4A6990` | Blue/gold/red cohort comparisons and forest plots; do not rely on several related blue tones to distinguish adjacent thin curves. |
| `tol_bright` | `#4477AA` `#EE6677` `#228833` `#CCBB44` `#66CCEE` `#AA3377` `#BBBBBB` | A compact alternative for categorical curves and points, designed by Paul Tol with color-vision accessibility in mind. |
| `tol_muted` | `#CC6677` `#332288` `#DDCC77` `#117733` `#88CCEE` `#882255` `#44AA99` `#999933` `#AA4499` | More categories in multi-panel biological or model comparisons; keep IDs stable across every panel and use darker outlines for pale fills. |

The ggsci sets are not all colorblind-safe. Tol's bright and muted sets address common red/green color-vision deficiencies, but do not guarantee grayscale separation or readability at every mark size. Check the colors actually used, not just the full swatch strip. Never interpolate these categorical sequences into a quantitative heatmap; ordered values still use a sequential or diverging map.

## CCFA Palette Variants

The seven existing showcase color sets are also available through `PALETTES` in the plotting library. All previous palette keys and values remain valid; variants broaden choice without changing established semantic mappings.

| Palette key | Hex sequence | Useful visual character |
| --- | --- | --- |
| `ccfa_gem` | `#174A7C` `#D95F02` `#1B9E77` `#7570B3` `#E7298A` `#66A61E` `#E6AB02` | Clear blue/orange with green and violet accents; distinct branches. |
| `ccfa_nocturne` | `#0E2A47` `#28587B` `#9FB798` `#F2C14E` `#F78154` `#B4436C` | Deep blue, sage, amber, and coral; strong hierarchy on a light canvas. |
| `ccfa_ceramic` | `#264653` `#2A9D8F` `#E9C46A` `#F4A261` `#E76F51` `#8AB17D` | Teal, sand, and terracotta; warm scientific objects and calm group regions. |
| `ccfa_orchid` | `#3B1F5E` `#6A4C93` `#B565A7` `#E56B6F` `#EAAC8B` `#355070` | Plum, mauve, and peach; contribution emphasis with subdued context. |
| `ccfa_arctic` | `#063B63` `#0B7285` `#38A3A5` `#80ED99` `#F4D35E` `#EE964B` | Blue/teal with lime and amber; spatial or temporal representations. |
| `ccfa_wine` | `#5F0F40` `#9A031E` `#FB8B24` `#E36414` `#0F4C5C` `#6A994E` | Burgundy, orange, and dark teal; a warm focal mechanism with cool support. |
| `ccfa_ink` | `#111827` `#374151` `#1D4ED8` `#059669` `#D97706` `#BE123C` | Dark neutrals with blue, green, and warm accents; restrained comparisons. |

Choose a palette for the figure's reading context, then assign roles explicitly: dark ink, contribution, supporting branches, neutral context, and light group fills. A method diagram usually needs 2-4 chromatic roles, not every swatch. Use an 8-15% accent tint over white for group backgrounds and dark text above it. Related figures keep the same role mapping; do not rotate palettes just to make each figure different.

These variants are starting sets, not certified color-vision-safe combinations. Pale swatches are better for fills than thin lines or text. Add non-color channels for adjacent similar hues. Categorical result plots may need more distinct series than a method diagram; never merge categories to meet a color budget. Ordered quantities still use a suitable sequential/diverging map. Choose actual colors once and include their hex values in the image prompt instead of relying on palette names.

## Semantic Color Rules

When no user/reference/template mapping is established and the figure has these roles, an optional starting map is reference/target `#1A1A1A`, primary method/result `#2C7FB8`, comparator/ablation `#E07A2D`, limit/constraint `#7A5195`, neutral substrate `#F5F5F5`. Use only the roles actually present. Preserve the role across lines, outline/fill pairs, annotations and any meaningful background region; a group fill must not imply a scientific category it does not have. This map does not replace the existing palettes, real image/depth encodings or sequential/diverging scales. Missing/invalid data remain distinct from ordinary background.

For quantitative plots, encode real distinctions with consistent line/marker treatment when not fixed by the template: solid reference, modestly stronger solid primary, distinct dashed/dash-dot comparison, and a translucent band only for a supplied or explicitly computed interval. About 1.5 pt can be a starting main-line width at the intended print size, subject to destination rules, density and template fidelity. Point jitter is only a declared display treatment for overlapping repeated observations; do not perturb meaningful time/position or alter pairing. Retain actual observations and the underlying values. Contours should expose useful levels sparsely, not manufacture extra analytical content.

- Map stable entity IDs to colors once across related figures, whether the entities are models, cell types, cohorts, or conditions. Keep the proposed method's mapping fixed; panel order must not silently reassign colors.
- If no user/template/role mapping is established, secondary baselines can use neutral gray; retain an already assigned comparator color across related figures.
- Use positive/negative colors only for true directional meaning.
- Do not encode a critical distinction with red/green alone; add markers, line styles, hatches, direct labels, or grouping.
- Keep color roles stable across main text, appendix, tables, and slides.
- Avoid palettes dominated by decorative gradients or many similar hues.
- For comparable heatmaps, share explicit limits and any meaningful center; use the same unit and transformation. Distinct quantities retain separate labeled scales even when their rows are aligned. Missing values need a distinct missing-data mark, not the color for zero. Reject invalid values instead of silently clipping the source to a color range.

## Accessibility Checks

- Check grayscale legibility.
- Check color-vision safety, especially for adjacent lines/bars and small legend keys.
- Check print visibility at final paper size, not at full-screen preview size.
- Make line styles, markers, hatches, direct labels, and panel ordering carry meaning even when color is removed.
- Keep text contrast high; avoid colored text on saturated backgrounds inside paper figures.

For monochrome delivery, assign distinguishable lightness, marker shapes, and line dashes before rendering. Direct labels and aligned small multiples often work better than dense hatching. Use hatches only where the destination permits them; Nature's current figure guide discourages patterns. Desaturating several equal-lightness colors is not a sufficient fallback, and accessibility must never depend on a colored word in a caption.

## Typography And Final Size

Use Times New Roman by default or selected Comic Sans MS for the actual requested figure. A destination may specify different type, dimensions or production formats; verify the exact journal/venue, stage and track only when those requirements affect this deliverable. A journal-inspired palette does not activate that journal's production rules or override the user's font choice.

Set physical width before choosing font sizes and line weights, and inspect the export at that width. Keep comparable panel labels, ticks, and legends consistent. Reduce redundant labels or split a crowded figure before shrinking text below the selected size. Layout spacing is measured after tick labels and legends are present, not only between the bare axes.

For Chinese labels, retain the selected Latin font and supply an installed CJK companion such as Noto Serif CJK SC, Source Han Serif SC, or SimSun for serif text; use the corresponding CJK sans family for a sans-serif destination. Confirm glyph coverage rather than assuming Times or Comic contains Chinese. Export as UTF-8, embed fonts in PDF with TrueType/type 42 when supported, keep text live in an explicitly requested SVG, and inspect Chinese, minus signs, Greek letters, and superscripts in the rendered result. Do not hide missing-glyph warnings or replace unavailable characters with blank boxes.

## Source Notes

Source URLs, versions and verification dates live in Common's `source-registry.yaml`; inspect the relevant row only. Preserve attribution without treating a palette as a venue requirement.

- Nan Xiao's ggsci palette definitions: `ggsci-palettes`. The named values/order are recorded with attribution; ggsci is GPL-3.0-or-later and its R implementation is not vendored here.
- Paul Tol's official notes: `tol-color-schemes`. The muted missing-data gray is outside the category sequence; the author retains attribution and this library does not copy his figures, prose or implementation.
- Exact-destination production guidance: `nature-figure-specifications`, `nature-panel-export` and `nature-final-lines`. Check the actual journal and submission stage when relevant, without importing those requirements into an unrelated paper.
