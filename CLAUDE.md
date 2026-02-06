
# Project Chimera: AI Agent Rules

## Project Context
Project Chimera is an autonomous influencer system using a Hierarchical Swarm pattern (Planner, Worker, Judge), with Management by Exception (HITL) safety, and economic agency via Coinbase AgentKit. All technical and functional details are governed by the current specifications in the `specs/` directory.

## The Prime Directive
- **Spec First**: NEVER generate code or design without first consulting the `specs/` directory. The specification is the absolute source of truth.
- **Data Model**: All entities, relationships, and validation rules are defined in `specs/main/data-model.md`.
- **Research**: Design decisions and rationale are documented in `specs/main/research.md`.
- **Contracts**: Skill output contracts are in `specs/main/contracts/`.
- **Quickstart**: Setup and onboarding are in `specs/main/quickstart.md`.
- **All external social and data interactions MUST be decoupled via MCP.**

## Traceability & Governance
- **Plan First**: You must explain your implementation plan before writing a single line of code.
- **Reference**: Cite specific requirement IDs (e.g., FR-001) from the current specs in your plan.
- **Economic Safety**: Always verify budget constraints and wallet logic against the economic agency rules in the data model and research specs.

## Specification Files
- `specs/main/data-model.md`: Entity and relationship definitions
- `specs/main/research.md`: Research and design rationale
- `specs/main/contracts/`: Skill output contracts (JSON schema)
- `specs/main/quickstart.md`: Setup and onboarding guide