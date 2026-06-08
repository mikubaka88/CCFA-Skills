---
name: ccf-paper-to-exemplar
description: "Convert user-provided conference paper PDFs into distilled writing exemplar cards for the ccf-paper-writer skill. Extracts full text, analyzes writing patterns by venue, and produces ready-to-use exemplar cards with story patterns, abstract/introduction/method/evidence moves, and citation-style analysis. Use when the user wants to add custom writing exemplars, convert favorite papers into reusable writing templates, or build a personal exemplar library for a target venue."
metadata:
 ccf_skill_controls:
 handoff_question_mode: partial
 respect_session_denylists: true
 protect_idea_scope_in_writing: true
 private_material_safety: moderate
 shared_controls: ../ccf-common/references/
---

# Paper-to-Exemplar

## Purpose

Convert one or more conference paper PDFs into distilled writing exemplar cards
that the `ccf-paper-writer` skill can use as style references. This skill does not
write papers. It produces exemplar cards that teach the writer skill how to write.

## When To Use

- User says: "use this paper as writing reference", "convert this PDF to exemplar", "add this to my writing templates"
- User wants to build a personal library of favorite papers for writing-style imitation
- User specifies a target venue and wants venue-matched exemplars loaded
- After downloading a best paper, the user wants it distilled for fast reuse

## Workflow

1. Receive PDF paths and optional target venue from the user.
2. Run `scripts/convert.py` to extract text and produce initial cards with `[ANALYZE]` placeholders.
3. Read the extracted full text (`.full.md` file) to understand the paper content.
4. Analyze the paper writing patterns:
 - Story arc: task -> gap -> root challenge -> insight -> method -> evidence -> limitation
 - Abstract moves: what information is packed into each sentence?
 - Introduction paragraph roles: what does each paragraph accomplish?
 - Method presentation: module-by-module, concept-first, or pipeline-first?
 - Evidence organization: table strategy, ablation logic, qualitative placement
 - Citation patterns: density, weaving style, author-name usage, grouping
5. Fill in the `[ANALYZE]` placeholders with concrete, actionable writing-pattern descriptions.
6. Save the completed card to `ccf-paper-writer/references/exemplars/cards/`.
7. Register the card in `ccf-paper-writer/references/exemplars/index.md` under the correct venue section.
8. If the user wants this as their default writing template, update `ccf-paper-writer/references/custom-format/default-user-format.md`.
9. Inform the user the exemplar is ready and what writing patterns it provides.

## Venue-Aware Routing

When the user specifies a target venue (e.g., "投CVPR", "for NeurIPS submission"):

1. Classify the target venue into its venue family using `../ccf-paper-writer/references/venue-guides/index.md`.
2. If the user provides a PDF, distill it with the venue tag so it is categorized correctly.
3. If the user does NOT provide a PDF but names a venue, check whether exemplar cards already exist for that venue:
 - Look in `../ccf-paper-writer/references/exemplars/index.md` for venue-matched bundles.
 - If matching exemplars exist, load them and offer them to the writer skill.
 - If no matching exemplars exist, suggest: "No {venue} exemplars found. Provide a {venue} best paper PDF and I will distill it."
4. When the writer skill is invoked for this venue, the exemplar index should route to the correct cards automatically.

## Integration With ccf-paper-writer

The writer skill loads exemplars through `references/exemplars/index.md`.
This skill populates that index. The handoff is:

```text
paper-to-exemplar (distill PDFs -> create cards -> update index)
 -> ccf-paper-writer (load cards from index -> write with venue-matched style)
```

When the writer skill starts, it checks:
1. Did the user specify a venue? If yes, load venue-matched cards.
2. If no venue specified, load the user default cards from `custom-format/default-user-format.md`.
3. If no default cards exist, load the most general-purpose cards (e.g., llava-4d, vggt).

## Output Contract

After processing PDFs:

1. List the generated card files and their locations.
2. Summarize the writing patterns extracted from each paper.
3. State which venue family each card belongs to.
4. If cards were registered as defaults, confirm the registration.
5. Provide next-action options: "Run ccf-paper-writer with these exemplars" or "Add more papers."

## Reference Files

- `scripts/convert.py`: PDF-to-markdown extraction and card skeleton generation.
- `../ccf-paper-writer/references/exemplars/index.md`: exemplar registry (this skill writes to it).
- `../ccf-paper-writer/references/exemplars/cards/`: card storage directory.
- `../ccf-paper-writer/references/custom-format/default-user-format.md`: default exemplar configuration.
- `../ccf-paper-writer/references/venue-guides/index.md`: venue family classification.

## Card Format

Every exemplar card follows this structure (see existing cards for examples):

```markdown
# Paper Title

Venue/year: CVPR2025.
Source: distilled from PDF by ccf-paper-to-exemplar.
Use when: writing {paper type} in the {venue} venue family.

## Story Pattern
Describe the story arc the paper follows.

## Abstract Moves
How does the abstract compress the contribution?

## Introduction Moves
Paragraph-by-paragraph role analysis.

## Method Moves
How is the method presented and justified?

## Evidence Moves
Evidence types, table/figure strategy, claim mapping.

## Citation Patterns
How are citations woven? Density? Style?

## Reusable Techniques
Transferable writing techniques.

## Do-Not-Copy Boundary
Do not copy specific task, claims, examples, or technical content.
```

## Dependencies

- Python3 with `pymupdf` (install: `pip install pymupdf`)
- The `convert.py` script handles PDF text extraction
