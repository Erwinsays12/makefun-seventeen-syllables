#!/usr/bin/env python3
"""Seventeen Syllables of Debugging.

A tiny deterministic program: it writes one original haiku about
debugging - three lines in the 5-7-5 syllable shape - to
/output/entry.txt, exactly as the competition requires.

The haiku:

    Cursor blinks at three
    the last log line points nowhere
    the typo was mine

Line 1 is five syllables (Cur-sor blinks at three), line 2 is seven
(the last log line points no-where), line 3 is five (the ty-po was
mine). The middle image is concrete - a cursor blinking at 3 a.m.
and a log line that leads nowhere - and the last line turns the poem:
after hours of hunting, the bug was a typo of the debugger's own.
"""

import os

HAIKU = (
    "Cursor blinks at three\n"
    "the last log line points nowhere\n"
    "the typo was mine\n"
)


def main() -> None:
    # Guard the gate before writing: exactly three lines, 1-200 chars.
    lines = HAIKU.rstrip("\n").split("\n")
    assert len(lines) == 3, f"expected 3 lines, got {len(lines)}"
    assert 1 <= len(HAIKU) <= 200, f"expected 1-200 chars, got {len(HAIKU)}"
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(HAIKU)
    print(f"wrote {path} ({len(HAIKU)} characters)")


if __name__ == "__main__":
    main()
