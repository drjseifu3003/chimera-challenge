# Skill: Wallet Manager (Coinbase AgentKit)
Handles on-chain transactions and balance checks for economic agency.

- **Input Contract**:
```json
{
  "action": "transfer|balance|check_tx",
  "amount": 0.0,
  "recipient_address": "string"
}
```

- **Output Contract**:
```json
{
  "action": "transfer|balance|check_tx",
  "status": "success|failed",
  "result": {
    "transaction_id": "string",
    "balance": 0.0,
    "currency": "string",
    "confirmation_status": "string",
    "confirmations": 0
  },
  "message": "string"
}
```