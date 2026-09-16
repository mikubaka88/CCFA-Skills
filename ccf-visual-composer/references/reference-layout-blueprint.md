# Reference-Driven Layout Blueprint

Inspect references before describing them. Translate observable composition into a layout that explains the supplied method; a reference name or a vague request to make it beautiful is insufficient.

## Reference Selection

Use, in order: user-provided references; public figures from relevant papers; then public design examples. Select references by topology, reading direction, aspect ratio, information density, and target venue—not merely by topic or color. Do not upload private manuscripts or unpublished screenshots to an external model without explicit authorization.

For each relevant reference, record observations in the existing specification, distinguishing measurements from estimates. The primary reference governs the overall treatment; each supporting reference serves a specific region or property. A style reference does not supply scientific topology, and a component suitable as a visual reference is not automatically a reusable licensed asset.

```text
Source and provenance:
Why it matches this topology:
Dominant reading path:
Hierarchy and anchor region:
Canvas ratio, approximate panel bounds/proportions, and anchor lines:
Grid, visible edge gaps, padding, repeated icon size, and label baselines:
Grouping and connector routing:
Text-to-visual density:
Useful principles to borrow:
Reference elements to retain or exclude:
```

Attach the actual reference through the host image workflow when it is authorized and useful. For multiple images, identify each by input order and role: layout, object appearance, palette, or existing draft to edit. State which reference governs a conflict. Only include images needed for those roles; do not send the surrounding manuscript or load the entire bundled image collection.

Describe observable geometry rather than a named style: for example, two aligned lanes share a merge column, the contribution occupies the wider middle region, and matching image tiles have equal edge gaps. Express panel bounds as canvas fractions when dimensions differ; then apply the chosen pixel tokens from `visual-contract.md`. A normalized measurement is an estimate unless measured from the source. Keep the method's correct topology when a reference cannot accommodate its branches.

## Layout-First Workflow

1. Freeze the supported node and edge inventory.
2. Choose a content-fit aspect ratio and assign areas to the main transformation and its supporting context. Sketch an internal wireframe with text slots and connectors; do not generate icons yet. Use a renderable skeleton as a tool reference only when exact geometry needs that extra support.
3. Choose a modular grid appropriate to the aspect ratio. Align outer boundaries, repeated box dimensions, text baselines, icon centers, and connector lanes across groups. Fit sizes to final-font text extents; do not default to equal-width columns when explanatory needs differ.
4. Establish one dominant scan path and one visual anchor for the contribution. Use proximity, similarity, continuity, containment, and whitespace to express grouping.
5. Use spacing tokens rather than arbitrary gaps. Keep boxes with equal semantic rank visually consistent; vary size only when information hierarchy justifies it.
6. Route edges before decorating. Reserve lanes for feedback, cross-stage, or supervision edges so they do not cut through labels and icons.
7. Place icon slots after the layout is stable, then apply palette and typography.
8. Inspect the whole-figure bounds and internal gaps, then render at final column width. Resolve accidental empty regions and crowded corners by rearranging supported content. If the mechanism remains unclear, revise its representation or hierarchy before adding decoration.

Boxes are not mandatory. Use containers only for true semantic groups; a sequence may read better as open lanes, a hierarchy as nested regions, and an iterative method as a state-centered loop. Controlled asymmetry is preferable when the scientific contribution is not uniform across stages.

For an overview plus detail view, identify the same object in both places. Use a source-region marker and non-directional detail leaders where needed; do not depict magnification as another computation or data-flow edge. In matrices or repeated frames, share the overview and enlarge only the relevant cells/frames, preserving indices instead of duplicating the full array. Keep legend entries only where the encoding would otherwise be ambiguous.

## Reference Boundaries

Use requested alignment, proportions, spacing, typography, and palette relationships; preserve supplied editable template geometry when requested. Do not transplant unrelated science, captions, logos, or artwork into the new method. Do not use a screenshot as the final background of an allegedly editable figure. Keep source links and credits in the existing specification; method names and output titles describe their function. Deliver a wireframe only when requested; otherwise plan internally. Search additional references only for an unresolved layout decision.

Research basis is registered in `../../ccf-common/references/source-registry.yaml` under `livefigure-editable-scientific-illustration`, `autofigure-edit-editable-svg`, `scifig-editable-figure-generation`, and `astradraw-visual-workflow`; grid and connector guidance also draws on `d2-grid-layout` and `elk-layered-layout`. Reference assets remain in the task cache unless their reuse and publication are authorized.
