# Agent Operating Rules

These rules apply to every AI/coding/research agent working in this repository.

## Required reading
Before changing the project, read `README.md`, `MEDICAL_SAFETY.md`, `PRIVACY.md`, `GOVERNANCE.md`, `docs/EVIDENCE_MODEL.md`, `docs/ARCHITECTURE.md`, and the relevant file in `plans/`.

## Non-negotiable invariants
1. Keep **research evidence**, **clinical interpretation**, and **patient experience** distinct.
2. Never commit identifiable patient health data, medical records, raw MRI/DICOM, private submissions, or consent records to Git.
3. Never fabricate a citation. A cited source must support the claim actually written.
4. Preserve uncertainty, subgroup limits, conflicting evidence, and negative/null findings.
5. AI may draft and review, but must not be the sole approver for changes that alter medical meaning or safety behavior.
6. Do not diagnose an individual or prescribe personalized surgery, medication, rehabilitation progression, exercise dose, or return-to-sport date.
7. Design the future website as the main interface for patients and most contributors; GitHub remains the source of truth and expert/maintainer interface.
8. Keep AI-provider integrations replaceable. Avoid unnecessary lock-in to one model/vendor.
9. Collect the minimum patient data required and preserve withdrawal/deletion paths outside Git.
10. Plain language, mobile-first UX, accessibility, and multilingual support are product requirements.

## Change discipline
- Use an issue or plan for non-trivial work.
- Keep PRs focused and explain why the change is needed.
- Update docs when architecture, data contracts, safety rules, or workflows change.
- Medical claims must retain source provenance and review state.
- If full source verification is unavailable, state that limitation and do not present a definitive conclusion.

## Never autonomously
- merge safety-critical medical content;
- publish private patient submissions;
- infer identity from health data;
- interpret raw imaging as a clinical diagnosis for a user;
- rank treatments/clinicians using unreviewed anecdotal outcomes;
- hide conflicting evidence for simplicity;
- strengthen a conclusion beyond what its source supports.

When convenience conflicts with safety, privacy, traceability, or evidence integrity, preserve safety/privacy/traceability/integrity and document the trade-off.
