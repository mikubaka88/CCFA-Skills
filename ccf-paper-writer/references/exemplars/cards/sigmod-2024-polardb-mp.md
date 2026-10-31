# PolarDB-MP Style Card

Venue/year: SIGMOD 2024.
Source: shared registry record `sigmod-2024-polardb-mp`; direct original locations below.
Use when: database systems, cloud-native DBMS, distributed transactions, shared storage/memory, storage-compute disaggregation, or architecture papers.

Award context: SIGMOD 2024 Industry Best Paper, not a research-track award.

Inspected writing: Author-hosted paper `https://cighao.com/papers/polardb_mp.pdf`, Abstract and Section 1; DOI `https://doi.org/10.1145/3626246.3653377`.

This card navigates selected original passages. The source observations below are distinct from the adaptation advice; read the relevant original when using it.

## Story Pattern

**Source observation:** The abstract compares database architecture choices through their bottlenecks, then explains why shared memory and storage allow transaction processing to stay on one node. It distinguishes the roles of Transaction Fusion, Buffer Fusion, and Lock Fusion. Section 1 connects the multi-primary design to write-intensive operation and failover needs.

## Abstract Moves

**Writing observation in the inspected passage:** The subsystem names follow their roles in a transaction path. The contribution can be understood through the changed coordination requirements, not through a generic claim that the system is more reliable.

## Reusable Techniques

**Adaptation advice for matching work:**

- Connect workload requirements to the architecture decision.
- Explain which operation becomes local and which state still requires coordination.
- Keep subsystem responsibilities and observed workload results distinct; preserve implementation detail that determines the scientific comparison.

## Do-Not-Copy Boundary

Use the target study's own definitions, mechanisms, conditions, results, and claims. Common academic phrasing and established terms may be reused when they fit; distinctive source sentences and scientific conclusions may not be transplanted.
