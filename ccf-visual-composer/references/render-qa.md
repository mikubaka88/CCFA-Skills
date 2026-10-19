# Render QA

For Chinese or mixed-script figures, check UTF-8 source text separately from font coverage. Inspect actual Chinese glyphs in the rendered output and, where applicable, PDF text extraction or native text objects. Boxes, missing characters, and garbled extraction are failures to investigate; changing an encoding label cannot fix a missing glyph or PDF font mapping. Preserve the selected Latin font and use an available CJK fallback from `../../ccf-common/references/artifact-contracts.md`.

Capture native converter diagnostics as bytes and decode them with the verified tool encoding before reporting them as UTF-8. Some Windows converters emit GBK logs even when their SVG/PDF text is correct. Confirm the encoding against known text or paths; do not apply a blanket GBK fallback or rewrite correct input files. A readable font/cache warning still needs its own assessment; successful log decoding does not resolve the underlying warning.

Visual QA is based on rendered output, not source optimism. When source files exist, compile or render and inspect the pages or exported images that contain the target figures/tables.

## Scope And Reuse

Run one integrated inspection of the requested formats, separating scientific fidelity from visual quality. A numeric chart needs data/axis/uncertainty checks; an architecture needs topology/label checks; PPTX checks apply only to PPTX. For a local revision, inspect the changed region plus affected dependencies at intended size. Reuse unchanged inspections; a shared font, scale, or layout change warrants broader coverage. A second independent assessment uses Common's effective `independent_review` preference or an explicit request, not a mandatory extra agent.

Use one current build preview per artifact under the shared working directory. Open it once for a meaningful change and inspect a targeted crop when a specific detail remains uncertain. Reuse an existing QA record; persist only unresolved or decision-relevant findings needed to continue. Do not produce a screenshot or report for each checklist bullet. Keep checking until the requested quality is met or a concrete tool/evidence limitation is identified.

## Scientific Fidelity

- Values, precision, units, sample sizes, uncertainty, and metric direction match traceable source data. Invalid correlation coefficients or probabilities fail before rendering; missing values and valid exact zeros retain their stated meaning instead of being silently clamped or relabeled.
- Related panels match entities by ID, with the intended order/grouping and correct annotation rows. Common colors, axes, legends, and heatmap limits encode the same quantities. Distinct units or free scales are explicit; independently scaled panels do not imply comparable magnitudes.
- Architecture nodes, groups, typed edges, and training/inference boundaries match the supplied method. Detail-view leaders cannot be mistaken for another computation; indices, equations, and essential labels remain intact.
- Generated labels match the approved inventory, without invented acronym expansions, ornamental numbers, or prose. Repair malformed raster text through the host image workflow, or in the native source when editable reconstruction is requested.
- Scientific images retain aspect ratios, scale bars, crop/contrast meaning, and actual evidence content. Conceptual illustrations do not impersonate observations. Icons preserve necessary scientific parts, individual licenses, and required attribution.

## Visual Quality

- Inspect the overview for a clear reading path and content-fit canvas, then the final paper/display width for text and object recognition. A paper mechanism figure exposes its computations; remove decorative banners, prose cards, or generic icons that obscure them.
- Check axis labels, legends, panel labels, captions, table notes, and surrounding content for clipping/overlap. Captions remain near the artifact, float order follows the argument, and cross-references resolve. Tables fit margins without unreadable shrinkage.
- Align data rectangles and corresponding crop regions across panels, accounting for unequal outer tick-label margins and fixed-aspect geometry. Shared legends describe matching encodings and do not duplicate every panel's entries.
- Check peer edges, text baselines, branch ports, repeated visible gaps, padding, icon optical sizes, and connector clearance against chosen anchors/tokens. Equal roles may have different widths to fit their content. In vector/native output, verify intended equalities within 1 design px after unit conversion; raster inspection cannot certify pixel-exact geometry.
- Inspect outer margins and internal holes separately. A module-sized empty patch prompts a layout check; retain plotting whitespace and connector lanes. Compactness comes from arranging supported content, without adding empty frames or decorative objects.
- Verify the final physical font sizes after embedding or composing panels, including axes, legends, math, and indices. Resize geometry separately from typography/strokes when necessary; reflow crowded content before reducing one label below its peers' readable scale.
- Use the selected Times New Roman, Comic Sans MS, or user/venue font consistently, with actual CJK coverage and appropriate math glyphs. Check substitution/embedding in editable formats; raster appearance cannot prove a font face. Ordinary labels use natural case while canonical acronyms remain uppercase.
- Color roles remain stable and legible in grayscale/color-vision checks. The chosen preset coordinates strokes, fills, type, and recognizable illustrations with consistent viewpoint/detail. Its venue suggestion has not been presented as an official rule.

## Requested Format And Edit Checks

- An editable SVG contains live text and selectable semantic vector groups. Export vector PDF from that canonical source and retain source editability; a whole-page raster or noisy auto-trace does not qualify. Raster previews have enough resolution to inspect the delivery size.
- A PPTX uses live text, native nodes/connectors/groups, and separately selectable assets. Identify native shapes, SVG graphics that need Office conversion, and isolated movable raster assets accurately. Render it to inspect font substitution, connector drift, transparency fringes, clipping, and z-order.
- Icons have clean alpha edges and consistent optical weight, without stray text or unsupported detail. For a selected-object edit, verify source/export versions, actual object IDs, attached connectors, and protected regions. Reconcile manual source edits before regenerating dependent exports.

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
