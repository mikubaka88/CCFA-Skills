# Scientific Diagram Generation And Refinement

Use GPT Image for an entire new or redrawn scientific method, architecture, flow or conceptual figure. Numerical analysis uses Python; existing-figure edits remain scoped to the current image/source. The entrypoint defines those boundaries. This reference supplies the prompt and attachment details, without a vector skeleton, shape reconstruction or component-assembly route.

## Before Stage 1: Understand The Scientific Task

Read the relevant method/caption, user requirements and useful authorized references. Establish what the reader should understand, the figure's scope, necessary objects and actual relationships, and its destination/font. Reuse current context; no separate brief, approval, report, agent or image call is required.

Separate observed inputs, estimated representations and inaccessible latent/ground-truth states. A causal equation explaining observations is not automatically an executable pipeline. Preserve supplied optional inputs, branches, train/inference distinctions and supervision. For an incomplete method, use the supported overview if sufficient, or ask about the missing mechanism needed by the requested scope. Do not invent conventional encoders, memory updates, retrieval steps or results to complete it. Repair only unambiguous notation damage.

Give each reference a role: scientific content, composition, object appearance, typography or color. Use the actual image when authorized; an absent reference is not an attachment. An appearance reference supplies no new scientific facts. Preserve source credits in the current record when useful; do not transplant unrelated labels, claims or artwork.

A paper figure explains its mechanism through concrete objects, transformations and meaningful connections, with short labels and an external caption. A slide, poster or outreach overview can use larger headings and explanatory callouts when that is the requested destination. Choose visual treatment from the actual task, not a fixed layout or conference stereotype.

## 1. Expand The Understanding Into Prompt P

Preserve a good user prompt and add only missing information. Otherwise use the useful parts of this structure; short tasks can merge the headings:

```text
PURPOSE: Draw [figure role/scope] so the reader understands [scientific message].
CONTENT: [Supported observed inputs -> operations/representations -> outputs, essential branches, exact short labels and needed equations. Distinguish estimated/latent/optional quantities where relevant.]
REFERENCES: [Article figure/section] supplies the science; [reference image] guides [composition, object appearance or palette]. Adapt its visual organization to this method.
APPEARANCE: Compact, information-rich figure for [actual slot/destination], with aligned related groups, short clear connections and recognizable scientific objects. Use [chosen font], differentiated heading/body hierarchy and [chosen semantic colors if useful]. Keep local breathing room, minimal wasted margins and short labels; leave caption prose outside the image.
DELIVERY: Crisp high-resolution PNG, readable at the intended paper/display size.
```

Let the image model choose detailed positions, sizes, proportions and illustrations. Do not append a generic style manifesto, pixel table, fixed grid or list of every preset. Apply exact spacing only if it is an actual user requirement, as an image target rather than coordinate construction. Keep required terminology and canonical acronym expansions; do not invent expansions or abbreviate away meaning.

Use Times New Roman by default, selected Comic Sans MS or the user's/destination's requirement. Key headings are bold; body labels and equations remain subordinate. Quantitative titles, axes, ticks and legends retain their requested boldness and readable size differences. Mathematical variables can be italic, with upright units and descriptive text. Panel letters support navigation rather than overpowering the subject.

Keep scientific objects coherent in viewpoint, detail and identity: image strips, masks, rays, camera poses, tokens or graphs should explain the supplied transformation. Generate them within the complete composition. Supplied assets can guide the result; a vector icon pack or a separate asset-generation pass is not a prerequisite. A separately requested isolated raster object can use the host image workflow with transparency when needed, preserving source/license/credit for reused assets.

Use one semantic color map, light fills and darker same-hue borders where appropriate. Preserve approved template mappings and actual image/depth scales. Optional colors and conditional line/band conventions are in [palette-and-accessibility.md](palette-and-accessibility.md); style does not create a comparator, threshold or uncertainty interval. A crisp, vector-like appearance remains a PNG quality target.

## 2. Generate G0 From P, References And Article Material

Actually call GPT Image. Attach relevant reference images and article figure/pages, identifying their order and roles in the tool envelope. Include the necessary method content in P. If the tool cannot attach a PDF, use the relevant page/figure images and factual content; omit unrelated pages and minimize private material within the established authorization.

Generate one complete composition using the host's supported operation and parameters. If the required image capability fails or is unavailable, retain the useful prompt/draft and report that specific failure; do not substitute code or vector construction. A prepared prompt is not an executed generation.

## 3. Refine G0 With The Same P Into G1

Inspect G0, then actually call GPT Image again with the same P and G0 as the edit target:

```text
ORIGINAL GOAL:
[P, unchanged]

EDIT THE ATTACHED DRAFT:
The attached image is G0. Preserve its accepted composition, scientific objects, labels, equations, color identities and required connections. Refine [actual related issues in one pass]. Keep unaffected content fixed. Improve compact alignment and final-size readability where needed; return the refined PNG.
```

The current image is the draft, not the article/reference; do not reuse attachment numbering from the generation envelope. Name real defects specifically, such as an incorrect merge or overlapping label. If none is identified, request restrained visual coordination/readability refinement while preserving content, without inventing a scientific error.

Preparation uses the current assistant; generation and refinement are **two actual image-tool calls for one candidate**. `figure_variants=off` only disables additional candidates and cannot skip refinement. Existing-image local edits do not restart this workflow unless the user requests a new composition or complete redraw.

Inspect G1 at its final intended size for the necessary source-to-target paths, directions, labels/equations, compactness and visual quality. Proximity does not establish a connection. Correct any surviving material defect through a bounded image edit and inspect affected dependencies. Repeated failures require a better representation/instruction, not more blind nudges or a vector fallback.

## Numerical Content And Delivery

Keep embedded quantitative marks, axes, labels and statistical definitions code-rendered. Compare them with the original numerical export after any image operation; do not repaint measurements or invent bands. Details of selected numerical templates and reference encodings belong to [figure-design-library.md](figure-design-library.md).

Deliver the final PNG. Requested PPTX/PDF placement preserves its raster nature and aspect ratio. Existing-source maintenance and placement checks are in [render-qa.md](render-qa.md); do not reconstruct a raster into editable shapes. Keep one current P/source record when needed and one final PNG, reusing the tool-managed G0 for refinement rather than copying attempt histories. Follow Common's artifact contract and inspect only the affected output formats.
