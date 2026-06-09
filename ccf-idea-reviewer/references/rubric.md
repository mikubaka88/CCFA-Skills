# Idea Review Rubric

Use 1-5 scores for each dimension. Score only the problem and method idea, not manuscript prose.

When novelty, insight, or acceptance potential is decision-critical, apply `strict-idea-review.md` first. If closest work was not searched, cap novelty at 3 and mark confidence low unless the user supplies credible prior-art coverage.

Score current readiness, not the user's worth or the absolute future of the direction. For rough seeds, include a separate development-potential label. A score of 2-3 often means "not ready without redesign"; it does not automatically mean "do not pursue."

## Weighted Dimensions

| Dimension | Weight |
| --- | ---: |
| Problem importance | 12 |
| Novelty against likely prior work | 14 |
| Conceptual innovation | 12 |
| Method soundness | 14 |
| Elegance and simplicity | 8 |
| Feasibility under resources | 8 |
| Experimental convincibility | 10 |
| Venue and audience fit | 8 |
| Timeliness and topic heat | 6 |
| Risk-adjusted acceptance potential | 8 |

Weights sum to 100. Adjust only when an official venue review form makes a dimension clearly more important, and state the adjustment.

## Quantitative Feedback Output

For standard idea review, output both a dimension scorecard and an aggregate score. Use:

```text
Weighted score (1-5) = sum(dimension score * weight) / 100
Optional overall score (1-10) = weighted score * 2
```

Do not treat the weighted score as an acceptance probability. The score is a decision aid that must be read with fatal risks, literature-search status, and development potential.

Include this table:

| Dimension | Weight | Score (1-5) | Confidence (1-5) | Deduction / evidence basis | Repair condition |
| --- | ---: | ---: | ---: | --- | --- |
| Problem importance | 12 |  |  |  |  |
| Novelty against likely prior work | 14 |  |  |  |  |
| Conceptual innovation | 12 |  |  |  |  |
| Method soundness | 14 |  |  |  |  |
| Elegance and simplicity | 8 |  |  |  |  |
| Feasibility under resources | 8 |  |  |  |  |
| Experimental convincibility | 10 |  |  |  |  |
| Venue and audience fit | 8 |  |  |  |  |
| Timeliness and topic heat | 6 |  |  |  |  |
| Risk-adjusted acceptance potential | 8 |  |  |  |  |

Then report:

```text
Weighted final score:
Current conference readiness:
Development potential:
Confidence:
Score-change conditions:
```

Every score of 3 or below must name the exact claim, missing mechanism, closest-work risk, missing evidence, or venue criterion that caused the deduction.

## Score Anchors

### 5

Clear CCF-A-level signal. The problem is important, the insight is non-obvious, the method has a defensible mechanism, closest-work comparison leaves a meaningful novelty delta, and the evidence package can decisively test the claim.

### 4

Promising. The idea has a real contribution and mostly coherent mechanism, but one material gap remains in novelty grounding, method detail, feasibility, or evidence design. The gap is repairable without changing the central idea.

### 3

Borderline. The idea may become publishable only after substantial refinement. The current problem-method chain leaves important doubts, the novelty delta is thin or unsearched, or the insight is more incremental than the framing suggests.

### 2

Weak in its current form. The idea is likely incremental, under-motivated, poorly grounded, internally inconsistent, or difficult to validate. A strict reviewer would probably reject the current version unless the problem, mechanism, or differentiation is changed. Still name the most plausible repair route if one exists.

### 1

Fatal for the current formulation. The problem is not important for the venue, closest work likely already covers the contribution, the method is unsound, the components conflict, or the central claim is untestable. Use `abandon` only if no credible reformulation remains.

## Dimension Guidance

- Problem importance: audience, stakes, bottleneck, and nontriviality. Penalize vague "important application" claims without a named bottleneck.
- Novelty: distance from closest work; mark uncertainty separately from low novelty. Do not score above 3 when closest work was not checked and novelty is central.
- Conceptual innovation: new insight, formulation, mechanism, benchmark, theory, or system design. Penalize pure module recombination unless the combination creates a new capability or explanation.
- Method soundness: assumptions, mechanism, feasibility, and plausible correctness. Penalize architectures whose components optimize incompatible objectives.
- Elegance: simplicity, necessity of components, and explanatory power.
- Feasibility: data, compute, implementation, timeline, and expertise.
- Experimental convincibility: ability to produce evidence that would change reviewer belief. "Run more experiments" is not enough; identify decisive baselines, ablations, datasets, proofs, systems measurements, or user studies.
- Venue fit: match to target community, track, and contribution taste.
- Timeliness: why now, relation to active questions, and risk of saturation.
- Acceptance potential: score after considering fatal risks and likely reviewer disagreement.

## Deduction Format

For every score <= 3, include:

```text
Dimension:
Deduction:
Anchor: closest work / missing mechanism / missing evidence / venue criterion / internal contradiction
Why it matters:
Repair condition:
Development-potential effect:
```
