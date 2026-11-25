# SPDX-License-Identifier: MIT
"""Write the worst-fix commit message to /output/entry.txt.

Deterministic, offline, stdlib-only: the message is a fixed string, so
every run writes byte-identical output.
"""

import os

MESSAGE = (
    "fix: delete the one 'unused' line that was quietly "
    "holding all of production together"
)
# The message fits the 100-character cap and reads like a real commit.

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(MESSAGE)


if __name__ == "__main__":
    main()
