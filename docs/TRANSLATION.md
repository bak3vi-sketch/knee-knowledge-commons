# Translation and Localization Strategy

The project should become multilingual without creating independent medical truths per language.

## Launch strategy
Knee Knowledge Commons is **Vietnam-first, global-ready**.

During the initial product phase:
- Vietnamese is the primary patient-facing language;
- user research and usability testing focus on Vietnam;
- local Vietnam care pathways, terminology, access constraints, and system-specific information are treated as local context;
- architecture, evidence provenance, schemas, identifiers, and AI-provider integrations remain internationally reusable.

## Canonical model
There is no requirement that every human-facing artifact use one canonical language.

Use English where it improves international interoperability, especially for:
- machine-readable schemas and identifiers;
- agent/developer instructions;
- technical architecture;
- evidence metadata tied to predominantly international source literature;
- cross-country collaboration.

For reviewed medical knowledge, preserve a shared underlying claim/evidence model rather than creating independent English and Vietnamese medical truths.

Vietnamese patient-facing content is a first-class product output, not a secondary convenience translation.

## Project-owner language policy
Any document that requires the project owner to make a decision, approve a direction, understand a material risk, prioritize work, or interpret project policy must provide either:
1. a Vietnamese companion document; or
2. a clearly marked Vietnamese owner-summary containing the problem, rationale, benefit, risk/trade-off, required decision, and completion condition.

Typical owner-facing documents include:
- roadmap and active plans;
- product vision and major UX decisions;
- governance and medical-safety policy;
- privacy/data policy;
- AI policy and major architecture trade-offs.

When an English owner-facing canonical document changes materially, its Vietnamese companion/summary must be updated in the same PR or explicitly marked `STALE` with the canonical revision/date it no longer matches.

## AI translation
AI may draft translations, but medically meaningful changes introduced during translation must be reviewed. Translation is not permission to simplify away uncertainty or turn technical nuance into certainty.

## Terminology
Maintain a glossary for high-risk terms such as ligament names, tear patterns, surgical procedures, rehabilitation milestones, and diagnostic findings. Prefer plain-language explanation alongside technical terminology.

For Vietnamese, record both commonly encountered clinical wording and patient-friendly explanation where they differ.

## Version drift
Translations and companion documents should record or link to the canonical source they correspond to. When canonical medical content changes, affected translations should be marked stale until updated/reviewed.

## Local context is not translation
Language translation and local clinical/system guidance are different tasks.

Do not silently convert one country's guideline, referral pathway, emergency number, insurance workflow, scope-of-practice assumption, or service availability into a universal recommendation.

Model information as separate layers where practical:
- **shared evidence / canonical claim**;
- **language presentation**;
- **jurisdiction/local context**.

This separation is a core requirement for future international expansion.
