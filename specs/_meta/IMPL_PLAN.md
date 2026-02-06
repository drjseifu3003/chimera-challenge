# Project Chimera - Implementation Plan

## Technical Context
- Hierarchical Swarm pattern: Planner, Worker, Judge agent roles
- HITL safety: Management by Exception, confidence thresholds
- Economic agency: Coinbase AgentKit, non-custodial wallets
- MCP for all integrations
- Hybrid storage: Weaviate, PostgreSQL, Redis
- Kubernetes for scaling

## Constitution Check
- All principles and non-negotiable rules from constitution.md are enforced in requirements and design
- No direct external calls; all via MCP
- HITL enforced for flagged content
- All agent actions and payments are auditable

## Phase 0: Research
- See research/research.md, research/architecture_strategy.md, research/tooling_strategy.md for rationale and alternatives

## Phase 1: Design & Contracts
- Data model in data-model.md
- API contracts in contracts/openapi.yaml
- Quickstart in quickstart.md

## Phase 2: Implementation Planning
- Implementation tasks and milestones to be defined in /specs/_meta/plan.md

---

**Created:** 2026-02-06
**Maintainer:** Project Chimera Core Team
