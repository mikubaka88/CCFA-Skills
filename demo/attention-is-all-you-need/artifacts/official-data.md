# Official Data Extract

Source: Vaswani et al., [*Attention Is All You Need*](https://papers.nips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf), NeurIPS 2017. Cross-reference: [arXiv:1706.03762](https://arxiv.org/abs/1706.03762).

This file records the verified data used by the demo. Re-check the source PDF before using these numbers in a real manuscript.

## Headline Results

| Task | Model | Official reported result | Source location |
| --- | --- | --- | --- |
| WMT 2014 English-to-German newstest2014 | Transformer big | 28.4 BLEU | Abstract; Section 6.1; Table 2 |
| WMT 2014 English-to-French newstest2014 | Transformer big single model | 41.0 BLEU | Abstract; Section 6.1; Table 2 |

## Training Data

| Dataset | Official reported setup | Source location |
| --- | --- | --- |
| WMT 2014 English-German | About 4.5M sentence pairs; BPE shared source-target vocabulary about 37,000 tokens | Section 5.1 |
| WMT 2014 English-French | 36M sentences; 32,000 word-piece vocabulary | Section 5.1 |
| Batching | Approximate sequence length batches with about 25,000 source tokens and 25,000 target tokens | Section 5.1 |

## Hardware And Schedule

| Model | Hardware | Step time | Steps | Duration | Source location |
| --- | --- | --- | --- | --- | --- |
| Base | One machine with 8 NVIDIA P100 GPUs | about 0.4 seconds | 100,000 | about 12 hours | Section 5.2 |
| Big | One machine with 8 NVIDIA P100 GPUs | about 1.0 seconds | 300,000 | about 3.5 days | Section 5.2 |

## Core Configuration

| Configuration | N | d_model | d_ff | heads | dropout | Training steps | Source location |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base | 6 | 512 | 2048 | 8 | 0.1 | 100K | Table 3 and Section 5.2 |
| Big | 6 | 1024 | 4096 | 16 | 0.3 | 300K | Table 3 and Section 5.2 |

## Layer-Type Comparison

| Layer type | Complexity per layer | Sequential operations | Maximum path length | Source location |
| --- | --- | --- | --- | --- |
| Self-attention | O(n^2 * d) | O(1) | O(1) | Table 1 |
| Recurrent | O(n * d^2) | O(n) | O(n) | Table 1 |
| Convolutional | O(k * n * d^2) | O(1) | O(log_k(n)) | Table 1 |
| Restricted self-attention | O(r * n * d) | O(1) | O(n/r) | Table 1 |

## Demo Use Policy

- `ccf-experiment-designer` may use these values to design experiments and build result tables/figures.
- `ccf-integrity-auditor` must check any claim against this file before marking it supported.
- `ccf-integrity-auditor` must verify source metadata before real reuse.
- No extra benchmark values should be added unless they are verified from the primary source.
