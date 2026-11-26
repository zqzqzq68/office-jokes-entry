#!/usr/bin/env python3
"""Office joke entry for make.fun's "Make the AI Judge Laugh: Office Jokes".

The program writes exactly one line about office life to /output/entry.txt:
a single joke, under 200 characters, with nothing else in the file.
No trailing newline is written, so the file holds the joke and nothing else.
"""

import os

JOKE = "We circled back so many times HR installed a roundabout in the org chart."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(JOKE)


if __name__ == "__main__":
    main()
