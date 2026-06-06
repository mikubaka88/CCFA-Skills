# Visual Autoregressive Modeling

Venue/year: NeurIPS 2024.
Source: NeurIPS Proceedings `https://proceedings.neurips.cc/paper_files/paper/2024/hash/9a24e284b187f662681440ba15c416fb-Abstract-Conference.html`.
Use when: writing image generation, autoregressive modeling, new prediction paradigm, scaling laws, or fast inference papers.

## Story Pattern

The paper redefines autoregressive image generation by changing what the next prediction is. Instead of raster-scan next-token prediction, the model predicts the next scale or resolution in a coarse-to-fine process. The story is powerful because a simple conceptual shift yields quality, speed, data-efficiency, and scaling-law evidence.

## Abstract Moves

- Name the paradigm shift in the first technical sentence.
- Contrast it with the standard formulation.
- State why the new formulation is intuitive and scalable.
- Report a dramatic benchmark improvement and speed gain.
- Extend the claim to scaling laws and zero-shot image editing.

## Introduction Moves

- Explain why text-style autoregression is awkward for images.
- Use spatial hierarchy as the reason next-scale prediction is natural.
- Position diffusion models as the benchmark to beat, but keep comparisons evidence-based.

## Method Moves

- Define the visual token hierarchy before transformer training.
- Make the prediction order visually understandable.
- Explain how inference speed follows from the formulation.

## Evidence Moves

- Pair headline metrics with speed and scalability curves.
- Include comparison to both AR and diffusion baselines.
- Use downstream editing/inpainting as evidence of generalization.

## Reusable Techniques

- A new prediction target can be the whole paper story.
- Make scaling claims with curves, not only final model performance.
- Let conceptual simplicity and empirical breadth reinforce each other.

## Do-Not-Copy Boundary

Do not reuse next-scale prediction, reported numbers, or diffusion-comparison claims unless the user's method and evaluation support them.
