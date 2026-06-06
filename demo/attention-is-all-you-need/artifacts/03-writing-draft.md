# 03 - Writing Draft

Owner: `ccf-paper-writer`

This step demonstrates the corrected writer behavior. The input is only an idea document plus official result tables, so the writer should not stop at a checklist. It should search the local venue guide for NeurIPS, use the NeurIPS LaTeX fallback, and create a manuscript draft with unsupported details marked as `TBD` or bounded notes.

## User-Style Command Simulated

```text
基于上面的 idea 和官方数据，假设投稿 NeurIPS，从 0 写一篇 LaTeX 草稿。
不要编造新结果；缺失的实验和引用用 TBD 标出。
```

## Writer Routing

- Mode: `draft`.
- Target venue: NeurIPS.
- Venue reference: `ccf-paper-writer/references/venue-guides/neurips.md`.
- Template fallback used for demo: `ccf-latex-templates/NeurIPS/neurips_2026.tex`.
- Output artifact: `paper/attention_neurips_demo.tex`.

## Actual Draft Artifact

The main writing output is not a report. It is the LaTeX file:

```text
demo/attention-is-all-you-need/paper/attention_neurips_demo.tex
```

It contains:

- NeurIPS-style preamble and anonymous author block.
- Abstract grounded in the original paper's official values.
- Introduction with task, gap, insight, method, and evidence story.
- Method section with attention equation and architecture explanation.
- Experiment section with official BLEU table and complexity/path-length table.
- Limitation section that clearly says this is not a reproduction.
- BibTeX-style bibliography entry for the original paper.

## Draft Abstract

We study whether sequence transduction can be performed without recurrent or convolutional sequence modeling layers. The resulting architecture, the Transformer, uses multi-head self-attention to relate positions directly and position-wise feed-forward networks to transform token representations. This design shortens dependency paths and enables more parallel training than recurrent computation. In the original official report, Transformer big reaches 28.4 BLEU on WMT 2014 English--German and 41.0 BLEU on WMT 2014 English--French as a single model. These results support attention as a complete backbone for machine translation rather than only an auxiliary alignment mechanism.

## Compression Mode Example

If the user asks to compress the abstract, the writer should preserve the prose format and return the compressed paragraph directly:

Transformer replaces recurrent and convolutional sequence modeling with multi-head self-attention. By directly relating sequence positions and adding positional encodings, it shortens dependency paths while enabling parallel training. The official paper reports 28.4 BLEU on WMT 2014 English--German and 41.0 BLEU on WMT 2014 English--French with Transformer big, supporting attention as a complete sequence transduction backbone.

## Presentation Mode Example

If the user asks for a talk instead of a manuscript, the writer should produce the requested presentation format:

1. Problem: sequence models need long-range dependencies without slow sequential recurrence.
2. Method: multi-head self-attention replaces recurrence/convolution; positional encodings restore order.
3. Evidence: official WMT BLEU, constant self-attention path length, ablations, and training-cost report.

## Why This Is Better Than The Previous Demo

The earlier demo made `ccf-paper-writer` look like a checklist generator. The corrected behavior is:

- Draft first, notes second.
- Preserve requested output format.
- Use venue LaTeX when starting from an idea.
- Keep review/audit strictness out of ordinary writing.
- Mark missing evidence without refusing to write.
