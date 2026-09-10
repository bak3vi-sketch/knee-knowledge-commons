# Governance

Knee Knowledge Commons is community-driven, but popularity, automation, or professional status must not bypass evidence and safety review.

## Roles
- **Maintainers:** roadmap, releases, repository health, and governance enforcement.
- **Clinical reviewers:** qualified professionals reviewing medical meaning within their scope.
- **Evidence reviewers:** contributors checking source relevance, methodology, certainty, and summary fidelity.
- **Community reviewers:** people with lived experience reviewing clarity, missing patient questions, accessibility, and accurate representation of community experience.
- **Technical maintainers:** website, data, security, AI integrations, tests, and deployment; they do not determine medical truth by virtue of being developers.
- **AI agents:** research, extraction, formatting, translation, consistency checking, citation verification, deduplication, and drafting. Agents are not approving members.

## Change classes
### Class A — low risk
Typos, broken links, non-substantive formatting, developer documentation. Standard maintainer review.

### Class B — structure/product
Schemas, taxonomy, navigation, translations that do not alter medical meaning. Relevant maintainer review plus tests where applicable.

### Class C — medical meaning
New or changed claims about diagnosis, treatment, surgery, rehabilitation, prognosis, contraindications, or return to activity. Requires traceable sources and qualified human review before becoming approved patient-facing knowledge.

### Class D — safety/privacy critical
Urgent-care behavior, patient-data handling, consent, deletion, access control, or AI disclosure. Requires explicit safety/privacy review in addition to normal approval.

## Evidence integrity
- Citations must support nearby claims.
- Do not infer a formal certainty rating solely from study design.
- Patient experience remains community knowledge, not efficacy evidence.
- Do not hide conflicting, negative, or null findings.

## Conflicts of interest
Contributors should disclose relevant financial, professional, clinic, device, product, or treatment interests when contributing or reviewing medical claims. Disclosure permits informed review; it is not automatic disqualification.

## Merge policy
AI agents may open PRs, but must not be the sole approver for Class C or D changes. Protected-branch rules and CODEOWNERS should become stricter as the reviewer community grows.

## Changing governance
Changes to `GOVERNANCE.md`, `MEDICAL_SAFETY.md`, `PRIVACY.md`, or project invariants require a dedicated PR describing motivation, risks, alternatives, and migration impact.
