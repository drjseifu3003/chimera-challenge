# Research Summary: Skill Output Contracts

## Decision: Document outputs in skill READMEs + JSON schemas
- Decision: Add an Output Contract section to each skill README and publish JSON schema files under specs/main/contracts.
- Rationale: Keeps developer-facing docs close to each skill while providing machine-readable contracts for validation and future tooling.
- Alternatives considered: README-only contracts (no machine-readable schema), schemas-only (harder for human scanning).

## Decision: Align trend analyzer output with existing tests
- Decision: Use {"trends": [{"topic", "relevance_score", "source_url"}]} for trend analyzer output.
- Rationale: Matches existing tests and avoids changes to behavior.
- Alternatives considered: Adding metadata envelopes or pagination fields (deferred until implementation exists).

## Decision: Use minimal, action-aware wallet manager output
- Decision: Standardize wallet manager output with {"action", "status", "result"} and optional fields based on action.
- Rationale: Supports transfer, balance, and check_tx without overfitting to backend details.
- Alternatives considered: Separate output shapes per action (more files, less reuse).
