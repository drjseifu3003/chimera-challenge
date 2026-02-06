
# Project Chimera: AI Agent Rules

## Project Context
Project Chimera is an autonomous influencer system using a Hierarchical Swarm pattern (Planner, Worker, Judge), with Management by Exception (HITL) safety, and economic agency via Coinbase AgentKit. All technical and functional details are governed by the current specifications in the `specs/` directory.

## The Prime Directive
- **Spec First**: NEVER generate code or design without first consulting the `specs/` directory. The specification is the absolute source of truth.
- **Data Model**: All entities, relationships, and validation rules are defined in `specs/data-model.md`.
- **Research**: Design decisions and rationale are documented in `specs/research.md`.
- **API & Contracts**: All API and integration details are in `specs/contracts/openapi.yaml`.
- **Quickstart**: Setup and onboarding are in `specs/quickstart.md`.
- **All external social and data interactions MUST be decoupled via MCP.**

## Traceability & Governance
- **Plan First**: You must explain your implementation plan before writing a single line of code.
- **Reference**: Cite specific requirement IDs (e.g., FR-001) from the current specs in your plan.
- **Economic Safety**: Always verify budget constraints and wallet logic against the economic agency rules in the data model and research specs.

## Specification Files
- `specs/data-model.md`: Entity and relationship definitions
- `specs/research.md`: Research and design rationale
- `specs/contracts/openapi.yaml`: API and integration contracts
- `specs/quickstart.md`: Setup and onboarding guide