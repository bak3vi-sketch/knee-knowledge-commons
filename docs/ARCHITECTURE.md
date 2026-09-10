# Architecture

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

## Components

### 1. Public website
Designed mobile-first around user situations rather than repository folders. It provides reading, search, source-grounded Q&A, contribution flows, and correction flows.

### 2. GitHub knowledge repository
Stores approved public knowledge, evidence metadata, schemas, governance, agent rules, plans, translations, and change history.

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
- no model-generated answer becomes durable knowledge without an explicit contribution/review step.
