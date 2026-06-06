# CollabLLM

Venue/year: ICML 2025.
Source: PMLR `https://proceedings.mlr.press/v267/wu25i.html`.
Use when: writing LLM, agent, human-AI collaboration, multiturn interaction, reward design, or user-study papers.

## Story Pattern

The paper reframes LLM interaction as a long-horizon collaboration problem rather than next-turn response quality. The method contribution is a training framework that gives credit to responses by their downstream contribution to user goals, and the evidence package combines benchmark tasks, LLM judges, and a user study.

## Abstract Moves

- Start with a training/evaluation mismatch: next-turn rewards do not optimize long-term interaction.
- Name a behavioral failure: passive responses to ambiguous or open-ended requests.
- Introduce the framework through its training signal.
- Report both task performance and interaction quality.
- Add human-user evidence to strengthen the collaboration claim.

## Introduction Moves

- Define what good collaboration means before introducing the method.
- Use ambiguous-user-intent examples as motivation, but keep them short.
- Present reward design as the core mechanism, not as an implementation detail.
- Link benchmark design to the paper's thesis.

## Method Moves

- Explain the simulation or reward pipeline as a credit-assignment solution.
- Keep the distinction clear among training data, reward estimation, fine-tuning, and evaluation.
- Define interaction metrics in reviewer-readable language.

## Evidence Moves

- Pair automatic evaluation with human judgment when claiming user-centered gains.
- Report both performance and interactivity so the method is not seen as only more verbose.
- Include a cost or time measure if the claim includes collaboration efficiency.

## Reusable Techniques

- Use "short-term objective versus long-term user goal" as a clean motivation axis.
- Treat benchmark design as part of the contribution when existing evaluation cannot test the thesis.
- Let user study evidence calibrate claims about user satisfaction.

## User Notes

Useful for any paper where the method changes how an AI system behaves in conversation, not just what it predicts.

## Do-Not-Copy Boundary

Do not borrow CollabLLM's reward terminology, benchmark framing, or human-study claims unless the user's work has analogous protocol and evidence.
