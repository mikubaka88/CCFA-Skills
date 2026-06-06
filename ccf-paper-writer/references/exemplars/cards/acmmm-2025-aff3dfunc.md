# Aff3DFunc

Venue/year: ACM MM 2025.
Source: University of Glasgow record `https://eprints.gla.ac.uk/360521/`; PDF `https://eprints.gla.ac.uk/360521/2/360521.pdf`.
Use when: writing open-vocabulary 3D understanding, affordance detection, language-geometry alignment, or robot validation papers.

## Story Pattern

The paper frames 3D affordance understanding as a practical robotics problem where label-only text descriptions are too weak for open-vocabulary generalization. The method adds functional text enhancement and multilevel representation alignment, then closes the loop with real-world robot validation.

## Abstract Moves

- Start with embodied interaction needs: manipulation and navigation.
- Name the weakness of label-based language prompts.
- Present text enhancement as semantic enrichment, not prompt decoration.
- Present multilevel alignment as the bridge between language and 3D geometry.
- End with zero-shot/generalization evidence and robot validation.

## Introduction Moves

- Explain affordance as function, not category.
- Show why open-vocabulary queries need richer language than labels.
- Tie each method component to a failure of previous representations.

## Method Moves

- Define query forms and 3D representation before alignment.
- Separate text enhancement from geometry-language alignment.
- Keep robot deployment requirements visible.

## Evidence Moves

- Evaluate under different textual query forms.
- Include fine-grained manipulation examples, not only segmentation maps.
- Use robot validation to support actionable affordance understanding.

## Reusable Techniques

- Treat language enhancement as functional grounding.
- Show generalization through query diversity.
- Pair perception metrics with downstream robot behavior.

## Do-Not-Copy Boundary

Do not reuse affordance labels, robot validation claims, or functional text method names unless they belong to the user's work.
