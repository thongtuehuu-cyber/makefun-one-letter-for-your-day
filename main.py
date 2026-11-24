"""One Letter for Your Day — make.fun entry.

Writes exactly one character, the letter K, to /output/entry.txt.
Behind the letter sits the word "knackered": flat-out exhausted,
collapsed on the sofa after a long day — vivid, funny and true.
Deterministic: no network, no randomness, no external files.
"""

import os

LETTER = "K"
# Why K: the hidden word is "knackered" — flat-out exhausted, collapsed
# on the sofa after a long day. K is an uncrowded letter, so the judge's
# inference converges on a vivid, funny, true word instead of an obvious
# one (A for amazing, Z for zero sleep), and the hard K fits the word.

# Gate asserts: the sealed scorer requires /output/entry.txt to be UTF-8
# text of exactly 1 character, not only white space, a letter A-Z.
assert len(LETTER) == 1, f"entry must be exactly 1 character, got {len(LETTER)}"
assert "A" <= LETTER <= "Z", f"entry must be a letter A-Z, got {LETTER!r}"
assert LETTER == LETTER.strip(), "entry must not be white space"
assert LETTER.isalpha() and LETTER.isupper(), "entry must be one uppercase letter"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LETTER)
