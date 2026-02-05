# Developer Tooling Strategy

## Model Context Protocol (MCP) Servers
To assist in the development of Project Chimera, the following MCP servers are configured:

### 1. git-mcp
- **Purpose**: Automated version control and branch management.
- **Usage**: Allows the AI agent to create feature branches for each spec and commit changes with descriptive, spec-referenced messages.

### 2. filesystem-mcp
- **Purpose**: Secure file system access.
- **Usage**: Enables the agent to read/write to the `specs/` and `skills/` directories, ensuring the Project DNA is always up to date.