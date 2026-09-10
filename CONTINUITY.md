# Continuity Ledger

This file is the **live project memory for agents and maintainers**. It answers: what are we trying to achieve now, what has already been decided, what is in progress, and what should happen next.

Do not copy conversation history here. Update only when goals, constraints, important decisions, state, open questions, or the active working set materially change.

Last updated: 2026-09-10

## Goal
Prove a safe, traceable, useful end-to-end knowledge workflow for Vietnamese patients with newly diagnosed **ACL injury with or without associated meniscus injury**, then reuse that workflow before expanding content or product scope.

## Constraints / assumptions
- Strategy is **Vietnam-first, global-ready**.
- GitHub is the canonical store for reviewed public knowledge, governance, evidence metadata, schemas, plans, and agent rules.
- Private/identifiable patient health data must stay outside Git.
- Patient experience, clinical interpretation, and research evidence remain distinct.
- AI can research, structure, draft, verify, translate, and prepare PRs, but cannot be the sole approver for changes that alter medical meaning or safety behavior.
- Browser/AI translation is acceptable for internal project documents; do not maintain duplicate translations by default.
- Vietnamese patient-facing medical content remains a deliberate product output and requires appropriate review.

## Key decisions
- Foundation v0.1 is complete.
- The first launch market and user-research context is Vietnam; architecture/evidence structures remain internationally reusable.
- Phase 1 begins with one vertical slice, not a broad ACL/meniscus encyclopedia.
- The active pilot scenario is a person newly diagnosed with ACL injury, with or without associated meniscus injury.
- `CONTINUITY.md` is the single live state ledger; do not create a competing `PROJECT_STATE.md`.
- `CHANGELOG.md` records notable project changes, not every commit.
- `docs/ARCHITECTURE.md` is the canonical architecture map; do not create a duplicate root architecture file.
- `docs/OWNER_GUIDE.vi.md` is a concise Vietnamese owner guide, not a mirror of all English project documentation.
- Keep `README.vi.md` for the initial Vietnamese community entry point; do not create parallel `.vi.md` copies of every policy/plan.

## State

### Done
- [x] Foundation v0.1: mission, governance, safety, privacy, evidence model, schemas, agent roles, plans, contribution templates.
- [x] Adopted Vietnam-first, global-ready strategy.
- [x] Narrowed Plan 0002 to one ACL ± meniscus vertical slice.
- [x] Established website-as-front-door / GitHub-as-canonical-knowledge architecture.

### Now
- [ ] Strengthen cross-agent continuity and documentation-sync workflow.
- [ ] Prepare to execute Plan 0002 / Issue #3.

### Next
1. Define and approve the first small set of real Vietnamese patient questions for the newly diagnosed ACL ± meniscus journey.
2. Build a small source inventory for that journey.
3. Create structured evidence records and applicability checks.
4. Obtain appropriate human review before approved Class C patient-facing content.
5. Produce one reviewed Vietnamese patient-facing journey and a source-grounded Q&A prototype.

## Open questions
- Who will serve as the first qualified clinical/evidence reviewer(s) for the pilot?
- What exact 5–10 patient questions should form the initial Vietnam pilot set?
- When should GitHub native branch protection/rulesets be enabled? See Issue #2.
- Which AI/retrieval provider should power the later prototype? This is intentionally deferred until the knowledge pipeline works.

## Active work / references
- Active plan: `plans/0002-acl-meniscus-knowledge-pilot.md`
- Active execution issue: #3 — Vietnam ACL ± meniscus vertical-slice pilot
- Repository-protection follow-up: #2
- Agent entrypoint: `AGENTS.md`
- Architecture: `docs/ARCHITECTURE.md`
- Documentation dependency map: `docs/CHANGE_MAP.md`
- Evidence rules: `docs/EVIDENCE_MODEL.md`
- Safety boundary: `MEDICAL_SAFETY.md`
- Privacy boundary: `PRIVACY.md`
- Governance: `GOVERNANCE.md`
- Owner orientation: `docs/OWNER_GUIDE.vi.md`

## Maintenance rule
Before declaring a non-trivial task complete, compare the result against this ledger. If reality changed, update this file in the same PR. If nothing here changed, do not edit it just to create activity.