# Venue Review Styles

Use this file after identifying the target venue or CCF-A family. Treat it as a weighting and evidence selector. If current-year policy, page limits, or official review forms matter, verify the official venue page first.

## AAAI

Primary dimensions: significance and novelty of contributions, theoretical or empirical soundness, relevance to the AAAI community, clarity, responsible research, and reproducibility.

Review emphasis:

- Reward substantive AI contribution, not just application packaging.
- Check whether the problem, method, experiments, analyses, and claims fit AAAI's broad AI audience.
- Require reproducibility details, proof/algorithm clarity, datasets, metrics, and responsible-research handling when relevant.
- Penalize unclear engagement with previous literature, unjustified AI-based approach, weak evaluation, or overbroad social-impact claims.

## NeurIPS

Primary dimensions: quality, clarity, significance, and originality, interpreted by contribution type.

Review emphasis:

- Match standards to contribution type: theory, dataset/evaluation, benchmark, concept/feasibility, empirical method, negative result, or analysis.
- Do not require SOTA empirical wins for theory-only papers, but require correctness and clear assumptions.
- For empirical work, require fair baselines, ablations, robustness, and honest limitations.
- Strong papers explain why others will use, build on, or learn from the result.

## ICML

Primary dimensions: technical quality, significance, novelty/originality, clarity, reproducibility, and fit to ML.

Review emphasis:

- Separate algorithmic or theoretical novelty from empirical performance.
- Require enough experimental breadth to justify general ML claims.
- Penalize weak statistical practice, missing strong baselines, unclear training/evaluation details, and overstated generalization.
- Reward clean problem formulation, theory/intuition, and evidence that explains why the method works.

## ICLR

Primary dimensions: value to the community, new knowledge, soundness, novelty, significance, clarity, and discussion responsiveness.

Review emphasis:

- Ask whether the submission brings sufficient value to the community.
- Prioritize conceptual clarity, representation/learning insight, empirical soundness, and clear distinction from prior work.
- For revision planning, identify which clarifications could reasonably raise a reviewer score.
- Penalize claims that are impressive in wording but not grounded in evidence or theory.

## ACL / ARR

Primary dimensions: soundness, excitement/usefulness, reproducibility, ethics, clarity, and fit for ACL readers.

Review emphasis:

- Soundness covers methodological validity, experimental design, annotation/data quality, linguistic or semantic validity, and evaluation validity.
- Excitement is more subjective; improve it through clear usefulness, insight, surprising finding, strong resource, new framing, or broad relevance.
- Reproducibility and responsible NLP details matter: data, annotation, human subjects, bias, societal impact, and checklist support.
- For resubmissions, explicitly show how prior review concerns were addressed.

## CVPR / ICCV / ECCV

Primary dimensions: novelty, technical quality, empirical validation, visual evidence, clarity, and fair comparison.

Review emphasis:

- Treat figures, qualitative examples, failure cases, and visual comparisons as evidence, not decoration.
- Require strong recent baselines, ablations, cross-dataset tests, robustness, and fair protocol.
- Penalize cherry-picked visuals, missing failure analysis, low-resolution or unreadable figures, and unclear relation to close CV work.
- Reward inspectable evidence and concise claims tied to benchmarks and visual examples.

## KDD / SIGMOD / VLDB / ICDE / SIGIR

Primary dimensions: realistic problem setting, novelty, effectiveness, efficiency, scalability, system or algorithm detail, and user/data utility.

Review emphasis:

- Require realistic workloads, datasets, query/search/user scenarios, and deployment constraints.
- Evaluate both effectiveness and efficiency when both are claimed.
- Penalize toy-only evidence, missing indexes/pipeline details, unclear complexity, and weak large-scale validation.

## Systems / Architecture / Networking / Storage

Primary dimensions: real problem, design soundness, implementation detail, evaluation realism, end-to-end impact, and operational boundaries.

Review emphasis:

- Start from bottlenecks, workloads, deployment pain, or hardware/network constraints.
- Require implementation specifics, baselines, sensitivity studies, overheads, and realistic workloads.
- Penalize benchmark artifacts, unrealistic assumptions, and missing failure modes.

## Security / Privacy / Cryptography

Primary dimensions: threat model, novelty, correctness, practical impact, responsible disclosure, and formal or empirical security evidence.

Review emphasis:

- Define attacker, defender, assumptions, scope, and guarantees early.
- For attacks, prove real-world impact and handle disclosure/ethics.
- For defenses, test bypasses, false positives/negatives, deployment constraints, and residual risk.
- For cryptography, prioritize definitions, assumptions, proof structure, and theorem readability.

## Software Engineering / PL / Formal Methods

Primary dimensions: problem precision, formal or empirical soundness, tool usefulness, scalability, developer relevance, and threats to validity.

Review emphasis:

- Define programs, properties, language features, or developer tasks precisely.
- For empirical SE, check dataset construction, baselines, metrics, statistical practice, and threats to validity.
- For PL/FM, require proof roadmaps, assumptions, soundness/completeness boundaries, and auditability.

## HCI / CSCW / UbiComp / UIST

Primary dimensions: research question, human problem, study design, analysis validity, ethics, and design/system contribution.

Review emphasis:

- Connect research questions to methods, participants, measures, analysis, and claims.
- For qualitative work, check coding, themes, triangulation, and reflexivity.
- For systems, keep interaction design and user value central.
- Penalize unsupported broad claims from narrow populations.

## Graphics / Visualization / Multimedia / VR

Primary dimensions: visual or perceptual contribution, technical pipeline, comparison quality, user/perceptual evidence, and generalization.

Review emphasis:

- Make visual improvement inspectable through high-quality figures or demos.
- Combine metrics with qualitative evidence and user/perceptual studies when needed.
- Penalize cherry-picked media, weak comparisons, and unclear visual advantage.

## Theory

Primary dimensions: correctness, nontriviality, novelty, precision, relation to known barriers, and proof readability.

Review emphasis:

- State model, assumptions, theorems, and contribution boundaries early.
- Give intuition before dense proof detail.
- Penalize unclear assumptions, missing proof steps, and overclaiming beyond theorem statements.

## Venue-Fit Output

```text
Venue:
Venue family:
Primary scoring dimensions:
Evidence package expected:
Likely reviewer taste:
Likely AC concern:
Biggest mismatch risk:
Writing moves that improve fit:
```
