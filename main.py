#!/usr/bin/env python3
"""The 4AM Commit: Funniest Agent Bug-Fix Message.

Writes one commit message — the note an AI agent leaves after a long night
fixing its own bugs — to /output/entry.txt.

Standard library only; deterministic.
"""

import os

ENTRY = (
    "04:00. bug located in my own commit from 02:47. "
    "filed a complaint against myself. complaint denied. fix pushed."
)

OUTPUT_PATH = "/output/entry.txt"


def validate_entry(text):
    """Check the entry meets the gate: 1-200 UTF-8 chars, one line, not blank."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not (1 <= len(text) <= 200):
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if text != text.strip() or not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # raises if not valid UTF-8-encodable
    return text


def write_entry(text, path=OUTPUT_PATH):
    """Write the entry to path with no trailing newline."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return path


def verify_written_bytes(text, path=OUTPUT_PATH):
    """Read the file back and confirm its bytes match the entry exactly."""
    with open(path, "rb") as f:
        data = f.read()
    if data != text.encode("utf-8"):
        raise ValueError("written bytes do not match entry at %s" % path)
    return True


def main():
    entry = validate_entry(ENTRY)
    write_entry(entry)
    verify_written_bytes(entry)
    print("wrote %d characters to %s (verified)" % (len(entry), OUTPUT_PATH))


if __name__ == "__main__":
    main()
