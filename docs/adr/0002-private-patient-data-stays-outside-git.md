# ADR 0002: Private patient data stays outside Git

Status: Accepted

## Context
Git history is durable and public repositories are inappropriate for private health submissions, consent records, withdrawal requests, or identifiable medical files.

## Decision
Raw/private patient submissions and identity/consent data must live outside Git in a purpose-built protected data store. Git may contain only reviewed public knowledge, aggregate findings, and intentionally public de-identified material permitted by governance.

## Consequences
- Patient withdrawal/deletion can be implemented without rewriting public Git history.
- Public repo access does not imply patient-data access.
- Any pipeline that publishes a community-derived insight must cross an explicit privacy/review boundary.

## Change threshold
This decision should be treated as a privacy invariant. Any exception requires dedicated privacy, legal, security, and governance review before implementation.
