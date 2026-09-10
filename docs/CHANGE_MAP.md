# Change Map

This file helps agents answer one question before finishing a task:

> **If I changed X, what else must I inspect before I can claim the work is complete?**

The table is a review trigger, not a requirement to edit every listed file. If a related file remains correct, leave it unchanged and note that it was checked when relevant.

| If this changes | Inspect at minimum | Typical reason |
|---|---|---|
| Project goal, current phase, active work, major decision | `CONTINUITY.md`, active `plans/`, `ROADMAP.md` | Keep live state and staged direction aligned |
| Product scope or major user journey | `docs/PRODUCT_VISION.md`, `docs/USER_JOURNEYS.md`, active plan, `CONTINUITY.md` | Avoid product/plan drift |
| Architecture, major component, data flow, system boundary | `docs/ARCHITECTURE.md`, relevant ADR, active plan, `CONTINUITY.md` | Preserve source-of-truth and critical paths |
| Durable architecture/governance decision | `docs/adr/`, `docs/ARCHITECTURE.md`, `GOVERNANCE.md` if relevant | Record why a hard-to-reverse decision exists |
| Schema or data contract | `schemas/`, `docs/CONTENT_MODEL.md`, `docs/DATA_BOUNDARIES.md`, `PRIVACY.md`, architecture | Prevent schema/data-policy mismatch |
| Private patient-data handling, consent, deletion, external AI data flow | `PRIVACY.md`, `docs/DATA_BOUNDARIES.md`, architecture, governance | Privacy is a hard boundary |
| AI retrieval/answer behavior, provider integration or evaluation policy | `docs/AI_POLICY.md`, architecture, safety, evaluation/test artifacts | Keep model behavior governed and replaceable |
| Medical meaning in patient-facing content | evidence record(s), `docs/EVIDENCE_MODEL.md`, review status, source citations, `MEDICAL_SAFETY.md` | Every meaningful medical claim must remain traceable |
| Evidence scope/applicability or certainty | evidence record(s), related knowledge page, contradiction/gap notes | Do not silently generalize evidence |
| Agent rule/workflow | `AGENTS.md`, PR template, `docs/CHANGE_MAP.md`, `CONTINUITY.md` if workflow state changes | Make agent behavior self-consistent |
| Contribution/review workflow | `CONTRIBUTING.md`, `GOVERNANCE.md`, `.github/`, architecture | Website/GitHub paths must converge on one review model |
| Translation/localization behavior | `docs/TRANSLATION.md`, patient-facing content, local-context model | Avoid duplicate truth and translation drift |
| Vietnam-specific health-system context | local-context content, translation/localization policy, evidence labels | Never present local context as universal evidence |
| Security/deployment behavior | `SECURITY.md`, architecture, relevant plan, validation/CI | Operational risk needs explicit checks |
| A notable user/reviewer/project behavior change | `CHANGELOG.md` | Preserve useful history without logging every commit |
| Task materially changes Goal/constraints/decisions/Now/Next/working set | `CONTINUITY.md` | Future agents need current state, not old chat history |

## Before opening or merging a non-trivial PR

1. Identify the rows above that match the work.
2. Inspect every listed source-of-truth that could now be stale.
3. Update only the files whose information actually changed.
4. Update `CONTINUITY.md` when the live project state changed.
5. Add a `CHANGELOG.md` entry only when the change is notable.
6. State any required check that could not be performed.

## Avoid documentation inflation

Do not create a new status, architecture, roadmap, changelog, translation, or policy file when an existing canonical file already owns that responsibility. Prefer one clear source of truth plus links over parallel documents that can drift.