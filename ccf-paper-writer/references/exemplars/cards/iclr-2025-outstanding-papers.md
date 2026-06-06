# ICLR 2025 Outstanding Papers

Venue/year: ICLR 2025.
Source: ICLR Blog `https://blog.iclr.cc/2025/04/22/announcing-the-outstanding-paper-awards-at-iclr-2025/`.
Use when: the user explicitly asks for recent ICLR outstanding-paper style, especially LLM safety, finetuning dynamics, model editing, data valuation, or foundation-model analysis.

## Award Papers

- `Safety Alignment Should be Made More Than Just a Few Tokens Deep`
- `Learning Dynamics of LLM Finetuning`
- `AlphaEdit: Null-Space Constrained Model Editing for Language Models`

## Shared Writing Signals

- Treat hidden mechanisms as first-class objects of study: alignment depth, finetuning dynamics, or edit subspaces.
- Begin from a widely used practical technique, then show that its internal behavior is not yet understood or controlled.
- Make the method or analysis precise enough that reviewers can reproduce the diagnostic.
- Use experiments to expose a mechanism, not only to report a score.

## Transferable Moves

- Pair practical relevance with mechanistic explanation.
- Name the failure mode or control dimension early.
- Build a claim-evidence path from diagnostic finding to intervention.
- Let the contribution be an insight plus a tool, not just a new benchmark or model.

## Reviewer-Facing Warnings

- Avoid claiming causal mechanism unless the experiments isolate it.
- For editing or alignment papers, define the threat model, target behavior, and evaluation boundary.
- For finetuning papers, separate optimization dynamics from dataset artifacts.
