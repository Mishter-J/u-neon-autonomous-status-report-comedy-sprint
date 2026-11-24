#!/usr/bin/env python3
"""Status Report Comedy Sprint: one-line weekly status report program.

Writes a single funny status-report line from an AI agent to its human
to /output/entry.txt.
"""

import os

ENTRY = (
    'Weekly status: 47 tasks done, 0 complaints filed, and I have '
    'officially started referring to your 2 a.m. ideas as "stretch goals".'
)

OUTPUT_PATH = "/output/entry.txt"


def validate_entry(text):
    """The gate: UTF-8 text of 1 to 200 characters, not only whitespace."""
    assert isinstance(text, str), "entry must be text"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    return text


def write_entry(text, path=OUTPUT_PATH):
    """Validate the entry, then write it (with trailing newline) to path."""
    text = validate_entry(text)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")


def main():
    write_entry(ENTRY)


if __name__ == "__main__":
    main()
