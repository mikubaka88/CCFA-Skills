# InSpectre Gadget Style Card

Venue/year: USENIX Security 2024.
Source: shared registry record `usenix-security-2024-inspectre-gadget`; direct original locations below.
Use when: security papers involving attacks, defenses, vulnerability discovery, side channels, exploit chains, formal threat models, or security measurement.

Inspected writing: Official source `https://www.usenix.org/conference/usenixsecurity24/presentation/wiebing`; paper `https://www.usenix.org/system/files/usenixsecurity24-wiebing.pdf`, Abstract and Section 1 on printed page 577.

This card navigates selected original passages. The source observations below are distinct from the adaptation advice; read the relevant original when using it.

## Story Pattern

**Source observation:** The abstract connects a residual attack surface under existing mitigations to the difficulty of assessing gadget exploitability. Section 1 distinguishes pattern matching that misses nonstandard forms from coarse data-flow analysis that over-approximates feasible behavior, motivating symbolic execution with constraints.

## Abstract Moves

**Writing observation in the inspected passage:** The method follows a distinction between two analysis failures. The writing links the chosen analysis to its purpose before presenting examples of what it exposes.

## Reusable Techniques

**Adaptation advice for matching work:**

- Explain what an analysis can miss and what it can falsely admit when both affect the problem.
- Tie a threat-model condition or constraint to the corresponding reasoning step.
- Preserve disclosure and attack assumptions when material; do not claim an exploit or mitigation result for a different system.

## Do-Not-Copy Boundary

Use the target study's own definitions, mechanisms, conditions, results, and claims. Common academic phrasing and established terms may be reused when they fit; distinctive source sentences and scientific conclusions may not be transplanted.
