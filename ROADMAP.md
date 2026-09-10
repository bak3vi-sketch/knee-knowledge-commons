# Roadmap

The roadmap is stage-gated rather than date-driven. Safety, evidence quality, and usable workflows matter more than shipping a large feature set quickly.

## Strategic launch model — Vietnam-first, global-ready
The first real-world product, content, contribution, and AI workflows are validated in Vietnam. This is a launch-market choice, not a limit on the evidence base or architecture. Core schemas, provenance, governance, identifiers, and AI-provider interfaces remain globally reusable. Vietnam-specific health-system context is modeled separately from universal or internationally sourced medical evidence.

## Phase 0 — Foundation
Goal: make the project difficult to accidentally steer in an unsafe or incoherent direction.

Deliverables:
- mission, governance, privacy, and medical-safety rules;
- agent operating rules;
- evidence/content models and system architecture;
- initial ACL + meniscus pilot structure;
- contribution templates and architecture decision records.

Exit condition: maintainers can classify a proposed change and know what review it requires.

Status: **complete for v0.1**, with governance expected to evolve.

## Phase 1A — Vietnam vertical-slice pilot: newly diagnosed ACL ± meniscus
Goal: prove one complete evidence-to-patient workflow before attempting a broad ACL/meniscus knowledge base.

Pilot question:
> A person in Vietnam has just been told they have an ACL injury, with or without an associated meniscus injury. What does the diagnosis mean, what can and cannot be concluded from the available information, what commonly matters next, and what useful questions should they prepare for a qualified clinician?

Deliverables:
- a small inventory of authoritative/current source material relevant to this journey;
- structured evidence records with population, scope, exclusions, limitations, provenance, and review status;
- explicit applicability checks distinguishing isolated ACL, isolated meniscus, and combined ACL + meniscus populations;
- citation-verification and contradiction/scope checks;
- one reviewed Vietnamese patient-facing knowledge journey;
- one prototype source-grounded Q&A path using only approved material;
- feedback from a small Vietnam pilot group when feasible.

Exit condition: at least one patient-facing answer can be traced end-to-end from Vietnamese question → reviewed knowledge claim → evidence record → original source, with limitations and applicability visible.

## Phase 1B — Expand the ACL + meniscus knowledge pilot
Only after Phase 1A succeeds, expand to additional journeys such as:
- understanding treatment pathways and decision factors;
- preparing for consultations and possible surgery;
- prehabilitation;
- rehabilitation stages and assessment concepts;
- return to running/sport concepts;
- recurring information gaps reported by patients.

Exit condition: multiple core journeys use the same evidence/review pipeline without creating inconsistent or duplicated medical truth.

## Phase 2 — Contribution system
Goal: make high-quality contribution easy for clinicians, researchers, and community members.

Deliverables:
- evidence submission and correction flows;
- reviewer roles and conflict/credential process;
- privacy-preserving patient-experience intake design;
- moderation and withdrawal procedures;
- Vietnam-first web contribution flows that do not require Git knowledge while preserving GitHub as the canonical public-knowledge workflow.

Exit condition: useful contributions do not require Git knowledge and private health information does not need to enter public GitHub.

## Phase 3 — Website MVP for Vietnam
Goal: make knowledge useful to ordinary people on mobile, beginning with Vietnamese users.

Initial journeys:
- I just injured my knee;
- I have a diagnosis or radiology report;
- I am comparing treatment paths;
- I am preparing for surgery;
- I am rehabilitating;
- I am preparing to return to running/sport;
- I want to contribute or suggest a correction.

Requirements:
- Vietnamese-first patient presentation;
- mobile-first and accessible UX;
- local Vietnam context clearly separated from general medical evidence;
- no requirement for ordinary users to understand GitHub.

Exit condition: users navigate by situation rather than by medical taxonomy and can understand where claims come from.

## Phase 4 — Source-grounded AI assistant
Goal: natural-language access without losing provenance.

Principles:
- retrieve from approved knowledge first;
- show sources and uncertainty;
- provider-agnostic AI gateway;
- answer policies by risk level;
- citation verification and evaluation sets;
- refusal/escalation behavior for unsupported personalized medical decisions;
- Vietnamese evaluation set before broader language rollout.

Exit condition: documented evaluations show the assistant reliably distinguishes evidence, community experience, local context, and uncertainty.

## Phase 5 — Community intelligence
Goal: responsibly learn from many lived experiences without confusing association with causation.

Potential capabilities:
- aggregate “what I wish I knew earlier” themes;
- common information gaps and failure points;
- cohort-like exploration of similar journeys;
- research-question generation from recurring unmet needs;
- multilingual synthesis.

Statistical comparisons that could imply treatment effectiveness require methodological review before publication.

## Phase 6 — International expansion
Expand beyond Vietnam only after the knowledge, contribution, privacy, and AI workflows are stable enough to localize rather than rebuild.

Expansion should add languages and jurisdiction-specific local-context modules while preserving shared evidence provenance and project invariants in `AGENTS.md`.

Potential growth areas:
- additional countries/languages;
- broader knee conditions;
- international clinical/research partnerships;
- stronger distributed governance and reviewer capacity;
- cross-country comparison of information/access gaps without assuming one care system is universal.