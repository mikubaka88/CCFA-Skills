# Idea Review Rubric

Use this rubric for concept-level assessment, with or without requested numeric scores. Judge the problem, novelty, insight, and mechanism. Experimental results, baselines, ablations, benchmark coverage, reproducibility packages, and submission completeness are outside the default scope. Their absence must not lower an idea score or trigger a request for experiments.

## Default Dimensions

| Dimension | Weight | Question |
| --- | ---: | --- |
| Problem importance and specificity | 20 | Is there a concrete, consequential research problem? |
| Novelty against closest work | 25 | What remains new after accounting for verified prior work? |
| Conceptual insight | 20 | Is there a non-obvious explanation, formulation, or connection? |
| Mechanism and logical soundness | 20 | Do the assumptions and proposed mechanism coherently address the problem? |
| Elegance and component necessity | 10 | Does each component contribute to the central idea? |
| Audience and contribution fit | 5 | Would the intended community value this contribution if realized? |

Weights sum to 100. Method soundness here means conceptual coherence, not demonstrated empirical effectiveness. Distinguish a mechanism that contradicts its own assumptions from a mechanism that has simply not been tested. Conceptual testability means the claim has a discernible meaning and could in principle be wrong; it does not require designing experiments or demanding a completed proof.

## Scoring And Coverage

Standard assessment includes the six-dimension scorecard unless the user asks for no scores. Quick qualitative judgment uses the same criteria without forcing a numeric table.

| Dimension | Weight | Score (1-5) | Basis / concern ID | Change condition |
| --- | ---: | ---: | --- | --- |

Use `not assessed` for a criterion whose basis cannot be inspected, and `N/A` for a criterion outside the agreed scope. Neither is zero. Calculate `weighted score = sum(score * weight) / sum(assessed weights)` and show assessed weight coverage. If no criteria can be assessed, omit the aggregate. Report overall confidence separately. Do not compare totals across ideas with materially different coverage as if they were equivalent.

Unsearched novelty stays unassessed or provisional when credible supplied prior-art evidence exists. Do not impose an arbitrary low novelty score merely because retrieval is unavailable. A known overlap can lower novelty; missing knowledge lowers confidence. Standard novelty judgments use `strict-idea-review.md` for grounding.

## Anchors

- **5:** A compelling concept with a specific problem, substantive differentiation, and a coherent mechanism on this dimension.
- **4:** A strong concept with one localized, repairable gap.
- **3:** A plausible concept with a material ambiguity or modest differentiation that needs a concrete refinement.
- **2:** A demonstrated conceptual weakness, close-work overlap, or contradictory assumption.
- **1:** The current formulation fails on this dimension for an identified reason.

Every deduction cites the relevant idea statement, assumption, or verified source and explains what would change the judgment. Missing experimental work is not a conceptual defect.

## Requested Extensions And Historical Comparisons

Assess experiment design, empirical evidence, or execution resources only when the user requests that extension. Place it in a separate optional block; do not silently add its score to the conceptual total. Full experiment design belongs to `ccf-experiment-designer`; assessment of manuscript results belongs to `ccf-paper-reviewer`.

The previous ten-dimension rubric included experimental convincibility and acceptance potential. Preserve existing historical reports and their frozen rubric when comparing versions. Mark a switch to this six-dimension rubric explicitly and rescore both concepts under the same scope before reporting a delta. Do not interpret the new concept score as the old publication-readiness score.
