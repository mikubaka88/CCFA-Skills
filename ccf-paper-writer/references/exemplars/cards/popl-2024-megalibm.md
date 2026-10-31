# MegaLibm Style Card

Venue/year: POPL 2024.
Source: shared registry record `popl-2024-megalibm`; direct original locations below.
Use when: programming languages, program synthesis, compiler/tool papers, numerical libraries, formal methods, or papers combining correctness with empirical tool evaluation.

Inspected writing: Official POPL 2024 paper abstract at `https://popl24.sigplan.org/details/POPL-2024-popl-research-papers/34/Implementation-and-Synthesis-of-Math-Library-Functions`; DOI `https://doi.org/10.1145/3632874`.

This card navigates selected original passages. The source observations below are distinct from the adaptation advice; read the relevant original when using it.

## Story Pattern

**Source observation:** The abstract starts from the difficulty of implementing mathematical library functions in low-level code. It presents MegaLibm through the development activities it separates: mathematical error checking, assembling implementations, and tuning orthogonal parameters. Interactive synthesis and evaluation then show how the approach is used.

## Abstract Moves

**Writing observation in the inspected passage:** The tool is defined through the tasks it supports and the distinctions between them. This gives meaning to the system description without requiring a feature-list narrative.

## Reusable Techniques

**Adaptation advice for matching work:**

- Explain the developer's actual problem before naming tool components.
- Distinguish mathematical correctness, implementation assembly, and tuning when the contribution depends on those boundaries.
- Use a synthesis or tool example only when it illustrates the current construction; do not invent formal guarantees.

## Do-Not-Copy Boundary

Use the target study's own definitions, mechanisms, conditions, results, and claims. Common academic phrasing and established terms may be reused when they fit; distinctive source sentences and scientific conclusions may not be transplanted.
