# Editable PPTX Reconstruction

Use this reference when the user requests PowerPoint. The PPTX is a reconstruction of the approved scientific topology and layout—not a slide containing the generated figure as one background image.

## Editability Levels

Report editability per element:

- `native`: live text, PowerPoint shapes, lines, arrows, connectors, simple graphs, and grouped modules; fully editable in PowerPoint.
- `svg-convertible`: a separate SVG graphic that is scalable and recolorable; supported PowerPoint versions can convert it to Office shapes for piece-level editing.
- `isolated-raster`: a transparent custom icon that is separately movable, resizable, replaceable, and croppable, but not vector-editable.

Prefer `native` for the complete information structure. Use `svg-convertible` for public icons and simple custom vector assets. Use `isolated-raster` only when a method-specific icon is visually valuable and faithful vector reconstruction would materially degrade it.

## Reconstruction Workflow

1. Set the user-requested page size; otherwise use a standard 16:9 canvas and record dimensions.
2. Recreate the approved reference-layout blueprint on a modular grid with explicit margins, alignment lines, and spacing tokens.
3. Build stages, boxes, nodes, labels, arrows, and connectors as native objects. Keep text live and connectors anchored where the authoring library permits.
4. Group objects by semantic module, use stable z-order, and give groups or assets meaningful names in the accompanying element map.
5. Insert public icons as separate SVG assets. Build simple method-specific icons from native shapes or SVG paths; use a cleaned transparent PNG only for custom icons whose intended appearance cannot be preserved otherwise.
6. Never place the generated whole-figure raster as the final slide background. It may be used temporarily as a visual comparison layer and must be removed or hidden before delivery.
7. Prefer deterministic generation with PptxGenJS when available because it supports native shapes, text, connectors, SVG assets, and reproducible coordinates. Another PowerPoint library is acceptable if the same editability contract is met.
8. Render the PPTX to a preview image or PDF and inspect it. Validate that there is no full-slide raster, live text remains searchable, key objects are separately selectable, and source icon files are present.

For an existing semantic SVG, the MIT-licensed `svg2pptx` converter is an available deterministic native-object route. Validate the installed version on a representative sample before batch conversion. Normalize percentage-only root dimensions to the numeric `viewBox` width and height in a separate conversion source, preserve the original SVG, and record the conversion. Its gradients, filters, and Bezier approximation are limitations to inspect in the rendered PPTX; reconstruct affected elements with native shapes when the converted slide diverges materially. A successful file write alone is insufficient: inspect shape counts, live-text counts, picture-shape counts, slide bounds, and a rendered preview.

## Delivery Package

```text
figure.pptx
preview.png or preview.pdf
assets/icons/*.svg or *.png
icon-manifest.yaml
element-map.md
figure.svg and figure.pdf when requested
```

The element map identifies slide dimensions, semantic groups, fonts, palette, icon editability levels, and any unavoidable limitation. Preserve source SVGs even when they are also inserted into the PPTX.

## PPTX QA

- Repeated modules align to common baselines and use consistent spacing.
- Text does not overflow or reflow after rendering.
- Connectors terminate at the intended objects and remain behind labels.
- Transparent icons have clean edges and no background rectangle or fringe.
- Public and custom icons share optical size, stroke/fill weight, and palette.
- The slide remains understandable when icons are temporarily hidden; icons support meaning rather than carry undocumented information.
- The preview and editable source express the same topology, labels, and hierarchy.

Research basis is registered in `../../ccf-common/references/source-registry.yaml` under `livefigure-editable-scientific-illustration`, `pptxgenjs-shapes`, `microsoft-edit-svg-office`, and `svg2pptx-native-shapes`.
