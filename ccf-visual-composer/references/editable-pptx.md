# Editable PPTX Reconstruction

Use this reference when the user requests PowerPoint. The PPTX is a reconstruction of the approved scientific topology and layout—not a slide containing the generated figure as one background image.

## Editability Levels

Report editability per element:

- `native`: live text, PowerPoint shapes, lines, arrows, connectors, simple graphs, and grouped modules; fully editable in PowerPoint.
- `svg-convertible`: a separate SVG graphic that is scalable and recolorable; supported PowerPoint versions can convert it to Office shapes for piece-level editing.
- `isolated-raster`: a transparent custom icon that is separately movable, resizable, replaceable, and croppable, but not vector-editable.

Prefer `native` for the complete information structure. Use `svg-convertible` for public icons and simple custom vector assets. Use `isolated-raster` only when a method-specific icon is visually valuable and faithful vector reconstruction would materially degrade it.

## Reconstruction Workflow

1. Use the user-requested page size or approved figure aspect ratio. A standalone editable paper figure keeps its content-fit bounds; a requested presentation slide may use 16:9 when no size is specified. Do not add empty slide margins merely to place a paper figure on a slide template.
2. Recreate the approved reference-layout blueprint with the chosen margins, alignment lines, and spacing tokens from `visual-contract.md`. Convert design coordinates once with `slide_inches / canvas_pixels`; set native font sizes in points using the same scale. Use the selected Times New Roman or Comic Sans MS family unless the user/venue specifies another, and check for substitution before export.
3. Build stages, boxes, nodes, labels, arrows, and connectors as native objects. Keep text live and connectors anchored where the authoring library permits.
4. Group objects by semantic module, use stable z-order, and give groups or assets meaningful names in the accompanying element map.
5. Insert public icons as separate SVG assets. Build simple method-specific icons from native shapes or SVG paths; use a cleaned transparent PNG only for custom icons whose intended appearance cannot be preserved otherwise.
6. Never place the generated whole-figure raster as the final slide background. It may be used temporarily as a visual comparison layer and must be removed or hidden before delivery.
7. Prefer deterministic generation with PptxGenJS when available because it supports native shapes, text, connectors, SVG assets, and reproducible coordinates. Another PowerPoint library is acceptable if the same editability contract is met.
8. Render the PPTX to a preview image or PDF and inspect it. Validate that there is no full-slide raster, live text remains searchable, key objects are separately selectable, and source icon files are present.

For an existing semantic SVG, the MIT-licensed `svg2pptx` converter is an available deterministic native-object route. Validate the installed version on a representative sample before batch conversion. Normalize percentage-only root dimensions to the numeric `viewBox` width and height in a separate conversion source, preserve the original SVG, and record the conversion. Its gradients, filters, and Bezier approximation are limitations to inspect in the rendered PPTX; reconstruct affected elements with native shapes when the converted slide diverges materially. A successful file write alone is insufficient: inspect shape counts, live-text counts, picture-shape counts, slide bounds, and a rendered preview.

## Delivery Package (Requested Formats And Necessary Sources Only)

```text
figure.pptx
build/preview.png or build/preview.pdf
assets/icons/*.svg or *.png
source/figure.js or the existing authoring source
source/spec.md  # only when continuing/reproducing the figure needs it
figure.svg and figure.pdf when requested
```

Keep dimensions, semantic groups, fonts, palette, icon provenance/editability, and material limitations in the authoring source or existing specification. Preserve source SVG assets used by the authoring code. Reuse an existing element map or manifest; create a separate one only when requested or required by downstream tooling. Normalize converter input under `build/`, update it in place, and preserve the canonical original SVG. A local correction updates the authoring source and dependent requested formats without another concept-generation pass.

Resolve a selected object from the actual current source and slide, using stable group/shape names or native IDs when available. Screenshot annotations are location hints, not native object IDs. Before replacing an export, check whether the user manually changed it since the source/export pair was last inspected; preserve and reconcile those edits instead of overwriting them from stale source. Move attached connector endpoints with their object and keep unaffected groups fixed. Reuse the current source record for any identity/version notes rather than adding a mandatory tracking file.

## PPTX QA

- Repeated modules align to common baselines and use consistent spacing.
- Text does not overflow or reflow after rendering.
- Connectors terminate at the intended objects and remain behind labels.
- Transparent icons have clean edges and no background rectangle or fringe.
- Public and custom icons share optical size, stroke/fill weight, and palette.
- The slide remains understandable when icons are temporarily hidden; icons support meaning rather than carry undocumented information.
- The preview and editable source express the same topology, labels, and hierarchy.

Research basis is registered in `../../ccf-common/references/source-registry.yaml` under `livefigure-editable-scientific-illustration`, `pptxgenjs-shapes`, `microsoft-edit-svg-office`, and `svg2pptx-native-shapes`.
