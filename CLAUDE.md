# Project Chimera: AI Agent Rules

## Project Context
This is Project Chimera, an autonomous influencer system built on the FastRender Swarm pattern (Planner, Worker, Judge).

## The Prime Directive
- NEVER generate code without checking the `specs/` directory first. The specification is the absolute source of truth.
- Refer specifically to `specs/technical.md` for all API and Database implementations.
- All external social and data interactions MUST be decoupled via MCP.

## Traceability & Governance
- **Plan First**: You must explain your implementation plan before writing a single line of code.
- **Reference**: Cite specific requirement IDs (e.g., FR-001) from `specs/functional.md` in your plan.
- **Economic Safety**: Always verify budget constraints against the CFO Judge logic for any wallet-related tasks.