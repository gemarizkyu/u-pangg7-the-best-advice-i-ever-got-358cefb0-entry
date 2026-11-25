"""Write one original sentence about the best advice ever received to entry.txt.

Deterministic: the same sentence, byte for byte, on every run. No randomness,
no network, no clock, no input files. It runs twice and produces byte-identical
output.
"""

import os

SENTENCE = "My grandmother, who raised six kids on a seamstress's wage, told me, 'Nobody remembers what you owned, love — they remember whether you showed up,' and I have tried to show up ever since."

MAX_CHARS = 200


def main():
    text = SENTENCE.strip()
    if not 1 <= len(text) <= MAX_CHARS - 1:
        raise SystemExit(f"sentence is {len(text)} chars, must be 1-199")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    # Read back what was written: the gate counts the file, so verify the file
    # itself — one sentence, 1-200 characters, not only white space.
    with open(out_path, encoding="utf-8") as f:
        written = f.read()
    if not 1 <= len(written.strip()) <= MAX_CHARS - 1 or len(written) > MAX_CHARS:
        raise SystemExit(f"entry.txt failed the gate: {len(written)} chars written")


if __name__ == "__main__":
    main()
