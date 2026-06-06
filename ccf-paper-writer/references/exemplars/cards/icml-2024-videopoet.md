# VideoPoet

Venue/year: ICML 2024.
Source: PMLR `https://proceedings.mlr.press/v235/kondratyuk24a.html`.
Use when: writing multimodal generation, video synthesis, autoregressive modeling, zero-shot capability, or large model adaptation papers.

## Story Pattern

The paper transfers the language-model training recipe to video generation. Rather than building a separate model for each conditioning type, it treats text, images, video, and audio as multimodal sequences handled by one decoder-only transformer. The contribution is a foundation model that can be adapted to many video generation tasks and demonstrates zero-shot motion quality.

## Abstract Moves

- Define the system by the range of conditioning signals it accepts.
- Present the architecture using a familiar model family.
- Separate pretraining from task-specific adaptation.
- Frame empirical results around zero-shot capability and motion fidelity.

## Introduction Moves

- Establish why video generation needs flexible conditioning.
- Contrast task-specific pipelines with a unified generative sequence model.
- Make the training protocol central to the contribution.

## Method Moves

- Explain tokenization or representation of each modality before training objectives.
- Group objectives by what capability they teach.
- Keep adaptation steps distinct from pretraining.

## Evidence Moves

- Use qualitative examples to demonstrate motion and conditional control.
- Pair zero-shot claims with task diversity.
- Avoid overloading the main text with demos; keep visual evidence organized.

## Reusable Techniques

- Use a unification story when one model handles many input-output modes.
- Make "LLM recipe for another modality" concrete through objectives and tokens.
- Present zero-shot as a capability supported by task coverage.

## Do-Not-Copy Boundary

Do not reuse VideoPoet's multimodal task mix, decoder-only framing, or zero-shot claims unless the user's model and evaluation support them.
