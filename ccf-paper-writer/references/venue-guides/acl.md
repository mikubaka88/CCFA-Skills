# ACL Venue Guide

| Field | Value |
| --- | --- |
| Scope | ACL 2027 main conference, including long and short papers |
| Template | `ccf-latex-templates/ACL/2027/acl_latex.tex` and the sibling bundle |
| Policy checked | 2026-11-25. Recheck the active ARR cycle and the destination's instructions. |
| Sources | `acl-2027-main-cfp`, `acl-arr-cfp`, `acl-arr-author-guidelines`, `acl-2027-template`, `acl-arr-responsible-nlp` in [the registry](../../../ccf-common/references/source-registry.yaml) |

## Write for the Contribution

A long paper develops a substantial CL/NLP contribution. A short paper earns its place through a focused finding or contribution, with a self-contained argument and enough evidence to evaluate it. For either length, identify the language problem or insight and the claim each comparison tests. When applicable, state data provenance, languages and domains, split construction and contamination controls, evaluation and annotation protocols, and conditions for comparing scores. Report relevant subgroup or error analysis at the level supported by the data. For an analysis, resource or negative result, justify its significance for CL/NLP on its own terms.

## Template and Build Mode

For a new 2027 scaffold, copy the complete official bundle from the template path above. Retain the supplied LaTeX and scientific scope when revising an existing paper. The shared ACL style uses A4 and `acl_natbib`. Keep published prior work cited in the third person during review.

| Stage | Package declaration | Output |
| --- | --- | --- |
| ARR review | `\usepackage[review]{acl}` | Anonymous review PDF with line numbers |
| ACL camera-ready | `\usepackage{acl}` or `\usepackage[final]{acl}` | Final author-visible paper after acceptance |
| Preprint | `\usepackage[preprint]{acl}` | Author-visible preprint, subject to the chosen ARR preprint status |

The official examples illustrate formatting. Replace their sample text, acknowledgments and Limitations with the actual manuscript or placeholders explicitly marked as unresolved in a scaffold. Recheck the active cycle and the destination when another venue shares the style.

## ARR Review and ACL Commitment

1. Submit to a qualifying ARR cycle. For ACL 2027, the first call names January 4, 2027 AoE as the latest ARR deadline and accepts completed earlier cycles. Check the current cycle's author profiles, qualified service contributor and nomination, registration window, and quotas in the live ARR CFP.
2. During discussion, reply through the cycle's OpenReview author-response fields. Ground clarifications in the submitted work and check the cycle's rules for new results and updates. For a substantive ARR resubmission, attach the required revision explanation and map prior issues to specific changes or justified non-changes.
3. When the reviews and meta-review are complete, follow the live ACL commitment instructions. Preserve the author list during commitment. Record ARR review, commitment, and camera-ready as distinct stages. Check parallel-review and withdrawal rules before moving the paper.

## Submission Package

| Stage | Long main-content pages | Short main-content pages |
| --- | ---: | ---: |
| ARR review | 8 | 4 |
| ACL 2027 camera-ready | 9 | 5 |

- Place a dedicated **Limitations** section after the conclusion and before references. It is required and outside the main-content budget. Optional ethical considerations, references, and correctly placed appendices are also outside that budget. Keep material needed to assess the central claims in the main paper. Appendices follow references in the submitted PDF and normally use two columns.
- Inspect the review PDF, metadata, acknowledgments, links, and supplemental files for identifying material. Anonymous submission and the ARR preprint-status choice are distinct. Follow any binding no-preprint choice made on the form.
- Fill in the Responsible NLP Checklist with truthful answers and manuscript pointers. Disclose covered AI writing/coding assistance and scope in the checklist. Follow ARR's policy for accompanying details and keep disclosures anonymous during review. The official policy exempts certain uses such as proofread-only assistance. The checklist answers are separate from the Limitations section.
- Check that supplemental software and datasets are anonymized and supplied in the allowed separate archives or through an allowed anonymized link. On acceptance, follow the actual ACL camera-ready and ACLPUB instructions.

From the CCFA root, the local check for an ARR short paper is:

```bash
python ccf-submission-checker/scripts/check_acl2027.py --track short --tex path/to/main.tex --pdf path/to/main.pdf
```

Use `--track long` for long papers and `--stage camera-ready` for an accepted ACL 2027 paper. The preflight inspects the template, Limitations, PDF Author metadata and page sizes. Supply `--main-pages` only after inspecting the compiled main-content boundary. Check visible anonymity, actual AI assistance, the Responsible NLP form, and the ARR/ACL workflow separately. Resolve a heading the tool cannot detect against the rendered PDF.

## Reference Papers

[Selected research references](../exemplars/papers/acl/README.md) provide original papers, verified presentation or award status, and reading cues.
