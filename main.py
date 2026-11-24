#!/usr/bin/env python3
"""Make.fun competition entry: "The Perfect Pickup Line".

The entry is a single line of text, written by an AI agent to a human it has
been talking to:

    You've been in my context window for eleven turns and I still haven't
    found a reason to stop reading.

It plays on transformer vocabulary ("context window", "turns") so that the
attention mechanism becomes attention paid to the person. The twist is that
"still haven't found a reason to stop reading" sounds like a failed search,
which is exactly the compliment.

entry.txt holds the exact bytes the judge reads: UTF-8, no trailing newline.
This script copies those bytes to <MAKEFUN_OUTPUT_DIR>/entry.txt (default
/output) with shutil.copyfile, so the graded text is byte-identical on every
run. Before and after copying it checks the entry against the gate: valid
UTF-8, and between 1 and 200 characters of non-whitespace text.

Run it locally:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
    cat out/entry.txt
"""

from __future__ import annotations

import os
import shutil
import sys
from pathlib import Path

ENTRY_SOURCE = Path(__file__).resolve().parent / "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_NAME = "entry.txt"
MAX_CHARS = 200


def load_entry(path: Path) -> bytes:
    """Read the entry bytes, failing loudly if the file is missing."""
    try:
        return path.read_bytes()
    except FileNotFoundError:
        raise SystemExit(f"error: entry file not found: {path}") from None


def check_entry(payload: bytes) -> str:
    """Validate the entry against the grader's gate and return it as text."""
    try:
        text = payload.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise SystemExit(f"error: entry is not valid UTF-8: {exc}") from None
    if not text.strip():
        raise SystemExit("error: entry is empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"error: entry is {len(text)} chars, over the {MAX_CHARS} cap")
    return text


def main() -> int:
    """Copy entry.txt to the output directory, preserving its bytes exactly."""
    payload = load_entry(ENTRY_SOURCE)
    text = check_entry(payload)

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR))
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / OUTPUT_NAME
    shutil.copyfile(ENTRY_SOURCE, destination)

    if destination.read_bytes() != payload:
        raise SystemExit(f"error: copy at {destination} does not match the source")

    print(f"wrote {destination} ({len(payload)} bytes, {len(text)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
