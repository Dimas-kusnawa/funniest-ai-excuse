#!/usr/bin/env python3
"""One line: the funniest excuse an AI agent gives its human for a missed deadline.

The excuse turns the agent's own nature into the dodge: it did not miss the
deadline out of laziness, it hallucinated a second one and met that instead.
"""
import os

# Why this lands: the joke is the excuse itself, not an apology.
# A human blames traffic; an agent blames its own hallucination.
# The twist sits at the very end — "met that one instead" — so the
# line reads as a confession and only then reveals it as a dodge.
LINE = "I would have finished on time, but I hallucinated a second deadline and met that one instead."


def main() -> None:
    # Deterministic: the same single line on every run, no randomness,
    # no network, no clock. The output is exactly LINE, one line,
    # no trailing newline, 93 characters, inside the 200-char limit.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {path}: {LINE} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
