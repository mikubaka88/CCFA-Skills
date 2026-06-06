# Result Tables And Caption Outputs

Owner: `ccf-experiment-designer`

Input source: `official-data.md`

Boundary: this file contains only official paper values from the source extract. It does not draw CCFA documentation diagrams and does not invent missing baseline or ablation numbers.

## Main Translation Results

| Task | Model | Official metric | Value | Source |
| --- | --- | --- | --- | --- |
| WMT 2014 English-to-German newstest2014 | Transformer big | BLEU | 28.4 | Attention Is All You Need, Abstract / Section 6.1 / Table 2 |
| WMT 2014 English-to-French newstest2014 | Transformer big single model | BLEU | 41.0 | Attention Is All You Need, Abstract / Section 6.1 / Table 2 |

Caption draft:

Table X. Official headline machine-translation results reported by Vaswani et al. for the Transformer big model. Values are copied into this demo only through `official-data.md`.

## Training Schedule

| Model | Hardware | Step time | Steps | Duration |
| --- | --- | --- | --- | --- |
| Base | 8 NVIDIA P100 GPUs | about 0.4 seconds | 100,000 | about 12 hours |
| Big | 8 NVIDIA P100 GPUs | about 1.0 seconds | 300,000 | about 3.5 days |

Caption draft:

Table Y. Official training hardware and schedule reported in Section 5.2. These values support the demo's efficiency and reproducibility notes but do not constitute a reproduction.

## Model Configuration

| Configuration | N | d_model | d_ff | heads | dropout | Training steps |
| --- | --- | --- | --- | --- | --- | --- |
| Base | 6 | 512 | 2048 | 8 | 0.1 | 100K |
| Big | 6 | 1024 | 4096 | 16 | 0.3 | 300K |

Caption draft:

Table Z. Base and big Transformer configurations used in this demo's writing, review, and artifact-planning slices.

## Layer-Type Comparison

| Layer type | Complexity per layer | Sequential operations | Maximum path length |
| --- | --- | --- | --- |
| Self-attention | O(n^2 * d) | O(1) | O(1) |
| Recurrent | O(n * d^2) | O(n) | O(n) |
| Convolutional | O(k * n * d^2) | O(1) | O(log_k(n)) |
| Restricted self-attention | O(r * n * d) | O(1) | O(n/r) |

Caption draft:

Table W. Official layer-type comparison from Table 1, used to support the mechanism claim that self-attention reduces maximum dependency path length relative to recurrent layers.

## QA Checklist

- [x] Every numeric value appears in `official-data.md`.
- [x] BLEU values are tied to task and model.
- [x] Hardware and schedule are tied to Section 5.2.
- [x] Complexity expressions are tied to Table 1.
- [x] No extra baseline numbers are inferred from PDF text extraction.
