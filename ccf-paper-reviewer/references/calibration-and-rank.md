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

When the user asks for rank or cohort-relative quality, require an inspectable comparable set, common rubric, and declared cohort. Report only the rank supported by those inputs. Without them, use the absolute stance anchors above and omit relative bands, percentiles, outperformed counts, and distribution plots. CSPaper's public rank method depends on its own cohort and calibration; a CCFA score is not interchangeable with it.

## Confidence

Use 1-5:

- 5: full paper, appendix, venue criteria, and relevant related-work search available.
- 4: full paper available; minor missing context.
- 3: main paper available but appendix/code/current policy incomplete.
- 2: partial draft or section-only review.
- 1: abstract/proposal only or weak domain match.

Low confidence changes certainty, not automatically the score.

## Cross-Version Calibration

For re-review or manuscript-version comparison, load `version-comparison.md`. Freeze dimensions, weights, anchors, reviewer roles, thresholds, and evidence standard before comparing versions. Report relative progress, current absolute readiness, and comparison confidence separately. Every decrease must be traceable to a current-version regression or newly revealed evidence. Previously undetected issues apply consistently to both versions rather than silently lowering only the current score.

## Consistency Check

Before finalizing scores:

1. Does the overall score match the strongest unresolved weakness?
2. Would a skeptical reviewer repeat a fatal concern?
3. Are strength claims backed by exact manuscript evidence?
4. Are score-change conditions concrete and feasible?
5. Is the score calibrated to the named venue rather than generic positivity?
6. For version comparison, did both versions use the same frozen contract and did every decrease pass the provenance rule?

## Mandatory Scorecard Output

For standard scientific/full review, put this scorecard inside the Critical Reviewer Ratings section of `fixed-output-format.md`. Use an explicit venue form when available. For writing-only or narrow assessment, use only its applicable criteria; honor no-score requests with qualitative judgments. If the available material cannot support an overall numerical judgment, give an evidence-limited stance and coverage instead of filling the Overall field with a guessed number. A verified central contradiction can support a negative stance even when other dimensions remain unassessed.

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

1. Assess each applicable dimension. Use `N/A` for an inapplicable criterion and `not assessed` when necessary material was not supplied; neither is zero. Do not invent a substitute score for a criterion outside scope. Missing support for an actual manuscript claim can justify a low Evidence score; unavailable excerpts do not establish a whole-paper defect.
2. Each score must be backed by at least one verifiable manuscript reference. Do not write "The paper is not well organized." Write "Section 3.1 (para 2) introduces a method without naming or motivating the insight and fails to separate the differential contribution from the components. 3/5 clarity."
3. Evidence means manuscript evidence, not promise. 1/5 evidence means the cited evidence is either not present or not persuasive. 5/5 means evidence is conclusive and includes ablations, robustness, and failure analysis.
4. Confidence reflects how well the relevant claims could be checked and familiarity with the closest work. Identify which decisive judgment an unavailable appendix or code prevents; its absence alone does not force confidence to 1/5. Separate confidence from quality and scientific stance.
5. Never round scores. If the paper is between 6 and 7, pick one and explain why the tie-breaker is decisive.

## Score-Change Conditions

After the scorecard, include a compact condition table:

| Change | Condition | Likely affected dimensions | Expected movement |
| --- | --- | --- | --- |
| Raise score | [concrete evidence/edit] | [dimensions] | [+0.5/+1 overall or dimension-only] |
| Lower score | [failure revealed by closer inspection] | [dimensions] | [-0.5/-1 overall or fatal] |
| No quick change | [issue requiring new result or new method] | [dimensions] | [unlikely before submission] |
