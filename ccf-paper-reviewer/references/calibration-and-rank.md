# Calibration And Rank

Use this file for scores, calibrated stance, confidence, and CSPaper-style relative interpretation.

## Default Overall Scale

Use 1-10 when the venue does not specify a scale:

- 10: award-level or clear top-tier accept.
- 9: strong accept.
- 8: accept.
- 7: weak accept.
- 6: borderline positive.
- 5: borderline negative.
- 4: weak reject.
- 3: reject.
- 2: strong reject.
- 1: desk-reject-level or unreviewable.

## Criterion Scale

Use 1-5 for:

- Quality,
- Clarity,
- Significance,
- Originality,
- Soundness,
- Evidence,
- Reproducibility,
- Ethics / Limitations.

Anchors:

- 5: clear strength,
- 4: good,
- 3: mixed,
- 2: weak,
- 1: fatal or near-fatal.

## Stance Bands

- Clear accept: no fatal risk; most criteria 4-5; overall usually 8-10.
- Lean accept: no fatal risk; one or two moderate concerns; overall usually 7.
- Borderline: merits and risks balanced; overall usually 5-6.
- Lean reject: one major concern or multiple moderate concerns; overall usually 4.
- Clear reject: fatal technical, novelty, evidence, policy, or venue issue; overall usually 1-3.

## CSPaper-Style Relative Interpretation

When the user asks for rank, review rank, or cohort-relative quality:

- State that the interpretation is approximate and not an official cutoff.
- Use bands: bottom, below average, average/borderline, above average, strong, top-tier.
- Explain what evidence would move the paper to the next band.
- Do not claim exact acceptance probability.
- Do not claim exact percentile unless the user provides a calibrated comparison set.

## Confidence

Use 1-5:

- 5: full paper, appendix, venue criteria, and relevant related-work search available.
- 4: full paper available; minor missing context.
- 3: main paper available but appendix/code/current policy incomplete.
- 2: partial draft or section-only review.
- 1: abstract/proposal only or weak domain match.

Low confidence changes certainty, not automatically the score.

## Consistency Check

Before finalizing scores:

1. Does the overall score match the strongest unresolved weakness?
2. Would a skeptical reviewer repeat a fatal concern?
3. Are strength claims backed by exact manuscript evidence?
4. Are score-change conditions concrete and feasible?
5. Is the score calibrated to the named venue rather than generic positivity?

## Mandatory Scorecard Output

After every review, output the following structured scorecard. Do not skip dimensions. Keep prose concise unless the user requests a detailed rationale.

```markdown
## Scorecard

| Dimension | Score (1-5) | Confidence (1-5) | Evidence basis | Deduction / score-change condition |
|:---|:---:|:---:|:---|:---|
| Novelty | [1-5] | [1-5] | [section/paragraph/line ref] | [deduction and repair condition] |
| Soundness | [1-5] | [1-5] | [section/paragraph/line ref] | [deduction and repair condition] |
| Evidence | [1-5] | [1-5] | [section/paragraph/line ref] | [deduction and repair condition] |
| Significance | [1-5] | [1-5] | [section/paragraph/line ref] | [deduction and repair condition] |
| Clarity | [1-5] | [1-5] | [section/paragraph/line ref] | [deduction and repair condition] |
| Reproducibility | [1-5] | [1-5] | [section/paragraph/line ref] | [deduction and repair condition] |
| Ethics / Limitations | [1-5] | [1-5] | [section/paragraph/line ref] | [deduction and repair condition] |

**Overall:** [1-10]  | **Scholarly Confidence:** [1-5]

**Recommendation:** [accept/weak-accept/borderline/weak-reject/reject]
**Verdict:** [What condition(s) would raise or lower the score by 1 point?]
```

## Scoring Rules

1. All dimensions must be scored. Do not skip dimensions because they are inconvenient. If a dimension genuinely does not apply, score it by the closest applicable standard and state the limitation.
2. Each score must be backed by at least one verifiable manuscript reference. Do not write "The paper is not well organized." Write "Section 3.1 (para 2) introduces a method without naming or motivating the insight and fails to separate the differential contribution from the components. 3/5 clarity."
3. Evidence means manuscript evidence, not promise. 1/5 evidence means the cited evidence is either not present or not persuasive. 5/5 means evidence is conclusive and includes ablations, robustness, and failure analysis.
4. Confidence is not a dimension score. Confidence is an estimate of how well evidence can be assessed without guesswork. Use 1/5 when there are almost no verifiable evidence citations or when an appendix/code is missing. Use 5/5 when all evidence is verifiable against the manuscript.
5. Never round scores. If the paper is between 6 and 7, pick one and explain why the tie-breaker is decisive.

## Score-Change Conditions

After the scorecard, include a compact condition table:

| Change | Condition | Likely affected dimensions | Expected movement |
| --- | --- | --- | --- |
| Raise score | [concrete evidence/edit] | [dimensions] | [+0.5/+1 overall or dimension-only] |
| Lower score | [failure revealed by closer inspection] | [dimensions] | [-0.5/-1 overall or fatal] |
| No quick change | [issue requiring new result or new method] | [dimensions] | [unlikely before submission] |
