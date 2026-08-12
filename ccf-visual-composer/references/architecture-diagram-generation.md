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
Canonical acronym expansions, or acronym-only locks:
Required equations or symbols:
Evidence-grounded visual encodings:
Unknown or unsupported elements:
Desired deliverables: raster draft / editable SVG / vector PDF / editable PPTX
```

Resolve ambiguity before drawing when it changes topology or scientific meaning. For minor visual choices, make a conservative assumption and record it. Never add a plausible-looking module merely to balance the composition.

## 2. Choose A Scientific Visual Grammar

First classify the destination using `paper-vs-presentation-diagrams.md`. For a paper method figure, scientific structure takes priority over explanatory presentation. Show representations and transformations directly; do not translate the method into a slide deck of stage cards. Use slide or poster grammar only when that is the explicit destination.

Match the layout to the method rather than defaulting to generic boxes:

- Sequential pipeline: aligned stages with one dominant reading direction.
- Hierarchical model: nested containers with clear parent-child boundaries.
- Multi-branch or multi-modal method: synchronized lanes that visibly merge at the correct operation.
- Iterative/agentic system: a loop with an explicit state, stop condition, and feedback edge.
- Training versus inference: two labeled zones or lanes; do not imply that training-only supervision exists at inference.
- Retrieval/memory system: distinguish query, store/index, retrieval result, and downstream consumer.
- Before/after or baseline/proposed comparison: matched geometry so the changed mechanism is visually isolated.

Use one anchor idea, restrained depth, consistent geometry, and whitespace. Reserve the strongest accent color for the paper's actual novelty. Avoid decorative 3D rendering, glossy UI cards, irrelevant people/robots, ornamental circuitry, fake charts, and ambiguous arrows.

For a paper figure, require a representation-to-operation map before prompting:

```text
Raw inputs:
Intermediate representations:
Operators acting on each representation:
Branch points and their scientific reason:
Merge points and their operation:
Final representation and consumer:
Caption-only explanations removed from the canvas:
```

If this map cannot be completed from the source, the figure specification is not ready. Do not compensate with numbered stages, large headings, descriptive cards, or generic icons.

When icons are useful, load `icon-system.md` and freeze an icon inventory before the full-figure prompt. Pass approved custom icon assets as references only when the user authorized those assets for the external call and the backend supports reference images; otherwise reserve clean icon slots and insert the assets during editable reconstruction. Do not rely on the whole-figure model to redraw a custom icon consistently.

## 3. Shape The GPT Image 2 Prompt Proportionally

Load `adaptive-architecture-style.md` and apply its prompt-specificity ladder before writing. Prompt intervention must be proportional to missing information:

- For a detailed user prompt, preserve it verbatim and append only the compact `Style refinement` suffix. Do not translate, reorder, or restate its modules and constraints.
- For a partial prompt, retain supplied wording and add only scientifically necessary missing relationships or output constraints.
- For a manuscript or notes, write a new prompt from the diagram specification. Do not reuse a generic architecture prompt or expose manuscript text beyond the structural content required for the figure.

For manuscript-derived or materially incomplete inputs, use these blocks in this order:

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
Use only these exact short labels after capitalization normalization: [label list]. Use natural title or sentence case for ordinary English, but preserve canonical uppercase acronyms and initialisms. Write `Visual Composer`, `GPT Image 2`, `Structure QA`, and `Editable SVG/PDF/PPTX`, not `VISUAL COMPOSER`, `Gpt Image 2`, `Structure Qa`, or `Editable Svg/Pdf/Pptx`. Keep `CCF`, `AI`, `GPT`, `QA`, `SVG`, `PDF`, `PPTX`, `PNG`, and comparable standardized abbreviations uppercase. Keep text horizontal, high-contrast, and large enough at final paper size. Do not invent or paraphrase labels. If exact text cannot be rendered reliably, leave a clean label slot for later reconstruction.

OUTPUT CONSTRAINTS
[Aspect ratio/resolution/background.] Preserve margins. Keep arrows unambiguous and prevent crossings where possible.

NEGATIVE CONSTRAINTS
No unsupported components, fake metrics, fabricated equations, logos, watermarks, UI chrome, illegible microtext, random icons, decorative gradients, 3D effects, or unlabeled flows.
```

Favor short labels of one to five words. Put long explanations in the caption, not inside the generated figure. When equations or exact typography are essential, reserve clean slots and add them during editable reconstruction.

For every visible acronym, either provide its exact source-verified expansion or instruct the model to display the acronym only. Do not permit plausible expansion. Treat a wrong expansion as a label-accuracy failure even when the topology is correct.

For every condition, choose at most three content-fit style principles from `adaptive-architecture-style.md`. Do not force macro/meso/micro hierarchy, phase zones, pastel cards, screenshots, or micro-insets when the method topology does not need them. For an already detailed prompt, the final outbound prompt should remain dominated by the user's original wording; exceeding the compact augmentation budget is a QA failure unless factual ambiguity requires resolution.

Before showing or sending the prompt, normalize the complete visible-text inventory to natural title or sentence case. Preserve canonical uppercase acronyms and initialisms inside the image as well as in prose, captions, filenames, and metadata. Do not use all caps for an entire ordinary phrase merely for emphasis; use weight, size, color, or spacing instead.

## 4. Default GPT Image 2 Generation

For method, architecture, system, pipeline, framework, and illustrative scientific diagrams, a user request to create the diagram selects GPT Image 2 as the default first-pass renderer. Show the diagram summary and complete prompt as useful provenance, but do not pause for a redundant pre-generation confirmation unless a private-material boundary requires a narrower outbound prompt. Follow the host image-generation instructions and use only a capability identified as GPT Image 2.

Use pure SVG/code-first generation only when the user explicitly says not to use GPT Image 2 or explicitly asks for pure SVG/code-first output. Label that route and all resulting benchmark/report entries as `pure SVG generation`; do not present it as GPT Image 2 output. If GPT Image 2 is unavailable or its backend identity cannot be verified, preserve the prompt and state the limitation. Do not silently substitute another image model or silently fall back to SVG.

For private manuscripts, unpublished methods, or confidential results, minimize the prompt to the structural content needed for the figure. Show the complete outbound prompt and request confirmation only when sending even the minimized structure would cross a privacy boundary not already authorized by the user. Do not upload the full manuscript, source tree, private result files, reviewer text, author identities, or unrelated proprietary details. Authorization covers only the shown prompt and explicitly listed reference images, not hidden additional material.

## 5. Inspect The Generated Draft

Inspect the generated image rather than assuming prompt compliance. Compare it with the diagram specification and record:

- missing, duplicated, invented, or renamed modules;
- incorrect arrow direction, topology, training/inference boundary, or grouping;
- unreadable or hallucinated labels/equations;
- any all-caps ordinary English phrase or incorrectly lowercased acronym that violates the capitalization rule;
- inconsistent visual encoding or novelty emphasis;
- paper-size readability, contrast, whitespace, and crop safety.

Revise the prompt and regenerate only when the scientific structure or legibility is materially wrong. Preserve approved structure across iterations.

## 6. Mandatory Post-Generation Question

After every successful architecture-image generation, ask this question even if the user did not previously mention vector output:

> 架构图草案已生成。是否需要我将它重建为可编辑的 SVG、矢量 PDF 或可编辑 PPTX？你可以选择一种或多种格式。

Do not begin reconstruction until the user agrees. If the user requests only one format, create only that format plus any minimal intermediate source required for a correct conversion.

## 7. Editable SVG/PDF/PPTX Reconstruction

On agreement, use the generated image as a visual reference, not as the final vector payload:

1. Reconstruct modules as named semantic groups with editable rectangles, paths, icons, and connectors.
2. Replace rasterized or malformed labels with live text; keep a text inventory so spelling matches the manuscript.
3. Give arrowheads, line styles, colors, and group boundaries explicit semantic roles.
4. Preserve equations as editable text where practical; otherwise use a separately replaceable vector/text object and disclose the limitation.
5. Keep any unavoidable raster element isolated in its own clearly named layer or PowerPoint object. Do not embed the whole raster in an SVG or use it as a full-slide PowerPoint background and call it editable.
6. Export PDF from the reconstructed vector source so shapes and text remain vector objects where the converter permits. State that editability depends on the downstream PDF editor; SVG is the canonical editable source.
7. For PPTX, load `editable-pptx.md`: use live text, native shapes and connectors for the layout; keep each custom icon as a separate transparent or vector asset; disclose whether each icon is native-shape editable, SVG-convertible, or raster-movable only.
8. Deliver the original generated draft, requested editable formats, source icon assets, an icon manifest, and a short layer/text map.

Do not infer an opt-out merely from strict editability, exact equations, dense labels, or reproducibility needs. Generate the GPT Image 2 concept first, then reconstruct exact text, equations, topology, and editable objects after user confirmation. Use deterministic vector-first generation only when the user explicitly rejects the raster concept pass or explicitly requests pure SVG/code-first output.

## 8. Architecture QA

Run the paper-mechanism acceptance gate in `paper-vs-presentation-diagrams.md` before the checks below whenever the destination is a paper. A visually clean result that reads as a slide, poster, README infographic, or product workflow still fails paper QA.

- Every module and connection is traceable to supplied content.
- Reading order is obvious within two seconds at final paper size.
- Arrow direction and line semantics are consistent and explained when non-obvious.
- Training-only, inference-only, optional, and repeated components are distinguishable.
- Novelty emphasis matches the manuscript rather than decorative salience.
- Labels match the manuscript terminology exactly.
- Ordinary English uses natural title or sentence case, while canonical acronyms and initialisms remain uppercase.
- SVG objects are individually selectable and text remains editable.
- The PDF is exported from vector source, not from a flattened screenshot.
- PPTX text, boxes, nodes, arrows, and connectors are native objects; the slide is not a flattened image.
- Common icons come from a coherent licensed family; custom icons are separate, background-free, semantically accurate assets without noise or invented detail.
- Raster draft and reconstructed vector tell the same scientific story.
- Detailed user prompts remain verbatim, with augmentation inside the compact specificity budget.
- The layout is derived from the current method rather than a fixed or observed figure template.
- Acronym expansions match the source exactly, or the figure uses the acronym alone.
