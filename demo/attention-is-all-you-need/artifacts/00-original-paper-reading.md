# 00 - Original Paper Reading

Source: Vaswani et al., *Attention Is All You Need*, NeurIPS 2017.

Purpose: read the original paper first, then derive a project idea and CCFA workflow from the paper itself. This is not a reproduction log.

## Reading Notes

### Problem

The paper targets sequence transduction, especially machine translation. Before this work, strong systems relied heavily on recurrent or convolutional sequence modeling, which made long-range dependency modeling and parallel training harder.

### Core Insight

Use attention as the main sequence modeling primitive. Instead of recurrence or convolution, the model represents relationships between tokens through self-attention layers, then uses encoder-decoder attention for conditional generation.

### Method Skeleton

- Encoder-decoder architecture.
- Multi-head self-attention.
- Position-wise feed-forward networks.
- Positional encodings because the model has no recurrence.
- Residual connections, layer normalization, dropout, label smoothing, and Adam schedule.

### Evidence In The Original Paper

- WMT 2014 English-German and English-French machine translation.
- BLEU comparison with previous sequence transduction models.
- Complexity/path-length comparison across self-attention, recurrence, convolution, and restricted self-attention.
- Ablation table over model size, heads, attention dimensions, dropout, positional encodings, and label smoothing.
- Training efficiency comparison with one machine using 8 NVIDIA P100 GPUs.

### Official Values Used In This Demo

- Transformer big reaches 28.4 BLEU on WMT 2014 English-German.
- Transformer big single model reaches 41.0 BLEU on WMT 2014 English-French.
- Base model trains for about 100K steps / 12 hours.
- Big model trains for about 300K steps / 3.5 days.

See `official-data.md` for the source locations.

## Initial CCFA Handoff

- Next owner: `ccf-idea-optimizer`.
- Reason: the paper reading has produced a research direction and evidence basis; the next step is to express it as a reusable idea brief.
