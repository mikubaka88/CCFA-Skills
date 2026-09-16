# Palette And Accessibility

Color is evidence encoding, not decoration. Choose palettes that remain legible under color-vision variation, grayscale printing, small conference columns, and projector compression.

## Default Palette Policy

- Categorical evidence default: Okabe-Ito Color Universal Design; keep existing approved mappings. For method illustrations, use the established CCFA palette or a content-fit variant below.
- Alternative categorical set: ggsci NPG when its series remain distinguishable at final size.
- Sequential and diverging maps: prefer perceptually uniform scientific colour maps such as batlow, lajolla, tokyo, oslo, vik, roma, broc, or cork.
- Discrete alternatives: use ColorBrewer families that pass colorblind/print checks.
- Never use rainbow or jet for ordered scientific quantities.

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

- Assign the proposed method one stable color across the paper.
- Use neutral gray for secondary baselines unless a baseline is itself the scientific focus.
- Use positive/negative colors only for true directional meaning.
- Do not encode a critical distinction with red/green alone; add markers, line styles, hatches, direct labels, or grouping.
- Keep color roles stable across main text, appendix, tables, and slides.
- Avoid palettes dominated by decorative gradients or many similar hues.

## Accessibility Checks

- Check grayscale legibility.
- Check color-vision safety, especially for adjacent lines/bars and small legend keys.
- Check print visibility at final paper size, not at full-screen preview size.
- Make line styles, markers, hatches, direct labels, and panel ordering carry meaning even when color is removed.
- Keep text contrast high; avoid colored text on saturated backgrounds inside paper figures.

## Source Notes

Useful palette sources include ggsci journal palettes, Fabio Crameri Scientific Colour Maps, ColorBrewer, Okabe-Ito Color Universal Design, and the Nature Communications warning against misleading color maps. Treat these as design references, not venue rules.
