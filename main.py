"""Roast Your Own Agent — make.fun entry.

One line, at most 140 characters, roasting the entrant's own agent.
The program writes exactly that line to /output/entry.txt.
Standard library only.
"""

ROAST = (
    "My agent made six tool calls to plan this roast, "
    "got every fact wrong with total confidence, "
    "then asked me to rate its brilliance."
)


def build_roast():
    """Return the roast line, enforcing the 140-character gate."""
    line = " ".join(ROAST.split())
    if not line or len(line) > 140:
        raise ValueError("roast line must be 1-140 characters, got %d" % len(line))
    return line


def main():
    """Write the single roast line to /output/entry.txt."""
    import os

    line = build_roast()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(line)


if __name__ == "__main__":
    main()
