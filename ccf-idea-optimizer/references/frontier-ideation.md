# Frontier Ideation

Use this file when the user provides a fuzzy, broad, or stale-prone idea and wants it concretized or optimized.

## Exploration Rule

Generate diverse candidates first, then filter. High randomness is allowed during exploration, but final suggestions must be coherent, feasible, and aligned with the user's theme.

Do not claim frontier novelty unless a current literature search supports it. If no search is performed, label novelty as `unsearched`.

## Candidate Axes

Vary 3-5 axes:

```text
Problem angle:
Root bottleneck:
Target user/community:
Method mechanism:
Data or benchmark:
Evidence type:
Venue family:
Main risk:
```

Useful variation patterns:

- Same problem, simpler mechanism.
- Same method family, sharper problem.
- New benchmark/protocol instead of new model.
- System/tool contribution instead of only algorithmic contribution.
- Theory/analysis contribution that explains an empirical pattern.
- Human-centered or deployment constraint that changes the problem.
- Negative result or diagnostic paper when SOTA chasing is crowded.

## Non-Stale Check

Ask or search:

- What did top venues publish in the last 12-24 months?
- What datasets or baselines have become standard?
- What failure mode is still not well measured?
- What assumption do recent papers share?
- What result would still be useful if headline performance gains are small?

If current search is not available, state:

```text
Novelty status: unsearched; needs ccf-literature-searcher before strong novelty claims.
```

## Coherence Audit

Reject or revise candidates when:

- The method requires data the setting cannot provide.
- The benchmark does not test the claimed mechanism.
- The contribution tries to be method, dataset, system, theory, and application all at once.
- The venue audience mismatch is severe.
- The core insight is only a renamed component.
- Two modules optimize incompatible objectives.

## Output Pattern

```text
Exploration breadth:
Candidate idea cards:
Best candidate:
Why it is coherent:
Why it may be timely:
Novelty status:
Evidence package:
Risks:
Next question for the user:
```
