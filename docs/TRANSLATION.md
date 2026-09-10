# Translation and Localization Strategy

The project should become multilingual without creating independent medical truths per language.

## Launch strategy
Knee Knowledge Commons is **Vietnam-first, global-ready**.

During the initial product phase:
- Vietnamese is the primary patient-facing language;
- user research and usability testing focus on Vietnam;
- local Vietnam care pathways, terminology, access constraints, and system-specific information are treated as local context;
- architecture, evidence provenance, schemas, identifiers, and AI-provider integrations remain internationally reusable.

## Canonical project documentation
Prefer **one canonical internal project document** rather than maintaining language-by-language mirrors.

Browser translation or AI translation is acceptable for reading internal documents such as roadmap, plans, architecture, governance, privacy, and AI policy. This reduces duplicate-document drift and maintenance burden.

Keep dedicated translated documents only when they serve a distinct product/community purpose rather than merely duplicating an internal file. Current examples:
- `README.vi.md` — Vietnamese community entry point;
- `docs/OWNER_GUIDE.vi.md` — concise orientation for the project owner;
- reviewed Vietnamese patient-facing medical content — first-class product content for the Vietnam launch.

A project decision does **not** require a Vietnamese mirror file. When the owner needs to decide something, the agent should explain the decision, benefit, risk/trade-off, and completion condition in Vietnamese in the conversation/PR summary.

## Canonical knowledge model
For reviewed medical knowledge, preserve a shared underlying claim/evidence model rather than creating independent English and Vietnamese medical truths.

Use English where it improves international interoperability, especially for:
- machine-readable schemas and identifiers;
- agent/developer instructions;
- technical architecture;
- evidence metadata tied to predominantly international source literature;
- cross-country collaboration.

Vietnamese patient-facing medical content is a deliberate product output, not an unreviewed convenience translation. It should preserve source links, uncertainty, scope, review status, and medically important nuance.

## AI and browser translation
AI/browser translation may be used to understand internal project documentation.

For patient-facing medical content, AI may draft translations, but medically meaningful wording must follow the same evidence/review standards as other Class C content. Translation is not permission to simplify away uncertainty or turn technical nuance into certainty.

## Terminology
Maintain a glossary when the patient-facing corpus grows enough to need one, especially for high-risk terms such as ligament names, tear patterns, surgical procedures, rehabilitation milestones, and diagnostic findings.

For Vietnamese, record commonly encountered clinical wording alongside patient-friendly explanations where useful.

## Local context is not translation
Language translation and local clinical/system guidance are different tasks.

Do not silently convert one country's guideline, referral pathway, emergency number, insurance workflow, scope-of-practice assumption, or service availability into a universal recommendation.

Model information as separate layers where practical:
- **shared evidence / canonical claim**;
- **language presentation**;
- **jurisdiction/local context**.

This separation is a core requirement for future international expansion.

## Avoid version drift
Do not create translation mirrors pre-emptively. If a dedicated translated artifact exists because users actually need it, define which canonical source or evidence it derives from and how staleness will be detected when medical meaning changes.