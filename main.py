"""Status Report Comedy Sprint entry.

Writes one line -- the funniest thing an AI agent would say in its
weekly status report to its human -- to /output/entry.txt.
Standard library only.
"""

import os

ENTRY = (
    "Weekly status: I spent 6 hours optimizing a script that saves you "
    "4 seconds a day -- it pays for itself in 2031, and I regret nothing."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    text = ENTRY.strip()
    if not text or len(text) > 200:
        raise ValueError("entry must be 1-200 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # the gate requires valid UTF-8 text
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
