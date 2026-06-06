# 02 - NeurIPS Skill Run

This file is the ordered dry run. It uses every current runtime skill once, including governance skills, while keeping merged helper abilities inside their owners.

| Step | Skill | Input | Action | Output / gate |
| --- | --- | --- | --- | --- |
| 1 | `ccf-project-scaffolder` | Target: NeurIPS-style demo | Create demo project state. | `ccfa.yaml` exists; no research content invented. |
| 2 | `ccf-pipeline-orchestrator` | `ccfa.yaml`, reading notes | Define stages: read -> idea -> evidence -> write -> review -> audit -> submit -> rebut. | Gate map in this file. |
| 3 | `ccf-idea-optimizer` | `00-original-paper-reading.md` | Convert original paper reading into a problem-gap-insight-method-evidence brief. | `01-idea-document.md`. |
| 4 | `ccf-idea-reviewer` | `01-idea-document.md` | Score idea risk. | Verdict: strong insight, high prior-art framing risk, evidence must be explicit. |
| 5 | `ccf-literature-searcher` | Idea and venue | Identify related-work targets. | Search targets: attention mechanisms, sequence-to-sequence, recurrent MT, convolutional seq2seq, WMT baselines. |
| 6 | `ccf-experiment-designer` | Idea + official data | Design WMT evidence package and real-result tables. | `result-tables.md`; no invented numbers. |
| 7 | `ccf-paper-writer` | Idea + result tables | Draft NeurIPS-style abstract/introduction outline; also show compression and talk-output modes. | `03-writing-draft.md`. |
| 8 | `ccf-paper-reviewer` | Writing draft | Run scientific + writing review. | `04-review-and-rebuttal.md` review section. |
| 9 | `ccf-integrity-auditor` | Draft + official values | Audit claim support, numbers, and citation metadata needs. | `04-review-and-rebuttal.md` audit section. |
| 10 | `ccf-submission-checker` | Draft + venue assumption | Check venue, package, and artifact readiness. | `05-submission-check.md`; cannot pass without compiled PDF/current policy check. |
| 11 | `ccf-rebuttal-writer` | Simulated reviews | Create response strategy, rebuttal draft, and revision ledger. | `04-review-and-rebuttal.md` rebuttal section. |
| 12 | `ccf-common` | Whole demo | Verify routing, privacy/evidence, and artifact contracts. | `skill-self-tests.md`; source-grounded boundaries. |
| 13 | `ccf-skill-forger` | Docs/SVG request | Maintain docs and generated SVG diagrams. | `tools/build_ccfa_diagrams.py` and `assets/ccfa-skills-*.svg`. |

## Idea Reviewer Result

Likely NeurIPS stance if judged before publication:

- Strength: clean and radical architectural simplification.
- Strength: strong training-parallelism motivation.
- Risk: attention was not new; novelty depends on the full architecture and evidence.
- Risk: reviewer skepticism would focus on whether attention-only modeling truly beats strong recurrent/convolutional baselines.
- Gate: proceed only if WMT results, ablations, complexity analysis, and positioning are all explicit.

## Literature Search Targets

This demo does not browse for new current literature because it is a historical paper walkthrough. For a real current submission, `ccf-literature-searcher` should search public sources for:

- Bahdanau-style attention in neural MT.
- Seq2seq recurrent encoder-decoder models.
- Convolutional sequence-to-sequence models.
- WMT 2014 benchmark reporting conventions.
- Efficient sequence modeling and long-range dependency papers.

## Experiment Designer Gate

The experiment plan must include:

- WMT 2014 English-German and English-French main results.
- Baseline comparison table.
- Complexity/path-length comparison.
- Ablations over model size, heads, attention dimensions, dropout, positional encodings, and label smoothing.
- Training cost and hardware statement.

Only values in `official-data.md` are filled in this demo.
