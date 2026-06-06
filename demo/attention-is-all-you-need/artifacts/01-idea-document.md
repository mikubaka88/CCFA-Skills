# 01 - Idea Document

Owner: `ccf-idea-optimizer`

Target venue assumption: NeurIPS-style machine learning conference.

## One-Sentence Idea

Build a sequence transduction model whose sequence modeling is handled entirely by attention, eliminating recurrent and convolutional layers while preserving translation quality and improving parallelizable training.

## Problem

Sequence transduction models need to capture token dependencies across long sequences. Recurrent models process positions sequentially; convolutional models reduce sequential dependency but still need stacked layers to connect distant positions.

## Gap

The core modeling question is whether attention alone can provide enough interaction structure for high-quality machine translation, while reducing sequential operations and long dependency paths.

## Insight

Self-attention can directly connect positions in a sequence, making the maximum path length constant for full self-attention and enabling more parallel computation than recurrence.

## Method Plan

1. Use an encoder-decoder Transformer architecture.
2. Replace recurrent/convolutional sequence modeling with multi-head self-attention.
3. Add positional encodings so order information remains available.
4. Use feed-forward blocks, residual connections, normalization, and regularization to stabilize training.

## Evidence Plan

| Claim | Required evidence | Source in demo |
| --- | --- | --- |
| Attention-only modeling is viable for MT. | WMT En-De and En-Fr BLEU. | `official-data.md`, `result-tables.md` |
| It improves parallelizability/path length. | Complexity and path-length table. | `official-data.md` |
| Model design choices matter. | Ablation categories. | Original paper Table 3, summarized without extra unverified values. |

## Risk Register

- Prior attention mechanisms existed; novelty must be framed as replacing the sequence modeling backbone, not inventing attention.
- BLEU results are official historical values, not reproduced in this demo.
- Current NeurIPS policy and benchmark expectations must be rechecked for any real submission.

## Next Owner

`ccf-idea-reviewer` for idea-level risk scoring, then `ccf-literature-searcher` and `ccf-experiment-designer` for evidence grounding.
