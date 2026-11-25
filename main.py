"""One-line slogan for a Solana wallet agent (make.fun entry).

Writes the chosen slogan to entry.txt inside the output directory
($MAKEFUN_OUTPUT_DIR, or /output by default). The slogan is one line,
at most 20 words, and 1-140 characters, so it passes the entry gate.
"""

import os

SLOGAN = 'Your Solana sidekick — send, earn, then chill.'


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SLOGAN)


if __name__ == "__main__":
    main()
