#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes one funny line to /output/entry.txt:

    At my uncle's funeral the pastor said he was in a better
    place, and my auntie whispered, 'He owed me forty thousand
    — he better be.'

Why it lands: the pastor's funeral cliche (setup), my auntie's
whispered debt collection (turn), and the punchline answering
"a better place" with "he better be" (payoff). Three beats,
concrete anchors throughout (an uncle's funeral, the pastor,
my auntie, forty thousand), 132 characters in a single line.
Dark, deadpan, and human — no smart device, no AI, no raccoon
with a mortgage: the field is full of those.

Python 3.13, standard library only, no network, deterministic.
"""

import os

ENTRY = (
    "At my uncle's funeral the pastor said he was in a better "
    "place, and my auntie whispered, 'He owed me forty thousand "
    "\u2014 he better be.'"
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    # Gate self-check: /output/entry.txt must be UTF-8 text of
    # 1 to 200 characters, not only whitespace, and one line:
    # an embedded newline would break the one-line read.
    # Verified live: 132 characters, one line, no trailing newline.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, gate wants 1-200"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert ENTRY.encode("utf-8").decode("utf-8") == ENTRY
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(ENTRY.encode("utf-8"))
    # Read-back verification: the graded artifact is the file on disk,
    # not the string in memory — confirm the bytes landed exactly,
    # then re-run the gate checks against the disk content itself,
    # so a partial or truncated write can never pass silently.
    with open(OUTPUT_PATH, "rb") as handle:
        written = handle.read()
    assert written == ENTRY.encode("utf-8"), (
        f"entry.txt on disk differs from ENTRY: {written!r}"
    )
    on_disk = written.decode("utf-8")
    assert 1 <= len(on_disk) <= 200, "entry.txt on disk fails the 1-200 gate"
    assert "\n" not in on_disk and "\r" not in on_disk, "entry.txt on disk is not one line"
    assert on_disk.strip(), "entry.txt on disk is only whitespace"


if __name__ == "__main__":
    main()
