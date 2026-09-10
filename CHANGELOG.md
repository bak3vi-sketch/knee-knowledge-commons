# Changelog

This file records **notable project changes** that matter to maintainers, contributors, reviewers, or users.

It is not a commit log. Do not add every formatting edit, typo fix, or routine evidence-record change. Use Git history and PRs for that level of detail.

For medical knowledge, `CHANGELOG.md` does **not** replace claim-level provenance, evidence records, review state, or source citations.

## [Unreleased]

### Changed
- Simplified multilingual project documentation: browser/AI translation is acceptable for internal project documents; duplicate `.vi.md` mirrors are no longer required by default.
- Added a cross-agent continuity model centered on `CONTINUITY.md`.
- Strengthened agent pre-flight/post-flight checks and documentation synchronization rules.
- Extended architecture documentation with source-of-truth and critical-path guidance.
- Advanced the active state to Plan 0002 / Issue #3 after completing the continuity-workflow upgrade.

### Added
- `CONTINUITY.md` — live project state and cross-agent memory.
- `docs/CHANGE_MAP.md` — documentation dependency/update triggers.
- `scripts/validate_repo.py` — lightweight structural/continuity validator; it intentionally does not judge medical correctness.
- `.github/workflows/repository-quality.yml` — runs the validator on pull requests and pushes to `main`.

## [2026-09-10] — Vietnam-first strategy and narrow pilot

### Changed
- Adopted **Vietnam-first, global-ready** as the launch strategy.
- Narrowed the first ACL/meniscus work from a broad knowledge base to one end-to-end vertical-slice pilot for newly diagnosed ACL injury with or without associated meniscus injury.
- Kept shared medical evidence separate from Vietnam-specific local context.

### Added
- A Vietnamese owner guide and initial Vietnamese community entry point.

## [2026-09-10] — Foundation v0.1

### Added
- Mission, README, contribution policy, code of conduct, governance, privacy, medical-safety and security policies.
- Evidence/content models, structured schemas, system architecture, roadmap, staged plans and ADRs.
- Specialized agent roles for evidence research, citation verification, privacy, safety, community intake, maintenance and translation.
- GitHub issue/PR templates and CODEOWNERS.

### Safety posture
- No personalized treatment engine, raw MRI interpretation, universal rehabilitation protocol, or private patient-data collection was introduced in the foundation.