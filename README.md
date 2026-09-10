# Knee Knowledge Commons

**Open, evidence-aware knowledge for people navigating knee injuries — built with patients, clinicians, researchers, and AI.**

Knee Knowledge Commons is a community project to help people prevent avoidable mistakes, understand their options, prepare better questions, and make better-informed decisions together with qualified healthcare professionals.

The initial focus is knee ligament and meniscus injuries, especially ACL and meniscus injuries. The long-term goal is a multilingual, patient-friendly knowledge commons that combines reviewed medical evidence with clearly labeled lived experience.

> **Launch strategy: Vietnam-first, global-ready.** The first real-world users, patient journeys, language, and local-context workflows will be developed and tested in Vietnam. Evidence structures, schemas, provenance, architecture, and governance remain internationally reusable so global expansion does not require rebuilding the project.

**Tiếng Việt:** [README.vi.md](README.vi.md) · **Dành cho chủ dự án:** [docs/OWNER_GUIDE.vi.md](docs/OWNER_GUIDE.vi.md)

## What this project is

- A versioned, reviewable source of truth for approved knowledge.
- A bridge between research evidence, clinical expertise, and patient experience.
- A foundation for a patient-friendly website, search, decision-support education, and source-grounded AI Q&A.
- An open workflow where AI agents help research, structure, translate, verify, and maintain knowledge, while humans retain responsibility for high-impact decisions.

## What this project is not

- It is **not a substitute for a clinician**.
- It does **not diagnose individuals or prescribe personalized treatment**.
- A patient story is **not proof** that a treatment works.
- AI-generated text is **not accepted as medical truth without traceable sources and appropriate review**.
- This public Git repository is **not a place for medical records, MRI/DICOM files, identifiable health data, or private patient submissions**.

## Product principle

> GitHub is the knowledge-management backend. The future website is the main door for patients and most contributors.

Patients, clinicians, and researchers should eventually be able to read, search, ask questions, suggest corrections, and contribute through a simple website. GitHub remains available for contributors who prefer it and for maintainers, developers, reviewers, and agents.

## Vietnam-first, global-ready

During the initial product phase:
- Vietnamese is the primary patient-facing language;
- early user research and usability testing focus on people in Vietnam;
- Vietnam-specific care pathways, terminology, and access constraints are stored as local context rather than universal medical truth;
- core evidence records, schemas, identifiers, and architecture remain language- and provider-neutral;
- international evidence remains usable when its population and scope are applicable;
- global expansion happens only after the end-to-end workflow works reliably in the first market.

## Knowledge layers

1. **Evidence** — guidelines, systematic reviews, trials, observational research, and other traceable sources.
2. **Clinical interpretation** — clearly attributed expert interpretation, never silently promoted to evidence.
3. **Community experience** — self-reported lived experience, always labeled as such.
4. **Synthesis** — reviewed summaries that explicitly preserve uncertainty, disagreement, population differences, and source provenance.

See [Evidence Model](docs/EVIDENCE_MODEL.md).

## Project memory and source-of-truth

The repository is designed so a new AI agent or maintainer can recover context without depending on previous chat history:

- `AGENTS.md` — how agents must work.
- `CONTINUITY.md` — current goal, decisions, state, next work, and active references.
- `ROADMAP.md` — long-term staged direction.
- `plans/` — bounded execution plans and acceptance criteria.
- `docs/ARCHITECTURE.md` — system boundaries, source-of-truth map, and critical paths.
- `docs/adr/` — durable architecture decisions and rationale.
- `docs/CHANGE_MAP.md` — what related documentation must be inspected after different kinds of changes.
- `CHANGELOG.md` — notable historical changes; not a duplicate commit log.

## Repository map

- `knowledge/` — approved patient-facing knowledge.
- `evidence/` — evidence records and source notes.
- `community-experience/` — rules and aggregate outputs for lived experience; raw/private submissions do not belong here.
- `schemas/` — machine-readable data contracts.
- `agents/` — task-specific agent instructions.
- `docs/` — architecture, product, safety-supporting and governance-supporting documentation.
- `plans/` — staged implementation plans.
- `.github/` — contribution and review workflows.

## Documentation language

Internal project documentation normally has **one canonical version**; browser/AI translation may be used when needed. We do not maintain language mirrors by default because duplicate documents can drift.

Dedicated Vietnamese artifacts are kept where they serve a distinct purpose, including the Vietnamese community README, the project-owner guide, and reviewed Vietnamese patient-facing medical content.

See [Translation and Localization Strategy](docs/TRANSLATION.md).

## Non-negotiable safeguards

Read these before contributing or asking an agent to change the project:

- [AGENTS.md](AGENTS.md)
- [MEDICAL_SAFETY.md](MEDICAL_SAFETY.md)
- [PRIVACY.md](PRIVACY.md)
- [GOVERNANCE.md](GOVERNANCE.md)
- [CONTRIBUTING.md](CONTRIBUTING.md)

## Current status

Do not rely on this paragraph as the live project tracker. See [`CONTINUITY.md`](CONTINUITY.md) for current state.

Foundation v0.1 is complete, the Vietnam-first strategy is adopted, and the first execution pilot is intentionally narrow: prove one complete, traceable Vietnamese patient journey for a person newly diagnosed with **ACL injury with or without associated meniscus injury** before expanding the ACL/meniscus knowledge base.