# BrickGPT

Venue/year: ICCV 2025.
Source: CVF `https://openaccess.thecvf.com/content/ICCV2025/html/Pun_Generating_Physically_Stable_and_Buildable_Brick_Structures_from_Text_ICCV_2025_paper.html`.
Use when: writing text-to-3D, generative design, physical constraints, autoregressive generation, dataset, or embodied construction papers.

## Story Pattern

The paper turns generative modeling into a physically constrained construction problem. The model is not only asked to match a text prompt; it must produce objects that obey assembly constraints, remain stable, and can be built by humans or robots. The story works because the method, dataset, inference checks, and buildability demonstrations all serve the same promise.

## Abstract Moves

- Claim firstness only after naming the concrete task boundary.
- Introduce dataset construction as the precondition for the model.
- State the generative mechanism and the physical safeguard separately.
- End with multiple validation modes: stable, diverse, visually aligned, manually buildable, robotically buildable.

## Introduction Moves

- Move from text-to-3D generation to the harder requirement of physical assembly.
- Make feasibility constraints part of the task definition, not a post-hoc filter.
- Explain why standard visual quality metrics are insufficient.

## Method Moves

- Separate representation, dataset, autoregressive model, validity check, and rollback.
- Treat inference-time constraint handling as a core algorithmic component.
- Make the object representation understandable before model training details.

## Evidence Moves

- Combine automatic metrics, physical validity checks, qualitative galleries, and real assembly demonstrations.
- Show failure cases where visual plausibility is not enough.
- Use dataset scale and diversity to support generalization claims.

## Reusable Techniques

- Define a generation task by downstream feasibility, not only by visual similarity.
- Pair data creation and inference constraints when real-world validity matters.
- Let build or deployment demonstrations close the evidence loop.

## User Notes

Use this card when a paper must convince reviewers that generated outputs are actionable in the physical world.

## Do-Not-Copy Boundary

Do not reuse brick-specific constraints, dataset claims, or buildability demonstrations unless the user's domain has equivalent evidence.
