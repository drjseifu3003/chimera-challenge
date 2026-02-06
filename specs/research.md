# Project Chimera - Research Summary

## Decision: Hierarchical Swarm Pattern
- Chosen: Planner, Worker, Judge agent roles for scalable, modular task execution
- Rationale: Enables clear separation of concerns, robust error handling, and parallelization
- Alternatives: Flat agent pool, single monolithic agent

## Decision: HITL Safety (Management by Exception)
- Chosen: Confidence-based review thresholds, mandatory human review for sensitive/low-confidence outputs
- Rationale: Balances autonomy with safety and compliance
- Alternatives: Fully automated, always-on human review

## Decision: Economic Agency via Coinbase AgentKit
- Chosen: Each agent operates a non-custodial wallet, all payments signed and auditable
- Rationale: Enables autonomous economic action, full auditability, and compliance
- Alternatives: Centralized wallet, custodial solutions

## Decision: MCP for Integration
- Chosen: All external access via Model Context Protocol (MCP) servers
- Rationale: Decouples agent reasoning from implementation, supports extensibility
- Alternatives: Direct API calls, custom integration layer

## Decision: Hybrid Storage
- Chosen: Weaviate (semantic), PostgreSQL (transactional), Redis (episodic)
- Rationale: Optimizes for performance, scalability, and data integrity
- Alternatives: Single DB, custom storage

---

**Created:** 2026-02-06
**Maintainer:** Project Chimera Core Team
