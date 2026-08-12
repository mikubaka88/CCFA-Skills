# Paper Mechanism Figures Versus Presentation Graphics

Classify the delivery context before writing a prompt or choosing a layout. A method architecture requested for a paper is not a slide, poster, product infographic, README hero, or explanatory dashboard.

## Paper Mechanism Figure

A paper figure must expose the scientific computation graph. Organize it around inputs, representations, operators, branches, fusion points, training or inference boundaries, and outputs. A reader should be able to recover the method's execution order and identify the contribution without relying on a paragraph inside the image.

Prefer:

- concrete scientific objects such as frames, masks, coordinates, trajectories, token sequences, tensors, graphs, prompts, and predictions;
- compact operator labels attached to the transformation they perform;
- one dominant computation path with accurately placed branches and merges;
- thin connectors whose source and destination are unambiguous;
- open whitespace and light semantic grouping rather than large stage panels;
- short labels, mathematical notation, and a caption outside the image;
- visual emphasis proportional to methodological novelty.

Reject as paper-style output when the figure is dominated by:

- large numbered stage banners, hero titles, slogans, or explanatory paragraphs;
- a collection of independent rounded cards that can be reordered without changing the method;
- oversized icons, decorative illustrations, UI chrome, badges, glossy shadows, or marketing gradients;
- repeated query or output callouts added to balance the composition;
- large colored containers that describe categories but obscure the computation graph;
- connector arrows that indicate a general narrative rather than a defined data transformation;
- more space devoted to decoration or prose than to representations and operations.

Use a publication figure at its expected paper width as the QA viewport. If labels, arrows, tensors, or branch relationships become unreadable at that size, simplify the topology or move explanation to the caption.

## Presentation Or Poster Graphic

A slide or poster may use stage numbering, larger typography, stronger color regions, callout cards, explanatory labels, and simplified reading order. These choices are acceptable only when the requested artifact is explicitly a presentation, poster, README overview, or outreach visual. Label such an artifact as `PPT/Poster style`; do not present it as a top-conference paper mechanism figure.

## Reference-Guided Paper Figures

When a public paper figure is selected as a reference, extract only its scientific grammar:

```text
Representation hierarchy:
Input and output treatment:
Operator shape language:
Branch and merge geometry:
Token, tensor, or sequence encoding:
Boundary and connector style:
Text density at paper size:
Principles to borrow:
Features that must not be copied:
```

Do not reduce the reference to palette adjectives. The primary value of a paper reference is how it makes computations and representations inspectable. Do not reproduce its exact layout, content, icons, token colors, or distinctive artwork.

## Paper-Mechanism Acceptance Gate

Before accepting a generated paper architecture draft, answer all of the following:

1. Can the method be narrated by following explicit edges from inputs to outputs?
2. Does every large region contain a representation or operation rather than presentation prose?
3. Are branches and fusion points located where the method actually branches and merges?
4. Are the proposed contributions visually distinguishable from generic encoders and the final model?
5. Are concrete scientific objects carrying the explanation instead of generic icons?
6. Would the figure still make sense without stage colors, shadows, and decorative framing?
7. Does it remain legible at the intended ICLR/CVPR/NeurIPS paper width?

Any `no` is a paper-style failure. Regenerate or reconstruct the structure; do not relabel a slide-like image as a paper figure.
