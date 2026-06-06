# Universal Review Rubric

Use this file for generic computer-science conference paper review when the venue is unknown or when a venue-specific guide does not define a dimension.

## Reading Protocol

Use a three-pass read:

1. First pass: establish category, context, correctness, contributions, and clarity from title, abstract, introduction, headings, conclusion, and references.
2. Second pass: inspect the core argument, figures, tables, experiments, proofs, related work, limitations, and appendix pointers.
3. Third pass: stress-test the central contribution as a reviewer would: assumptions, novelty, evidence, baselines, reproducibility, and failure modes.

## Universal Dimensions

Score each dimension on 1-5 unless a venue requires a different scale.

1. Contribution and novelty
   - 5: clear nontrivial contribution that changes knowledge, capability, framing, data, or practice.
   - 4: meaningful contribution with a well-defended novelty claim.
   - 3: incremental but potentially useful contribution; novelty needs sharper positioning.
   - 2: weak novelty or unclear difference from close prior work.
   - 1: no clear contribution or likely overlap with known work.
2. Significance and impact
   - 5: important problem, strong audience relevance, and likely follow-on use.
   - 4: clear value to the target community.
   - 3: useful but narrow or under-motivated.
   - 2: limited audience relevance or unclear practical/scientific importance.
   - 1: trivial, mis-scoped, or not venue-relevant.
3. Technical soundness
   - 5: assumptions, derivations, algorithms, implementation, statistics, and analysis are credible.
   - 4: mostly sound with minor gaps.
   - 3: plausible but has unresolved assumptions or incomplete validation.
   - 2: material correctness or methodology concerns.
   - 1: central claim likely invalid.
4. Evidence and evaluation
   - 5: strong evidence package matched to claims: baselines, ablations, robustness, analysis, proofs, studies, or realistic workloads.
   - 4: adequate evidence with some missing secondary checks.
   - 3: evidence supports part of the story but leaves important claims exposed.
   - 2: weak baselines, missing ablations, insufficient datasets, invalid metrics, or underpowered study.
   - 1: central evidence absent or misleading.
5. Clarity and organization
   - 5: the contribution, mechanism, evidence, and limitations are recoverable after one careful pass.
   - 4: clear overall, with fixable local issues.
   - 3: understandable but requires effort or hidden context.
   - 2: confusing story, unstable terminology, or weak figure/table narration.
   - 1: reviewers cannot reconstruct the contribution.
6. Positioning and related work
   - 5: strongest related work and baselines are handled honestly.
   - 4: close work is mostly covered.
   - 3: important comparisons or citations may be missing.
   - 2: close prior work is omitted or novelty is overstated.
   - 1: likely novelty collapse due to missing prior art.
7. Reproducibility and auditability
   - 5: methods, data, code/artifacts, hyperparameters, protocols, and appendix details enable audit.
   - 4: mostly reproducible with minor omissions.
   - 3: key details exist but require inference.
   - 2: important details missing.
   - 1: results cannot be independently assessed.
8. Ethics, limitations, and responsible research
   - 5: risks, limitations, sensitive data, human subjects, bias, misuse, and environmental cost are handled where relevant.
   - 4: mostly adequate disclosure.
   - 3: limitations are generic or incomplete.
   - 2: material risk is under-addressed.
   - 1: policy or ethics issue may trigger rejection.

## Fatal-Risk Triage

Mark a risk as fatal when it can independently justify rejection:

- The central contribution is unclear.
- The novelty claim collapses under close prior work.
- A main claim lacks evidence.
- The strongest baseline or comparison is missing.
- The method, proof, threat model, study design, or evaluation protocol is invalid.
- The paper is not reproducible enough for the claim type.
- The venue fit is wrong.
- A policy, anonymity, ethics, data, or responsible-research issue is serious.

## Claim-Evidence Audit

For every major claim in Abstract, Introduction, and Conclusion, produce:

```text
Claim:
Where stated:
Evidence provided:
Evidence type:
Strength: strong / adequate / weak / absent
Reviewer deduction:
Required fix:
```

Hard rule: unsupported claims must be weakened, removed, or backed by evidence. Do not recommend rhetorical strengthening for an unsupported claim.

## Review Tone

Be specific, evidence-grounded, and decision-relevant. Name the exact missing artifact or logic gap. Avoid vague statements such as "needs more experiments" unless paired with the experiment, baseline, metric, dataset, or analysis that would change the score.
