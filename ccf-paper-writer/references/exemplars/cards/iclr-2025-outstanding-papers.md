# ICLR 2025 Outstanding Papers

Venue/year: ICLR 2025.
Source: ICLR Blog `https://blog.iclr.cc/2025/04/22/announcing-the-outstanding-paper-awards-at-iclr-2025/`.
Use when: the user explicitly asks for recent ICLR outstanding-paper style, especially LLM safety, finetuning dynamics, model editing, data valuation, or foundation-model analysis.

## Award Papers

- `Safety Alignment Should be Made More Than Just a Few Tokens Deep`
- `Learning Dynamics of LLM Finetuning`
- `AlphaEdit: Null-Space Constrained Model Editing for Language Models`

## Adaptation Guidance

The guidance below suggests adaptations for the named research topics. The award source establishes award context, not these writing techniques; inspect a selected paper passage before attributing a specific move to it.

- Treat hidden mechanisms as first-class objects of study: alignment depth, finetuning dynamics, or edit subspaces.
- Begin from a widely used practical technique, then show that its internal behavior is not yet understood or controlled.
- Explain the diagnostic's inputs, operation, and measured behavior precisely enough to reproduce it.
- Use experiments to expose a mechanism, not only to report a score.

## Transferable Moves

- Pair practical relevance with mechanistic explanation.
- Name the failure mode or control dimension early.
- Explain how the diagnosed behavior motivates the intervention and distinguish its predicted and observed effects.
- Let the contribution be an insight plus a tool, not just a new benchmark or model.

## Adaptation Conditions

- Avoid claiming causal mechanism unless the experiments isolate it.
- For editing or alignment papers, define the threat model, target behavior, and evaluation boundary.
- For finetuning papers, separate optimization dynamics from dataset artifacts.
