# Calibration

Use this file after scoring dimensions.

## Weighted Score

Compute:

```text
weighted_score = sum(score_i * weight_i) / 100
```

Report the result on a 1-5 scale and optionally convert to a 100-point table for readability.

## Recommendation Bands

- 4.3-5.0: `accept-to-develop`. Develop aggressively only after closest-work comparison and evidence planning support the central claim.
- 3.7-4.2: `revise`. Promising, but one or two named score blockers must be fixed.
- 3.0-3.6: `pivot`. Keep the best ingredient but change problem, method, evidence, or venue.
- 1.0-2.9: `abandon` unless the user has hidden evidence, a new framing, or a different venue target.
- Any score with high novelty uncertainty: `needs-literature-search` if novelty is decision-critical.

## Fatal Gates

Apply these after the weighted score:

- Novelty <= 2 with high confidence: cap recommendation at `pivot`.
- Novelty unknown and no closest-work search: cap recommendation at `needs-literature-search` unless the user asked for quick mode only.
- Method soundness <= 2: cap recommendation at `pivot`.
- Experimental convincibility <= 2 and no alternative proof/study/system evidence: cap at `pivot`.
- Venue fit <= 2: recommend venue switch or pivot.
- Feasibility <= 2 under fixed deadline: cap at `pivot` or `abandon`.
- No identifiable insight beyond applying known modules: cap recommendation at `pivot`.
- Internal mechanism conflict: cap recommendation at `pivot` until resolved.

## Confidence Labels

Use:

- High: close work, venue fit, and evidence feasibility are well grounded.
- Medium: most inputs are available but literature or resources remain partially uncertain.
- Low: idea is vague, venue is unknown, or closest prior work was not checked.

Do not lower the idea score merely because confidence is low. Lower confidence separately and recommend the next check.

## Fixability Table

```text
Issue:
Affected dimension:
Severity: high / medium / low
Fix class:
Can fix before writing? yes / partly / no
Required evidence or design change:
Risk-reduction condition:
Owner skill: ccf-literature-searcher / ccf-idea-optimizer / ccf-experiment-designer / ccf-paper-writer / ccf-paper-reviewer
```

## Multi-Idea Tournament

For multiple drafts:

1. Normalize every idea first.
2. Score independently before comparing.
3. Apply fatal gates.
4. Prefer the idea with the strongest fixable path, not just highest average.
5. Keep one backup idea if it has lower novelty risk or better feasibility.

## Fairness Rules

- Do not reward hype without mechanism or evidence.
- Do not punish niche ideas if the target venue values depth and rigor.
- Separate "novelty unknown" from "low novelty".
- Do not require experiments for theory ideas, proofs for empirical ideas, or user studies for non-HCI ideas.
- Penalize unsupported acceptance claims, not ambitious but testable ideas.
- Do not hide a reject-level problem under "future work".
- Do not say "worth pursuing" without naming the exact condition under which it becomes worth pursuing.
