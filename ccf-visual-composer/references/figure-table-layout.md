# Figure And Table Layout

The visual must sit inside the paper's argument, not after it. Place each figure/table near its first substantive discussion and make the text explain why the reader should look at it.

## Manuscript Integration

- Mention the figure/table in text before the float appears.
- The surrounding paragraph should state the question, then the visual should answer it.
- Captions should identify what is shown, the setting, the key takeaway, units/statistics, and source-data caveats when needed.
- Do not let captions make claims that are stronger than the supplied evidence.
- Prefer stable labels: `fig:overview`, `fig:main-results`, `tab:main`, `tab:ablation`.

## Figure Composition

- Apply the shared typography and scaled spacing tokens in `visual-contract.md` to panels, image tiles, legends, and tables. Align plot areas as well as their outer boxes; long tick labels may require unequal outer padding to keep the data regions aligned.
- Decide single-column versus full-width before arranging panels.
- Choose the combined figure's aspect ratio from those bounds and its contents. Align plot areas, panel labels, and caption baselines across blocks; reserve a shared legend only when its encodings are genuinely shared. Tighten unused outer and between-panel space without distorting data axes or image geometry.
- Use full-width (`figure*`) when the reader must compare many panels horizontally or when labels would be unreadable in one column.
- Avoid excessive panel counts in the main paper; use appendix for secondary robustness grids.
- Use lowercase panel labels `(a)`, `(b)`, `(c)` unless the venue/template requires another style.
- Put legends outside dense plotting areas or in a dedicated legend strip/panel.
- Preserve editable vector text when possible: for matplotlib use `svg.fonttype = 'none'`; export SVG/PDF for final paper and PNG only for preview.
- Use consistent axis names, units, limits, and ordering across related panels.
- Keep only necessary annotations and a shared legend where it remains unambiguous. Remove duplicate explanation, not meaningful ticks, values, uncertainty, or scale information. Avoid an internal hero title when the manuscript caption already supplies it.
- For image plates, include scale bars, crop rules, channel labels, and contrast notes; do not use contrast adjustments that change scientific interpretation.

## Table Composition

- Use `booktabs` style: no vertical rules, clear header grouping, and sparse horizontal rules.
- Use `siunitx` or aligned numeric columns when precision matters.
- Keep numeric precision consistent with the experiment; do not imply false accuracy.
- Fit tables to `\columnwidth` or intentionally use `table*`; avoid unreadably tiny font.
- Keep same-role text at the same final point size across panels/tables. Measure the rendered result after font or column changes; do not shrink a single crowded cell while leaving its peers large.
- Split wide tables by scientific question instead of shrinking everything.
- Put table notes under the table for metric direction, units, significance markers, or missing values.
- Tables inserted as images are a last resort and should not be used for ordinary manuscript tables.

## LaTeX Float Strategy

- Prefer `[t]` or `[tb]` for normal floats; avoid forcing `[H]` unless the template/workflow truly requires it.
- Use `figure*`/`table*` for full-width two-column floats when needed.
- Keep captions and labels together: caption first, then label, unless the template says otherwise.
- Verify float order after compile; do not assume source order equals PDF order.
- Avoid placing a key visual so late that reviewers must search for evidence after the claim.
