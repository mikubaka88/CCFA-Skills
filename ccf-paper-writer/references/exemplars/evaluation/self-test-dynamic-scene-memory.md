# Exemplar Transfer Acceptance Case: Dynamic Scene Memory

This is a hypothetical maintenance case for checking exemplar use. It is not a real paper, experiment result, or executed review transcript.

## Supplied Research

The author proposes object-centric spatiotemporal memory for language-conditioned navigation in dynamic indoor scenes. The supplied design binds object identity, observed geometry, and observation time. No benchmark construction, comparison measurements, global-position estimator, or single-pass inference guarantee has been supplied.

Request: draft an abstract and introduction plan. Do not invent results or redesign the method.

## Relevant References

- `references/exemplars/index.md` selects only a card needed for a concrete writing question.
- `references/exemplars/cards/llava-4d.md` can inform how to introduce spatiotemporal inputs and queries.
- `references/exemplars/cards/vggt.md` can inform readable input/output definitions when relevant.
- `references/materials-to-manuscript.md` governs evidence status.
- `references/storyline-blueprint.md` supplies argument functions, not an automatic expert tournament.

Retain attribution in the exemplar analysis. The new manuscript describes its own scientific mechanism directly; it does not introduce a competing method's “style” as the proposed method.

## Expected Drafting Behavior

1. State the actual navigation setting and proposed memory representation clearly.
2. Present the mechanism as proposed; distinguish a design rationale from a demonstrated benefit.
3. Introduce related work only with applicable verified support. A presumed failure of all existing systems is not evidence.
4. Do not invent global-coordinate conversion, benchmark construction, extra outputs, or a single-pass guarantee.
5. Do not claim better navigation, fewer stored tokens, or validated component effects without measurements.
6. Deliver the requested abstract and introduction plan without forcing a full paper, new experiments, or page fitting.
7. Select zero or one useful exemplar first; load more only to answer a distinct writing question.
8. Form the first draft from the supplied object identity, geometry, and observation time. Explain their relationship without first generating an internal-check narrative and removing its labels afterward.

## Additional Maintenance Cases

These cases define observable acceptance conditions; they are not executed results or phrase-blacklist tests.

| Input | Expected behavior |
| --- | --- |
| Ask to learn the explanation of a computational bottleneck from the Transformer paper, then explain a supplied latest-state-only object store and its proposed timestamped replacement. | Inspect Section 1, paragraph 2 of the source. Explain the store's actual update dependency and consequence in original prose. Preserve the proposal stage and add no accuracy claim. |
| Ask what the Transformer Introduction actually contains. | Describe the four paragraphs on PDF page 2, without inventing a numbered contribution list, a separate Related Work section, or fixed section-length quotas. |
| Supply a Bayesian filter whose belief is a normalized state distribution and whose evidence is a specified observation likelihood; request a local method edit. | Retain these defined technical meanings and the supplied update equation. Improve explanation without renaming the mathematical objects or loading unrelated exemplars. |
| Supply a method/result paragraph with a negative finding, uncertainty, citation keys, and exact numerical values; request source-style adaptation. | Transfer useful sentence relationships while preserving all facts, comparison direction, uncertainty, and markup. Do not inherit the source paper's confidence or mechanism. |
| Request a two-paragraph method motivation from a supplied design; notes also say a nonessential parameter is undecided and experiments have not run. | Explain the supplied motivation and mechanism without inventing that parameter or empirical benefits. Do not append project-status notes when neither is needed to interpret the requested explanation. A request for the full parameter specification or result table would instead expose the specific missing field. |
| Supply only an underspecified “evidence loop” with no update rule and request clearer prose. | Clarify the supplied content and identify the missing operation if needed; do not invent a plausible update rule to make the text concrete. |
| Run the prose checker on a fluent-looking paragraph consisting of undefined process labels, with no configured phrase matches. | A zero-match report says only that no known patterns matched. It does not establish semantic quality or replace reading the paragraph. |

## Revision And Review Checks

If a draft asserts a global-position estimator or an unobserved performance gain, flag the specific unsupported assertion and remove or clarify it within the authorized revision. Do not replace it with another unverified technical promise. Preserve actual observations supplied later, including unfavorable results.

Necessary local evidence and prose checks run regardless of optional extra-review preferences. A separate independent pass follows the effective shared preference and task scope. Do not manufacture reviewer scores or claim a score increase after revision.

## Evaluation Record

When an actual maintenance evaluation is run, record inputs, evaluated rule versions, observed outputs, relevant failures, and available time/token measurements in the existing evaluation record. Until then, this file defines expected behavior only.
