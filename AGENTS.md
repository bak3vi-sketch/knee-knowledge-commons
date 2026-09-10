# Agent Operating Rules

These rules apply to every AI, coding, research, documentation, and maintenance agent working in this repository.

## Start every non-trivial session

1. Read `CONTINUITY.md` first. It is the live project memory: current goal, constraints, decisions, state, next work, and active files/issues.
2. Read the active plan named in `CONTINUITY.md`.
3. Read `README.md` when you need mission/scope orientation.
4. Load specialized context only when the task needs it:
   - medical/evidence work → `MEDICAL_SAFETY.md` + `docs/EVIDENCE_MODEL.md`;
   - patient/private data → `PRIVACY.md` + `docs/DATA_BOUNDARIES.md`;
   - architecture/AI/data flow → `docs/ARCHITECTURE.md` + relevant ADR/`docs/AI_POLICY.md`;
   - governance/review changes → `GOVERNANCE.md`;
   - language/localization → `docs/TRANSLATION.md`.
5. Do not guess the content or state of a file you have not inspected when that file could materially affect the task.

The goal is **progressive context loading**: read enough to be correct and safe, but do not flood the context with unrelated documents.

## Non-negotiable invariants

1. Keep **research evidence**, **clinical interpretation**, and **patient experience** distinct.
2. Never commit identifiable patient health data, medical records, raw MRI/DICOM, private submissions, or consent records to Git.
3. Never fabricate a citation. A cited source must support the claim actually written.
4. Preserve uncertainty, subgroup limits, conflicting evidence, negative/null findings, and source applicability.
5. AI may draft and review, but must not be the sole approver for changes that alter medical meaning or safety behavior.
6. Do not diagnose an individual or prescribe personalized surgery, medication, rehabilitation progression, exercise dose, or return-to-sport date.
7. Design the future website as the main interface for patients and most contributors; GitHub remains the canonical public-knowledge/review backend.
8. Keep AI-provider integrations replaceable. Avoid unnecessary lock-in to one model/vendor.
9. Collect the minimum patient data required and preserve withdrawal/deletion paths outside Git.
10. Plain language, mobile-first UX, accessibility, and multilingual support are product requirements.
11. Follow **Vietnam-first, global-ready**: validate the first product and contribution flows in Vietnam while keeping schemas, evidence provenance, identifiers, architecture, and governance internationally reusable.
12. Do not silently turn Vietnam-specific care pathways, insurance assumptions, terminology, referral patterns, or access constraints into universal guidance.
13. Prefer one canonical project document over parallel copies that can drift. Browser/AI translation is acceptable for internal documentation. Vietnamese patient-facing medical content remains a deliberate reviewed product output.

## Pre-flight before changing anything substantial

Before implementation/research edits, identify:
- the active goal/plan;
- the exact problem being solved;
- the governance/risk class (A/B/C/D when applicable);
- which sources of truth own the affected information;
- which rows in `docs/CHANGE_MAP.md` apply;
- what evidence/check will show the task is actually complete.

If the request conflicts with the active plan or an invariant, do not silently broaden scope. Explain the conflict and take the smallest safe path that preserves project direction.

## Change discipline

- Use an issue or plan for non-trivial work.
- Keep PRs focused and explain why the change is needed, not only which files changed.
- Medical claims must retain source provenance, applicability, uncertainty, and review state.
- Significant scope changes update the active plan before or with implementation.
- Durable architecture/governance decisions should use or update an ADR when appropriate.
- `CONTINUITY.md` is the only live project-state ledger; do not create competing state/status files.
- `CHANGELOG.md` records notable changes, not every commit.
- `docs/ARCHITECTURE.md` is the canonical architecture map; do not create a duplicate root architecture file.

## Post-flight before saying “done”

1. Review the complete diff/change set, not only the last edited file.
2. Use `docs/CHANGE_MAP.md` to inspect every related source of truth that could now be stale.
3. Update `CONTINUITY.md` if Goal, constraints, decisions, Now/Next, open questions, or working set materially changed.
4. Update the active plan if progress, scope, acceptance criteria, blockers, or completion state changed.
5. Update `docs/ARCHITECTURE.md`/ADR only when architecture, boundaries, critical paths, or durable decisions changed.
6. Add a `CHANGELOG.md` entry only for notable project/user/reviewer behavior changes.
7. Run the relevant enforced checks/validation if available. Markdown rules are guidance, not evidence that a check passed.
8. If an expected check cannot be run, state **not run**, why, and the remaining risk.
9. For Class C/D medical/safety changes, do not treat agent review as final human approval.

A task is not complete merely because the requested file/code was edited; the repository must remain internally consistent.

## Owner-facing communication

When a non-trivial task requires a decision from the project owner, explain in Vietnamese and plain language:
- the problem;
- why it matters now;
- expected benefit;
- important risk/trade-off;
- what decision is needed;
- what counts as completion.

Do not require the owner to interpret implementation details, schemas, AI infrastructure, or medical-research terminology without explanation. This does **not** require maintaining duplicate Vietnamese copies of internal documentation.

## Never autonomously

- merge safety-critical medical content;
- publish private patient submissions;
- infer identity from health data;
- interpret raw imaging as a clinical diagnosis for a user;
- rank treatments/clinicians using unreviewed anecdotal outcomes;
- hide conflicting evidence for simplicity;
- strengthen a conclusion beyond what its source supports;
- expand from the Vietnam pilot to global product assumptions before the workflow is proven reusable;
- mark a plan/phase complete when its exit criteria are not evidenced.

When convenience conflicts with safety, privacy, traceability, evidence integrity, or maintainable internationalization, preserve those constraints and document the trade-off.