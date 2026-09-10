# Data Boundaries

This document defines where each type of information is allowed to live.

| Data type | GitHub | Private DB | AI index | Public website |
|---|---|---|---|---|
| Governance / policies | Yes | No | Optional | Yes |
| Reviewed knowledge | Yes | Derived/cache only | Yes | Yes |
| Evidence metadata | Yes | Optional cache | Yes | Reviewer/public views |
| Draft medical claims | PR/branch only | Optional | Reviewer-only index | No |
| Raw patient submission | **No** | Yes | Only under approved policy | No |
| Consent / withdrawal | **No** | Yes | No | Account UI only |
| Identifiable health data | **No** | Only if explicitly justified and protected | Avoid/minimize | No |
| Aggregate community findings | Yes after review | Derived | Yes | Yes |
| App accounts/auth | No | Yes | No | User-controlled UI |

## Canonical vs derived data

GitHub is canonical for reviewed public knowledge. Search indexes, embeddings, caches, and generated website pages are derived and must be rebuildable from canonical sources.

The private database is canonical for patient submissions and consent state. The repository must never become a backup copy of those records.

## Publication boundary

Moving information from private submission to public knowledge is a publication event, not a sync operation. It requires explicit transformation, privacy review, provenance, consent/governance checks, and human approval where required.

## AI boundary

Do not automatically send every stored field to a model. Create task-specific minimum-data views. Patient-facing retrieval should prefer reviewed public knowledge; private data should be used only for a clearly requested, consented function with documented handling.
