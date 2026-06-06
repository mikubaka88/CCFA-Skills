# 1000 Layer Networks for Self-Supervised RL

Venue/year: NeurIPS 2025.
Source: NeurIPS Proceedings `https://proceedings.neurips.cc/paper_files/paper/2025/hash/e74ee34cc0f2d0780f34ee77d8fba25b-Abstract-Conference.html`.
Use when: writing scaling, RL, self-supervised learning, architecture depth, goal-conditioned learning, or capability-emergence papers.

## Story Pattern

The paper imports a familiar scaling lesson from language and vision into reinforcement learning, then argues that RL had not benefited because the right building blocks were missing. The specific axis is network depth, and the evidence is both quantitative improvement and qualitative change in learned behavior.

## Abstract Moves

- Open with a cross-field contrast: scaling transformed language/vision but not RL.
- Identify one design axis as critical.
- State the experimental setting in a way that raises difficulty: no rewards or demonstrations.
- Quantify gains across tasks.
- Add that scaling changes behaviors, not only metrics.

## Introduction Moves

- Explain why existing shallow RL architectures may be a bottleneck.
- Make the unsupervised goal-conditioned setting central to the difficulty.
- Present depth scaling as a systematic study, not a one-off architecture trick.

## Method Moves

- Define the base algorithm before scaling modifications.
- Separate architecture depth, stability tricks, objective, and training protocol.
- Keep compute and implementation details visible for reproducibility.

## Evidence Moves

- Show scaling curves rather than only best numbers.
- Compare against goal-conditioned baselines.
- Include qualitative behavior examples to support the capability-change claim.

## Reusable Techniques

- Use cross-domain analogy carefully, then validate it in the target domain.
- Pair scaling laws with concrete downstream behaviors.
- Make absence of supervision part of the challenge framing.

## User Notes

Use for papers where a simple scaling dimension unlocks surprising performance or behavior.

## Do-Not-Copy Boundary

Do not reuse the depth-scaling claim, unsupervised RL setup, or magnitude of gains unless supported by the user's experiments.
