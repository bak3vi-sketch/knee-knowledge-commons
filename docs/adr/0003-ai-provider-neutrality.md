# ADR 0003: AI provider neutrality

Status: Accepted

## Context
AI model quality, pricing, privacy terms, tool support, and availability change quickly. The project's knowledge and community should outlive any one vendor.

## Decision
Patient-facing and maintainer AI features should use a thin provider-neutral gateway or adapter layer. Vendor-specific tools may be used when useful, but canonical knowledge, evaluation cases, prompts/policies, and core data models must not depend on one provider.

Research workspaces such as Gemini Notebook/NotebookLM may be used as optional research aids, not as the canonical publication system.

## Consequences
- Models/providers can be changed without rebuilding the product.
- Different tasks can use different providers.
- Vendor-specific features must not become hidden requirements for accessing the knowledge commons.
- Model changes require safety/quality evaluation before broad rollout.

## Change threshold
Any deliberate vendor lock-in must be documented with the benefit, exit strategy, migration cost, privacy impact, and alternatives.
