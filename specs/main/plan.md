# Implementation Plan: Add Output Contracts to Skills

**Branch**: `main` | **Date**: 2026-02-06 | **Spec**: specs/research.md
**Input**: Feature specification from `specs/research.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Add output contracts for each skill (content generator, trend analyzer, wallet manager) by documenting JSON outputs in the skill READMEs and providing JSON schema files in specs/main/contracts plus a quickstart reference. Keep contracts aligned with existing tests (trend analyzer output) and avoid changing runtime behavior.

## Technical Context

**Language/Version**: Python 3.12  
**Primary Dependencies**: mcp, pydantic, uv (tooling), pytest (tests)  
**Storage**: N/A  
**Testing**: pytest  
**Target Platform**: Linux containers + GitHub Actions runners
**Project Type**: single repo (skills/, tests/, specs/)  
**Performance Goals**: N/A  
**Constraints**: Documentation-only change; output contracts must match existing tests  
**Scale/Scope**: 3 skills, 3 schema files, docs updates

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- Spec-Driven Development: PASS (contracts documented + schemas added)
- Hierarchical Swarm Architecture: PASS (no architecture change)
- MCP Integration: PASS (contracts align with MCP-based skills)
- HITL Safety Framework: PASS (docs only; no behavior change)
- Economic Agency: PASS (wallet manager output contract documented)
- Technology Stack Requirements: PASS (no stack deviation)

## Project Structure

### Documentation (this feature)

```text
specs/main/
├── plan.md              # This file (/speckit.plan command output)
├── research.md          # Phase 0 output (/speckit.plan command)
├── data-model.md        # Phase 1 output (/speckit.plan command)
├── quickstart.md        # Phase 1 output (/speckit.plan command)
├── contracts/           # Phase 1 output (/speckit.plan command)
└── tasks.md             # Phase 2 output (/speckit.tasks command - NOT created by /speckit.plan)
```

### Source Code (repository root)
<!--
  ACTION REQUIRED: Replace the placeholder tree below with the concrete layout
  for this feature. Delete unused options and expand the chosen structure with
  real paths (e.g., apps/admin, packages/something). The delivered plan must
  not include Option labels.
-->

```text
skills/
├── skill_content_generator/
│   └── README.md
├── skill_trend_analyzer/
│   └── README.md
└── skill_wallet_manager/
  └── README.md

specs/
└── main/
  ├── contracts/
  ├── data-model.md
  ├── quickstart.md
  └── research.md

tests/
├── test_skills_interface.py
└── test_trend_fetcher.py
```

**Structure Decision**: Single repo layout with skills/, tests/, and specs/main

## Complexity Tracking

No constitution violations.
