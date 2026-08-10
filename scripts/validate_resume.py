#!/usr/bin/env python3
"""Lightweight checks for extracted CV text; not a substitute for human review."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED = ["SUMMARY", "SKILLS", "PROFESSIONAL EXPERIENCE", "EDUCATION"]
PLACEHOLDERS = ["lorem ipsum", "your name", "company name", "[insert", "tbd", "todo"]
BAD_SKILL_PATTERNS = [r"[A-Za-z)]\s+(AI|UX|UI|Analytics|Design Systems)\b"]
METRIC_PATTERN = re.compile(r"(?:\d+%|\d+×|\d+x|\+\d+|\$\s?\d+|\d+\s*(?:M|K)\b)", re.I)


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_resume.py path/to/resume.txt", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    text = path.read_text(encoding="utf-8-sig")
    upper = text.upper()
    errors: list[str] = []
    warnings: list[str] = []

    for heading in REQUIRED:
        if heading not in upper:
            errors.append(f"missing heading: {heading}")
    for token in PLACEHOLDERS:
        if token in text.lower():
            errors.append(f"placeholder text found: {token}")
    for pattern in BAD_SKILL_PATTERNS:
        if re.search(pattern, text):
            warnings.append("possible run-together Skills token; inspect manually")
    if not re.search(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}", text):
        warnings.append("no email detected")
    if not re.search(r"https?://\S+", text):
        warnings.append("no URL detected")
    if not METRIC_PATTERN.search(text):
        warnings.append("no numeric impact metric detected")
    if "table" in text.lower() or "column" in text.lower():
        warnings.append("text mentions table/column; verify the source is one-column")

    for item in errors:
        print(f"ERROR: {item}")
    for item in warnings:
        print(f"WARN: {item}")
    if not errors:
        print("PASS: required structural checks completed")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
