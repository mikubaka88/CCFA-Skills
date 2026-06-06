# 03 - Idea Review

Owner: `ccf-idea-reviewer`

Target: ICLR-style evaluation of the idea before manuscript writing.

## Verdict

Proceed, but only if the novelty claim is architecture-level and the evidence story is explicit. The idea is strong because it replaces the sequence modeling backbone rather than adding a module to an existing recurrent system. It becomes weak if written as "we use attention for machine translation" because attention in neural MT already existed.

## Score Table

| Dimension | Score | Evidence | Main risk |
| --- | --- | --- | --- |
| Problem importance | 9/10 | Machine translation is a central sequence transduction task. | Must not overclaim beyond sequence transduction evidence. |
| Insight | 9/10 | Attention as the full backbone is a clean structural shift. | Needs clear distinction from prior attention mechanisms. |
| Method completeness | 8/10 | Encoder-decoder, multi-head attention, positional encoding, FFN blocks, residual/normalization are coherent. | Implementation details and optimization schedule must be sufficiently described. |
| Evidence strength | 8/10 | Official WMT BLEU, path-length analysis, ablations, training cost. | Demo lacks full ablation values and reproduction package. |
| ICLR fit | 8/10 | Strong architecture insight and empirical validation. | Current ICLR would expect more reproducibility, modern baselines, and broader task evidence. |

## Closest Prior-Art Risk

| Prior line | Why close | Required distinction |
| --- | --- | --- |
| Recurrent seq2seq | Same encoder-decoder transduction objective | Transformer changes the representation-building operation. |
| Attention-based NMT | Attention already aligns source and target tokens | Transformer makes attention the main backbone and uses self-attention inside encoder/decoder. |
| Convolutional seq2seq | Parallel sequence modeling alternative | Transformer gives direct pairwise interaction with constant maximum path length under full attention. |

## Required Revision Before Writing

1. Abstract must say the challenge is recurrent/convolutional backbone dependency, not "lack of attention."
2. Introduction must introduce attention as a backbone shift, not as an alignment trick.
3. Method must explain why positional encoding is necessary after removing recurrence and convolution.
4. Experiments must pair every headline BLEU number with dataset and model configuration.
5. Limitation must acknowledge quadratic self-attention cost and historical WMT scope.

## Handoff

`ccf-paper-writer` can proceed to a full ICLR LaTeX draft. The writer must preserve the source paper's mode: task -> bottleneck -> insight -> architecture -> evidence -> bounded limitation.
