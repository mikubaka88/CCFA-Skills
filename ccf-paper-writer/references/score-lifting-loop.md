# Score-Risk Loop

Use this file when the user reports weak review scores, asks to reduce rejection risk, requests a pre-submission check, or wants a paper revised for AAAI/NeurIPS/ICML/ICLR/ACL/CVPR or another CCF-A venue.

## Core Rule

Reduce review risk by fixing reviewer deductions, not by making the prose sound more positive. A claim can be strengthened only when the paper contains or can add evidence. Otherwise weaken the claim, add the missing evidence, or mark the issue as requiring new results.

Before running this loop, load `references/writing-checklists.md` and use its score-risk and final-readiness checks.

## Loop

1. Establish the target:
   - Venue and track.
   - Current draft state.
   - Current known review scores, if any.
   - Target threshold: default to "no fatal reject risk and at least weak-accept stance".
2. Build or refresh the global story:
   - task -> gap -> root challenge -> insight -> mechanism -> evidence -> limitation.
3. Run a reviewer deduction scan:
   - contribution unclear,
   - novelty weak,
   - significance unclear,
   - soundness risk,
   - evidence weak,
   - missing baseline or related work,
   - missing ablation/proof/study,
   - reproducibility gap,
   - unclear figures/tables,
   - overclaim,
   - limitations/ethics gap,
   - venue mismatch.
4. Score the draft. If `ccf-paper-reviewer` was explicitly requested or confirmed after the optional-module gate, use its scientific review rubric, venue style, and calibration files. Otherwise use the venue adapter plus the scoring table below.
5. Convert every deduction into a fix class:
   - writing-fixable,
   - analysis-fixable,
   - citation/positioning,
   - literature-search,
   - experiment-design,
   - compression,
   - figure/table,
   - reproducibility,
   - requires-new-result,
   - accepted-limitation,
   - venue-mismatch.
6. Revise in priority order:
   - first resolve fatal or high-severity issues,
   - then fix central contribution and evidence alignment,
   - then improve venue-specific presentation,
   - then polish local clarity.
7. Re-score only after checking the revised text. Report conditional review-risk effects only for concrete changes and name the confidence level.
8. Stop only when:
   - no central claim is unsupported,
   - no likely reviewer repeats a fatal concern,
   - venue-specific evidence is visible in the main paper,
   - remaining weaknesses are honest limitations or require new results.

## Fast Scoring Table

Use 1-5 per criterion and 1-10 overall if no venue-specific scale is supplied:

```text
Contribution / novelty:
Significance / venue relevance:
Technical soundness:
Evidence / experiments / proof / study:
Clarity / organization:
Positioning / related work:
Reproducibility:
Ethics / limitations:
Overall:
Confidence:
```

Interpretation:

- 8-10: likely accept range if venue fit is strong.
- 7: weak accept, still vulnerable in discussion.
- 5-6: borderline; must fix one or more score blockers.
- 4: weak reject; at least one major concern.
- 1-3: clear reject or fatal issue.

## Fixability Table

```text
Issue:
Likely reviewer wording:
Criterion affected:
Severity: high / medium / low
Fix class:
Can writing fix it? yes / partly / no
Required evidence:
Where to revise:
Concrete edit:
Risk-reduction condition:
Status: open / fixed / requires new result / accepted limitation
```

## Score-Improving Writing Moves

Use these moves only when supported by the manuscript:

- Put the contribution claim early and make it specific.
- Name the closest prior work and state the exact difference.
- Tie each contribution to visible evidence.
- Replace broad claims with scoped, testable claims.
- Explain why the method works, not just that it performs well.
- Move decisive evidence into the main text or signpost appendix evidence clearly.
- Use literature search for stale or missing closest work instead of adding guessed citations.
- Use experiment design for missing baselines, ablations, or result-table structure instead of inventing numbers.
- Use compression for page-limit fixes instead of deleting claim-critical evidence.
- Add figure/table captions that state what a reviewer should learn.
- Make limitations precise so they bound risk instead of weakening the whole paper.
- Align Abstract, Introduction, Experiments, and Conclusion claims.

## Venue-Specific Score Lift

- AAAI: make AI contribution, soundness, relevance, responsible research, and reproducibility explicit.
- NeurIPS/ICML/ICLR: tie insight to mechanism and evidence; separate contribution types; show why the community gains knowledge.
- CVPR/ICCV/ECCV: strengthen visual evidence, fair baselines, ablations, and qualitative failure analysis.
- ACL: clarify task/data/annotation validity, soundness, usefulness, replicability, and ethics.
- DB/KDD/IR: show realistic workload, scale, effectiveness, efficiency, and deployment or user utility.
- Systems: show real bottleneck, implementation detail, end-to-end evaluation, and operational boundaries.
- Security: define threat model, guarantees, disclosure/ethics, bypasses, and scope.
- HCI: align research question, participants, method, analysis, ethics, and claim scope.
- Theory: state model, assumptions, theorem novelty, proof intuition, and relation to known barriers.

## Output Format

```text
Current likely score:
Target score:
Main blockers:
Fixability table:
Priority revision queue:
Claims to strengthen:
Claims to weaken:
Evidence to add:
New results required:
Revised text or exact edit instructions:
Post-revision score:
Remaining risk:
```
