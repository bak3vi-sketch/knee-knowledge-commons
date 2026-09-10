# Plan 0004 — Website MVP

Status: Planned

## Goal
Make reviewed knowledge useful to ordinary people through a simple, mobile-first interface while keeping GitHub as the canonical knowledge backend.

## Core screens
- Home: “What situation are you in?” journey chooser.
- Topic/journey page: concise answer, reviewed evidence, uncertainty, community experience, questions to ask, sources.
- Search: natural-language and structured filters.
- Explain a report: user enters/pastes wording from an existing radiology report for plain-language explanation, not raw-image diagnosis.
- Prepare for appointment: generate a personal question/checklist summary from user-provided context without prescribing treatment.
- Contribute/correct: clinician, researcher, community, and product feedback entry points.

## Technical principles
- static/derived rendering where possible for speed and reliability;
- canonical content pulled from GitHub-reviewed sources;
- private user data handled separately from public content;
- accessibility and translation built into component/content design;
- analytics should minimize collection and avoid unnecessary health-data tracking.

## Non-goals for first public MVP
- raw MRI/DICOM interpretation;
- treatment recommendation engine;
- clinician/hospital rankings;
- large social feed;
- uncontrolled patient-to-patient medical advice;
- complex account system unless required for contribution privacy/withdrawal.

## Acceptance criteria
A non-technical user on a phone can find the relevant journey, understand the status/source of information, reach source details, suggest a correction, and understand that the site supports rather than replaces individualized clinical care.
