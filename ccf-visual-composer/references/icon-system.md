# Icon System

Use icons only when they improve recognition or reduce text. An icon must express one supported concept at final paper size; creativity is useful only when the meaning remains immediate.

## Selection Ladder

1. Use a native diagram primitive for arrows, masks, graphs, trajectories, tensors, databases, and repeated geometric structures when the primitive already communicates the idea.
2. For common concepts, choose one coherent open-source SVG family per figure. Prefer Lucide for restrained line icons; use Material Icons only when its filled or rounded grammar fits the figure better. Record the source, icon name, URL, license, and any modification.
3. Generate a custom icon only for a method-specific concept that cannot be expressed accurately with the chosen family or a native primitive. Do not mix icon families merely for novelty.

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

Generate one icon concept per asset rather than asking an image model to improvise icons inside the whole architecture figure. Request a simple silhouette, few semantic parts, flat color, no lettering, no scene, no texture, no particles, no glow, no pseudo-data, and no decorative circuitry. Inspect the result at its final display size. Reject ambiguous shapes, excess detail, false arrows, accidental labels, duplicated parts, and any visual that implies unsupported method behavior.

If the generator does not return reliable transparency, use a flat high-contrast key background and the installed image-generation workflow's chroma-key removal utility. Inspect alpha edges over both light and dark test backgrounds; remove halos and stray pixels. Keep the original and cleaned icon as separate assets.

## Normalization

- Normalize viewBox, optical size, stroke width, corner radius, and fill/stroke behavior across icons.
- Align icons by optical center, not only bounding-box center.
- Use a small set of icon sizes and preserve a common visual weight.
- Recolor public SVGs through semantic theme colors; do not add gradients or shadows unless the complete figure uses them for meaning.
- Test recognition in grayscale and at final paper size.

## Editable Asset Truthfulness

- Native PowerPoint shapes are fully editable.
- An inserted SVG is scalable and recolorable; piece-level editing may require conversion to Office shapes in a supported PowerPoint version.
- A transparent PNG is independently movable, resizable, replaceable, and croppable, but it is not vector-editable.
- If full vector editability is required for a custom icon, redraw its simple geometry as SVG paths or native shapes. Do not auto-trace a noisy bitmap and label the result cleanly editable.

Deliver an icon manifest with `asset_id`, semantic role, type, source or custom prompt, license, editability level, and file path.

Research basis is registered in `../../ccf-common/references/source-registry.yaml` under `lucide-icons`, `material-icons-svg`, `microsoft-edit-svg-office`, and `livefigure-editable-scientific-illustration`.
