# 01 - ICLR Idea Brief

Owner: `ccf-idea-optimizer`

Target venue: ICLR-style machine learning paper.

## One-Sentence Idea

Replace recurrent and convolutional sequence modeling with multi-head self-attention so that all positions can interact directly while the model remains trainable and competitive on machine translation.

## Problem-Gap-Insight Card

| Field | Content |
| --- | --- |
| Problem | Sequence transduction requires modeling local and long-range token dependencies. |
| Gap | Recurrent backbones create sequential dependencies; convolutional backbones need stacked layers for distant communication. |
| Root cause | The representation-building operation does not connect all positions directly in one layer. |
| Insight | Full self-attention gives constant interaction path length between positions. |
| Method | Transformer encoder-decoder with multi-head attention, positional encodings, feed-forward blocks, residual paths, normalization, and regularization. |
| Evidence | WMT 2014 En-De and En-Fr BLEU, path-length/complexity table, ablations, training-cost report. |
| Limitation | Quadratic self-attention cost in sequence length; evidence is historical WMT translation, not universal sequence modeling proof. |

## Optimized Contribution Claims

1. Attention can serve as the main sequence modeling backbone, not only as a recurrent decoder's alignment module.
2. Multi-head self-attention plus positional encoding forms a complete encoder-decoder architecture for translation.
3. The architecture improves direct token interaction and training parallelism while reporting strong official WMT BLEU values.
4. Complexity/path-length analysis explains why the design is structurally different from recurrent and convolutional alternatives.

## Evidence Plan

| Claim | Required artifact | Current demo status |
| --- | --- | --- |
| Architecture-level novelty | Method section with module roles and related-work distinction | Available in `paper/attention_iclr_submission.tex`. |
| Translation quality | WMT BLEU table | Filled with official values. |
| Parallelism/path-length argument | Complexity table | Filled with official Table 1 summary. |
| Component causality | Ablation table over heads, dimensions, dropout, positional encoding, label smoothing | Planned; not fully filled unless copied from official source. |
| Reproducibility | Data, training schedule, hardware, implementation notes | Partially filled from official values; code/artifact package absent. |

## Reviewer Risks Before Writing

| Risk | Why it matters | Planned mitigation |
| --- | --- | --- |
| "Attention was already known." | Novelty can be misread as an attention mechanism claim. | Frame contribution as replacing the full sequence modeling backbone. |
| "Self-attention is not always cheaper." | Quadratic cost can undercut efficiency claims. | State exact path-length and parallelism claim; do not claim universal cost reduction. |
| "Results are historical official values." | Demo is not a reproduction. | Mark values as official source values and avoid reproduction claims. |
| "Ablations are incomplete in the demo artifact." | ICLR reviewers expect component causality. | Keep missing ablation values explicit and route to experiment designer/integrity auditor. |

## Next Skill

`ccf-idea-reviewer` should judge whether the idea framing is ICLR-worthy before writing. If it passes with conditions, `ccf-paper-writer` should draft a full ICLR LaTeX manuscript rather than an abstract-only sample.
