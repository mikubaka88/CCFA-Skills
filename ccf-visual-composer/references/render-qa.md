# Render QA

Visual QA is based on rendered output, not source optimism. When source files exist, compile or render and inspect the pages or exported images that contain the target figures/tables.

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
- Generated-image labels match the approved label inventory; malformed text is corrected during semantic SVG reconstruction.
- An editable SVG contains live text and selectable vector groups rather than a full-page embedded or auto-traced raster.
- A requested vector PDF is exported from the reconstructed vector source, with SVG retained as the canonical editable artifact.
- Public icons use a coherent family and recorded license; custom icons remain separate assets with clean alpha edges, no background halo, no embedded text, and no hallucinated internal detail.
- The layout follows explicit alignment lines and spacing tokens; information boxes with the same role share dimensions or baselines unless hierarchy requires a visible exception.
- A requested PPTX contains live text, native boxes/nodes/connectors, semantic groups, and separately selectable icon assets rather than one full-slide image.
- PPTX editability is reported per asset: native shape, SVG graphic convertible to Office shapes, or isolated raster that is movable but not vector-editable.
- The PPTX is rendered to a preview and inspected for clipping, font substitution, connector drift, transparency fringes, and z-order errors.

## QA Ledger

Use this table for non-trivial QA:

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

After three unresolved high-severity visual issues, escalate to the next owner instead of silently continuing:

- missing or unsupported data -> `ccf-experiment-designer`
- claim/number mismatch -> `ccf-integrity-auditor`
- prose or narrative placement issue -> `ccf-paper-writer`
- final venue/package rule issue -> `ccf-submission-checker`
