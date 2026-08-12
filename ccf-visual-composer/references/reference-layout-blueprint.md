# Reference-Driven Layout Blueprint

Use references to learn composition, not to copy a figure. The goal is a content-specific layout that inherits useful reading patterns while remaining original and scientifically faithful.

## Reference Selection

Use, in order: user-provided references; public figures from relevant papers; then public design examples. Select references by topology, reading direction, aspect ratio, information density, and target venue—not merely by topic or color. Do not upload private manuscripts or unpublished screenshots to an external model without explicit authorization.

For each reference, record only transferable observations:

```text
Source and provenance:
Why it matches this topology:
Dominant reading path:
Hierarchy and anchor region:
Grid, alignment, and spacing rhythm:
Grouping and connector routing:
Text-to-visual density:
Useful principles to borrow:
Exact features not to copy:
```

## Layout-First Workflow

1. Freeze the supported node and edge inventory.
2. Sketch a low-fidelity wireframe using plain boxes, text slots, and connectors; do not generate icons yet.
3. Choose a modular grid appropriate to the aspect ratio. Align outer boundaries, repeated box dimensions, internal text baselines, icon centers, and connector lanes.
4. Establish one dominant scan path and one visual anchor for the contribution. Use proximity, similarity, continuity, containment, and whitespace to express grouping.
5. Use spacing tokens rather than arbitrary gaps. Keep boxes with equal semantic rank visually consistent; vary size only when information hierarchy justifies it.
6. Route edges before decorating. Reserve lanes for feedback, cross-stage, or supervision edges so they do not cut through labels and icons.
7. Place icon slots after the layout is stable, then apply palette and typography.
8. Render and inspect at final column width. If the page feels generic, revise hierarchy or grouping before adding decoration.

Boxes are not mandatory. Use containers only for true semantic groups; a sequence may read better as open lanes, a hierarchy as nested regions, and an iterative method as a state-centered loop. Controlled asymmetry is preferable when the scientific contribution is not uniform across stages.

## Anti-Imitation Boundary

Do not reproduce a reference's exact node placement, icon set, distinctive palette, proprietary artwork, labels, or decorative signature. Do not use a screenshot as a hidden template or final background. Keep source links in the working provenance record; deliver the new wireframe and the principles distilled from the references.

Research basis is registered in `../../ccf-common/references/source-registry.yaml` under `livefigure-editable-scientific-illustration`, `autofigure-edit-editable-svg`, and `scifig-editable-figure-generation`.
