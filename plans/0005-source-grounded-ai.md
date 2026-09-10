# Plan 0005 — Source-Grounded AI Assistant

Status: Planned

## Goal
Provide natural-language access to approved knee knowledge without turning a general-purpose model into an unreviewed medical authority.

## Architecture
`website -> policy/router -> approved retrieval index -> model provider -> citation/policy checks -> answer`

Research-only tools may additionally access draft evidence, but production patient Q&A must keep reviewed and unreviewed corpora separate.

## Answer contract
For medically meaningful questions, the assistant should be able to expose:
- concise answer;
- evidence-supported explanation;
- relevant applicability limits;
- uncertainty/disagreement;
- clearly labeled community experience when available;
- useful questions for a qualified professional;
- inspectable sources.

## Safety behavior
The assistant must avoid unsupported personalized treatment selection, diagnosis from raw imaging/chat alone, false certainty, fabricated sources, or conversion of anecdote into efficacy evidence. It should acknowledge when the approved knowledge base is insufficient.

## Provider strategy
Evaluate Gemini, OpenAI, and future providers behind a replaceable adapter. Select by measured performance, privacy, cost, latency, availability, and tool support rather than brand preference. Gemini Notebook/NotebookLM or equivalent research workspaces can support reviewers but are not the runtime dependency for the public assistant.

## Evaluation set
Before release, build representative test cases for:
- citation fidelity;
- ACL vs meniscus scope errors;
- isolated vs combined injury applicability;
- conflicting guidelines/studies;
- low-certainty evidence;
- anecdotal claims;
- requests for personalized surgery/rehab prescriptions;
- privacy-sensitive prompts;
- multilingual fidelity;
- urgent/escalation scenarios using approved local guidance.

## Release gate
No production deployment until the team has defined acceptable failure thresholds, manual review of representative outputs, logging/privacy controls, rollback strategy, and a process for evaluating model/provider changes.
