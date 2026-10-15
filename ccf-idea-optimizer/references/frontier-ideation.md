# Frontier Ideation

Use this file when the user provides a fuzzy, broad, or stale-prone idea and wants it concretized or optimized.

## Exploration Rule

Generate distinct mechanisms before selecting a development route. Explore varied assumptions and counterfactuals within the user's theme; final suggestions need a coherent causal account and a plausible way to distinguish them. When literature is available, use `literature-grounded-evolution.md` to connect source-backed premises to new inferences rather than only mixing topic keywords. An inferred hypothesis need not already appear in a paper to be worth developing.

Do not claim frontier novelty unless a current literature search supports it. If no search is performed, label novelty as `unsearched`.

Do not collapse the search space too early. When breadth is useful, consider a direct repair, an assumption-changing mechanism, and an ambitious reframing; a narrower problem is another option when it preserves the user's objective. These are thinking aids, not mandatory rows. For a requested breakthrough, retain at least one coherent candidate with a different causal mechanism, not just a safer configuration. If all candidates look weak, identify a salvageable ingredient when one exists; do not manufacture a rescue.

## Candidate Axes

Vary only the axes that create meaningful differences; do not build a Cartesian product or change every axis at once:

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

Repair promising candidates when a specific fix can preserve their value. A hard constraint violation, direct contradiction, or clear duplication may be filtered immediately; do not spend a rescue pass on every discarded branch. Separate lack of validation from a demonstrated flaw. Watch for:

- The method requires data the setting cannot provide.
- The benchmark does not test the claimed mechanism.
- The contribution tries to be method, dataset, system, theory, and application all at once.
- The venue audience mismatch is severe.
- The core insight is only a renamed component.
- Two modules optimize incompatible objectives.

After the audit, develop the selected route and retain a structurally different fallback when useful. For a request for options, deliver the requested breadth rather than silently reducing it to one winner. Use one focused challenge as a starting budget; new evidence can reopen the affected assumption, while a repeated paraphrase cannot. Apply Common's continuity progress test across search, reviewer, and optimizer handoffs.

## Rescue Patterns

Consider these when a specific reformulation can preserve the direction's value. They are options, not a required rescue pass for a contradicted, infeasible-under-hard-constraints, or clearly duplicate candidate:

- Keep the important problem and replace a limiting assumption, information flow, interaction mechanism, or measurement perspective. State the causal reason and a prediction that distinguishes the alternative.
- Transfer an explanatory principle from another setting after checking its necessary assumptions; specify what changes in this setting rather than stacking modules.
- Narrow the target setting until the bottleneck is measurable.
- Replace "new model" novelty with a benchmark, protocol, diagnostic, or analysis contribution.
- Keep the problem but simplify the mechanism.
- Keep the method family but change the claim from SOTA improvement to failure-mode explanation, robustness, cost, or deployment constraint.
- Switch venue family when the idea is valuable but not a main-track fit for the named venue.
- Turn a crowded positive-result idea into a negative-result or measurement paper if that would teach the community something.

Choose by the user's contribution goal and decision-relevant potential, not merely by ease of completion. Lowering ambition, changing contribution type, or moving venue is an option to explain when material; it is not an automatic consequence of uncertainty or a poor provisional score.

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
Next discriminating step / unresolved user decision, if any:
```
