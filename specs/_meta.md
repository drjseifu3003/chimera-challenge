# Project Chimera: Autonomous Influencers System - Meta

## Vision

Build the core system for Project Chimera as described in the research documents, implementing the Hierarchical Swarm Architecture with MCP integration, HITL safety framework, and economic agency.

## Core Constraints

- **Hierarchical Swarm Architecture (FastRender)**: System uses Planner, Worker, Judge roles for scalability, cognitive fidelity, and self-healing.
- **MCP Integration**: All external interactions use Model Context Protocol for decoupling reasoning from implementation details.
- **HITL Safety Framework**: Probability-based human-in-the-loop with confidence thresholds (high >0.90 auto-approve, medium 0.70-0.90 async approval, low <0.70 reject) and mandatory reviews for sensitive topics.
- **Economic Agency**: Agents have non-custodial crypto wallets for economic participation, managing P&L, negotiating deals, and paying for computational resources.

## Key Entities

- **Agent**: Autonomous entity with reasoning, creative expression, and economic capabilities; has wallet, memory (semantic/episodic), persona, and task execution history
- **Swarm**: Group of agents coordinated by planner; has global state, task queue, and shared objectives
- **Orchestrator**: Central hub managing multi-tenancy, global state, and inter-swarm communication
- **Task**: Executable unit with DAG dependencies, assigned to workers by planner
- **Content**: Generated output (text, images, posts) with metadata, confidence scores, and review status