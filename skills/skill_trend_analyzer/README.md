# Skill: Trend Analyzer
Polls MCP social/news resources to identify trends relevant to a specific persona.

- **Input Contract**:
```json
{
  "persona_id": "string",
  "sources": ["list of MCP resource URIs"]
}
```

- **Output Contract**:
```json
{
  "trends": [
    {
      "topic": "string",
      "relevance_score": 0.0,
      "source_url": "string"
    }
  ]
}
```