# Partial Distance Correlation in Deep Learning

Venue/year: ECCV 2022.
Source: ECVA PDF `https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136860318.pdf`; arXiv `https://arxiv.org/abs/2207.09684`.
Use when: writing representation analysis, statistical tools for deep learning, regularization, disentanglement, or robustness papers.

## Story Pattern

The paper revives a statistical dependence measure and shows that it solves several deep-learning problems that look different on the surface. The writing move is to make a tool feel versatile without becoming vague: each application is tied to a shared need to compare or constrain functional behavior across feature spaces.

## Abstract Moves

- Start from a broad recurring need: comparing what neural networks learn.
- Explain why existing comparison tools are awkward at scale or across dimensions.
- Introduce the statistical tool and its partial variant.
- List diverse applications only after the common mechanism is clear.

## Introduction Moves

- Use a thought experiment to make "functional behavior comparison" intuitive.
- Contrast layer-wise analysis with cross-network functional comparison.
- Position the method as a general regularizer or constraint, then prove utility by applications.

## Method Moves

- Explain the statistical quantity before using it as a loss or constraint.
- Provide deployment details needed for large-scale models.
- Separate diagnostic use from training-time regularization.

## Evidence Moves

- Choose applications that demonstrate different faces of the same mechanism.
- Avoid a scattershot feeling by returning to the shared dependence-control theme.
- Include robustness or disentanglement evidence where the constraint should matter.

## Reusable Techniques

- Turn an old tool into a new ML contribution by explaining deployment friction.
- Use one unifying mechanism to justify many applications.
- Make versatility credible through recurring notation and repeated evidence pattern.

## Do-Not-Copy Boundary

Do not reuse the partial-distance-correlation method or versatility claim unless the user's work genuinely supports multiple validated uses.
