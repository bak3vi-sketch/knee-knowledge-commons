# Roadmap

The roadmap is stage-gated rather than date-driven. Safety, evidence quality, and usable workflows matter more than shipping a large feature set quickly.

## Phase 0 — Foundation
Goal: make the project difficult to accidentally steer in an unsafe or incoherent direction.

Deliverables:
- mission, governance, privacy, and medical-safety rules;
- agent operating rules;
- evidence/content models and system architecture;
- initial ACL + meniscus pilot structure;
- contribution templates and architecture decision records.

Exit condition: maintainers can classify a proposed change and know what review it requires.

## Phase 1 — Knowledge pilot: ACL + meniscus
Goal: prove the evidence workflow on a narrow scope before expanding conditions.

Deliverables:
- inventory of major guidelines and systematic reviews;
- reviewed patient-facing pages for core ACL/meniscus journeys;
- provenance and review-status metadata;
- citation-verification workflow;
- explicit gaps/conflicts register.

Exit condition: important claims can be traced to reviewed sources and uncertainty is visible.

## Phase 2 — Contribution system
Goal: make high-quality contribution easy for clinicians, researchers, and community members.

Deliverables:
- evidence submission and correction flows;
- reviewer roles and conflict/credential process;
- privacy-preserving patient-experience intake design;
- moderation and withdrawal procedures.

Exit condition: useful contributions do not require Git knowledge and private health information does not need to enter public GitHub.

## Phase 3 — Website MVP
Goal: make knowledge useful to ordinary people on mobile.

Initial journeys:
- I just injured my knee;
- I have a diagnosis or radiology report;
- I am comparing treatment paths;
- I am preparing for surgery;
- I am rehabilitating;
- I am preparing to return to running/sport;
- I want to contribute or suggest a correction.

Exit condition: users navigate by situation rather than by medical taxonomy.

## Phase 4 — Source-grounded AI assistant
Goal: natural-language access without losing provenance.

Principles:
- retrieve from approved knowledge first;
- show sources and uncertainty;
- provider-agnostic AI gateway;
- answer policies by risk level;
- citation verification and evaluation sets;
- refusal/escalation behavior for unsupported personalized medical decisions.

Exit condition: documented evaluations show the assistant reliably distinguishes evidence, community experience, and uncertainty.

## Phase 5 — Community intelligence
Goal: responsibly learn from many lived experiences without confusing association with causation.

Potential capabilities:
- aggregate “what I wish I knew earlier” themes;
- common information gaps and failure points;
- cohort-like exploration of similar journeys;
- research-question generation from recurring unmet needs;
- multilingual synthesis.

Statistical comparisons that could imply treatment effectiveness require methodological review before publication.

## Phase 6 — Global knowledge commons
Expand conditions, languages, professional partnerships, governance capacity, accessibility, and research collaboration while preserving the project invariants in `AGENTS.md`.
