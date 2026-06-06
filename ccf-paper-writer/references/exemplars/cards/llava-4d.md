# LLaVA-4D

Venue/year: ICLR 2026.
Venue family: ICLR.
Custom status: user-custom writing-format exemplar. This card participates in the default custom writing format when the user does not specify a target venue.
Source: `paper_ref/LLaVA-4D.pdf`; OpenReview `https://openreview.net/forum?id=URpbmVEsqB`; arXiv `https://arxiv.org/abs/2505.12253`.
Use when: writing multimodal, 3D/4D scene, embodied AI, prompt-embedding, or dataset plus model papers.

## Story Pattern

Broad success in 2D multimodal understanding is narrowed to a physical-world failure: missing spatial representation. The introduction then shows that existing 3D LMMs improve static spatial modeling but do not model temporal variation. The proposed method is framed as a minimal dimensional extension with a concrete mechanism: add time to coordinates and disentangle spatial and temporal visual features.

## Abstract Moves

- Start with a capability gap tied to the physical world.
- Describe the prior approach in one sentence, then immediately name its failure case.
- Introduce the method as a general framework with one memorable mechanism.
- Add a dataset contribution after the modeling contribution.
- End with broad task validation, not only one benchmark.

## Introduction Moves

- Paragraph 1: field momentum and why the current generation of LMMs is insufficient for physical interaction.
- Paragraph 2: prior 3D LMMs as a ladder, followed by the dynamic-object failure.
- Paragraph 3: observation that static background and moving objects share positions but differ in motion.
- Paragraph 4: module preview with explicit mapping from observation to design.
- Contributions: one model-level claim, two insight-to-module claims, one dataset/evidence claim.

## Method Moves

- Name each module by the role it plays in the story, not just by architecture.
- Explain coordinate encoding before fusion so the reader understands what information is being injected.
- Keep dataset construction separate from model mechanics so reviewers can evaluate each contribution.

## Evidence Moves

- Use a first figure that contrasts old paradigm, new paradigm, benchmark summary, and qualitative task behavior.
- Include multiple tasks so the paper reads as a framework rather than a narrow fix.
- Pair quantitative results with dynamic qualitative examples that expose the failure mode of static models.

## Reusable Techniques

- Turn a missing dimension into a writing spine: 2D to 3D to 4D.
- Convert an observation into a design decision, then into a contribution bullet.
- Make the first figure carry both motivation and evidence.

## User Notes

This is one of the user's recognized exemplars. Use it especially when the user's paper needs to justify a new representation for dynamic scenes.

## Do-Not-Copy Boundary

Do not reuse the 4D coordinate prompt claim, dynamic-scene examples, dataset framing, or contribution wording unless they are actually the user's own technical content.
