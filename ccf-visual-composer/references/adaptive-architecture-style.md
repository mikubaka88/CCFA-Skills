# Adaptive Architecture Style

Use this reference only for scientific method, system, model, and pipeline diagrams. It records transferable design reasoning, not reusable figure templates.

## Prompt-Specificity Ladder

Choose the smallest intervention that preserves the user's scientific intent.

1. **Detailed prompt:** Keep the user's prompt verbatim. Append only missing refinements; for a local edit, a short delta usually suffices. For a requested layout redesign, supply enough geometry, typography, reference roles, and label constraints to make the design executable. Do not impose a word/percentage ceiling that discards requirements, and do not restate inventories or constraints already present.
2. **Partial prompt:** Preserve supplied wording and topology. Add only missing scientific relationships, reading order, label constraints, or output constraints that affect correctness.
3. **Manuscript or notes only:** Extract a factual diagram specification first, then write a complete content-derived prompt. Minimize private material to module names, relationships, short labels, and the scientific takeaway needed for the figure.

Never expand a strong prompt merely to demonstrate that the skill was used. Prompt length is a cost and latency surface, not a quality signal.

Lock acronym handling before generation. If the source gives a canonical expansion, include that exact expansion once in the label inventory. If the expansion is not supplied or verified, require the acronym alone and explicitly forbid the image model from inventing an expansion.

## Transferable Design Principles

Select the few principles that address the actual composition. Apply the concrete spacing and typography tokens in `visual-contract.md`; do not load every principle into every prompt.

- **Information-scale hierarchy:** Establish macro regions, meso modules, and micro evidence only when all three carry different scientific roles.
- **Semantic regions:** Use restrained background tint, boundaries, or headings to group real stages, phases, branches, or evidence families.
- **Dominant reading path:** Make the main inference or processing path visually immediate; keep auxiliary context, retrieval, feedback, and supervision subordinate.
- **Typed connections:** Distinguish primary flow from feedback, control, retrieval, or cross-branch context through line treatment when the distinction matters.
- **Evidence-bearing insets:** Use small frames, masks, trajectories, graphs, attention maps, or state snapshots only when they explain a named operation. Avoid decorative screenshots and icons.
- **Importance-weighted space:** Give the actual contribution and scientifically decisive transformations more area than generic encoders, adapters, or output heads.
- **Matched comparison geometry:** For baseline/proposed, training/inference, or before/after comparisons, align shared elements and visually isolate the changed mechanism.
- **Problem-to-mechanism bridge:** When a failure mode motivates a module, a compact local cue may connect the ambiguity or missing evidence to the mechanism that resolves it. Do not turn the whole architecture into a motivation figure unless requested.

## Adaptive Selection

Base the layout on topology:

- sequential stages -> one aligned flow with nested detail near the relevant stage;
- parallel evidence branches -> synchronized lanes that merge at the true integration point;
- graph or memory reasoning -> preserve node/edge semantics and show the consumer of the retrieved trace;
- iterative repair or verification -> show state, loop direction, and exit condition;
- dense geometry or temporal evidence -> use a small number of concrete evidence snapshots rather than explanatory paragraphs.

Prefer visible scientific objects over generic decoration: a video strip can express time, a mask overlay can express segmentation, arrows can express motion, and a graph can express relational evolution. Each inset must be traceable to supplied content.

## Destination-Aware Style

Do not use one meaning of `beautiful` across destinations.

- For a paper mechanism figure, beauty comes from an economical computation graph, legible representations, precise alignment, disciplined whitespace, and a contribution that is structurally visible. Avoid hero composition, large stage numbers, dashboard cards, callout prose, and poster-like color fields.
- For PPT/Poster, beauty may include stronger hierarchy, explanatory cards, larger icons, stage banners, and more generous display spacing.
- For README/outreach, beauty may include a headline, overview metaphor, product capability groups, and simplified flows.

If the user asks for a top-conference paper figure, default to the first grammar even when the image generator tends toward presentation layouts. A generated slide-like composition is a failed draft, not a palette variant.

## Coordinated Presets

Select one preset for a new design or explicit style change. A preset coordinates representation, font, strokes, fills, and emphasis; it does not prescribe the scientific graph or a fixed aspect ratio. Keep an approved preset for local edits. Use the user's inspected primary reference over a generic preset when they differ. Reuse the palette keys in `palette-and-accessibility.md`; put the selected actual colors and dimensions in the prompt, not all presets.

| Preset | Representation and grouping | Type and line treatment | Color starting point |
| --- | --- | --- | --- |
| `formal-roman` / Formal mechanism | Open computation graph, compact operators, fine semantic separators; show the decisive transformation explicitly. | Times New Roman; regular labels and bold group names; thin connectors, near-square operator corners. | `ccfa_ink`: dark neutral context with one blue or green contribution accent. |
| `soft-mechanism` / Soft mechanism | Concrete tensors, tokens, graphs, or objects with small low-tint groups; detail stays near its operation. | Times New Roman; consistent modest corner radius and connector weight; restrained soft shading inside objects. | `ccfa_ceramic`: teal/terracotta accents with pale warm fills. |
| `visual-evidence` / Visual evidence | Matched image strips or crops, aligned modality lanes and a compact mechanism inset; use actual evidence images where required. | Times New Roman; identical crop sizes, frame indices, label baselines, and thin overlays. | `ccfa_arctic` or `ccfa_gem`: 2-4 stable semantic colors, quiet backgrounds. |
| `geometric-flow` / Geometric flow | Supported distributions, trajectories, or spatial structures; sparse reference geometry under a stronger transformation path. | Times New Roman with compatible math; shared viewpoint, light mesh/contours, clear foreground path. | `ccfa_nocturne` or `ccfa_ceramic`: muted context and one warm transformation accent. |
| `compact-comic` / Compact comic | Recognizable simplified scientific objects on a precise grid; compact rounded grouping where useful. | Comic Sans MS with legible math; consistent optical size and clean connectors, no decorative line wobble. | `ccfa_orchid` or `ccfa_ceramic`: limited muted accents with dark labels. |

All presets use the final-size type scale in `visual-contract.md`. A comic treatment must fit the requested reference or user preference; do not infer it solely from a conference name. Sparse geometry is a representation choice, not permission to add an unsupported field, probability density, or result. For numerical plots, carry over typography/color roles only; render all values and geometry reproducibly from data.

## Venue Context

These are CCFA design suggestions, not official conference styles or formatting rules. Content and an explicit reference determine the preset; verify actual template/font/figure requirements for the exact venue, year, and track only when those requirements affect the deliverable.

| Reading context | Useful starting choices |
| --- | --- |
| General ML methods, e.g. NeurIPS / ICML / ICLR | `formal-roman` for computation/proofs; `soft-mechanism` for representation changes; `geometric-flow` only for a spatial/continuous mechanism. |
| Vision methods, e.g. CVPR / ICCV / ECCV | `visual-evidence` for image/video correspondences, with a compact mechanism inset; `geometric-flow` for grounded geometry. |
| Language methods, e.g. ACL / EMNLP / NAACL | `formal-roman` or `soft-mechanism` with aligned token spans, short exact examples, and clear retrieval/training boundaries. |
| Systems/security methods, e.g. SOSP / OSDI / USENIX Security | `formal-roman` with precise interfaces, shared ports, and meaningful system/trust boundaries. |
| An explicitly requested informal explanation or matching reference | `compact-comic`, retaining final-size readability and truthful scientific objects. |

Reference-workflow provenance is registered as `astradraw-visual-workflow` in `../../ccf-common/references/source-registry.yaml`. Preset names and outward method descriptions remain functional. Do not import a reference project's scripts, component pack, or asset library by default.

## Style Refinement Format

For an already detailed prompt, append one short paragraph rather than rewriting it:

```text
Style refinement: [Missing alignment anchors, chosen spacing tokens, primary font, and text constraints.] Keep the specified topology and exact labels. Give the proposed mechanism the clearest visual weight; place its scientific illustrations inside the allocated slots.
```

Remove clauses that duplicate the original prompt. The final suffix should be specific enough to affect composition and short enough that the user's wording remains dominant.

## Reference Use Boundary

Translate an inspected reference into geometric relationships and visual properties. A user request to follow a supplied reference authorizes that reference's use within the host's permitted image workflow; do not ask again within that scope. Preserve explicit template geometry when requested, but do not transfer unrelated scientific labels or claims. Keep provenance in source records and credits. Do not name a competitor's style in method introductions or output titles. Unrelated private local images remain outside the request; follow the shared privacy rules for any new transfer boundary.

During QA, ask:

- Does the composition arise from this method's topology?
- Would removing a visual inset remove scientific information?
- Is the strongest emphasis on the actual contribution?
- Is the figure recognizably different from unrelated diagrams using the same skill?
- Did each added constraint resolve a real design decision without duplicating the original prompt?
- Are acronym expansions either source-verified or suppressed?
