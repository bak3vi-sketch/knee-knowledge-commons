# Plan 0003 — Contribution System

Status: Planned

## Goal
Make useful contribution easy for patients, clinicians, and researchers without requiring GitHub skills or compromising privacy.

## Contributor paths

### Clinician/researcher
Website form accepts a DOI/PMID/URL, affected topic, short note, and conflict-of-interest disclosure. Agents retrieve/structure the source, compare it with existing knowledge, and prepare a reviewer packet or PR.

### Patient/community member
A guided conversational form gathers lived experience using minimal, coarse, privacy-aware fields. The user reviews what will be stored/shared and can later withdraw private submissions through the application workflow.

### GitHub-native contributor
Issues/PRs remain available and enter the same review state machine as website submissions.

## Required pipeline
`submitted -> privacy/safety screening -> normalized -> source/evidence checks -> human review -> approved/rejected -> publish/index`

Private patient submissions never synchronize directly into Git.

## Required design work before collecting patient stories
- consent language and versioning;
- data-minimization review;
- re-identification risk review;
- moderation rules;
- withdrawal/deletion workflow;
- access roles;
- retention policy;
- clear explanation of public vs private use;
- jurisdiction/legal review appropriate to launch regions.

## Non-goals
- public GitHub issues as a patient-story database;
- fully automated acceptance of contributed medical claims;
- ranking treatment effectiveness from uncontrolled community submissions.

## Acceptance criteria
A contributor can provide useful input in a few minutes without Git knowledge; reviewers receive structured, traceable material; patient-private data remains outside Git; and all entry points converge on one review workflow.
