<!--
Sync Impact Report:
- Version change: none → 1.0.0
- List of modified principles: All principles added (Spec-Driven Development, Hierarchical Swarm Architecture, MCP Integration, HITL Safety Framework, Economic Agency)
- Added sections: Technology Stack Requirements, Development Workflow
- Removed sections: None
- Templates requiring updates: None
- Follow-up TODOs: None
-->

# Project Chimera Constitution

## Core Principles

### I. Spec-Driven Development
All development must follow Spec-Driven Development methodology. Specifications are executable and drive implementation, ensuring high-quality software through structured planning and validation.

### II. Hierarchical Swarm Architecture
System architecture must use Hierarchical Swarm pattern with Planner, Worker, Judge roles for scalability, cognitive fidelity, and self-healing capabilities.

### III. MCP Integration
All external interactions must use Model Context Protocol for decoupling reasoning logic from implementation details and ensuring universal connectivity.

### IV. HITL Safety Framework
Implement probability-based Human-in-the-Loop for safety, with confidence thresholds (high >0.90 auto-approve, medium 0.70-0.90 async approval, low <0.70 reject) and mandatory reviews for sensitive topics.

### V. Economic Agency
Agents must have non-custodial crypto wallets for economic participation, managing P&L, negotiating deals, and paying for computational resources.

## Technology Stack Requirements
Use Kubernetes for orchestration, Gemini 3 Pro/Claude Opus 4.5 for reasoning, Gemini 3 Flash for routine tasks, Weaviate for semantic memory, PostgreSQL for transactional data, Redis for episodic cache, Coinbase AgentKit for crypto integration.

## Development Workflow
Follow Spec-Driven workflow: constitution -> specify -> plan -> tasks -> implement. Use HITL for reviews on medium confidence and sensitive topics. Amendments to constitution require approval and migration plan.

## Governance
Constitution supersedes all other practices. All PRs must verify compliance. Complexity must be justified.

**Version**: 1.0.0 | **Ratified**: 2026-02-05 | **Last Amended**: 2026-02-05
