# Revision Actions

Use this file to convert writing-review deductions into concrete improvements. The goal is a closed loop: diagnose, revise, and confirm that the same reviewer confusion would not remain.

Before producing a revision plan, load `references/review-checklists.md` and apply its writing-revision checks. If the user asks for scientific re-score, acceptance-style scoring, simulated reviewers, or AC/meta-review, route to `ccf-paper-reviewer` under the CCFA handoff mode.

## Action Classes

Classify every issue:

- Writing-fixable: contribution statement, paragraph flow, terminology, figure narration, related-work framing, limitation wording.
- Structure-fixable: reorder sections, move paragraphs, split mixed paragraphs, merge repeated paragraphs, or change section headings.
- Claim-qualification: weaken, scope, move, or support claims that currently exceed evidence.
- Analysis-fixable: add deeper explanation, error analysis, complexity analysis, sensitivity analysis, qualitative analysis, or proof intuition using existing results.
- Citation/positioning: add close related work and explain the technical difference, not just a citation.
- Figure/table: improve readability, captions, grouping, visual examples, failure cases, or main-text signposting.
- LaTeX/format: fix template, labels, references, citations, captions, equations, algorithms, package conflicts, or spacing/style violations.
- Compression: cut redundant background, move detail to appendix, merge paragraphs, shorten captions, or reduce repetitive result narration.
- Reproducibility: add pseudocode, implementation details, hyperparameters, dataset splits, metrics, code/data availability, artifact notes.
- Requires-new-result: new baseline, ablation, dataset, theorem, user study, measurement, statistical test, or deployment evaluation.
- Accepted-limitation: disclose scope honestly when the issue cannot be solved before submission.
- Venue-mismatch: change framing, track, or target venue.

## Deduction-To-Action Map

### Contribution unclear

Reviewer deduction: "I cannot tell what is new."

Actions:

- Add a one-sentence contribution claim in Abstract and early Introduction.
- State contribution type: method, theory, dataset, benchmark, system, analysis, study, resource, or negative result.
- Separate "what is new" from "what is inherited from prior work."
- Add a contribution table only if it clarifies close comparisons.

### Novelty weak

Reviewer deduction: "This appears incremental or already known."

Actions:

- Identify the closest prior work and write the exact difference.
- Avoid claiming first-ever unless verified.
- Reframe novelty as insight, formulation, evidence, scale, robustness, efficiency, or integration if method novelty is limited.
- Add missing citations or baseline comparisons.

### Significance unclear

Reviewer deduction: "Why should this venue care?"

Actions:

- Tie the problem to a concrete community bottleneck.
- Show who will use the result and what new capability or understanding it enables.
- Replace broad motivation with field-specific stakes.
- Add a "why now" sentence if the problem is timely.

### Soundness risk

Reviewer deduction: "Claims may not be technically valid."

Actions:

- State assumptions and boundaries explicitly.
- Add proof sketch, derivation, algorithmic invariant, threat model, statistical test, or study-design justification.
- Remove or weaken claims that exceed the evidence.
- Add a limitation if the concern is real but bounded.

### Evidence weak

Reviewer deduction: "The evaluation does not support the main claim."

Actions:

- Map each claim to an experiment/proof/study.
- Add strongest baseline, ablation, robustness check, error analysis, or dataset.
- If no new result can be added, narrow the claim to what current evidence supports.
- Put the most decision-relevant evidence in the main text, not only appendix.

### Baseline or related work missing

Reviewer deduction: "Comparison is incomplete."

Actions:

- Add the strongest recent baseline or explain why it cannot be run.
- Use fair protocols and report comparable metrics.
- Add a close-related-work paragraph that explains differences in task, assumption, method, or evidence.
- Avoid dismissive wording about prior work.

### Ablation missing

Reviewer deduction: "The proposed components are not justified."

Actions:

- Add component ablation, sensitivity study, or controlled variant.
- If an ablation is impossible, provide mechanistic analysis and mark it as a limitation.
- Explain how each component connects to the central insight.

### Reproducibility gap

Reviewer deduction: "I cannot reproduce or audit the result."

Actions:

- Add pseudocode, hyperparameters, dataset preprocessing, split details, metrics, hardware, training schedule, random seeds, and artifact availability.
- Reference appendix/code clearly from the main paper.
- Add details for negative or failed experiments if they affect interpretation.

### Clarity and story weak

Reviewer deduction: "The paper is hard to follow."

Actions:

- Use a global storyline: task -> gap -> root challenge -> insight -> mechanism -> evidence -> limitation.
- Make each paragraph carry one message.
- Stabilize terminology across sections.
- Use figures and captions to explain mechanism and evidence.

### Paragraph logic broken

Reviewer deduction: "This paragraph mixes roles or does not advance the argument."

Actions:

- Assign the paragraph one job: motivation, gap, insight, method, evidence, limitation, or transition.
- Split mixed claim/evidence/background paragraphs.
- Move details to the section where a reviewer expects them.
- Replace vague transition sentences with the specific logical link to the next paragraph.

### LaTeX or format risk

Reviewer deduction: "The submission looks careless or may violate venue rules."

Actions:

- Fix template mode, anonymization/camera-ready settings, page limits, and appendix placement.
- Resolve undefined references, duplicate labels, missing citations, and stale figure/table references.
- Remove style-breaking spacing hacks unless the venue template permits them.
- Make captions self-contained and ensure tables/figures remain readable without excessive scaling.

### Terminology or notation inconsistent

Reviewer deduction: "I cannot tell whether these terms refer to the same object."

Actions:

- Choose one canonical term for each concept and use it throughout.
- Define symbols before first use and reuse notation consistently.
- Align abstract, introduction, method, experiments, and conclusion wording for the same contribution.
- Add a notation table only if the method section is notation-heavy.

### Overclaim

Reviewer deduction: "The paper overstates its result."

Actions:

- Replace universal language with scoped language.
- Move speculative claims to limitations or discussion.
- Add conditions under which the method works or fails.
- Align Abstract and Conclusion claims with actual evidence.

### Venue mismatch

Reviewer deduction: "This is not a good fit for the venue."

Actions:

- Reframe around the venue's audience and evidence standards.
- Move application details behind the technical contribution if targeting AI/ML.
- Move technical novelty behind user value if targeting HCI.
- Consider a different venue if the contribution type cannot fit.

## Revision Queue Format

```text
Priority:
Issue:
Reviewer deduction:
Criterion affected:
Fix class:
Required edit:
Evidence needed:
Where to revise:
Risk-reduction condition:
Status: open / fixed / requires new result / accepted limitation
```

## Re-Score Gate

After revision, ask:

1. Would a skeptical reviewer repeat the same criticism?
2. Does each major claim have visible evidence?
3. Are the closest baselines and related works handled?
4. Are limitations honest and bounded?
5. Is the target venue's evidence package visible in the main text?
6. Does the paragraph now have one clear role and one retained message?
7. Are labels, citations, captions, notation, and format issues actually fixed in source?

Do not mark an issue fixed until the revised text or available evidence would plausibly change a criterion score.
