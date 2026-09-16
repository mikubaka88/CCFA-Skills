# Universal Review Rubric

Use this file for generic computer-science conference paper review when the venue is unknown or when a venue-specific guide does not define a dimension.

## Reading Protocol

Use a three-pass read:

1. First pass: establish category, context, correctness, contributions, and clarity from title, abstract, introduction, headings, conclusion, and references.
2. Second pass: inspect the core argument, figures, tables, experiments, proofs, related work, limitations, and appendix pointers.
3. Third pass: stress-test the central contribution as a reviewer would: assumptions, novelty, evidence, baselines, reproducibility, and failure modes.

## Canonical Rubric And Contribution Type

Use the ordered `generic-7` table in `calibration-and-rank.md` as the sole source of scientific dimensions, labels, and score anchors. Related-work positioning is evidence for Novelty; overall Quality is the synthesis, not another dimension. Do not create duplicate deductions for aliases or for the same finding in several report sections. Verified venue forms and inherited version-comparison rubrics retain their own contracts.

Establish the contribution type before judging support. Check assumptions and proof arguments for theory; claim-relevant comparisons and protocols for empirical work; realistic workloads for systems; and appropriate study design and analysis for human-subject or qualitative work. Request a baseline, ablation, robustness test, or new experiment only when it could resolve a specific central claim. No universal checklist of experiment counts or SOTA wins applies. This manuscript rubric never expands a concept-only idea review.

## Fatal-Risk Triage

Treat the following as prompts for investigation, not automatic rejection triggers. Mark a risk as critical only when verified evidence shows that it independently undermines a central claim or violates an applicable requirement. Check the strongest answer in the manuscript and supplied appendix before retaining the finding:

- The central contribution is unclear.
- The novelty claim collapses under close prior work.
- A main claim lacks evidence.
- A decisive claim requires a comparison that the inspected evidence does not provide.
- The method, proof, threat model, study design, or evaluation protocol is invalid.
- The paper is not reproducible enough for the claim type.
- The venue fit is wrong.
- A policy, anonymity, ethics, data, or responsible-research issue is serious.

## Claim-Evidence Audit

Map each distinct central claim from Abstract, Introduction, and Conclusion to support, reusing repeated claims and anchors. Keep this audit inside the report rather than producing a second full report:

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
