# Strict Idea Review Protocol

Use this file when the user asks for idea scoring, idea ranking, novelty risk, investment decisions, or `standard` mode review. The goal is to prevent generic reviewer prose.

## Standard-Mode Search Requirement

In standard mode, search for related literature before giving a strong novelty, insight, or acceptance-potential judgment unless the user explicitly forbids browsing or privacy constraints prevent safe searching.

Search process:

1. Convert the idea into public-safe keywords: problem, setting, method family, claimed mechanism, dataset/benchmark, target venue family, and 2-3 likely synonyms.
2. Do not paste confidential user wording into a search query when the idea is unpublished and specific. Query generic public keywords first. If exact private wording is necessary, ask before using it.
3. Prefer authoritative and high-impact sources: official proceedings, OpenReview, arXiv only when needed for fast-moving fields, ACM/IEEE/USENIX/ACL Anthology/CVF/PMLR/NeurIPS/ICLR/AAAI pages, DBLP, Semantic Scholar, OpenAlex, and major journal publishers. Apply the shared source-quality exclusions.
4. Record 3-8 closest works or state why fewer were found.
5. Separate `not searched`, `searched but weak coverage`, and `searched with closest-work confidence`.

If no search was performed, the final recommendation must either be `needs-literature-search` or carry low novelty confidence. Do not say "high novelty" without a search-backed nearest-neighbor comparison or strong user-provided prior-art evidence.

## Closest-Work Table

Include this table in standard mode:

```text
Closest work:
Venue/year:
Link/source:
What it already does:
Overlap with user idea:
Remaining novelty delta:
Risk to the idea: fatal / high / medium / low
Needed differentiation:
```

## No-Filler Rule

Do not output generic comments such as:

- "有一定创新性"
- "建议进一步完善"
- "需要更多实验"
- "创新性不足"
- "方法描述不够清楚"
- "related work 需要加强"

unless each phrase is immediately followed by:

```text
Exact claim or mechanism under review:
Closest prior art or missing evidence:
Why a strict reviewer would deduct:
Concrete repair or pivot:
What would change the score:
```

Every major criticism must have at least one anchor:

- a searched paper or known literature line,
- a venue criterion,
- a missing mechanism,
- a missing baseline/evidence path,
- a contradiction inside the proposed idea,
- or a resource/feasibility constraint.

## Harsh Reviewer Lens

Act as a strict target-venue or target-journal reviewer. Be professional, but do not soften the verdict with motivational padding. Prefer short, diagnostic sentences.

Strict does not mean terminal. For early ideas, state `current conference readiness` and `development potential` separately. A close prior-art hit, missing mechanism, or missing benchmark is a blocker for the current version, not proof that the direction cannot become publishable. Before recommending `abandon`, name the best possible rescue route and explain why it still fails.

Judge the idea through these axes:

1. Insight: Is there a non-obvious observation that would teach the community something, or is it a wrapper around known components?
2. Problem: Is the bottleneck important, current, and specific enough for the target venue?
3. Method mechanism: Is there a causal or algorithmic reason the method should work?
4. Novelty delta: What exactly remains new after subtracting closest work?
5. Elegance: Are the components necessary, coherent, and mutually compatible?
6. Evidence path: Can decisive experiments, proofs, user studies, benchmarks, or systems measurements test the central claim?
7. Feasibility: Can the user plausibly execute it with available data, compute, engineering effort, and timeline?
8. Venue taste: Would the venue see this as a main-track contribution or as a workshop/application variant?

## Stage-Aware Verdict Rule

Use this distinction whenever the idea is a seed, direction, or partial sketch:

```text
Current conference readiness: high / medium / low
Development potential: high / medium / low
Main reason it is not ready:
Best rescue route:
Evidence needed to decide:
```

Do not mark `abandon` for:

- novelty not yet searched,
- a crowded topic with a plausible narrower bottleneck,
- missing experiments when a decisive evidence path can be named,
- vague mechanism when a concrete mechanism family can be proposed,
- venue mismatch when another venue family may fit.

Mark `abandon` only when the idea has no testable central claim, the closest work already covers the same problem and mechanism, and no meaningful problem/method/evidence reframing remains.

## Required Verdict Shape

For one idea in standard mode, use:

```text
Verdict first:
Search basis:
Normalized idea:
Closest prior art table:
Novelty delta:
Serious blockers:
Development potential:
Dimension scores:
Strict reviewer comments:
Repair plan:
Evidence that would change my score:
Final recommendation:
```

For multiple ideas, first run the closest-work and serious-risk scan independently, then rank by serious-risk-adjusted score. Do not rank by buzzword appeal.

## Score Guardrails

- Cap novelty at 3 if closest work was not searched and novelty is decision-critical.
- Cap acceptance potential at 3 if the method mechanism is unclear.
- Cap recommendation at `pivot` if closest prior art already solves the central problem with a similar mechanism. If a different evidence setting, assumption, user group, system constraint, or theory angle could still be meaningful, name that rescue route.
- Cap recommendation at `pivot` if the only novelty is applying a known method to a new dataset without a venue-valued insight.
- Mark as `abandon` only when the idea has no testable central claim and no plausible reformulation after the best rescue route has been considered.
