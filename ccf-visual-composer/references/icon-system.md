# Icon System

Use icons only when they improve recognition or reduce text. An icon must express one supported concept at final paper size; creativity is useful only when the meaning remains immediate.

## Selection Ladder

1. Reuse an approved component from this project's existing figure/source when its meaning, treatment, and reuse rights fit. Keep its stable asset ID, live label, ports, and source path; do not import an entire external pack or create a separate component library for one figure.
2. Use a native diagram primitive for arrows, masks, graphs, trajectories, tensors, databases, and repeated geometric structures when it already communicates the idea.
3. Search a relevant public SVG source for an unmet object: Lucide or Material Icons for general concepts, and Bioicons for recognizable biological/chemical structures or instruments. Inspect the actual object and its individual license; a collection's availability does not give every asset the same terms. Record author/source, asset name/URL, license, required attribution, and modifications in the existing specification. Preserve scientifically meaningful parts while matching optical weight and palette.
4. Generate a method-specific object when suitable primitives or permitted assets do not explain it. Keep one coherent treatment and search only for the required object; no additional dependency or asset-generation call is needed for an already suitable component.

## Custom Icon Micro-Spec

Before generation, write:

```text
Concept and scientific role:
One must-read visual metaphor:
Required silhouette and invariant detail:
Forbidden or misleading detail:
Target size and aspect ratio:
Stroke/fill grammar and palette:
Background: transparent or flat removable key color
Output: one isolated icon, no text
```

In an initial whole-figure draft, let GPT Image render scientific objects inside specified slots with a shared viewpoint and treatment. For a reusable custom icon or editable reconstruction, isolate one concept per canonical asset; do not require an extra generation call for every already suitable icon. Reuse repeated objects instead of independently redrawing them.

Request a recognizable silhouette and a few meaningful details, without lettering or pseudo-data. Flat vector-like objects suit compact paper figures; restrained depth, material, or soft shading may help explain spatial structure when used consistently. Avoid decorative glow, particles, circuitry, noisy texture, and scene backgrounds in icon slots. Supplied evidence images keep their actual content. Inspect each object at final display size; reject ambiguous forms, false arrows, accidental labels, duplicated parts, or unsupported behavior.

If the generator does not return reliable transparency, use a flat high-contrast key background and the installed image-generation workflow's chroma-key removal utility. Inspect alpha edges over both light and dark test backgrounds; remove halos and stray pixels. Retain one cleaned canonical asset. Keep its generated source only when needed to reproduce the cleanup, under the same working directory; do not retain every failed candidate.

## Normalization

- Normalize viewBox, optical size, stroke width, corner radius, and fill/stroke behavior across icons.
- Align icons by optical center, not only bounding-box center.
- Use a small set of icon sizes and preserve a common visual weight.
- Use the chosen icon slots and edge-gap tokens from `visual-contract.md`; align caption baselines and balance optical size within those slots. Preserve viewpoint, line treatment, and detail level across repeated objects.
- Recolor public SVGs through semantic theme colors; do not add gradients or shadows unless the complete figure uses them for meaning.
- Test recognition in grayscale and at final paper size.

## Editable Asset Truthfulness

- Native PowerPoint shapes are fully editable.
- An inserted SVG is scalable and recolorable; piece-level editing may require conversion to Office shapes in a supported PowerPoint version.
- A transparent PNG is independently movable, resizable, replaceable, and croppable, but it is not vector-editable.
- If full vector editability is required for a custom icon, redraw its simple geometry as SVG paths or native shapes. Do not auto-trace a noisy bitmap and label the result cleanly editable.

Reuse an existing suitable icon before searching or generating another. Keep `asset_id`, semantic role, source/license, editability, and canonical path in the existing specification or source comments. Deliver a separate icon manifest only when requested or required for the package. Reuse the same asset across SVG/PDF/PPTX exports.

Research basis is registered in `../../ccf-common/references/source-registry.yaml` under `lucide-icons`, `material-icons-svg`, `bioicons`, `microsoft-edit-svg-office`, `livefigure-editable-scientific-illustration`, and `astradraw-visual-workflow`.
