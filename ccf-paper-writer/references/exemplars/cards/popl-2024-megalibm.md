# MegaLibm Style Card

Venue/year: POPL 2024 family.
Source: ACM Best Paper Awards source record `acm-best-paper-awards`; verify the exact paper page before public award-status claims.
Use when: programming languages, program synthesis, compiler/tool papers, numerical libraries, formal methods, or papers combining correctness with empirical tool evaluation.

## Story Pattern

The paper type is PL/tool research: start with a correctness, synthesis, or verification bottleneck that practitioners face, state the formal object being produced or checked, then explain how the method bridges proof, implementation, and empirical utility.

## Abstract Moves

- State the artifact or formal target clearly.
- Explain why existing synthesis, verification, or library-engineering approaches are insufficient.
- Present the key technical idea before the tool name.
- Preview evidence as correctness, coverage, performance, or usability, not only speed.

## Introduction Moves

- Use one concrete failure mode or maintenance pain point to motivate the formal problem.
- Define the core formal challenge before implementation details.
- State how the technique changes the search, proof, or compilation space.
- Separate theoretical guarantee, implementation, and evaluation contributions.

## Method Moves

- Put definitions before algorithms.
- Give a proof or soundness roadmap before dense formalism.
- Explain tool architecture only after the core semantics or synthesis idea is clear.

## Evidence Moves

- Combine formal guarantees with benchmarks on real programs or libraries.
- Report coverage, correctness, performance, and failure cases.
- Include threats to validity for benchmark selection and specification assumptions.

## Do-Not-Copy Boundary

Do not reuse library-specific examples, theorem wording, or tool claims. Transfer only the PL proof-plus-artifact writing pattern.
