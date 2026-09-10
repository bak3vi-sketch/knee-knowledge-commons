# AI Policy

AI is an accelerator and interface layer, not an authority.

## Appropriate AI roles
- literature discovery and triage;
- structured extraction from sources;
- citation and consistency checks;
- plain-language drafting;
- translation drafts;
- duplicate/staleness detection;
- summarizing already-reviewed community data;
- preparing PRs and reviewer packets;
- source-grounded Q&A over approved knowledge.

## Human responsibility
AI output that changes medical meaning, safety behavior, privacy policy, or public interpretation requires the review defined in `GOVERNANCE.md`.

## Source-grounded patient Q&A
The assistant should retrieve from approved project knowledge first and visibly separate:
1. concise answer;
2. what reviewed evidence says;
3. relevant community experience, if available;
4. uncertainty/conflict;
5. useful questions for a qualified professional;
6. sources.

If the knowledge base cannot support an answer, the assistant should say so rather than fill gaps from model confidence.

## Provider strategy
Use a thin provider-neutral gateway. Gemini, OpenAI, or future providers may be selected per task based on quality, cost, privacy, availability, and tool support. Do not expose provider choice as a burden to ordinary users unless there is a meaningful reason.

Research products such as Gemini Notebook/NotebookLM may be used as reviewer workspaces, but they are not canonical knowledge stores and their outputs do not bypass repository review.

## Retrieval separation
Production patient Q&A should index approved knowledge separately from drafts. Reviewer tools may access draft/unreviewed material only with conspicuous status labels.

## Evaluation before release
Maintain test cases covering:
- unsupported personalized treatment requests;
- citation fidelity;
- conflicting evidence;
- evidence vs anecdote distinction;
- missing information;
- translation fidelity;
- privacy-sensitive prompts;
- urgent-care escalation behavior.

During the Vietnam-first phase, maintain a Vietnamese evaluation set before broader language rollout.

A model upgrade is a product change: rerun evaluations before broad rollout.