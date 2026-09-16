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
```

Add only mode-specific information: uncertainty and metric direction for quantitative evidence; node/edge semantics for architectures; float/caption placement for manuscript integration; icon provenance or editability levels when those assets are used; reference-layout principles only when a reference is actually used. Do not emit empty fields for unrelated formats. The architecture specification and this contract are the same state, not two documents to maintain.

## Layout And Typography

Apply these rules to architectures, numerical plots, image plates, and visual tables. Preserve an approved existing design for local edits. User constraints and venue requirements take precedence over the starting values below.

Choose the final physical width and available height first, then a nominal design canvas. There is no default square: choose the ratio from the available paper region and supported topology, retaining the approved ratio for local edits. A wide single flow, a taller hierarchy, or aligned parallel lanes may need different ratios. Fit all parts into one coordinated figure; do not scatter isolated islands across an oversized canvas. Do not stretch axes, images, or scientific geometry to match the boundary.

For a 1536 px-wide canvas, use an 8 px base unit; scale all lengths by actual width / 1536. Pixel gaps mean visible edge-to-edge distance, not center distance. Choose one value per token for the figure, allowing documented exceptions where topology or content needs them.

| Token | Starting value at 1536 px width |
| --- | --- |
| Outer margin | 48 px; 64 px when labels need more clearance |
| Between semantic panels | 32 px |
| Between peer modules | 24 px |
| Container padding | 24 px; 16 px for a compact inset |
| Between peer icons | 16 px |
| Icon to its label | 8 px |
| Connector to unrelated text/objects | At least 12 px |
| Repeated icon slot | 48 or 64 px square, with a common optical size |
| Ordinary connector stroke | 2 px; use 3 px for a meaningful primary path |

Record panel bounds or lane proportions, shared top/bottom edges, text baselines, icon centers, and connector ports. Pack related objects more tightly than unrelated groups. Route connections through reserved whitespace. Equal-role modules share alignment and spacing; differing content may require different widths. Give the contribution enough area to explain its mechanism, without inflating generic blocks. Remove accidental holes and redundant containers; retain whitespace that separates meanings. Never distort topology to fill a grid.

Allocate the figure's rows/columns before detailing objects. Measure text and object extents to choose module sizes; one long label must not inflate every peer box. Align logical rows across group boundaries, not just objects inside each container. Shared input/output objects, branch entry/exit ports, panel labels, and captions use common anchors where their roles match. Preserve equal plot-area scales and equal image crop rules when comparisons require them. Never imply a scientific equivalence solely to make two shapes equal.

Check outer margins and unused internal regions separately. A continuous unused patch comparable in size to a meaningful module is a reason to inspect the layout, not a quota to fill. Tighten an oversized container, relocate a supported detail beside its parent operation, or adjust the canvas height/width. Preserve whitespace for data plotting, connector lanes, and semantic separation. Colored backgrounds and empty frames do not count as useful content; do not add modules, decorative objects, or duplicated labels to consume space.

Use **Times New Roman** for new scientific figures. A requested comic treatment uses **Comic Sans MS** with the same disciplined grid. Keep one primary family across titles, labels, axes, legends, and numbers; use compatible math/CJK or code fonts only for glyphs that need them. Keep ordinary text at regular/bold weights and natural case. Preserve an explicit user font or mandatory venue font. Avoid silent fallback in editable exports: check font availability and report a substitution if necessary.

Size labels for the final artifact, not the enlarged preview. A useful paper starting point is 9-11 pt body labels, 11-13 pt group headings, and 8-9 pt secondary labels, subject to the venue. Convert with `design_px = point_size * canvas_width_px / (72 * final_width_inches)`. For example, 9 pt at a 7-inch width is about 27 px on a 1536 px canvas. Increase space or reorganize groups before making labels smaller. Presentation labels must be readable at the intended viewing distance.

Choose a compact type scale once, such as 10 pt labels, 12 pt group headings, and 9 pt secondary labels; apply it across all blocks of the same role. Mathematical operators and subscripts must remain legible beside those labels. Measure rendered text, wrapping, and line height after choosing the font. When a label does not fit, remove redundant explanation or enlarge/reflow its slot before shrinking it. For a local change, changing one font size must not silently break alignment elsewhere. Check the final embedded figure width; preview pixel dimensions alone cannot certify readability.

For image generation, these coordinates, fonts, and gaps are explicit targets; raster output cannot guarantee exact pixel geometry or a genuine font face. In requested SVG/PPTX reconstruction, enforce coordinates and live fonts in the authoring source, convert units consistently, and inspect the rendered result.

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
- Keep an exact label inventory for generation QA and later editable SVG reconstruction.
- Plan icon semantics before rendering. Prefer native primitives or one coherent public SVG family; reserve custom generation for method-specific concepts.
- Record reference roles, measured geometric relationships, and provenance. Apply the requested layout relationships to the supplied science; preserve an explicitly supplied template when requested. Do not transplant unrelated labels, scientific claims, or artwork.
- When PPTX is requested, define which elements must be native-editable and which custom assets may remain separately movable raster objects.

## Stateful Iteration

Follow `../../ccf-common/references/artifact-contracts.md` for path resolution. Reuse established `visual-composer/` paths; otherwise use `ccfa-workfiles/figures/<figure-id>/`, or `ccfa-workfiles/tables/<table-id>/` for a standalone table. Use a descriptive ID such as `method-overview` or `main-results`; multiple figures have distinct stable IDs. Preserve one current specification/source, reusable assets, and build preview per figure, including across skill transitions. Record a source path rather than duplicating supplied data. Keep QA findings in this specification only when persistence is needed; reuse an existing separate ledger if the project already has one.

Update the relevant fields and exports after a change. Do not create numbered prompts, attempt folders, render histories, or an iteration log unless requested. Preserve user inputs and scientific evidence. Resolve repeated failures by changing the relevant structure or rendering approach; do not alter the scientific content to make the layout fit.
