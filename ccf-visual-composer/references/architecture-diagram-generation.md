# Scientific Architecture Diagram Generation

Use this reference for method, model, framework, system, workflow, dataflow, and training/inference architecture figures. Do not use image generation for ordinary numeric plots that should remain code- and data-reproducible.

## 1. Build The Diagram Specification

Extract only content supported by the user's manuscript, notes, code, equations, or explicit description:

```text
Figure purpose:
Single-sentence scientific takeaway:
Target venue and final column width:
Reader scan path: left-to-right / top-to-bottom / cyclic / hierarchical
Inputs and outputs:
Ordered stages:
Named modules and submodules:
Typed connections: data / control / supervision / gradient / retrieval / feedback
Training-only versus inference-only elements:
Novel contribution to emphasize:
Exact short labels:
Required equations or symbols:
Evidence-grounded visual encodings:
Unknown or unsupported elements:
Desired deliverables: raster draft / editable SVG / vector PDF
```

Resolve ambiguity before drawing when it changes topology or scientific meaning. For minor visual choices, make a conservative assumption and record it. Never add a plausible-looking module merely to balance the composition.

## 2. Choose A Scientific Visual Grammar

Match the layout to the method rather than defaulting to generic boxes:

- Sequential pipeline: aligned stages with one dominant reading direction.
- Hierarchical model: nested containers with clear parent-child boundaries.
- Multi-branch or multi-modal method: synchronized lanes that visibly merge at the correct operation.
- Iterative/agentic system: a loop with an explicit state, stop condition, and feedback edge.
- Training versus inference: two labeled zones or lanes; do not imply that training-only supervision exists at inference.
- Retrieval/memory system: distinguish query, store/index, retrieval result, and downstream consumer.
- Before/after or baseline/proposed comparison: matched geometry so the changed mechanism is visually isolated.

Use one anchor idea, restrained depth, consistent geometry, and whitespace. Reserve the strongest accent color for the paper's actual novelty. Avoid decorative 3D rendering, glossy UI cards, irrelevant people/robots, ornamental circuitry, fake charts, and ambiguous arrows.

## 3. Write A Content-Derived GPT Image 2 Prompt

Write a new prompt from the diagram specification. Do not reuse a generic “beautiful AI architecture” prompt. Include these blocks in this order:

```text
ROLE AND OUTPUT
Create a publication-grade scientific architecture diagram for [field/task], suitable for [venue] at [single-column/full-width] size and [aspect ratio].

SCIENTIFIC MESSAGE
The figure must communicate: [single takeaway].

STRUCTURE AND READING ORDER
[Exact spatial arrangement, zones, lanes, hierarchy, stages, and panel structure.]

COMPONENTS
[Every supported module with its exact short display label and visual role.]

CONNECTIONS
[Every directed/undirected edge, source, target, semantic type, and line style.]

VISUAL ENCODING
[Color semantics, shapes, grouping, novelty highlight, training/inference distinction, legend needs.]

STYLE
Clean scientific vector-illustration aesthetic; flat shapes; precise alignment; generous whitespace; restrained accessible palette; consistent stroke widths; no photorealism; no unnecessary decoration.

TYPOGRAPHY
Use only these exact short labels after title-case normalization: [label list]. Capitalize only the first letter of every displayed English word and keep the remaining letters lowercase. Never use all-caps text; write `Visual Composer`, `Gpt Image 2`, and `Editable Svg/Pdf`, not `VISUAL COMPOSER`, `GPT IMAGE 2`, or `EDITABLE SVG/PDF`. Keep text horizontal, high-contrast, and large enough at final paper size. Do not invent or paraphrase labels. If exact text cannot be rendered reliably, leave a clean label slot for later vector reconstruction.

OUTPUT CONSTRAINTS
[Aspect ratio/resolution/background.] Preserve margins. Keep arrows unambiguous and prevent crossings where possible.

NEGATIVE CONSTRAINTS
No unsupported components, fake metrics, fabricated equations, logos, watermarks, UI chrome, illegible microtext, random icons, decorative gradients, 3D effects, or unlabeled flows.
```

Favor short labels of one to five words. Put long explanations in the caption, not inside the generated figure. When equations or exact typography are essential, reserve clean slots and add them during editable reconstruction.

Before showing or sending the prompt, normalize the complete visible-text inventory to title case. This visible-image rule applies to titles, module names, legends, annotations, badges, axis labels, and table headers. Keep canonical model or acronym spelling outside the image in prose, captions, filenames, and metadata when needed. Do not silently return to all caps for emphasis; use weight, size, color, or spacing instead.

## 4. Required GPT Image 2 Confirmation Gate

Before calling an external image model, show the diagram summary and the complete prompt. Then ask:

> 架构图内容与生成 prompt 已准备好。是否现在调用 GPT Image 2 生成架构图草案？

The user explicitly saying in the current request to call/use GPT Image 2 counts as approval; a general request to “make a diagram” does not. On approval, follow the host's image-generation skill/tool instructions and use the available image-generation capability that is identified as GPT Image 2. If no such capability is available or the backend identity cannot be verified, preserve the prompt, state the limitation, and offer a deterministic SVG-first route. Never claim that an unknown backend was GPT Image 2.

For private manuscripts, unpublished methods, or confidential results, minimize the prompt to the structural content needed for the figure. Show the complete outbound prompt before confirmation; do not upload the full manuscript, source tree, private result files, reviewer text, author identities, or unrelated proprietary details. The confirmation authorizes only the shown prompt and any explicitly listed reference images, not hidden additional material.

## 5. Inspect The Generated Draft

Inspect the generated image rather than assuming prompt compliance. Compare it with the diagram specification and record:

- missing, duplicated, invented, or renamed modules;
- incorrect arrow direction, topology, training/inference boundary, or grouping;
- unreadable or hallucinated labels/equations;
- any all-caps English word or label that violates the required title-case display rule;
- inconsistent visual encoding or novelty emphasis;
- paper-size readability, contrast, whitespace, and crop safety.

Revise the prompt and regenerate only when the scientific structure or legibility is materially wrong. Preserve approved structure across iterations.

## 6. Mandatory Post-Generation Question

After every successful architecture-image generation, ask this question even if the user did not previously mention vector output:

> 架构图草案已生成。是否需要我把它重建为可编辑的 SVG，并同时导出矢量 PDF？

Do not begin vector reconstruction until the user agrees. If the user requests only one format, create only that format plus any minimal intermediate source required for a correct conversion.

## 7. Editable SVG/PDF Reconstruction

On agreement, use the generated image as a visual reference, not as the final vector payload:

1. Reconstruct modules as named SVG groups with editable rectangles, paths, icons, and connectors.
2. Replace rasterized or malformed labels with live text; keep a text inventory so spelling matches the manuscript.
3. Give arrowheads, line styles, colors, and group boundaries explicit semantic roles.
4. Preserve equations as editable text where practical; otherwise use a separately replaceable vector/text object and disclose the limitation.
5. Keep any unavoidable raster element isolated in its own clearly named layer. Do not embed the whole raster in an SVG and call it editable.
6. Export PDF from the reconstructed vector source so shapes and text remain vector objects where the converter permits. State that editability depends on the downstream PDF editor; SVG is the canonical editable source.
7. Deliver the original generated draft, the canonical SVG, the PDF when requested, and a short layer/text map.

Use a deterministic vector-first route instead of image generation when the user initially requires strict editability, exact equations, dense labels, or pixel-stable reproducibility and does not want a raster concept pass.

## 8. Architecture QA

- Every module and connection is traceable to supplied content.
- Reading order is obvious within two seconds at final paper size.
- Arrow direction and line semantics are consistent and explained when non-obvious.
- Training-only, inference-only, optional, and repeated components are distinguishable.
- Novelty emphasis matches the manuscript rather than decorative salience.
- Labels match the manuscript terminology exactly.
- Every displayed English word uses title case with only its first letter capitalized; no all-caps styling remains.
- SVG objects are individually selectable and text remains editable.
- The PDF is exported from vector source, not from a flattened screenshot.
- Raster draft and reconstructed vector tell the same scientific story.
