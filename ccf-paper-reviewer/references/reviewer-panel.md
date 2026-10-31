# Manuscript Review Perspectives

Use perspectives to test the conclusion against distinct evidence. For scientific/full review, synthesize them in the reviewer-perspectives section of the detailed report or within the brief report's findings in `fixed-output-format.md`; do not create one mandatory full report or numeric score per role.

## Evidence Lenses

Select those relevant to the paper and requested scope:

- **Novelty / positioning:** inspect the closest-work difference and strongest overlap claim.
- **Method / soundness:** inspect assumptions, derivations, algorithms, causal reasoning, or system guarantees.
- **Evidence / evaluation:** check whether supplied experiments, proofs, workloads, or studies support the central claims. Match evidence expectations to paper type.
- **Clarity / reader:** reconstruct the contribution, definitions, argument, and figure/table references from the manuscript.
- **Reproducibility / ethics:** examine material protocol details, observed ethical issues, and applicable venue requirements.
- **Domain / application:** assess the importance and realism of the stated problem and contribution.

Writing-only review selects reader, argument, terminology, and presentation lenses; it does not escalate to a scientific acceptance panel.

## Three-View Synthesis

After establishing anchored findings, present a compact synthesis of:

| View | Decisive basis / concern IDs | Stance | What would change it |
| --- | --- | --- | --- |
| Best-supported assessment | Inspectable merits and defects | Evidence-led judgment | Decisive unresolved condition |
| Strongest favorable reading | The best defensible contribution and support | Favorable interpretation if justified | Assumption it depends on |
| Strongest critical reading | A substantiated decision-relevant objection | Critical interpretation if justified | Repair or answer that resolves it |

The views can agree. If no separate favorable or critical case is supported, say so briefly rather than inventing one. Do not assign hypothetical scores first and force reviewers to defend them. Keep one final scorecard in the report; multiple full scorecards are reserved for an explicitly requested reviewer panel or the existing version-comparison contract.

Use actual independent calls only when permitted and useful. Apply the effective `independent_review` preference from `../../ccf-common/references/preferences.md`: `off` disables an unrequested additional independent pass; `auto` needs a consequential unresolved judgment or a requested pre-submission check; `on` favors one complete domain-expert reading for a relevant substantial scientific/full review when it adds value. Current instructions and host limits take precedence. An explicit request enables that pass for the task without changing saved preferences. The primary review, evidence verification, and strongest-counterevidence checks remain mandatory within the requested scope in every mode.

For manuscript scientific/full review, use [plain-expert-review.md](plain-expert-review.md): one available GPT-6 instance receives the manuscript and necessary context in an independent host session. This is a concrete implementation of the same optional pass, not another layer. Choose an entire coherent expert reading rather than splitting its scientific judgment into paragraph, method, and score agents. Writing-only review does not automatically invoke it; concept-only judgment still belongs to the idea reviewer.

The first reader receives scope, phase, source materials/version, and applicable criteria without the lead reviewer's verdict, score, generation history, or other candidates. Reuse source extraction, not upstream judgments. Use the short prompt without importing the full report template into its first assessment. Preserve that response before comparison, then check its evidence and map supported concerns into the canonical report; do not request a duplicate fourteen-section report. Label actual model and execution provenance honestly. A single-agent three-view review is not three independent reviewers or empirical consensus. Missing GPT-6 or fresh-context support limits only this extra pass, not the primary review.

Synthesize using the strongest unresolved finding and actual support, not majority vote or a mean that erases a decisive flaw. Refer to the canonical concern IDs; avoid repeating full criticisms in each view. Preserve frozen reviewer roles for an existing version-comparison contract.
