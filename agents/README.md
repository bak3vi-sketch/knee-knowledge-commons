# Agent Roles

Agents are specialized helpers. Their outputs are proposals, structured records, checks, or drafts — not independent medical authority.

All agents inherit `AGENTS.md`, `MEDICAL_SAFETY.md`, `PRIVACY.md`, and `GOVERNANCE.md`.

## Initial roles
- `evidence-researcher.md` — discover and structure relevant literature/guidelines.
- `citation-verifier.md` — verify that sources exist and support claims.
- `community-intake.md` — structure lived-experience submissions without turning them into evidence.
- `privacy-reviewer.md` — detect risky personal/health information before publication.
- `safety-reviewer.md` — classify medical/safety impact and flag unsupported guidance.
- `knowledge-maintainer.md` — detect stale knowledge and prepare update PRs.
- `translator.md` — produce translation drafts while preserving medical nuance.

## Common workflow
`input -> role-specific analysis -> structured output -> status label -> human review when required -> durable knowledge change`

Agents should communicate uncertainty and missing access explicitly. They must not fabricate completion, source verification, credentials, consent, or review state.
