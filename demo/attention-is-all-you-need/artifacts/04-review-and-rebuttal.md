# 04 - Review And Rebuttal

Owners: `ccf-paper-reviewer`, `ccf-integrity-auditor`, `ccf-rebuttal-writer`

## Paper Reviewer - Scientific And Writing Review

Reviewed artifact: `paper/attention_neurips_demo.tex`.

Likely stance in a NeurIPS-style pre-publication review: strong accept potential if the empirical comparison and prior-art positioning are clear.

### Strengths

- Clear architectural thesis: attention can be the primary sequence modeling mechanism.
- Strong empirical headline on WMT English-German and English-French.
- Complexity/path-length comparison gives a clean theoretical motivation.
- Ablations and training schedule make the design more inspectable.

### Major Risks

| Risk | Severity | Evidence basis | Required action |
| --- | --- | --- | --- |
| Prior attention work may make novelty look incremental. | Major | Attention existed before the full Transformer architecture. | Position novelty as architecture-level replacement of recurrence/convolution. |
| BLEU claims need exact setup and source clarity. | Major | Demo uses official paper values only. | Tie each number to `official-data.md` and original source location. |
| Complexity claims can be overgeneralized. | Medium | Table 1 depends on sequence length and representation dimension. | State assumptions and avoid universal speedup claims. |
| Demo has no reproduced training. | Medium | This repo is a workflow demo. | Mark as official-paper data, not reproduction. |

### Writing Review

- The abstract should say "official paper reports" when using historical values.
- The introduction should distinguish "attention as an auxiliary mechanism" from "attention as the full sequence modeling backbone."
- The method section should introduce positional encoding before claiming the model can remove recurrence.
- Result narration should pair BLEU with dataset and model size.
- The LaTeX draft correctly puts the primary writing artifact before process notes; remaining review output should not be fed back as manuscript text until `ccf-paper-writer` applies the revisions.

## Integrity Auditor

| Claim | Support status | Notes |
| --- | --- | --- |
| Attention-only sequence modeling is the central idea. | Supported | Architecture summary from original paper. |
| Self-attention has constant maximum path length in Table 1. | Supported | Table 1 in original paper. |
| Transformer big reports 28.4 BLEU on WMT 2014 En-De. | Supported | Abstract, Section 6.1, Table 2. |
| Transformer big single model reports 41.0 BLEU on WMT 2014 En-Fr. | Supported | Abstract, Section 6.1, Table 2. |
| Demo reproduces training. | Unsupported | Must not be claimed. |

Citation audit:

- Primary citation should be Vaswani et al., NeurIPS 2017, *Attention Is All You Need*.
- arXiv:1706.03762 can be listed as a mirror, not the sole official venue source.
- Any additional related work must be searched and verified before inclusion.

## Simulated Reviewer Comments

R1: The idea is elegant, but attention existed before. The submission should explain why this is more than applying known attention mechanisms to machine translation.

R2: The efficiency argument is promising, but the paper should be careful not to imply that self-attention is always cheaper than recurrence for every sequence length.

R3: The empirical results are strong, but the response should clarify whether the reported BLEU values are reproduced by the authors or taken from the original paper.

## Rebuttal Writer - Draft Response

We thank the reviewers for identifying the two places where our framing needs to be sharper: the scope of the novelty claim and the interpretation of the efficiency argument. Our central claim is not that attention itself is new. The contribution is an architecture in which attention replaces recurrent and convolutional sequence modeling as the core backbone, with positional encodings and multi-head attention making the model viable for sequence transduction.

For the efficiency discussion, we will revise the text to state the assumptions behind the path-length and per-layer-complexity comparison. In particular, we will avoid claiming a universal computational advantage and instead describe the exact comparison summarized in the original Table 1.

Finally, the BLEU values used in this demo are official values from the original paper, not newly reproduced results. We will label them as source-reported results and keep the demo's contribution limited to workflow validation.

## Revision Ledger

| Reviewer | Concern | Action | Owner | Status |
| --- | --- | --- | --- | --- |
| R1 | Novelty over prior attention | Add architecture-level novelty framing. | `ccf-paper-writer` | planned |
| R2 | Overbroad efficiency claim | Add assumptions around complexity/path length. | `ccf-paper-writer` | planned |
| R3 | Reproduction ambiguity | Mark BLEU as official source-reported values. | `ccf-integrity-auditor` | done |
