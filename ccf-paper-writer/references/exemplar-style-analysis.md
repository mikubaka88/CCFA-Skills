# Exemplar Style Analysis

Use for substantive drafting, a passage whose expression needs repair, or requested learning from real papers. Learn how good original passages explain their science at the sentence and paragraph level. A generic outline or a set of banned phrases is insufficient.

## Select A Source For A Writing Question

Identify the target passage and the concrete writing problem: introducing a representation, explaining a bottleneck, connecting an observation to a design, narrating a theorem, or interpreting a comparison. Select by scientific object and writing function, using `exemplars/index.md` when useful.

Reuse matched supplied or stored originals first, using cards for navigation. Several sources may answer different writing questions, such as an abstract definition, a motivation-to-mechanism transition, and a result interpretation. Select a passage because its objects are clear, its reasoning can be followed, its emphasis serves the contribution, and its language fits the target field. A famous paper can contain weak prose; do not adopt every phrase or its whole outline.

Additional retrieval follows Common's `reference_style_search` preference. The default `on` combines reuse of matching originals with a targeted search for other well-written passages during substantive drafting or expression rewriting. Search for the actual writing question, even when a useful existing example is available; a completed, still-applicable search for that same question can be reused. Select passages for their quality and fit without requiring a paper count. `auto` searches when available passages leave a writing-function gap; `off` skips unrequested extra search. Explicit requests to search remain part of the task in all modes. Do not search again for every paragraph or create an extra model call to interpret a passage. Ordinary clear local edits need no new source search. A requested full-paper exemplar analysis still covers the source in coherent sections.

The card guides navigation. Verify descriptions of the source against the source itself, especially paragraph counts, section organization, purported quotations, and claims about what is always present. Inspect the PDF when extraction mixes columns, equations, or paragraph boundaries. If a source is unavailable, identify the unverified part and work from available material without claiming source-based learning.

## Read Before Drafting

Inspect a coherent passage that performs the selected function, including adjacent context needed to understand it. Recover:

- **Scientific content:** the object, operation or observation, conditions, and inference.
- **Sentence construction:** what serves as subject, what the main verb explains, how technical terms and variables enter, and where qualifications attach.
- **Progression:** how known information introduces the next point and how successive sentences explain, support, contrast, or qualify it.
- **Paragraph function:** what the reader understands by the end and why the next paragraph follows.

Trace these choices to a page, section, or identifiable paragraph. Separate source observations from recommendations for the user's work. Do not turn a source's layout into a universal sentence count or invent a source move that merely resembles a familiar paper template.

## Compose From The User's Material

Recover the target passage's propositions independently of the source. Choose only the source technique that helps express their relationship. Draft with the user's objects, operations, conditions, results, and terminology; preserve the actual strength of the claim.

Transfer a relation such as “define a computation, explain its dependency, then derive its consequence.” Reuse conventional academic phrases, established technical terms, and natural verb–noun combinations when they fit the target meaning; avoiding copying does not require invented synonyms or an unfamiliar name for a known concept. Compose the target passage independently. Do not reproduce a distinctive sentence by swapping nouns, import a source's mechanism, or borrow confidence from its results. Source awards do not justify stronger language.

Keep source analysis in working context during drafting. Return the requested text without a compulsory style report. When analysis itself is requested, explain the useful technique, source location, and its fit or mismatch.

## Grounded Example

Different writing questions benefit from different original passages. The following inspected examples are available through the exemplar library or the shared source registry:

| Writing question | Inspected original | Observed relationship |
| --- | --- | --- |
| Explain why a computation creates a bottleneck | *Attention Is All You Need*, Section 1, paragraph 2, PDF page 2; `exemplars/cards/transformer-writing-style.md` | A dependency between recurrent states explains sequential computation and its consequence for parallelization. |
| Define what a model predicts | *VGGT*, Abstract, PDF page 1; `exemplars/cards/vggt.md` | The model's operation, predicted quantities, and input conditions give the definition substance. |
| Explain why an efficiency metric misses the actual bottleneck | *FlashAttention*, arXiv:2205.14135v2, Abstract; shared source `flashattention-io-awareness-writing` | The gap between reduced operation counts and elapsed speed motivates attention to memory IO and then the tiling approach. |

These are selected passages, not endorsements of every sentence in their papers. Use more than one when their functions complement each other; the target manuscript still needs one coherent argument and voice. The sources' architectures, numerical results, and priority claims do not transfer.

The following observations come from Vaswani et al., *Attention Is All You Need*, Section 1, paragraph 2 (PDF page 2); see `exemplars/cards/transformer-writing-style.md`.

**Source observation:** the paragraph explains how recurrent states depend on earlier states, connects that dependency to sequential computation, and then explains the effect on parallelization and batching. The mechanism precedes the consequence; a lower score is not used as a substitute for the explanation.

**Transferable technique:** introduce the operation, carry its dependency into the next sentence, and derive the relevant consequence. The new paper needs its own valid dependency; the technique does not establish one.

**Hypothetical adaptation, with the stated design supplied and no empirical claim:** an object store retains only the latest observation, while a query asks where an object was earlier.

> The memory retains only the latest state of each object. Updating an entry therefore removes the earlier state that a retrospective query requires. We retain observations with their timestamps so that the query can select the state recorded at the requested time.

This example describes a storage rule and its logical consequence. It does not assert improved accuracy, sufficient memory capacity, or an observed model failure. If the user did not supply the storage rule, do not invent it for smoother prose.

## Card And Analysis Format

Use the existing card headings. Under source-specific moves, record the location and the observed technique. Under Reusable Techniques, explain the transferable relationship and when it is useful. A compact entry can contain:

```text
Source and location:
Observed sentence/paragraph relationship:
Why it helps explain this scientific point:
Adaptation to the supplied material:
Material mismatch, if any:
```

Omit unused fields. Preserve source attribution and distinguish paraphrase, short attributed quotation, and original illustrative example. Never label a suggested outline as the paper's actual organization.

## Check The Adaptation

Read the new paragraph for its scientific meaning and progression. Confirm that actors, operations, conditions, negation, quantities, comparisons, and uncertainty survived. Check that sentences explain the target research rather than the source's prestige, reviewer reaction, or the drafting process.

Use the writer's ordinary affected-passage check; this workflow adds no independent review, mandatory warning block, or repeated generation loop.
