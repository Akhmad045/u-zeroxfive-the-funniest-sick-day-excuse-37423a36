#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — writes one funny sick-day excuse to
/output/entry.txt.

The line is a text a real person could send their boss: locked out of the
house by their own toddler, locksmith delayed till noon, so they are
technically homeless until lunch. Setup, escalation, and the punchline on
the last words.

Stdlib only, deterministic, no network, no randomness.
"""
import hashlib
import os
import sys

ENTRY = ("My toddler locked me out of the house and the locksmith "
         "can't come till noon, so I'm technically homeless until lunch.")

MAX_CHARS = 200


def validate(text):
    """Enforce the competition gate: 1-200 chars, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if len(text) == 0:
        raise ValueError("entry is empty (gate needs 1-200 characters)")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, over the 200-character gate"
        )
    if text.strip() == "":
        raise ValueError("entry is only whitespace")
    if text != text.strip():
        raise ValueError("entry has leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    # A texted excuse has no control characters: reject tabs and other
    # invisible control codes the gate's "UTF-8 text" would still allow.
    for ch in text:
        if ord(ch) < 32 and ch not in ("\n", "\r"):
            raise ValueError(
                f"entry contains a control character U+{ord(ch):04X}"
            )
    return text


def self_test():
    """Exercise validate() against the gate's rejection cases."""
    cases = [
        ("", "empty"),
        (" ", "whitespace-only"),
        ("x" * 201, "201 chars"),
        ("a\nb", "multi-line"),
        ("a\tb", "tab control character"),
        ("a\x01b", "control character"),
        ("trailing ", "trailing whitespace"),
        (" leading", "leading whitespace"),
        (" padded ", "padded both sides"),
    ]
    for text, label in cases:
        try:
            validate(text)
        except ValueError as exc:
            print(f"self-test ok: rejected {label}: {exc}")
        else:
            raise SystemExit(f"self-test FAIL: {label} was accepted")
    # boundaries: exactly 1 char and exactly 200 chars must pass
    validate("z")
    print("self-test ok: 1-char boundary accepted")
    validate("y" * 200)
    print("self-test ok: 200-char boundary accepted")
    validate(ENTRY)
    print("self-test ok: entry itself accepted")
    print("self-test: all cases passed")
    return 0


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--self-test":
        return self_test()
    if len(sys.argv) > 1:
        print("usage: main.py [--self-test]", file=sys.stderr)
        return 2
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    text = validate(ENTRY)
    data = text.encode("utf-8")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "wb") as fh:
        fh.write(data)  # no trailing newline: the file is exactly the line
    with open(out_path, "rb") as fh:
        roundtrip = fh.read()
    if roundtrip != data:
        raise SystemExit("round-trip mismatch: file does not match entry")
    print(f"wrote {out_path}: {len(text)} chars, "
          f"sha256 {hashlib.sha256(data).hexdigest()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
