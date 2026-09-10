# Privacy and Patient Data Policy

Privacy is a core design constraint.

## Never commit identifiable health data to Git
Do not place patient names, emails, phone numbers, addresses, record/account identifiers, medical records, prescriptions, appointment documents, raw MRI/DICOM, or combinations of exact dates/locations/details that materially increase re-identification risk in this repository.

Git history is intentionally durable. Deleting a file from the current branch does not reliably erase prior history, so Git is the wrong storage layer for private patient submissions.

## Future patient contribution storage
Private or semi-private submissions should live in a database designed for explicit consent, minimal collection, access control, moderation state, withdrawal/deletion, auditability, and separation of identity/account information from health-experience data where practical.

## What may enter the public repository
- aggregate findings derived from reviewed community submissions;
- intentionally public, reviewed, de-identified summaries where governance permits;
- schemas, methods, prompts, and analysis code that do not expose private records.

De-identification reduces risk; it does not guarantee anonymity.

## Data minimization
If a field is not needed for a defined product or research purpose, do not collect it “just in case.” Prefer broad age ranges and coarse timelines over exact dates unless a validated use case needs precision.

## External AI providers
Before sending private health-related content to an AI provider, document what data is sent, why it is necessary, retention/training settings where applicable, relevant contractual/jurisdictional constraints, user consent, and any non-AI alternative. Provider integration must not silently expand data use.