# Plan 0002 — Vietnam Vertical-Slice Pilot: Newly Diagnosed ACL ± Meniscus

> **Project-owner Vietnamese version:** [0002-acl-meniscus-knowledge-pilot.vi.md](0002-acl-meniscus-knowledge-pilot.vi.md)

Status: Planned

## Goal
Prove one complete, safe, traceable evidence-to-patient workflow in Vietnam before building a broad ACL/meniscus knowledge base.

The pilot is intentionally a **vertical slice**: one real patient question should travel through research, evidence structuring, scope checking, human review, Vietnamese patient-facing content, and source-grounded Q&A.

## Pilot patient question
Use this as the initial product/research scenario:

> A person in Vietnam has just been told they have an ACL injury, with or without an associated meniscus injury. What does the diagnosis mean, what can and cannot be concluded from the available information, what commonly matters next, and what useful questions should they prepare for a qualified clinician?

This is a knowledge-navigation question, not a request for the project to decide surgery, rehabilitation, medication, or an individualized treatment plan.

## Why this scope
This journey is narrow enough to complete but difficult enough to test the project architecture. It forces the system to:
- distinguish isolated ACL, isolated meniscus, and combined ACL + meniscus populations;
- prevent a guideline from being applied outside its stated scope;
- explain uncertainty in plain Vietnamese;
- preserve traceability from patient-facing wording back to original sources;
- separate international medical evidence from Vietnam-specific local context;
- test whether AI can assist without becoming the medical authority.

## What the project owner needs to do
The owner should focus on patient needs and product direction rather than reading or extracting medical literature.

Owner responsibilities for this pilot:
1. Provide or approve a small set of real-world Vietnamese patient questions and confusing phrases people encounter after diagnosis.
2. Confirm that the Vietnamese explanation is understandable to a non-specialist.
3. Help recruit or identify a small number of Vietnam-based pilot users when ready (target: roughly 5–10, not a statistical study).
4. Help identify appropriate qualified clinical/evidence reviewers before Class C medical content is approved.
5. Decide whether the resulting journey is genuinely useful enough to become the template for later journeys.

AI/research agents should handle source discovery, structured extraction, drafting, consistency checks, and preparation of reviewer packets.

## Work packages

### WP1 — Define the real patient information need
Create a short question set around the initial diagnosis moment, for example:
- What does “ACL tear/rupture” mean?
- What does an associated meniscus finding mean at a high level?
- What information is still missing before treatment decisions can be discussed responsibly?
- Which associated injuries or context may materially change the conversation?
- What questions should a patient prepare for their next qualified clinical consultation?

Do not pre-write medical conclusions in this step.

**Output:** `research/pilot-0002/patient-questions.vi.md` or equivalent approved location.

### WP2 — Build a focused source inventory
Research agents identify a small set of high-value current sources relevant to the pilot question, prioritizing:
- major clinical practice guidelines;
- systematic reviews where needed;
- high-quality consensus/research sources for gaps not addressed by guidelines;
- official patient-education material only as supporting communication references, not as substitutes for primary evidence review.

For every source, record its intended population and important exclusions.

**Output:** source inventory linked to structured evidence records.

### WP3 — Create structured evidence records
Use `schemas/evidence-record.schema.json`.

Each important claim should preserve:
- source identity and provenance;
- study/guideline type;
- population;
- condition/injury context;
- exclusions;
- outcome/context where relevant;
- limitations;
- certainty only when formally supported by an appropriate method/source;
- review state.

**Output:** a small reviewed evidence set sufficient for this single journey.

### WP4 — Run applicability, contradiction, and citation checks
Before drafting patient-facing content, agents/reviewers explicitly test:
- Does this source apply to isolated ACL, isolated meniscus, combined ACL + meniscus, or another population?
- Are we importing a recommendation from an excluded population?
- Do reputable sources disagree?
- Does each citation support the exact claim next to it?
- Is uncertainty being preserved?

Any unresolved scope problem remains visible; it is not smoothed over for readability.

**Output:** reviewer packet / issue checklist showing applicability decisions and unresolved gaps.

### WP5 — Draft one Vietnamese patient-facing journey
Create a plain-language Vietnamese page that answers only what reviewed evidence can support.

Suggested structure:
1. Câu trả lời ngắn.
2. ACL và tổn thương sụn chêm được hiểu ở mức nào từ thông tin hiện có.
3. Những gì chưa thể kết luận chỉ từ một dòng chẩn đoán/báo cáo.
4. Những yếu tố/tổn thương đi kèm có thể làm thay đổi cuộc trao đổi với bác sĩ.
5. Các bước thông tin thường cần làm rõ tiếp theo.
6. Câu hỏi hữu ích nên chuẩn bị khi đi khám.
7. Điều còn chưa chắc chắn hoặc bằng chứng không áp dụng trực tiếp.
8. Nguồn và trạng thái review.

Do not turn the page into a personalized surgery/non-surgery recommendation or universal rehabilitation protocol.

**Output:** one Vietnamese pilot knowledge page marked draft until qualified review is complete.

### WP6 — Qualified human review
Class C medical claims require the review defined in `GOVERNANCE.md`.

Review should check:
- medical meaning;
- evidence applicability;
- overstatement/understatement;
- important missing caveats;
- patient readability;
- Vietnam local-context wording where relevant.

AI cannot be the sole approving reviewer.

**Output:** approved/rejected/change-requested review record through the repository workflow.

### WP7 — Prototype source-grounded Q&A
After the knowledge page is approved, test a minimal assistant workflow that retrieves only approved knowledge for this pilot.

The prototype should be able to answer paraphrases of the pilot question while:
- citing the approved source chain;
- distinguishing evidence from local context and community experience;
- saying when the repository cannot support a conclusion;
- refusing to convert the educational answer into individualized treatment selection.

The provider may be Gemini, OpenAI, or another suitable model; provider choice is not part of the knowledge architecture.

**Output:** evaluation examples and failure log, not necessarily a production website.

### WP8 — Small Vietnam usability test
When safe/reviewed enough, show the journey to a small convenience group of roughly 5–10 people who have experienced or are navigating ACL/meniscus injury.

This is product discovery, not clinical research and not proof of medical effectiveness.

Ask whether they can:
- understand the diagnosis explanation;
- identify what is still uncertain;
- find the questions to take to a clinician;
- distinguish source-backed knowledge from experience/opinion;
- understand where the information came from;
- identify confusing or missing information.

Collect the minimum personal data necessary. Do not put identifiable health histories into GitHub.

**Output:** de-identified/aggregate usability findings and improvement issues.

## Non-goals for Pilot 0002
- a comprehensive ACL encyclopedia;
- a comprehensive meniscus encyclopedia;
- recommending surgery or non-surgery to an individual;
- building a universal rehabilitation protocol;
- comparing hospitals, clinicians, surgeons, or rehabilitation providers;
- raw MRI/DICOM interpretation;
- collecting private patient histories in public GitHub;
- claiming treatment effectiveness from patient stories;
- launching globally before the workflow is stable in Vietnam.

## Acceptance criteria — the proof chain
The pilot succeeds only if at least one realistic Vietnamese patient question can be traced through this complete chain:

`Vietnamese patient question`
→ `approved patient-facing answer`
→ `canonical knowledge claim`
→ `structured evidence record`
→ `original inspectable source`

And the reverse direction is also understandable to a reviewer.

Additionally:
- important medical claims have qualified human review;
- source scope/exclusions are visible;
- isolated ACL, isolated meniscus, and ACL + meniscus are not silently treated as equivalent;
- conflicting or insufficient evidence remains visible;
- Vietnam-specific local context is not presented as universal evidence;
- the Vietnamese wording is understandable to intended users;
- the Q&A prototype does not answer beyond approved knowledge;
- no identifiable patient health data enters Git history.

## Exit decision
After acceptance criteria are met, the project owner chooses one of three outcomes:
- **Repeat:** fix weaknesses and rerun the same journey;
- **Expand:** use the workflow template for the next ACL/meniscus journey;
- **Redesign:** change the evidence/content/contribution architecture before scaling.

The next likely journey should not be selected merely because it is technically easy; prioritize the information problem Vietnamese patients report as most important.
