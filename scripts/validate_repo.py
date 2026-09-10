#!/usr/bin/env python3
"""Lightweight structural validator for Knee Knowledge Commons.

This script enforces repository-maintenance invariants that can be checked
mechanically. It does NOT validate medical truth, evidence quality, reviewer
qualifications, or clinical correctness.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "AGENTS.md",
    "CONTINUITY.md",
    "CHANGELOG.md",
    "ROADMAP.md",
    "GOVERNANCE.md",
    "MEDICAL_SAFETY.md",
    "PRIVACY.md",
    "docs/ARCHITECTURE.md",
    "docs/CHANGE_MAP.md",
    "docs/EVIDENCE_MODEL.md",
    "docs/TRANSLATION.md",
    "plans/README.md",
    ".github/pull_request_template.md",
]

FORBIDDEN_DUPLICATE_STATE_FILES = [
    "PROJECT_STATE.md",
    "ARCHITECTURE.md",  # canonical architecture is docs/ARCHITECTURE.md
]

CONTINUITY_MARKERS = [
    "## Goal",
    "## Constraints / assumptions",
    "## Key decisions",
    "## State",
    "## Open questions",
    "## Active work / references",
]

MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def check_required_files(errors: list[str]) -> None:
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).is_file():
            fail(errors, f"missing required file: {rel}")

    for rel in FORBIDDEN_DUPLICATE_STATE_FILES:
        if (ROOT / rel).exists():
            fail(errors, f"duplicate source-of-truth file should not exist: {rel}")


def check_continuity(errors: list[str]) -> None:
    path = ROOT / "CONTINUITY.md"
    if not path.is_file():
        return
    text = path.read_text(encoding="utf-8")
    for marker in CONTINUITY_MARKERS:
        if marker not in text:
            fail(errors, f"CONTINUITY.md missing section: {marker}")


def check_agent_hooks(errors: list[str]) -> None:
    checks = {
        "AGENTS.md": ["CONTINUITY.md", "docs/CHANGE_MAP.md", "Post-flight"],
        "plans/README.md": ["CONTINUITY.md"],
        ".github/pull_request_template.md": ["CONTINUITY.md", "docs/CHANGE_MAP.md"],
        "docs/ARCHITECTURE.md": ["Source-of-truth map", "Agent session continuity"],
    }
    for rel, markers in checks.items():
        path = ROOT / rel
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for marker in markers:
            if marker not in text:
                fail(errors, f"{rel} missing continuity hook: {marker}")


def normalize_link_target(raw: str) -> str | None:
    raw = raw.strip()
    if not raw or raw.startswith("#"):
        return None
    if raw.startswith(("http://", "https://", "mailto:", "tel:", "data:")):
        return None

    # Markdown links may contain optional titles. Paths in this repo do not
    # require spaces wrapped as titles, so use the first whitespace-delimited
    # token after stripping angle brackets.
    if raw.startswith("<") and ">" in raw:
        raw = raw[1 : raw.index(">")]
    else:
        raw = raw.split()[0]

    raw = unquote(raw.split("#", 1)[0])
    return raw or None


def check_internal_markdown_links(errors: list[str]) -> None:
    for md in ROOT.rglob("*.md"):
        # Ignore hidden VCS/cache directories if present locally.
        if any(part in {".git", ".venv", "node_modules"} for part in md.parts):
            continue
        try:
            text = md.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            fail(errors, f"markdown file is not valid UTF-8: {md.relative_to(ROOT)}")
            continue

        for raw_target in MARKDOWN_LINK_RE.findall(text):
            target = normalize_link_target(raw_target)
            if target is None:
                continue
            resolved = (md.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                fail(errors, f"link escapes repository: {md.relative_to(ROOT)} -> {target}")
                continue
            if not resolved.exists():
                fail(errors, f"broken internal link: {md.relative_to(ROOT)} -> {target}")


def check_json(errors: list[str]) -> None:
    for path in ROOT.rglob("*.json"):
        if any(part in {".git", ".venv", "node_modules"} for part in path.parts):
            continue
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            fail(errors, f"invalid JSON: {path.relative_to(ROOT)}: {exc}")


def main() -> int:
    errors: list[str] = []
    check_required_files(errors)
    check_continuity(errors)
    check_agent_hooks(errors)
    check_internal_markdown_links(errors)
    check_json(errors)

    if errors:
        print("REPOSITORY VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("REPOSITORY VALIDATION OK")
    print("Structural/continuity checks passed. Medical correctness still requires evidence and human review.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
