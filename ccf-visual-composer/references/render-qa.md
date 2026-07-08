# Render QA

Visual QA is based on rendered output, not source optimism. When source files exist, compile or render and inspect the pages or exported images that contain the target figures/tables.

## Checks

- No clipped axis labels, legends, panel labels, captions, or table notes.
- No incoherent overlap between text, plots, legends, subfigures, floats, or surrounding paragraphs.
- Float order matches the paper logic and cross-references resolve.
- Fonts are embedded or accepted by the target template; labels remain readable at final size.
- Vector text remains editable when requested; raster previews are high enough resolution.
- Color contrast survives grayscale and color-vision checks.
- Figure captions and table captions are present, near the artifact, and not detached by bad float placement.
- Tables do not exceed margins and do not use unreadable shrinkage.
- Numeric precision, units, sample size, confidence intervals, and metric direction match the manuscript.
- Source data or scripts are traceable enough for later integrity audit.

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
