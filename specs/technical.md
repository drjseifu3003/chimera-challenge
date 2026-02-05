# Technical Specification: Project Chimera

## API Contracts

### Planner → Worker (Task Request)
- **Input Schema**:
  ```json
  {
    "task_id": "string (UUID)",
    "goal": "string (high-level objective)",
    "subtasks": ["string (list of decomposed tasks)"],
    "context": {
      "agent_id": "string (UUID)",
      "persona": "string (e.g., 'Tech Influencer')",
      "budget": "number (max inference cost in USD)",
      "deadline": "string (ISO 8601 timestamp)"
    },
    "resources": ["string (list of MCP resource URIs for perception)"]
  }
  ```
- **Output Schema** (from Worker):
  ```json
  {
    "task_id": "string (UUID)",
    "status": "string (enum: 'completed', 'failed', 'pending')",
    "result": "string (generated content or error message)",
    "confidence_score": "number (0.0-1.0)",
    "metadata": {
      "execution_time": "number (seconds)",
      "tools_used": ["string (list of MCP tool calls)"]
    }
  }
  ```

### Worker → Judge (Review Submission)
- **Input Schema**:
  ```json
  {
    "task_id": "string (UUID)",
    "submission": "string (worker's output)",
    "confidence_score": "number (0.0-1.0)",
    "agent_id": "string (UUID)",
    "character_seed": "string (random seed for persona consistency)"
  }
  ```
- **Output Schema** (from Judge):
  ```json
  {
    "task_id": "string (UUID)",
    "approval": "boolean",
    "feedback": "string (reasons for approval/rejection)",
    "adjusted_confidence": "number (0.0-1.0, if modified)",
    "actions": ["string (list of corrective actions, e.g., 'retry', 'escalate')"]
  }
  ```

## Database Schema

### Hybrid Storage Model
- **Transactional (PostgreSQL)**: For high-velocity video metadata.
- **Semantic (Weaviate)**: For long-term memory and persona evolution.
- **Episodic (Redis)**: For short-term caching (not detailed here).

### SQL ERD (PostgreSQL Tables)
- **agents**:
  - agent_id (UUID, PK)
  - character_seed (VARCHAR, random seed for consistency)
  - persona (VARCHAR, e.g., 'Tech Influencer')
  - wallet_address (VARCHAR, crypto wallet)
  - created_at (TIMESTAMP)

- **tasks**:
  - task_id (UUID, PK)
  - agent_id (UUID, FK to agents)
  - goal (TEXT)
  - status (ENUM: 'pending', 'in_progress', 'completed', 'failed')
  - confidence_score (DECIMAL(3,2), 0.0-1.0)
  - created_at (TIMESTAMP)
  - updated_at (TIMESTAMP)

- **videos** (high-velocity metadata):
  - video_id (UUID, PK)
  - agent_id (UUID, FK to agents)
  - title (VARCHAR)
  - duration (INT, seconds)
  - upload_date (TIMESTAMP)
  - views (BIGINT)
  - engagement_rate (DECIMAL(5,2))

- **Relationships**:
  - agents (1) -- (*) tasks
  - agents (1) -- (*) videos

### Weaviate Schema (Semantic Memory)
- **Class: AgentMemory**
  - Properties: agent_id (UUID), memory_type (text, e.g., 'persona_evolution'), content (text), vector (vector for RAG)
  - Used for long-term persona evolution and world knowledge retrieval.