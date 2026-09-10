# Architecture

This is the **canonical architecture map** for Knee Knowledge Commons. It describes system boundaries, sources of truth, and critical paths. It is not a roadmap, changelog, or live status file.

## Core principle

**GitHub is the source of truth for reviewed public knowledge; the future website is the primary interface for people.**

```text
Patients / clinicians / researchers / community
                    |
                 Website
          search | chat | forms
                    |
                AI Gateway
          /         |         \
      retrieval   policy    models
          |                    |
   Approved knowledge       Gemini/OpenAI/
          |                 future providers
          |
       GitHub repo

Private patient submissions --> protected database
Research workspaces/tools ----> draft evidence --> PR/review --> GitHub
```

## Source-of-truth map

| Concern | Canonical source |
|---|---|
| Live project goal/state/next work | `CONTINUITY.md` |
| Long-term staged direction | `ROADMAP.md` |
| Executable stage scope and acceptance criteria | `plans/` |
| Agent operating behavior | `AGENTS.md` |
| Medical safety boundary | `MEDICAL_SAFETY.md` |
| Patient/private data boundary | `PRIVACY.md` + `docs/DATA_BOUNDARIES.md` |
| Governance/review authority | `GOVERNANCE.md` |
| Evidence semantics and certainty rules | `docs/EVIDENCE_MODEL.md` |
| Machine-readable data contracts | `schemas/` |
| Product intent and user journeys | `docs/PRODUCT_VISION.md` + `docs/USER_JOURNEYS.md` |
| Translation/localization model | `docs/TRANSLATION.md` |
| Durable architectural decisions | `docs/adr/` |
| Notable historical changes | `CHANGELOG.md` |
| Documentation dependency/update triggers | `docs/CHANGE_MAP.md` |

Do not introduce a second file that owns the same responsibility without explicitly migrating/deprecating the old source.

## Components

### 1. Public website
Designed mobile-first around user situations rather than repository folders. It provides reading, search, source-grounded Q&A, contribution flows, and correction flows.

### 2. GitHub knowledge repository
Stores approved public knowledge, evidence metadata, schemas, governance, agent rules, plans, and change history.

### 3. Private application database
Stores accounts, consent, private drafts, patient-experience submissions, moderation state, and withdrawal/deletion state. These do not belong in Git history.

### 4. AI gateway
A small provider-neutral layer that decides what sources a model may retrieve, which risk policy applies, which provider/model to call, what citations are required, and what output schema is expected.

The gateway should make model providers replaceable rather than embedding one vendor throughout the product.

### 5. Retrieval/index layer
Indexes **approved** knowledge for patient-facing answers. Draft/unreviewed material should be isolated from production retrieval unless clearly marked for reviewer workflows.

### 6. Research workspace
Tools such as Gemini Notebook/NotebookLM, literature databases, or other research agents may help reviewers study source collections. They are research aids, not the canonical source of published knowledge.

### 7. Agent workflows
Agents can discover new literature, extract structured evidence, find stale claims, check citations, translate, and open PRs. Medical/safety publication remains subject to governance review.

## Critical paths

### Knowledge publication

```text
patient/research question
  -> source discovery
  -> structured evidence record
  -> applicability/citation/contradiction checks
  -> draft canonical knowledge
  -> qualified human review where required
  -> approved GitHub knowledge
  -> retrieval index
  -> patient-facing website / AI answer
```

**Invariant:** a fluent model answer is never the source of truth; approved knowledge and inspectable evidence are.

### Community contribution

```text
website or GitHub contribution
  -> privacy/safety screening
  -> structuring/classification
  -> evidence/source checks when relevant
  -> human review
  -> approved public knowledge OR protected private storage
```

**Invariant:** website and GitHub contribution paths must converge on one review model rather than create parallel truth systems.

### Patient-data path

```text
private patient submission
  -> consent/minimum necessary collection
  -> protected database
  -> moderation/de-identification/aggregation
  -> reviewed aggregate or permitted public output
  -> GitHub only when governance allows
```

**Invariant:** identifiable patient health data and raw private records never become ordinary Git content.

### Agent session continuity

```text
new agent/session
  -> CONTINUITY.md
  -> active plan
  -> task-specific source(s) of truth
  -> work
  -> CHANGE_MAP review
  -> checks/review
  -> update CONTINUITY/plan/docs only when reality changed
```

**Invariant:** future agents should recover project context from the repository, not depend on private chat history.

## One contribution pipeline

Website contributions and GitHub contributions must converge into the same review states rather than becoming parallel truth systems:

`submitted -> privacy/safety screening -> structured -> evidence/source checks -> human review -> approved -> published/indexed`

## Architecture invariants

- one canonical approved knowledge layer;
- raw/private patient data outside Git;
- source provenance attached to medical claims;
- provider-neutral AI integration;
- review state visible to machines and humans;
- ability to rebuild search/indexes from canonical sources;
- no model-generated answer becomes durable knowledge without an explicit contribution/review step;
- no duplicate status/architecture/evidence truth systems maintained for convenience.

## When to update this file

Update `docs/ARCHITECTURE.md` when any of these materially change:
- major components or repository layers;
- source-of-truth ownership;
- data flow or system boundaries;
- a critical publication/contribution/patient-data path;
- an architecture invariant.

Do **not** update it for ordinary content additions, routine evidence records, typo fixes, or task status changes. Use `CONTINUITY.md`, plans, PRs, and `CHANGELOG.md` for those responsibilities.

See `docs/CHANGE_MAP.md` before finishing structural work.