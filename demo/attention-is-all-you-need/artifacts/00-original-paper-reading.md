# 00 - Original Paper Idea Summary

Source: Vaswani et al., *Attention Is All You Need*, NeurIPS 2017.

This file is the source-reading artifact for the demo. It extracts the paper's research idea before any CCFA skill writes, reviews, or rebuts the manuscript.

## Motivation

Sequence transduction models need to map one sequence to another while preserving long-range dependencies. Machine translation exposes this need clearly: a target token may depend on distant source words, phrase-level alignment, global syntax, and previous target-side decisions. A strong architecture should therefore model distant interactions and train efficiently.

## Existing Problem

Before the Transformer, strong neural machine translation systems typically used recurrent or convolutional sequence modeling.

| Existing line | Strength | Remaining problem |
| --- | --- | --- |
| Recurrent encoder-decoder models | Natural order-aware sequence modeling | Sequential computation creates long dependency paths and limits parallel training. |
| Attention over recurrent states | Lets the decoder select relevant source positions | Attention is still auxiliary; the sequence representation backbone remains recurrent. |
| Convolutional sequence models | More parallel than recurrence | Distant tokens communicate through stacked convolutional layers. |

The core unresolved issue is architectural: the main sequence modeling operation does not directly connect all positions in a single layer.

## Insight

Self-attention can be used as the sequence modeling backbone. Instead of processing tokens sequentially or through local convolutional neighborhoods, a self-attention layer lets each token directly read all other tokens. This gives a constant maximum interaction path under full attention. Multi-head attention lets different heads specialize in different relation patterns, while positional encodings restore order information.

## Concrete Solution

The paper builds an encoder-decoder architecture with:

| Component | Role |
| --- | --- |
| Multi-head self-attention | Direct token-to-token interaction inside encoder and decoder. |
| Masked decoder self-attention | Autoregressive target-side generation without seeing future tokens. |
| Encoder-decoder attention | Target queries read source-side representations. |
| Position-wise feed-forward networks | Independent nonlinear transformation at each position. |
| Positional encodings | Supply order information after removing recurrence/convolution. |
| Residual connections, layer normalization, dropout, label smoothing | Stabilize and regularize training. |

## Results Used In This Demo

Only official values from the original paper are used:

| Claim | Official evidence |
| --- | --- |
| Attention-only sequence transduction is viable. | Transformer big reports 28.4 BLEU on WMT 2014 English-German. |
| The architecture scales to a larger MT dataset. | Transformer big single model reports 41.0 BLEU on WMT 2014 English-French. |
| It improves interaction path length and parallelism. | Official Table 1 compares self-attention with recurrent and convolutional layers. |
| Design choices matter. | Original ablations cover model size, heads, attention dimensions, dropout, positional encoding, and label smoothing. |

## Contribution Project Idea

If this idea were prepared as an ICLR-style submission, the project should be framed as:

> A sequence transduction architecture showing that attention can replace recurrence and convolution as the main representation-building primitive.

The strongest contribution type is architecture-level insight plus empirical validation, not the invention of attention itself.

## Source Writing Pattern

The original paper's writing mode is:

1. Start from a widely understood task: sequence transduction / machine translation.
2. State a structural bottleneck in previous architectures: sequential computation and long paths.
3. Introduce a concise insight: attention alone can model dependencies.
4. Present the architecture as a clean replacement, not a small patch.
5. Support the claim with headline results, complexity/path-length comparison, and ablations.

This source pattern is what `ccf-paper-writer` should preserve in the ICLR draft: task -> bottleneck -> insight -> architecture -> evidence -> bounded limitation.
