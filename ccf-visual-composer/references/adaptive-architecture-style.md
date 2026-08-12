# Adaptive Architecture Style

Use this reference only for scientific method, system, model, and pipeline diagrams. It records transferable design reasoning, not reusable figure templates.

## Prompt-Specificity Ladder

Choose the smallest intervention that preserves the user's scientific intent.

1. **Detailed prompt:** Keep the user's prompt verbatim. Append only a compact `Style refinement` of at most 110 English words and no more than 35% of the original prompt length. Select at most three improvements that materially help this method. Do not restate the pipeline, module inventory, labels, palette, or negative constraints already present.
2. **Partial prompt:** Preserve supplied wording and topology. Add only missing scientific relationships, reading order, label constraints, or output constraints that affect correctness.
3. **Manuscript or notes only:** Extract a factual diagram specification first, then write a complete content-derived prompt. Minimize private material to module names, relationships, short labels, and the scientific takeaway needed for the figure.

Never expand a strong prompt merely to demonstrate that the skill was used. Prompt length is a cost and latency surface, not a quality signal.

Lock acronym handling before generation. If the source gives a canonical expansion, include that exact expansion once in the label inventory. If the expansion is not supplied or verified, require the acronym alone and explicitly forbid the image model from inventing an expansion.

## Transferable Design Principles

Select two or three principles that fit the content. Do not require all of them in every figure.

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

## Style Refinement Format

For an already detailed prompt, append one short paragraph rather than rewriting it:

```text
Style refinement: Preserve the prompt above verbatim. [Two or three content-fit layout or hierarchy improvements.] Keep one dominant reading path, give the proposed mechanism the clearest visual weight, and use evidence-bearing insets only where they explain an operation. Do not add components or imitate a fixed published layout.
```

Remove clauses that duplicate the original prompt. The final suffix should be specific enough to affect composition and short enough that the user's wording remains dominant.

## Anti-Imitation Gate

Before generation, reject any prompt that instructs the model to reproduce a particular observed figure, fixed panel geometry, exact palette sequence, icon set, caption, typography, wording, or distinctive visual metaphor. Do not attach local style-study images to an external model unless the user separately authorizes those exact images. Do not name or expose private local references in the outbound prompt.

During QA, ask:

- Does the composition arise from this method's topology?
- Would removing a visual inset remove scientific information?
- Is the strongest emphasis on the actual contribution?
- Is the figure recognizably different from unrelated diagrams using the same skill?
- Did prompt augmentation stay within the specificity budget?
- Are acronym expansions either source-verified or suppressed?
