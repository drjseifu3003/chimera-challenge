# Quickstart: Skill Output Contracts

This quickstart documents output contracts for the core skills. Contracts are defined in skill READMEs and JSON schema files under specs/main/contracts.

## Content Generator
- Input: skills/skill_content_generator/README.md
- Output schema: specs/main/contracts/content-generator.output.json

Example output:
```json
{
  "content_id": "cg_123",
  "format": "text",
  "content_url": "https://cdn.example.com/content/cg_123.txt",
  "metadata": {
    "title": "Daily Insight",
    "caption": "Key trends for today"
  }
}
```

## Trend Analyzer
- Input: skills/skill_trend_analyzer/README.md
- Output schema: specs/main/contracts/trend-analyzer.output.json

Example output:
```json
{
  "trends": [
    {
      "topic": "Autonomous Agents",
      "relevance_score": 0.98,
      "source_url": "https://mcp.news/trends/1"
    }
  ]
}
```

## Wallet Manager
- Input: skills/skill_wallet_manager/README.md
- Output schema: specs/main/contracts/wallet-manager.output.json

Example output:
```json
{
  "action": "balance",
  "status": "success",
  "result": {
    "balance": 12.5,
    "currency": "USDC"
  },
  "message": "Balance retrieved"
}
```
