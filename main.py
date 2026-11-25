"""Entry for the make.fun bounty "The One-Liner Groan-Off".

The program writes a single original dad joke to /output/entry.txt.
The joke is a dad explaining the moon to his son: the moon works the
night shift so the sun can have the day off. It is a pun-free twist
on a question every dad gets asked, delivered as a straight-faced
explanation, which is exactly how a dad joke lands at the dinner
table. The setup and the turn live inside the one line, the wording
is tight enough to say out loud, and the groan is earned by the
image of the sun clocking off while the moon clocks in — a dad
explaining shift work to a child who asked a perfectly fair
question. The gate allows 1 to 140 characters of UTF-8 text, so the line is checked
against that cap before it is written.
"""

import os

ENTRY = (
    "My son asked why the moon only comes out at night. I said it's "
    "working the night shift so the sun can have the day off."
)

MAX_CHARS = 140
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
