# ADR 0001: GitHub is canonical for reviewed public knowledge

Status: Accepted

## Context
The project needs transparent provenance, version history, reviewable changes, and a stable substrate for humans and agents.

## Decision
Reviewed public knowledge, governance, schemas, and project rules are canonical in this GitHub repository. Website pages, search indexes, embeddings, and caches are derived from that canonical layer.

## Consequences
- Public knowledge changes are auditable and reversible.
- AI agents can propose changes through PRs.
- The website does not become a separate competing truth system.
- Private patient submissions are explicitly excluded; see ADR 0002.

## Change threshold
Reversing this decision requires a dedicated governance PR explaining migration, provenance, auditability, and agent-workflow implications.
