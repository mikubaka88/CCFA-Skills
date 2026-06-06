# L25GC+ Style Card

Venue/year: SIGCOMM 2024 family.
Source: SIGCOMM 2024 program source record `sigcomm-2024-program`; verify the exact paper page before public award-status claims.
Use when: networking systems, mobile core networks, low-latency data planes, NFV, packet processing, or deployment-driven network architecture papers.

## Story Pattern

The paper type is a networked-systems contribution: open with a real latency, throughput, or deployment pain point, then show how the architecture changes the bottleneck. The writing should make the operational setting and workload realism central.

## Abstract Moves

- State the network setting and why current designs miss the target.
- Present the design as a re-architecture around one bottleneck.
- Preview evaluation on realistic traces, deployments, or workloads.
- Avoid broad "faster network" claims unless the measured setting supports them.

## Introduction Moves

- Start with user or operator consequences of the bottleneck.
- Distinguish protocol, implementation, and deployment constraints.
- Explain why common optimizations are insufficient.
- End the introduction with design goals and evidence categories.

## Method/System Moves

- Show control plane, data plane, and state management explicitly.
- Make assumptions and deployment boundaries auditable.
- Keep performance-critical paths readable and reproducible.

## Evidence Moves

- Include end-to-end results plus sensitivity to workload, traffic mix, and scale.
- Use microbenchmarks to prove which part of the design removes the bottleneck.
- Report overhead, resource use, and failure behavior when relevant.

## Do-Not-Copy Boundary

Do not reuse network-specific claims or names unless they are the user's actual system. Transfer only the bottleneck-driven systems narrative.
