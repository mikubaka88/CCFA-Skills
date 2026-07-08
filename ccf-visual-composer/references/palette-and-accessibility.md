# Palette And Accessibility

Color is evidence encoding, not decoration. Choose palettes that remain legible under color-vision variation, grayscale printing, small conference columns, and projector compression.

## Default Palette Policy

- Categorical default: Okabe-Ito Color Universal Design.
- Journal-style categorical accent: ggsci NPG only when the paper needs a polished multi-series palette and accessibility still passes.
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
