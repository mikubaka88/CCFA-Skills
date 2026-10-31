# BrickGPT

Venue/year: ICCV 2025.
Source: CVF `https://openaccess.thecvf.com/content/ICCV2025/html/Pun_Generating_Physically_Stable_and_Buildable_Brick_Structures_from_Text_ICCV_2025_paper.html`.
Use when: writing text-to-3D, generative design, physical constraints, autoregressive generation, dataset, or embodied construction papers.

Inspected writing: Stored original text `references/exemplars/papers/iccv-2025-brickgpt.md`, Abstract and Introduction.

This card navigates selected original passages. The source observations below are distinct from the adaptation advice; read the relevant original when using it.

## Story Pattern

**Source observation:** The introduction distinguishes a visually plausible digital shape from an object that can be assembled and remain stable. The abstract explains next-brick prediction, a physically stable training dataset, and inference-time validity checks with rollback before describing assemblies and evaluations.

## Abstract Moves

**Writing observation in the inspected passage:** Different physical requirements motivate different parts of the construction. The method is described through what changes during generation rather than through a list of unnamed reliability guarantees.

## Reusable Techniques

**Adaptation advice for matching work:**

- Make physical feasibility concrete when it is the actual scientific requirement.
- Explain how a generation rule and a constraint check interact.
- Keep dataset, inference mechanism, and observed assembly results separate; do not import these components into unrelated methods.

## Do-Not-Copy Boundary

Use the target study's own definitions, mechanisms, conditions, results, and claims. Common academic phrasing and established terms may be reused when they fit; distinctive source sentences and scientific conclusions may not be transplanted.
