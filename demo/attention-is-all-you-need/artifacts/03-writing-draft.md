# 03 - Writing Draft

Owner: `ccf-paper-writer`

Mode: draft + polish + compression + presentation.

## NeurIPS-Style Abstract Draft

We present the Transformer, a sequence transduction architecture based entirely on attention. The model removes recurrent and convolutional sequence modeling layers, using multi-head self-attention to connect positions directly and feed-forward blocks to transform token representations. This design shortens dependency paths and enables highly parallel training. On WMT 2014 English-to-German, Transformer big reports 28.4 BLEU; on WMT 2014 English-to-French, the single model reports 41.0 BLEU. The official paper reports training on one machine with 8 NVIDIA P100 GPUs, with the big English-to-German model trained for about 300K steps over about 3.5 days. These results support attention as a complete sequence modeling backbone for machine translation.

## Introduction Storyline

1. Sequence transduction requires modeling relationships across positions.
2. Recurrent models create sequential computation paths; convolutional models reduce this issue but require stacked layers for distant interactions.
3. Attention can connect sequence positions directly.
4. The key question is whether attention can replace recurrence and convolution as the central architecture, not only act as an auxiliary alignment module.
5. The Transformer answers this with multi-head self-attention, positional encodings, and encoder-decoder attention.
6. Evidence comes from WMT translation quality, complexity/path-length analysis, ablations, and training efficiency.

## Compressed Abstract

Transformer is a sequence transduction architecture built entirely on attention. By replacing recurrent and convolutional sequence modeling with multi-head self-attention and positional encodings, it shortens dependency paths and enables parallel training. The official paper reports 28.4 BLEU on WMT 2014 English-German and 41.0 BLEU on WMT 2014 English-French with Transformer big, supporting attention as a complete backbone for machine translation.

## Talk / Poster Output

Three-slide talk skeleton:

1. Problem: sequence modeling needs long-range dependencies without slow sequential computation.
2. Method: multi-head self-attention replaces recurrence/convolution; positional encodings restore order.
3. Evidence: WMT BLEU, path-length comparison, ablations, and training schedule.

## Writing Boundaries

- No extra benchmark values were added.
- No current NeurIPS policy claims were made.
- Claims are phrased as official-paper results, not demo reproduction results.
