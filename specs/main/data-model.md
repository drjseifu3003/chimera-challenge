# Data Model: Skill Output Contracts

## ContentGeneratorOutput
- **content_id**: string, required
- **format**: string, enum: video | image | text, required
- **content_url**: string (URL), required
- **metadata**: object, optional
  - **title**: string, optional
  - **caption**: string, optional

## TrendAnalyzerOutput
- **trends**: array of TrendItem, required

### TrendItem
- **topic**: string, required
- **relevance_score**: number (0.0 - 1.0), required
- **source_url**: string (URL), required

## WalletManagerOutput
- **action**: string, enum: transfer | balance | check_tx, required
- **status**: string, enum: success | failed, required
- **result**: object, required
  - **transaction_id**: string, optional (transfer/check_tx)
  - **balance**: number, optional (balance)
  - **currency**: string, optional (balance)
  - **confirmation_status**: string, optional (check_tx)
  - **confirmations**: integer, optional (check_tx)
- **message**: string, optional
