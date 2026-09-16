# Scientific Architecture Diagram Generation

Use this reference for new method, model, system, framework, dataflow, or training/inference diagrams, and the relevant reconstruction sections for editable delivery. Numerical plots stay code- and data-reproducible. Updating an existing editable source does not require a new image-generation pass.

## 1. One Diagram Specification

Reuse the visual contract or source specification. Extract only supported method content, without producing a second overlapping document:

```text
Purpose and scientific takeaway:
Final size / destination / requested formats:
Inputs, representations, operators, and outputs:
Modules, groups, branches, merges, and typed connections:
Training/inference boundaries, supervision, and iteration:
Contribution emphasis and evidence-backed encodings:
Exact short labels, equations, and acronym handling:
Reading path / layout / existing assets:
Design canvas, panel bounds, alignment anchors, and spacing tokens:
Primary font, final-size label scale, and illustration treatment:
Source locations and unresolved scientific information:
```

Resolve an unknown before drawing only when it changes topology or meaning. Make routine visual choices from context. Never add components to balance a composition. Keep canonical acronym expansions from the source; otherwise use the acronym alone. Long explanations belong in the caption, not inside the figure.

## 2. Content-Fit Visual Grammar

For a paper, apply `paper-vs-presentation-diagrams.md`: show scientific objects and computations instead of explanatory stage cards. Use presentation or outreach grammar when that is the destination.

| Topology | Suitable layout |
| --- | --- |
| Sequential stages | Compact aligned flow; place a local expansion beside its parent operation instead of extending the whole canvas. |
| Hierarchy | Nested semantic groups with explicit containment. |
| Multiple branches/modalities | Aligned lanes with shared entry/exit anchors, consistent label baselines, and the actual integration point. |
| Iteration or agents | State, loop direction, stop condition, and feedback edge. |
| Training versus inference | Clearly distinguished paths; no inference-time training supervision. |
| Retrieval or memory | Query, storage/index, retrieved content, and consuming operator. |
| Before/after or baseline/proposed | Matched common geometry, emphasizing the changed mechanism. |

Use representations, tensors, graphs, frames, or trajectories only when grounded in the method. Load `reference-layout-blueprint.md` only for actual reference-based composition. Reuse established layout and style for an update.

For a new design, choose one applicable preset from `adaptive-architecture-style.md`. Allocate compact panel areas after establishing the final-size type scale. Keep scientific node/edge relationships separate from presentation groups: visual adjacency is not a connection, and a detail inset is not a repeated execution. Check whole-figure occupied bounds before asking the image model to elaborate objects.

## 3. Prompt Specificity

For a detailed user prompt, preserve it and append only genuinely missing refinement. Follow `adaptive-architecture-style.md`: local edits need a delta; a layout redesign needs sufficient geometry and typography, without an arbitrary word ceiling. A partial prompt needs missing scientific relationships or output constraints; manuscript-only input needs a content-derived prompt. Resolve the layout and font tokens from `visual-contract.md` once, then include their chosen values rather than the whole reference document.

Use the following compact structure for a new prompt, merging empty or redundant blocks:

```text
OUTPUT: Destination, final size/aspect ratio, background, and scientific takeaway.
REFERENCES: Input image order and role; observed layout relationships to retain or adapt.
STRUCTURE: Supported modules, representations, operations, reading order, and groups.
CONNECTIONS: Exact source/target relationships, directions, and semantic line types.
LAYOUT: Content-fit aspect ratio, nominal canvas, compact panel bounds, shared baselines/edges across blocks, chosen gaps, padding, icon slots, and reserved connector lanes.
ENCODING: Contribution emphasis, training/inference distinctions, semantic palette roles with hex values.
TEXT: Only the quoted visible-label inventory and necessary equations; exact primary font, final-size label scale, weight, and placement.
ILLUSTRATIONS: Scientific objects, viewpoint, coherent detail/material treatment, and invariants across repeated assets; keep them inside the planned slots.
CONSTRAINTS: Preserve the specified science; no invented components, metrics, equations, or acronym expansions; no watermarks, illegible microtext, or decorative flows.
```

Use natural sentence/title case for ordinary text and preserve canonical uppercase acronyms. Do not render prompt headings, spacing measurements, explanatory prose, or extra numbers as figure labels. Treat coordinates as generation targets, not proof of exact geometry. Allow visual invention in faithful scientific objects and local detail while keeping labels, topology, positions, and palette roles stable. Do not repeat the same inventory in several blocks. Preserve user-required wording and image-tool input requirements.

## 4. Authorized Default Generation

For a new architecture concept, use the verified GPT Image 2 capability unless the user requests pure SVG/code-first or opts out. Follow the host image-generation instructions. If the backend is unavailable or cannot be identified, state the limitation and retain the usable specification; do not silently substitute another backend or mislabel pure SVG output.

A diagram request authorizes its necessary generation stage. Show a brief diagram summary when useful; do not repeat the full outbound prompt in chat unless requested or needed for approval/provenance. For private content, follow `../../ccf-common/references/privacy-and-evidence.md`: minimize inputs to required structure and use only authorized references. Ask about the exact minimized prompt and images only when transfer crosses an unapproved boundary. Do not send the full manuscript or unrelated identities, reviews, source trees, or result files.

Generate one complete candidate by default. Requested alternatives may share the same verified specification and assets. An existing source change, additional export, or local edit does not restart this default concept stage.

Use the requested or content-derived aspect ratio and an adequate canvas when the host exposes size controls. Do not default to 1:1 or to a single landscape size. The 1536 px width in the spacing guide is a scaling reference, not an aspect-ratio requirement. When quality controls are exposed, use medium/high for a detailed final diagram; low is appropriate for an explicitly rough composition check. Do not invent unavailable tool parameters. GPT Image 2 already uses high input fidelity; do not pass an unsupported `input_fidelity` option. Follow current host capabilities for transparency and dimensions.

## 5. Inspect And Correct The Draft

Compare the actual rendered draft with the specification: missing/invented/renamed modules, edge direction and semantics, training/inference boundaries, exact labels/acronyms, equations, contribution emphasis, crop safety, and final-size legibility.

Inspect the whole figure for hierarchy and balance, then its final-size labels and illustration details. Compare repeated gaps, row alignment, icon optical sizes, and text density with the contract. Correct specific defects with a local request such as aligning the named row or removing a duplicated label; explicitly preserve accepted topology, text, colors, and surrounding objects. Raster-only delivery still requires repairing malformed text through the image-editing workflow; do not leave a known defect for an unrequested future SVG.

If scientific composition is wrong, make a targeted correction to the prompt or image using the host workflow. If editable reconstruction is already requested and the composition is usable, repair labels, equations, alignment, and local geometry in the vector/native source instead of regenerating a whole raster to fix typography. Preserve accepted topology, layout, and reusable icons.

After two unsuccessful corrections of the same defect, diagnose the failure and change the relevant strategy. For example, route a connector differently, separate true semantic groups, or rebuild malformed text in the requested editable source. Do not lower scientific accuracy, discard a requested format, or accept an unreadable figure to satisfy an attempt budget.

## 6. Requested Editable Deliverables

If editable SVG, vector PDF, PPTX, or reconstruction was requested, continue without asking again. A later local correction preserves that format request. When reconstruction is additional work beyond a raster-only request, offer it once after delivering the raster and wait only for that optional work.

Create only requested formats and the minimum reusable source needed for them. Follow `../../ccf-common/references/artifact-contracts.md`: one stable working directory per figure, one current source/specification, reusable assets, and current build preview. Preserve explicit existing paths; do not save parallel contract/prompt/inventory files with repeated content.

## 7. Semantic Reconstruction

1. Rebuild modules as named selectable vector/native groups and typed connectors. Keep labels as live text matching the scientific inventory.
2. Preserve equations as editable text where practical, or as separately replaceable vector objects with the limitation stated.
3. Keep an unavoidable raster element isolated and identified. A full-image background, embedded raster, or noisy auto-trace is not semantic editability.
4. Export requested vector PDF from the canonical vector source. Keep SVG as the editable source when it is the authoring format; downstream PDF editability depends on the editor.
5. For PPTX, use `editable-pptx.md`: native layout/text/connectors, separately selectable icons, and honest native/SVG-convertible/raster editability. Reuse a supplied editable SVG when suitable instead of rebuilding its geometry from a preview.
6. Preserve necessary reusable source and assets. Record provenance and element semantics in the existing source/specification; a separate manifest or element map is needed only when requested or required by a converter/package.
7. For later changes, edit the canonical source, refresh dependent requested exports, and inspect the affected result. Retain the last usable artifact if a replacement fails; mark any export that is not current.

Strict editability alone does not opt out of the default raster concept for a new figure. Explicit pure SVG/code-first uses deterministic generation immediately. These defaults do not force a new raster pass for an existing editable figure.

## 8. Applicable QA

Use the shared `render-qa.md` checks for the requested output only. A paper mechanism figure must expose its representations and computation; presentation decoration must not replace scientific structure. Confirm that all delivered formats communicate the same data, topology, labels, and hierarchy. Inspect vector/native editability for requested editable formats and actual rendered appearance at final size. A successful export or XML parse alone does not verify either scientific correctness or visual quality.

Official capability and prompting references are registered in `../../ccf-common/references/source-registry.yaml` under `openai-image-generation-guide` and `openai-image-prompting-guide`. The CCFA layout tokens are working design defaults, not OpenAI guarantees.
