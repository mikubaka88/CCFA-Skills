# PolarDB-MP Style Card

Venue/year: SIGMOD 2024 family.
Source: ACM Best Paper Awards source record `acm-best-paper-awards`; verify the exact paper page before public award-status claims.
Use when: database systems, cloud-native DBMS, distributed transactions, shared storage/memory, storage-compute disaggregation, or architecture papers.

## Story Pattern

The paper type is a systems/database contribution: start from a concrete scalability or operational bottleneck, show why existing architectures are constrained by that bottleneck, then introduce a design that changes the system boundary. The story should make the workload, deployment assumption, and architecture tradeoff visible before implementation details.

## Abstract Moves

- Name the real system bottleneck before naming the system.
- State the architecture change as a design principle, not only a component list.
- Mention the workload or deployment setting that makes the problem matter.
- Summarize evidence as throughput, latency, scalability, isolation, fault tolerance, or operational cost, using only user-provided numbers.

## Introduction Moves

- Move from cloud workload pressure to a precise database-system limitation.
- Explain why simpler fixes such as caching, sharding, or tuning are insufficient.
- Introduce the key architectural insight early.
- State contributions as design, implementation, and evaluation claims.

## Method/System Moves

- Use a system diagram with data/control paths, consistency boundaries, and failure assumptions.
- Separate design goals from mechanisms.
- Explain concurrency, recovery, and resource management only after the architecture is clear.

## Evidence Moves

- Use realistic workloads and scale studies.
- Include end-to-end evaluation plus targeted microbenchmarks.
- Report operational costs or overheads when relevant.
- Treat missing deployment detail as a reviewer risk, not as prose polish.

## Do-Not-Copy Boundary

Do not borrow product-specific claims, architecture details, or performance language. Use only the systems-writing pattern.
