# Shared Visual Decisions

Use the actual article, data, selected design and destination to make the figure understandable at its final size. The existing specification/current context holds these decisions; a separate contract, measurement sheet or checklist report is not required.

## Scientific Meaning

Establish the message, relevant source, exact labels/units, necessary relationships and intended final slot. For conceptual figures, use the understanding and three-stage workflow in [architecture-diagram-generation.md](architecture-diagram-generation.md). For numerical figures, reuse the selected Python/JSON or choose a design through [figure-design-library.md](figure-design-library.md).

Classify data independently from chart type. Raw samples, quantile summaries and binned counts are different inputs; given envelopes are not automatically confidence intervals. Preserve observation IDs, pairing, denominators, interval meanings and transformations. Do not fabricate raw observations from a summary or infer pairing from equal lengths.

A rich analysis unit combines supported relationships: distributions and conditional regions, central ranges and tails, category levels and supplied trends, or trajectories and real events. Extra labels, an empty inset or another view of the same mean do not create information. Keep a separate panel/zoom when its question, unit or domain requires one; do not force either one axis or a uniform multi-panel grid.

For requested screenshot-based numerical reconstruction, record which values are estimated, freeze the input for comparisons and preserve the reference's actual statistical encodings. Calibrated reconstruction weights are not recovered measurements. The specific encodings and implementation controls are maintained in the design-library guide.

## Compact Layout And Type

Start from the actual paper/display slot and a content-fit aspect ratio. Align related data rectangles, image crops, peer objects and label baselines. Remove accidental gaps and redundant containers while retaining space that separates meanings or belongs to the data geometry. Do not stretch images, alter axes, hide observations or add unsupported content to fill a hole.

Use Times New Roman by default or selected Comic Sans MS, subject to user/destination overrides. Bold titles, legends, axes/ticks and quantitative colorbar text; method headings remain distinct from subordinate labels and equations. Apply one coherent font family with real math/CJK glyph coverage. Mathematical variables and ordinary units keep their appropriate notation.

Choose sizes in physical units for code-rendered plots and inspect the final embedded width. Preserve the selected template's scale; reflow or wrap crowded labels before shrinking them below their peers. Raster inspection checks appearance/readability and does not certify an exact font face or pixel equality.

Bars, boxes, whiskers and caps use darker opaque shades paired with lighter same-hue fills. Dense scatter points, density bins and matrix cells retain their own encoding rather than receiving heavy borders by default. Keep scientific emphasis on the important mechanism or comparison. Labels are concise; required terminology, units, equations and identifiers remain intact, with explanations in the caption.

## Shared Identity And Scale

Match repeated subjects, genes, methods or conditions by stable IDs before arranging related views. Retain a common order/group split when the scientific comparison needs it; show missing entries explicitly. Equal row counts or matching label strings alone do not establish identity.

Share category colors and legends only when their encodings match. Share numeric limits/normalization only for comparable quantities with the same units and transformation; distinct quantities keep labeled scales. An aligned annotation row follows the same entities as its data. Preserve spatial aspect ratios, crop correspondence and scale bars in image plates.

Use [palette-and-accessibility.md](palette-and-accessibility.md) for an actual color/type decision, [adaptive-architecture-style.md](adaptive-architecture-style.md) for an unresolved diagram treatment, and [figure-table-layout.md](figure-table-layout.md) for manuscript/table integration. Do not load every reference for a local edit.

## Iteration And Acceptance

Reuse one stable artifact directory and current source/specification, following Common's artifact contract. Keep required inputs and reusable assets; update current exports in place. Do not create numbered prompts, per-attempt folders or extra QA ledgers by default.

Inspect scientific fidelity and visual quality together through [render-qa.md](render-qa.md). A local change checks its affected dependencies. A repeated action needs a concrete defect or changed hypothesis; revise the relevant representation/instruction when nudging fails, without changing the scientific content to make it fit. New/redrawn diagrams stay in the image workflow throughout; existing source edits and explicit numerical exports retain their actual formats.
