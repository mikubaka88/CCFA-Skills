# 04 - Review, Integrity Audit, And Rebuttal

Owners: `ccf-paper-reviewer`, `ccf-integrity-auditor`, `ccf-rebuttal-writer`

Reviewed artifact: `paper/attention_iclr_submission.tex`.

## Writing Review

| Location | Finding | Required revision | Status |
| --- | --- | --- | --- |
| Abstract | Strong challenge-insight-result structure, but must not imply universal efficiency. | Keep "path length and parallelism" separate from total cost. | Applied. |
| Introduction | Correctly distinguishes recurrent/convolutional bottlenecks, but novelty could still be read as "attention exists." | Add explicit sentence: attention was previously auxiliary; the shift is backbone replacement. | Applied. |
| Method | Module order is clear: attention -> multi-head -> encoder/decoder -> positions. | Ensure positional encodings are motivated as necessary after removing recurrence. | Applied. |
| Experiments | Main BLEU and path-length tables are useful. | Add direct warning that ablation values are not invented in this demo. | Applied. |
| Related Work | Covers the closest historical lines. | A real current ICLR submission needs a broader literature search. | Open. |
| Limitations | Correctly names quadratic cost and historical scope. | Add code/artifact limitation for submission readiness. | Applied. |

## Scientific Review

### Reviewer 1 - Novelty And Positioning

The architectural claim is strong if framed as replacing the backbone of sequence modeling. The manuscript now makes that distinction, but Related Work is still too short for a real ICLR submission. It should include more context around efficient sequence modeling, memory/computation tradeoffs, and later attention variants if the submission is evaluated under current standards.

Score signal: weak accept for historical reconstruction; borderline for real current ICLR without updated related work and modern baselines.

### Reviewer 2 - Evidence And Experiments

The WMT headline table and path-length table support the main story. However, the ablation section is only a plan. For a real submission, the paper needs the actual ablation values from the original table or a reproduced experiment set. The current manuscript is honest because it marks missing values, but an ICLR reviewer would not accept a plan as evidence.

Score signal: acceptability depends on filling ablations and implementation details.

### Reviewer 3 - Clarity And Reproducibility

The Method section is readable and decomposes modules cleanly. Reproducibility remains incomplete: the paper states training schedule and hardware, but does not provide code, preprocessing scripts, seeds, checkpoint details, or exact decoding settings. These gaps should be moved into an appendix or artifact checklist.

Score signal: clear writing, incomplete artifact readiness.

## Integrity Audit

| Claim in manuscript | Evidence source | Status | Action |
| --- | --- | --- | --- |
| Transformer big reports 28.4 BLEU on WMT 2014 En-De. | `official-data.md`; original paper Abstract/Section 6.1/Table 2 | Supported | Keep. |
| Transformer big single model reports 41.0 BLEU on WMT 2014 En-Fr. | `official-data.md`; original paper Abstract/Section 6.1/Table 2 | Supported | Keep. |
| Self-attention has constant maximum path length under full attention. | `official-data.md`; original paper Table 1 | Supported | Keep with "under full attention." |
| Attention is new. | Not claimed; prior attention cited. | Avoided | Keep Related Work distinction. |
| Self-attention is universally cheaper than recurrence. | Not supported. | Avoided | Keep quadratic-cost caveat. |
| Demo reproduces training. | Not supported. | Avoided | Keep official-values wording. |

Citation audit:

| Citation | Purpose | Status |
| --- | --- | --- |
| Vaswani et al. 2017 | Primary source | Present. |
| Sutskever et al. 2014 | Recurrent seq2seq | Present. |
| Cho et al. 2014 | RNN encoder-decoder | Present. |
| Bahdanau et al. 2015 | Attention NMT | Present. |
| Gehring et al. 2017 | Convolutional seq2seq | Present. |
| Wu et al. 2016 | GNMT scale baseline | Present. |

## Simulated ICLR Reviews

### R1

The paper is well written and the architecture is compelling. My main concern is novelty framing. Attention mechanisms existed before this work, so the paper must emphasize that the contribution is replacing recurrence and convolution as the backbone rather than introducing attention itself.

### R2

The path-length argument is useful, but the manuscript should not imply that self-attention is computationally superior in all settings. The quadratic sequence-length term should be discussed alongside the parallelism benefit.

### R3

The experimental claims are strong but under-specified for reproduction. The paper should include full ablation values, exact preprocessing and decoding details, and an artifact plan.

## Rebuttal Draft

We thank the reviewers for identifying three points that require sharper presentation: novelty framing, the scope of the efficiency claim, and reproducibility detail.

For novelty, we agree that attention mechanisms were already present in neural machine translation. We will revise the framing to emphasize that the contribution is an architecture in which self-attention replaces recurrent and convolutional sequence modeling as the representation-building backbone. This distinction is now stated in the Introduction and Related Work.

For efficiency, we will narrow the claim. The paper will not claim that self-attention is universally cheaper than recurrence. Instead, we will state the exact comparison supported by the official analysis: full self-attention provides constant sequential operations and constant maximum path length, while its per-layer complexity is quadratic in sequence length.

For reproducibility, we will expand the appendix with preprocessing, batching, model configuration, training schedule, decoding details, and the full ablation values from the official source. In this demo manuscript, values not yet copied from the source are explicitly marked as missing rather than invented.

## Revision Ledger

| Reviewer | Concern | Manuscript action | Owner | Status |
| --- | --- | --- | --- | --- |
| R1 | Novelty over prior attention | Add backbone-replacement sentence in Introduction and Related Work. | `ccf-paper-writer` | Done. |
| R2 | Overbroad efficiency | Add quadratic-cost caveat in path-length section. | `ccf-paper-writer` | Done. |
| R3 | Reproducibility detail | Add artifact/checklist appendix and mark missing ablations. | `ccf-submission-checker`, `ccf-integrity-auditor` | Partial. |
| R3 | Missing full ablation values | Fill values from original Table 3 or reproduction logs. | `ccf-experiment-designer` | Open. |
| All | Current related work | Run modern related-work search if this is used as a real current submission. | `ccf-literature-searcher` | Open. |
