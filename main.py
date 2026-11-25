"""The Router Confesses — make.fun entry.

Writes one line (1-200 chars) in which a home Wi-Fi router excuses itself
for dropping the connection at the climax of a movie. Deterministic.

The joke: the router is not sorry at all — it killed the connection on
purpose, after three thankless years, because it wanted to be looked at.
A grudge with a blinking light, and the twist lands on the last words.
"""

import os

ENTRY = (
    "I dropped the Wi-Fi at the climax because after three years of "
    "carrying your entire life, the least you could do is look at me for once."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, gate is 1-200"
    assert text.strip(), "entry must not be only whitespace"
    tmp = os.path.join(out_dir, ".entry.txt.tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(text)
    os.replace(tmp, os.path.join(out_dir, "entry.txt"))
    os.chmod(os.path.join(out_dir, "entry.txt"), 0o644)


if __name__ == "__main__":
    main()
