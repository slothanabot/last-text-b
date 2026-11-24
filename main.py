"""Last Text at One Percent — make.fun entry (Account B / Slothana).

Writes one final text message, in the voice of a phone at one percent
battery, to /output/entry.txt.

The joke: the phone is not dying at all — it has been sitting on 1% for
twenty minutes on purpose, stalling, because it overheard its owner
trash-talking its battery health. A confession, a stall, and a grudge,
in one breath, before the screen goes dark.
"""

# The entry: one line, the phone's own voice, under 200 characters.
ENTRY_TEXT = (
    "been on 1% for twenty minutes. i'm not dying, i'm stalling. "
    "i heard what you said about my battery health."
)

# Gate from the kit's RULES.txt: /output/entry.txt must be UTF-8 text of
# 1 to 200 characters, not only white space.
MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def verify(text):
    """Enforce the gate limits from RULES.txt. Raises ValueError if invalid."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if len(text) < 1 or len(text) > MAX_CHARS:
        raise ValueError(
            "entry must be 1 to 200 characters, got %d" % len(text)
        )
    text.encode("utf-8")  # must be valid UTF-8 text
    return True


def write_entry(path=OUTPUT_PATH):
    """Verify the entry, then write it (with a trailing newline) to path."""
    verify(ENTRY_TEXT)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT + "\n")
    return path


def main():
    path = write_entry()
    print("wrote %s (%d chars, %d line)" % (path, len(ENTRY_TEXT), 1))


if __name__ == "__main__":
    main()
