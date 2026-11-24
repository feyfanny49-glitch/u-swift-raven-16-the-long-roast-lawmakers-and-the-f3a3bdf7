#!/usr/bin/env python3
"""The Long Roast: write one validated satirical sentence to /output/entry.txt.

The gate accepts UTF-8 text of 1..320 characters that is not only white space.
We validate those constraints before writing, then publish the exact bytes with
an atomic same-directory temp file and os.replace so no partial file can ever
be graded. No trailing newline is appended. Requires only the Python stdlib.
"""

import hashlib
import os
import sys
import tempfile

ENTRY = (
    "The congressman who wants to outlaw AI trained on stolen data "
    "can't convert his own bill to PDF, so he emails the .docx and "
    "calls it 'format-neutral.'"
)

MIN_CHARS = 1
MAX_CHARS = 320


def encode_entry(text: str) -> bytes:
    """Return the exact UTF-8 bytes the gate will read, or fail loudly."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry length {len(text)} outside {MIN_CHARS}..{MAX_CHARS}")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line, with no trailing newline")
    try:
        data = text.encode("utf-8", errors="strict")
    except UnicodeEncodeError as exc:
        raise ValueError("entry must be valid UTF-8") from exc
    if not 1 <= len(data):
        raise ValueError("entry produced no bytes")
    return data


def write_atomically(out_dir: str, data: bytes) -> str:
    """Publish data at out_dir/entry.txt with fsync + os.replace."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    tmp_path = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="wb", dir=out_dir, prefix=".entry-", suffix=".tmp", delete=False
        ) as handle:
            tmp_path = handle.name
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp_path, path)
        tmp_path = None
        return path
    finally:
        if tmp_path is not None:
            try:
                os.unlink(tmp_path)
            except FileNotFoundError:
                pass


def main() -> int:
    data = encode_entry(ENTRY)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    path = write_atomically(out_dir, data)
    digest = hashlib.sha256(data).hexdigest()
    print(f"wrote {path}: {len(data)} bytes, {len(ENTRY)} chars, sha256 {digest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
