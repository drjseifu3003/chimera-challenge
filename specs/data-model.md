# Project Chimera - Data Model

## Entities

### Agent
- id: UUID
- role: enum (Planner, Worker, Judge)
- wallet_address: string
- status: enum (active, paused, error)
- confidence_score: float
- assigned_tasks: [Task]

### Task
- id: UUID
- type: enum (content_generation, trend_analysis, payment, etc.)
- status: enum (pending, in_progress, completed, failed)
- agent_id: UUID
- input_data: JSON
- output_data: JSON
- confidence_score: float
- requires_review: bool

### Review
- id: UUID
- task_id: UUID
- reviewer_id: UUID
- status: enum (pending, approved, rejected)
- comments: string
- timestamp: datetime

### Wallet
- address: string
- agent_id: UUID
- balance: float
- last_transaction: datetime

### MCPResource
- id: UUID
- type: string
- endpoint: string
- description: string

## Relationships
- Agent 1:N Task
- Task 1:1 Review (optional)
- Agent 1:1 Wallet
- Agent N:M MCPResource (via access rights)

## Validation Rules
- confidence_score in [0, 1]
- status enums must match allowed values
- Wallet balance >= 0

## State Transitions
- Task: pending → in_progress → completed/failed
- Review: pending → approved/rejected
- Agent: active ↔ paused ↔ error

---

**Created:** 2026-02-06
**Maintainer:** Project Chimera Core Team
