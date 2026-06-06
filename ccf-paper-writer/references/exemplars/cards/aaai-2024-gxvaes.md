# GxVAEs

Venue/year: AAAI 2024.
Source: AAAI OJS `https://ojs.aaai.org/index.php/AAAI/article/view/29248`.
Use when: writing biomedical AI, conditional molecule generation, paired representation learning, or application-driven generative model papers.

## Story Pattern

The paper starts from a practical drug-discovery goal: generate molecules that are both drug-like and bioactive. The gap is that molecular generators often ignore disease-related cellular context. The method is framed as a two-part bridge between gene expression profiles and molecule generation, with one representation model extracting disease context and another generating molecules conditioned on that context.

## Abstract Moves

- Start with a real application and its scientific constraint.
- Identify what previous generative models leave out.
- Introduce the architecture as two coupled modules with distinct roles.
- Tie the method to biological meaning, not only chemical validity.
- End with experiments plus case studies to support applied relevance.

## Introduction Moves

- Explain the domain stakes before model details.
- Convert "context matters" into a clear modeling gap.
- Make the conditioning variable scientifically meaningful.
- Use case studies as a bridge from metrics to expert plausibility.

## Method Moves

- Separate the profile representation module from the molecule generator.
- State how the latent spaces interact.
- Keep domain constraints visible: bioactivity, drug-likeness, and disease specificity.

## Evidence Moves

- Combine standard generative metrics with disease-oriented case studies.
- Compare against baselines that lack the biological condition.
- Avoid claiming therapeutic efficacy unless validated experimentally.

## Reusable Techniques

- For applied AI, make the omitted context the root gap.
- Pair quantitative baselines with domain case studies.
- Show how architecture mirrors the scientific causal story.

## Do-Not-Copy Boundary

Do not reuse molecule-generation claims, disease-profile conditioning, or therapeutic language unless the user's work has matching biomedical evidence.
