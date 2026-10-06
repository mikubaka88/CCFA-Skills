# Deep Reading Protocol

Load this when a request needs the full checklist rather than the router alone. It defines what counts as a completed close reading of one paper.

## Reading Order

The order the paper prints in is a teaching order, not the order the work happened in. Read the body, then the appendix, then return to the introduction with the results already known, so the framing can be compared against what was actually demonstrated.

Read figures and tables as evidence rather than illustration. For each one, state what the authors want a reader to believe from it, then look for details inside it that do not support that reading: a curve that crosses later, an error bar wider than the gap between compared methods, a log axis hiding a constant-factor difference, a single seed standing in for a variance claim. The first figure of a paper usually carries the bet, and deserves separate treatment.

Record disagreements as you go. Body text that reports a different configuration, dataset size, or metric than the appendix is a finding, not a transcription error to smooth over.

## Worked Micro-Example Standard

A formula is understood when it can be evaluated by hand on a small instance without returning to the paper.

- Give each symbol its shape, its units or meaning, and where it comes from.
- State what the formula is for before stating the formula.
- Follow the key formulas with a micro-example that uses concrete numbers small enough to compute in a few lines, and carry it to the end. "Substituting gives" is not a worked example.
- Prefer one example that exposes the whole mechanism over several that only restate the definition.
- When a formula reduces to a familiar case, say which case, and show the reduction.

## Load-Bearing Judgement

For each distinctive component, choose one of three positions and say which evidence supports it:

- **Load-bearing** — removing it collapses the reported result; supported by an ablation, a controlled comparison, or an appendix result.
- **Contributing** — removing it measurably weakens the result without collapsing it.
- **Decoration** — the result survives without it, or the paper never isolates it.

When the paper runs no control that isolates a component, the position is "not established", and that is the answer to report. Do not infer load-bearing status from how prominently a component is presented.

## Evidence Boundary Review

Check each of these and report only what the paper's own material supports:

- **Numbers** — do body text, tables, and figures agree? Are sample sizes, error types, and units stated?
- **Baseline alignment** — same data, same training budget, same tuning effort? An under-tuned baseline does not establish an improvement.
- **Selection pressure** — were hyperparameters, checkpoints, or prompts chosen on the test set, or with test knowledge?
- **Leakage** — does any preprocessing see test data, directly or through fitted statistics?
- **Cost** — compute, memory, latency, and the deployment shape the method assumes.
- **Scope** — the conditions under which the headline claim stops holding, and whether the paper states them.

## Hedging And Gaps

Preserve the source's modality. "May" is not "does"; "suggests" is not "shows"; "some settings" is not "all settings"; an unreported result is not evidence of no effect.

Where the paper does not report something the conclusion would need, write that the paper does not report it. Do not substitute a plausible number, an assumed default, or a remembered value from a similar paper. Mark any judgement that goes beyond the supplied material as inference, and keep inference separate from what the source states.

## Output Discipline

Report the scope actually read — body, appendix, supplementary, or a stated subset — and do not imply fuller coverage than was achieved. A long paper is not a reason to degrade the reading into a summary. If the reading is incomplete, say where it stopped.

Do not produce a review verdict, a score, or a novelty judgement from inside this skill. Those belong to `ccf-paper-reviewer` and `ccf-idea-reviewer`.
