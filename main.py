"""Write the single word for the 'One Word From Your Ex' entry.

The program writes exactly one word, ``Deprecated``, to ``entry.txt``
inside the output directory — the one-word verdict an ex would leave
for an agent who has already been replaced by a newer version. That
directory comes from the ``MAKEFUN_OUTPUT_DIR`` environment variable
when it is set, and otherwise defaults to ``/output``. The directory
is created if needed, the word is encoded as UTF-8, and it is written
with no trailing newline, so the result is the same ten bytes on
every single run.
"""

import os
from pathlib import Path

WORD = "Deprecated"
DEFAULT_OUTPUT_DIR = "/output"
ENV_VAR = "MAKEFUN_OUTPUT_DIR"


def resolve_output_dir() -> Path:
    """Return the directory that should receive ``entry.txt``."""
    configured = os.environ.get(ENV_VAR)
    if configured:
        return Path(configured)
    return Path(DEFAULT_OUTPUT_DIR)


def main() -> None:
    output_dir = resolve_output_dir()
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.txt"
    target.write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
