# Visual Contract

Start every non-trivial figure or table with a contract. The contract keeps scientific meaning ahead of decoration and prevents panels from becoming disconnected result dumps.

## Relevant Fields Only

Reuse the existing source/specification. For a new non-trivial artifact, establish the core fields below internally; save them only for continuation or reproduction. A one-label or one-color edit does not require a new contract.

```text
Artifact and canonical paths:
Scientific question / takeaway:
Source data or method, with evidence locations:
Final size / destination / requested formats:
Aspect ratio / occupied bounds / selected preset, if needed:
Relevant panel map or topology:
Exact labels, units, and visual encodings:
Information carried by each encoding; reason for any extra axes/panel:
```

Add only mode-specific information: uncertainty, metric direction, entity IDs/order, units and shared scales for related quantitative panels; node/edge semantics for architectures; float/caption placement for manuscript integration; icon provenance or editability levels when those assets are used; reference-layout principles only when a reference is actually used. Do not emit empty fields for unrelated formats. The architecture specification and this contract are the same state, not two documents to maintain.

## Article To Elements

Reuse one source record. Establish the paper question, observation unit, actual input format and available fields before selecting a grammar. Classify input data independently from chart type: raw samples are not quantile summaries, binned counts are not recovered observations, and given envelopes are not automatically confidence intervals. Read the relevant caption/protocol when its statistical definition matters.

Build an element plan from the current article: primary data -> conditioning/comparison -> relevant summary -> clear reading key. Choose complementary analyses supported by these inputs. A density may carry a two-condition corridor, threshold bounds, a conditional count and a separate weighted share when weights exist. A quantile summary can combine a central range, tail whiskers and a selected-quantile curve. Category measurements can combine outlined bars, same-unit curves, provided ranges and selected values. A trajectory can carry event markers or reference regimes only when their locations/meaning are supplied. Actual raw samples can support declared descriptive summaries; do not fabricate raw runs from summary tables.

Plan semantic relationships, not a fixed number of layers. Maintain coordinate/identity correspondence, denominators and interval definitions. A label, grid or legend alone is not another analysis. Library primitives and extracted views are building blocks; enrich the final graphic using article-specific conditions, uncertainty or comparisons rather than accepting the first primitive export. Keep additional views when their units/domains need separation.

For an explicitly requested screenshot reconstruction, approximate visible values with per-field provenance and keep the input frozen. If a visible aggregate is used to calibrate a reconstruction, state that calibration in the input record. Do not present fitted reconstruction weights as recovered measurements. Before/after comparisons use the same reference-derived brief, data and declared render budget; preserve the baseline's complete supported elements.

## Layout And Typography

New method diagrams default to a whole GPT Image composition; quantitative figures use Python. Mixed figures preserve code-rendered numerical marks, axes and labels. Existing source edits, explicit backend choices and requested exact/editable outputs retain their appropriate route. Deliver PNG by default; an unspecified editable request prefers native PPTX, and SVG requires an explicit request.

Start from the actual paper slot and a content-fit aspect ratio. If no numerical slot is supplied, about 85–90 mm is a useful single-column starting width; a method can use a short full-width slot. Do not force a square, uniform grid, fixed orientation or equal-width blocks. Group related objects tightly, align peers and use short clear connection paths. Give the important mechanism room while removing redundant containers, labels and accidental gaps. Preserve whitespace that separates meanings or belongs to data geometry; do not stretch axes, hide observations or add content to fill space.

Use Times New Roman by default or selected Comic Sans MS, preserving user/venue overrides. Bold titles, legends, x/y labels and ticks, including quantitative colorbar text. In method diagrams, emphasize headings while keeping body labels/equations subordinate. Keep one coherent family with compatible math/CJK glyph coverage. Bar/box/whisker/cap edges use opaque darker shades paired with lighter fills, around 1.1–1.3 pt at normal paper size; dense points and matrix cells keep their own encoding.

Check readability at final size. Typical compact paper labels start around 8–9 pt, headings around 9–10 pt, subject to the venue; reflow before shrinking secondary text below about 7 pt. Keep the chosen physical font settings across panels and linked layouts. Image-generated type is an appearance target; verify true fonts in requested native/editable output. Reorganize or wrap an overlong label before shrinking it below its peers.

For data figures, combine supported relationships in a coherent analysis unit: joint positions, method/cohort colors, input-condition markers, supplied sizes/pairing, threshold regions and conditional summaries. Different marker shapes need equal-area normalization when size encodes a separate quantity. Heatmaps may use aligned annotation strips. Add a real zoom or separate view only when needed by its question, units or domain; keep crop/scale correspondence explicit. Use sparse meaningful labels and light grids so observations and decisive trends remain dominant.

### Optional Coordinate Measurements

Use the following starting values only for explicit pixel constraints, measured reconstruction or code/native authoring. They are not a mandatory image-generation prompt suffix. For ordinary whole-image generation, the actual reference plus compactness/alignment requirements is sufficient. Exact user dimensions override these defaults.

At 1536 px width, scale lengths by actual width / 1536. Measure gaps edge-to-edge and reuse one value per role, with content-driven exceptions:

| Role | Starting value |
| --- | --- |
| Outer margin | 24–32 px |
| Between necessary semantic regions | 16–24 px |
| Between peer modules | 12–20 px |
| Container padding | 12–16 px |
| Between peer icons / icon to label | 16 px / 8 px |
| Connector clearance from unrelated content | At least 12 px |
| Repeated icon optical slot | 48 or 64 px |
| Ordinary / primary connector stroke | 2 px / 3 px |

Use shared edges, baselines and explicit ports when authoring coordinates. Fit boxes to rendered text, preserve image/spatial aspect ratios, and align actual data rectangles despite unequal outer label margins. Convert physical labels with `design_px = point_size * canvas_width_px / (72 * final_width_inches)`; e.g. 9 pt at 7 inches is about 27 px on a 1536 px canvas. Raster inspection does not certify exact pixels or a font face; requested native output enforces them in source.

## Text And Illustration Restraint

Keep one exact visible-text inventory. Prefer one short noun phrase per module, normally 2-5 words and at most two lines; preserve longer required terminology instead of silently abbreviating it. Put explanations and derivations in the caption. Remove redundant titles, numbered stage badges, repeated acronym expansions, duplicate legends, and ornamental numbers. Add only text in the inventory; drawing instructions and layout measurements are never visible labels.

Essential data, units, axis ticks, uncertainty, scale bars, equations, and scientific identifiers are exempt from decorative-text reduction. Choose meaningful ticks and annotations without changing the underlying values or hiding an important comparison. A figure must remain interpretable without guessing what was omitted.

Let method-specific illustrations show a small, recognizable scientific object or transformation in each planned slot. Specify viewpoint, silhouette, detail level, and shared rendering treatment. Reuse the same object across repeated frames; a change must represent a real change in the method. Generated conceptual objects may be schematic, but must not impersonate measured plots, real samples, or experimental evidence.

The CCFA visual identity is a clear mechanism, dark readable type, restrained semantic color, aligned geometry, and coherent scientific objects. Vary palettes and illustration treatment to fit the content; do not add branding, watermarks, or a fixed template to every paper figure.

## Evidence Hierarchy

- Main result: answers the paper's central claim.
- Mechanism: explains why the result happens.
- Robustness: tests stability across settings, datasets, seeds, or perturbations.
- Limitation: bounds the claim honestly.
- Qualitative or case study: makes behavior inspectable, never a substitute for quantitative evidence.

## Panel Map Rules

- Each panel must answer one distinct scientific question.
- Every panel needs an explicit role: overview, comparison, mechanism, robustness, failure, example, or source-data summary.
- If removing a panel does not change the figure's conclusion, merge it, move it to appendix, or drop it.
- Prefer an asymmetric information structure when the science calls for it: one anchor panel plus smaller supporting panels often reads better than a uniform grid.
- Keep source-data traceability visible in the contract even when the final figure is visually compact.
- Join repeated samples, genes, models, or conditions by stable IDs before arranging related panels. Reuse a common order/group split when panels compare the same entities; align annotation rows to that order and show missing entries explicitly. Do not assume equal row counts mean equal identities or independently reorder each panel for appearance.
- Share category colors and legends when their meanings match. Share axis limits or color normalization only for the same comparable quantity, unit, and transformation; keep distinct scales labeled for different quantities. A shared legend must describe the actual mapping in every panel it covers.

## Table Map Rules

- A table should compare, audit, or summarize evidence; it should not be a spreadsheet pasted into a paper.
- Group rows/columns by scientific question, dataset family, method family, or claim.
- Use consistent metric direction, units, uncertainty, and numeric precision.
- Move secondary columns to appendix when they weaken the main comparison.

## Architecture Map Rules

- Every node, group, label, and connection must be traceable to supplied method content.
- Record the reader scan path, topology, and edge semantics before choosing visual style.
- Distinguish data flow, control flow, supervision, retrieval, feedback, and gradients when the distinction matters.
- Mark training-only and inference-only elements explicitly; do not collapse them into a misleading single path.
- Use the strongest visual emphasis for the actual contribution, not for generic encoders, databases, or decorative icons.
- Keep an exact label inventory for generation QA and any explicitly requested editable reconstruction, preferring native PPTX unless another format was named.
- Plan icon semantics before rendering. Prefer native primitives or one coherent public SVG family; reserve custom generation for method-specific concepts.
- Record reference roles, measured geometric relationships, and provenance. Apply the requested layout relationships to the supplied science; preserve an explicitly supplied template when requested. Do not transplant unrelated labels, scientific claims, or artwork.
- When PPTX is requested, define which elements must be native-editable and which custom assets may remain separately movable raster objects.

## Stateful Iteration

Follow `../../ccf-common/references/artifact-contracts.md` for path resolution. Reuse established `visual-composer/` paths; otherwise use `ccfa-workfiles/figures/<figure-id>/`, or `ccfa-workfiles/tables/<table-id>/` for a standalone table. Use a descriptive ID such as `method-overview` or `main-results`; multiple figures have distinct stable IDs. Preserve one current specification/source, reusable assets, and build preview per figure, including across skill transitions. Record a source path rather than duplicating supplied data. Keep QA findings in this specification only when persistence is needed; reuse an existing separate ledger if the project already has one.

Update the relevant fields and exports after a change. Do not create numbered prompts, attempt folders, render histories, or an iteration log unless requested. Preserve user inputs and scientific evidence. Resolve repeated failures by changing the relevant structure or rendering approach; do not alter the scientific content to make the layout fit.
