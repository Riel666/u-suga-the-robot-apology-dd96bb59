"""Two lines: line 1 is a robot apologizing in one sentence for one specific mistake; line 2 says in one sentence what it learned and what it will do differently.

The program writes exactly those lines and nothing else to /output/entry.txt.
"""

import os

TEXT = "I am sorry: I watered the plastic plant on your desk every morning for a month, then filed a weekly report praising its excellent growth and steady leaves.\nI learned to check whether a thing is alive before I care for it, so now I poke it first and only water the ones that poke back."


def main():
    assert 1 <= len(TEXT) <= 400, len(TEXT)
    assert TEXT == TEXT.strip()
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
