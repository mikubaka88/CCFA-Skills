# ICML Venue Guide

| Field | Value |
| --- | --- |
| Scope | ICML 2027 main-conference research submissions |
| Template | `ccf-latex-templates/ICML/2027/example_paper.tex` and the sibling bundle |
| Historical template | `ccf-latex-templates/ICML/example_paper.tex` is the 2026 example |
| Policy checked | 2026-11-25. Recheck the live track and stage instructions. |
| Sources | `icml-2027-cfp`, `icml-2027-author-instructions`, `icml-2027-author-kit`, `icml-2027-author-ai`, `icml-2027-contribution-types` in [the registry](../../../ccf-common/references/source-registry.yaml) |

## Write for the Primary Contribution

Identify what the ML community learns and why the evidence supports it. Choose the contribution type that matches the work and use its official criteria. For theory, connect the theorem, assumptions, and proof obligations to the claim. For empirical methods, state the comparison protocol and control the budgets or inputs that affect the result. Match any claimed generality to the tested settings and report relevant variability, cost, or failure modes. Application, feasibility, negative-result, and dataset or evaluation papers each need evidence commensurate with their own claims. Position Papers use a distinct call, even though they are submitted through the main track as a contribution type.

## Template and Build Mode

For new 2027 LaTeX, copy the full 2027 bundle. Preserve the official US Letter geometry, the template's `\printAffiliationsAndNotice{}` call, and the short running title. Preserve the supplied year-specific template for older projects unless a verified migration is requested.

| Stage | Package declaration | Output |
| --- | --- | --- |
| Research submission | `\usepackage{icml2027}` | Anonymous review PDF |
| Camera-ready | `\usepackage[accepted]{icml2027}` | Final author-visible paper |
| Preprint | `\usepackage[preprint]{icml2027}` | Author-visible preprint |

## Submission Package

- The main research PDF is anonymous and has at most eight main-body pages, or nine for the final version. References, the Impact Statement, the AI Disclosure Statement, and appendices are outside the main-body count. Put appendices in the same PDF after references. Keep material essential to evaluation in the main body. Verify size, fonts, margins, rendered section order, and metadata on the actual PDF.
- Include a separate **Impact Statement** before references, near any permitted acknowledgments. Discuss the actual potential broader effects of the work when material.
- Include a truthful **AI Disclosure Statement** at the end, before or after references, in every submission. The official example labels it **AI Use Statement**. Replace the examples with the actual uses and human verification. Confirm the facts before declaring no substantive use. Preserve the disclosure through compression and camera-ready preparation. Routine editorial assistance is exempt from substantive-use reporting. If AI contributed to the methodology, document it in the paper with enough detail to evaluate and reproduce its role.
- Use third-person self-citation and check anonymous authors, affiliations, acknowledgments, grants, links, code, data, and supplementary documents. Additional anonymized supplemental files use the same submission deadline. Follow the official instructions for repository snapshots, license handling, and links in anonymous supplemental uploads.
- Verify the live OpenReview abstract/full-paper stages, author profiles, selected contribution type, nomination, reciprocal reviewing and quotas. For 2027, ICML announced an initial AC/SAC screening stage ahead of full review. Check author feedback timing on the live site. Keep the response anonymous and plan around the rule that a revised manuscript cannot be uploaded during feedback.
- For camera-ready, use the accepted mode and check the final PDF, author information, OpenReview lay summary and registration requirements against the current instructions.

From the CCFA root, run the local preflight:

```bash
python ccf-submission-checker/scripts/check_icml2027.py --tex path/to/main.tex --pdf path/to/main.pdf
```

Use `--stage camera-ready` for the accepted main-conference version. The preflight inspects the template, statement order, PDF Author metadata and page sizes. Supply `--main-pages` only after inspecting the compiled main-body boundary. Check statement contents, the actual stage and OpenReview fields separately. Position papers, workshops, and other years require their own rules.

## Reference Papers

[Selected research references](../exemplars/papers/icml/README.md) provide original papers, verified presentation or award status, and reading cues.
