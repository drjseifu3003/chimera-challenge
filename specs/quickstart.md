# Project Chimera - Quickstart Guide

## Prerequisites
- Python 3.10+
- Docker & Docker Compose
- PostgreSQL, Redis, Weaviate running (see docker-compose.yml)
- Coinbase AgentKit credentials

## Setup
1. Clone the repository:
   git clone https://github.com/your-org/chimera-challenge.git
2. Install dependencies:
   uv sync
   # Uses pyproject.toml and uv.lock for dependency management
3. Start services:
   docker-compose up -d
4. Configure environment variables:
   - MCP_SERVER_URL
   - COINBASE_API_KEY
   - POSTGRES_URL
   - REDIS_URL
   - WEAVIATE_URL
5. Run migrations:
   python scripts/migrate.py
6. Launch the agent swarm:
   python main.py

## Testing
- Run all tests:
  pytest tests/

## Extending
- Add new MCP tools in the /skills directory
- Update OpenAPI contracts in /specs/contracts

---

**Created:** 2026-02-06
**Maintainer:** Project Chimera Core Team
