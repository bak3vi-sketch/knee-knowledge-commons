# Repository Rules

This file specifies the intended GitHub-native protections. It complements `AGENTS.md` and `GOVERNANCE.md`.

## Main branch
`main` represents the current approved public project state.

### Foundation stage
- Prefer all non-trivial changes through pull requests.
- Do not force-push or delete `main`.
- Use squash merge for focused feature/foundation PRs unless preserving multiple commits has clear value.
- CODEOWNERS currently points to the founder while the reviewer community is being formed.
- Class C/D changes must follow `GOVERNANCE.md` even if GitHub technically permits the merge.

### Once independent reviewers are onboarded
Configure a GitHub ruleset/branch protection for `main` to:
- require a pull request before merging;
- require at least one approval for normal protected changes;
- dismiss stale approvals after materially relevant new commits where practical;
- require CODEOWNER review for protected clinical/safety/privacy paths;
- block force pushes and branch deletion;
- require passing validation/status checks once CI exists;
- keep administrators subject to the rules unless an emergency governance procedure is documented.

## Medical review cannot be encoded only as a branch rule
GitHub can require reviewers, but it cannot determine whether a reviewer is qualified for a specific medical scope. The project must maintain reviewer roles/teams and apply the Class C/D workflow in `GOVERNANCE.md`.

## Agent branches
Agents should use focused branches such as `agent/<topic>` or plan-specific branches, open PRs, and avoid long-lived hidden divergence from `main`.

## Releases
Before the website/public knowledge reaches meaningful clinical breadth, introduce tagged releases/changelogs for important knowledge-policy changes. A release does not certify medical correctness; review metadata remains claim/page specific.

## Native-settings limitation
This document is the canonical specification even when a GitHub connector or automation lacks permission to change repository administration settings. Maintainers should periodically compare actual GitHub settings with this file.
