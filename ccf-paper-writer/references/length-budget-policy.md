# Length Budget Policy

Load for explicit compression, fixed-length drafting, or submission preparation. A new content-first draft follows `materials-to-manuscript.md` and has no page quota.

## Phase Before Budget

Complete the substantive scientific explanation and check alignment before reducing length. A named venue provides an audience and template, not an instruction to shorten the initial draft. An explicit request for a submission-ready or fixed-length paper authorizes fitting after the content check in the same task. A local word-count reduction stays local.

During content-first drafting, fix overflow, broken references, and unreadable formatting, but treat page count as informational. Do not expand or cut text to reach a percentage of a venue limit. Results-pending drafts can be content-complete within their requested scope without being evidence-complete.

## Establish The Actual Constraint

For the fitting phase, determine the target venue, year, track, template, counted sections, main-body limit, and any user exclusions. Verify current official rules through `ccf-submission-checker` when asserting compliance. A stale local guide can support provisional formatting, not a final page-limit claim.

Record only useful fields in the existing context or project state:

```text
Phase:
Requested length:
Venue / year / track:
Official counted sections:
Protected sections and figures:
Current length and build status:
```

References, appendices, disclosures, acknowledgements, and limitations have venue-specific counting rules. Do not assume universal exclusions or impose a nine-page limit across papers.

## Allocate By Contribution

Assign space to scientific importance and explanatory dependencies, not a fixed section ratio. A benchmark paper needs room for task definition, construction, and evaluation meaning; a method paper needs core computation and learning/inference; theory needs statements and proof ideas; empirical or human-subject work needs its study design and analysis.

Keep these in the main text:

- The scientific question and contribution.
- The observation and mechanism needed to understand the work.
- Definitions and conditions needed to interpret the primary evidence.
- The main empirical result or theoretical statement, when available.
- Material comparison conditions and necessary pointers to supplementary details.

Supporting derivations, full protocols, hyperparameters, extended tables, and secondary analyses can move to a referenced appendix. Delete repetition and irrelevant execution records rather than storing them in an appendix.

## Fit Without Losing Explanation

Use `compression-rules.md`. Remove repeated motivation, generic background, nominal padding, duplicate definitions, and number-by-number narration before cutting mechanisms or evidence interpretation. Preserve the source format and the user's protected sections/figures. Larger cuts need a section-level plan internally; do not repeatedly request approval already given.

If a short paper has a real explanatory gap, add the supported missing explanation. Do not lengthen an adequate paper merely to occupy every page. Do not invent modules, assumptions, citations, experiments, or favorable interpretations. If results are missing, retain the authorized experiment scaffold with `\emptycell` values and no predicted findings.

After cuts, recheck newly adjacent sentences and paragraphs. A removed definition, missing antecedent, unintroduced symbol, or broken connection is a compression regression even if the page count improves. Reconcile abstract, contributions, captions, appendix references, and conclusion where meaning changed.

## Compile And Inspect

When LaTeX tools are available:

1. Compile with the existing build configuration and normal bibliography passes.
2. Inspect counted pages, reference resolution, equation/table overflow, float order, caption readability, and appendix boundaries.
3. Correct actual content/layout problems within the authorized scope.
4. Recompile after relevant changes and inspect affected pages.
5. Stop when the requested content and applicable formatting checks pass, or report the concrete remaining issue.

Do not shrink template fonts or margins to evade limits, add filler to fix float whitespace, or loop without progress. If compilation is unavailable, say `not compiled`; an estimate is not verified compliance.

## Delivery

For a fitting task, report the canonical file, checked length, substantive moves/cuts, and remaining material issues. For a content-first task, report content completion and missing evidence without classifying the draft as underfilled or overfilled against an inactive budget.
