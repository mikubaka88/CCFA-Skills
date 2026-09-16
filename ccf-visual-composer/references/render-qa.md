# Render QA

For Chinese or mixed-script figures, check UTF-8 source text separately from font coverage. Inspect actual Chinese glyphs in the rendered output and, where applicable, PDF text extraction or native text objects. Boxes, missing characters, and garbled extraction are failures to investigate; changing an encoding label cannot fix a missing glyph or PDF font mapping. Preserve the selected Latin font and use an available CJK fallback from `../../ccf-common/references/artifact-contracts.md`.

Capture native converter diagnostics as bytes and decode them with the verified tool encoding before reporting them as UTF-8. Some Windows converters emit GBK logs even when their SVG/PDF text is correct. Confirm the encoding against known text or paths; do not apply a blanket GBK fallback or rewrite correct input files. A readable font/cache warning still needs its own assessment; successful log decoding does not resolve the underlying warning.

Visual QA is based on rendered output, not source optimism. When source files exist, compile or render and inspect the pages or exported images that contain the target figures/tables.

## Scope And Reuse

Run the applicable checks below, not every format's checklist. A numeric chart needs data/axis/uncertainty checks; an architecture needs topology/label checks; PPTX checks apply only to PPTX. For a local revision, inspect the changed region plus affected dependencies at intended size. Reuse unchanged inspections; a shared font, scale, or layout change warrants broader coverage.

Use one current build preview per artifact under the shared working directory. Open it once for a meaningful change and inspect a targeted crop when a specific detail remains uncertain. Reuse an existing QA record; persist only unresolved or decision-relevant findings needed to continue. Do not produce a screenshot or report for each checklist bullet. Keep checking until the requested quality is met or a concrete tool/evidence limitation is identified.

## Checks

- No clipped axis labels, legends, panel labels, captions, or table notes.
- No incoherent overlap between text, plots, legends, subfigures, floats, or surrounding paragraphs.
- Float order matches the paper logic and cross-references resolve.
- Fonts are embedded or accepted by the target template; labels remain readable at final size.
- Ordinary visible English uses natural title or sentence case; canonical acronyms and initialisms remain uppercase, and no complete ordinary-language title, module label, legend, axis, annotation, badge, or table header is styled in all caps.
- Vector text remains editable when requested; raster previews are high enough resolution.
- Color contrast survives grayscale and color-vision checks.
- Figure captions and table captions are present, near the artifact, and not detached by bad float placement.
- Tables do not exceed margins and do not use unreadable shrinkage.
- Numeric precision, units, sample size, confidence intervals, and metric direction match the manuscript.
- Source data or scripts are traceable enough for later integrity audit.
- Architecture nodes, groups, and connections match the supplied method; no plausible-looking component was invented.
- A paper architecture figure exposes representations, operators, branches, merges, and outputs; it is not a set of explanatory stage cards, a dashboard, a README hero, or a PPT/Poster graphic.
- Paper-figure QA rejects large stage banners, repeated callout bubbles, decorative hero titles, oversized generic icons, and prose-heavy cards that do not correspond to computations.
- Architecture arrows have correct direction and semantics, and training/inference boundaries remain truthful.
- Generated-image labels match the approved inventory, with no extra explanatory prose, invented acronym expansions, or ornamental numbers. Repair malformed raster text through the image-editing workflow, or directly in the vector/native source when reconstruction is requested. Preserve essential data labels, units, ticks, and equations.
- An editable SVG contains live text and selectable vector groups rather than a full-page embedded or auto-traced raster.
- A requested vector PDF is exported from the reconstructed vector source, with SVG retained as the canonical editable artifact.
- Public icons use a coherent family and recorded license; custom icons remain separate assets with clean alpha edges, no background halo, no embedded text, and no hallucinated internal detail.
- The layout follows explicit alignment lines and spacing tokens; information boxes with the same role share dimensions or baselines unless hierarchy requires a visible exception.
- Check repeated edge gaps, padding, text baselines, optical icon size, and reserved connector clearance against the selected design tokens. In vector/native output, verify coordinates in design units (within 1 px for intended equalities after conversion); for raster output, inspect visible consistency and state any unresolved precision limit instead of claiming pixel-exact placement.
- The figure has one clear entry and reading path on a content-fit canvas; no default square or mandatory ratio. Inspect outer margins and internal holes separately. A blank patch as large as a meaningful module triggers a layout check; plotting whitespace and reserved connector lanes are legitimate. Do not pass compactness by filling backgrounds, enlarging empty frames, or adding unsupported content.
- Alignment continues across block boundaries: peer top/bottom edges, label baselines, branch ports, panel labels, and comparable plot/crop regions share the intended anchors. Equal rank does not require an oversized uniform box when content extents differ.
- Inspect the overview for hierarchy, then the actual paper/display width for fonts. Verify the chosen point-size roles after scaling, including axes, secondary labels, math and indices. Do not shrink just one crowded block below the readable type scale; revise its content placement or available area.
- Times New Roman or the selected Comic Sans MS treatment is consistent across ordinary text and numbers, subject to user/venue overrides. Check actual font availability and substitution in editable output; do not infer a genuine font face from a generated raster's appearance.
- Internal illustrations are recognizable at their allocated size, with coherent viewpoint, detail, color, and rendering treatment. Repeated objects remain visually consistent and conceptual imagery is not presented as experimental evidence.
- The chosen preset coordinates font, line weight, grouping, and fill. A conference suggestion has not been presented as an official rule. Detail-view leaders cannot be mistaken for extra computation or flow; matrices/frame strips retain necessary indices and symbols.
- A requested PPTX contains live text, native boxes/nodes/connectors, semantic groups, and separately selectable icon assets rather than one full-slide image.
- PPTX editability is reported per asset: native shape, SVG graphic convertible to Office shapes, or isolated raster that is movable but not vector-editable.
- The PPTX is rendered to a preview and inspected for clipping, font substitution, connector drift, transparency fringes, and z-order errors.
- For a selected-object edit, verify the current source/export correspond and identify actual source object IDs. Check the changed objects, attached connectors, and unchanged protected regions. Preserve a manually edited user file until its changes have been reconciled with the authoring source.

## QA Ledger

Use this table inside the current specification/report only when QA findings must persist; do not create another ledger by default:

```text
| Issue | Artifact | Page/section | Severity | Fix | Owner | Status |
| --- | --- | --- | --- | --- | --- | --- |
```

Severity:

- High: can mislead reviewers, hide evidence, break compilation, or violate venue constraints.
- Medium: reduces readability or weakens the evidence chain.
- Low: polish issue that does not affect interpretation.

## Anti-Loop Rule

If two tactical tweaks fail, change structure rather than keep nudging fonts or spacing. Examples: split the table, move robustness to appendix, switch to a more appropriate chart family, use a full-width float, remove redundant panels, or redraw labels directly.

Route a concrete dependency to its owner as soon as that evidence is needed; continue unaffected visual fixes. An issue count alone does not justify stopping:

- missing or unsupported data -> `ccf-experiment-designer`
- claim/number mismatch -> `ccf-integrity-auditor`
- prose or narrative placement issue -> `ccf-paper-writer`
- final venue/package rule issue -> `ccf-submission-checker`
