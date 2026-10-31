# MiniLongBench

Venue/year: ACL 2025, Outstanding Paper.
Source: ACL Anthology `https://aclanthology.org/2025.acl-long.560/`.
Use when: writing benchmark, evaluation efficiency, long-context LLM, dataset pruning, or low-cost evaluation papers.

Inspected writing: Stored original text `references/exemplars/papers/acl-2025-minilongbench.md`, Abstract and Introduction around Figure 1.

This card navigates selected original passages. The source observations below are distinct from the adaptation advice; read the relevant original when using it.

## Story Pattern

**Source observation:** The introduction connects long input sequences and repeated model evaluation to time and memory costs, then asks whether the benchmark needs all of its samples. The abstract pairs the cost of the smaller benchmark with agreement in model rankings.

## Abstract Moves

**Writing observation in the inspected passage:** The two reported quantities answer different questions: how much evaluation is saved and how much of the original comparison is retained. They are not interchangeable evidence of quality.

## Reusable Techniques

**Adaptation advice for matching work:**

- Explain the practical burden before introducing a compression objective.
- Report the preserved property alongside the resource reduction when both matter.
- Keep cost, fidelity, and dataset coverage distinct; use only the current study's measured values.

## Do-Not-Copy Boundary

Use the target study's own definitions, mechanisms, conditions, results, and claims. Common academic phrasing and established terms may be reused when they fit; distinctive source sentences and scientific conclusions may not be transplanted.
