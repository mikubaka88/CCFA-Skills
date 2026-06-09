# 02 - ICLR Closed-Loop Skill Run

This file records the intended closed loop across the current 15 runtime skills. It is not a routing checklist only: each row names a concrete artifact or decision produced by that skill.

| Step | Skill | Input | Concrete output |
| --- | --- | --- | --- |
| 1 | `ccf-project-scaffolder` | Target venue ICLR, source paper, demo directory | `ccfa.yaml`, `paper/attention_iclr_submission.tex`, copied `paper/iclr2026_conference.sty`. |
| 2 | `ccf-pipeline-orchestrator` | `ccfa.yaml`, source-reading notes | Stage gates: source reading -> idea brief -> idea review -> evidence plan -> ICLR manuscript -> writing review -> scientific review -> integrity audit -> submission check -> rebuttal. |
| 3 | `ccf-idea-optimizer` | Original paper reading | `01-idea-document.md`, with problem-gap-insight-method-evidence framing. |
| 4 | `ccf-idea-reviewer` | Idea brief | `03-idea-review.md`, strict ICLR novelty/soundness/evidence verdict. |
| 5 | `ccf-literature-searcher` | Idea and source-related lines | Related-work targets: recurrent seq2seq, attention NMT, convolutional seq2seq, GNMT, WMT setup. |
| 6 | `ccf-experiment-designer` | Idea, official data | Evidence matrix, BLEU table, complexity table, ablation plan, training-cost note. |
| 7 | `ccf-paper-writer` | Idea, venue guide, evidence artifacts | Full ICLR LaTeX manuscript: `paper/attention_iclr_submission.tex`. |
| 8 | `ccf-paper-reviewer` | ICLR manuscript | `04-review-and-rebuttal.md`: writing review and scientific review with concrete revision actions. |
| 9 | `ccf-integrity-auditor` | Manuscript, official data | Claim/number/citation audit table inside `04-review-and-rebuttal.md`. |
| 10 | `ccf-submission-checker` | TeX, style, venue guide | `05-submission-check.md`: ICLR double-blind, page, build, artifact, metadata checks. |
| 11 | `ccf-rebuttal-writer` | Simulated reviews | Rebuttal draft and revision ledger inside `04-review-and-rebuttal.md`. |
| 12 | `ccf-common` | Whole demo | Artifact ownership and trigger-boundary consistency. |
| 13 | `ccf-skill-forger` | Skills and demo quality | Writer policy upgrades, ICLR guide fix, demo self-audit in `06-family-self-audit.md`. |

## Gate Decisions

| Gate | Pass condition | Demo status |
| --- | --- | --- |
| Idea gate | Contribution is not framed as "inventing attention"; it is framed as attention replacing the backbone. | Pass with strict framing condition. |
| Evidence gate | Main claims have official values or explicit missing-value markers. | Pass for headline BLEU/path-length; partial for ablations. |
| Writing gate | Full ICLR manuscript exists and preserves the source paper's writing mode. | Pass: 6-page LaTeX draft compiles. |
| Review gate | Writing and scientific risks are concrete enough to revise. | Pass: review table names exact claims and sections. |
| Submission gate | TeX builds, ICLR guide is current enough for demo, artifact gaps are named. | Demo pass; real submission still requires current policy and artifact package. |

## Closed-Loop Output Principle

The previous demo was too short because it treated skills as route labels. The corrected loop requires every skill to leave a useful artifact: a decision, table, draft section, review finding, audit result, or revision action.
