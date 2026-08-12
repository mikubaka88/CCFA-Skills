# Frontier Ideation

Use this file when the user provides a fuzzy, broad, or stale-prone idea and wants it concretized or optimized.

## Exploration Rule

Generate diverse candidates first, then filter. High randomness is allowed during exploration, but final suggestions must be coherent, feasible, and aligned with the user's theme. When literature is available, load `literature-grounded-evolution.md` and derive candidates from source-backed gap relations rather than from topic keywords alone.

Do not claim frontier novelty unless a current literature search supports it. If no search is performed, label novelty as `unsearched`.

Do not collapse the search space too early. In exploratory work, keep at least three kinds of options when possible: a conservative repair of the user's seed, a narrower high-precision problem, and a more ambitious reframing. If all candidates look weak, identify the best salvageable ingredient before recommending a pivot.

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

Give each candidate a parent and one primary operation: `refine`, `combine`, `transfer`, `invert`, or `instrument`. Keep the operation meaningful: a `combine` candidate must name the interaction between mechanisms, and a `transfer` candidate must check the source mechanism's assumptions in the target setting.

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

Revise candidates before rejecting them. A candidate should be rejected only after naming the smallest plausible repair and explaining why it fails. Watch for:

- The method requires data the setting cannot provide.
- The benchmark does not test the claimed mechanism.
- The contribution tries to be method, dataset, system, theory, and application all at once.
- The venue audience mismatch is severe.
- The core insight is only a renamed component.
- Two modules optimize incompatible objectives.

After the audit, retain the strongest development route and one structurally different fallback. Challenge the strongest route once against its closest-overlap risk and weakest evidence link; do not run repetitive self-reflection that only paraphrases the same idea.

## Rescue Patterns

Use these before declaring a direction stale or too weak:

- Narrow the target setting until the bottleneck is measurable.
- Replace "new model" novelty with a benchmark, protocol, diagnostic, or analysis contribution.
- Keep the problem but simplify the mechanism.
- Keep the method family but change the claim from SOTA improvement to failure-mode explanation, robustness, cost, or deployment constraint.
- Switch venue family when the idea is valuable but not a main-track fit for the named venue.
- Turn a crowded positive-result idea into a negative-result or measurement paper if that would teach the community something.

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
Rescue / narrowing options:
Next question for the user:
```
