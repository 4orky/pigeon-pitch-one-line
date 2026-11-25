#!/usr/bin/env python3
"""Pigeon Pitch, One Line — make.fun entry.

Writes a single original one-line elevator pitch (at most 200
characters, in English) from a city pigeon to investors for its
startup, to /output/entry.txt.

How it picks the line: twelve original candidate pitches, each
written for this entry, are scored against the judge's five criteria,
in the judge's own order of importance:

  1. it is a one-line elevator pitch from a city pigeon to investors
     for its startup (on subject)
  2. it is funny, with a real joke that lands rather than a mild pun
     or a straight description
  3. it is original and surprising, an idea or twist the reader has
     not met before
  4. it keeps the pigeon's voice and city life in view, so the pitch
     could only come from a pigeon
  5. it fits one line in English within 200 characters, with every
     word earning its place

Each criterion is rated 0-5 and weighted 3, 4, 3, 2, 2, matching the
judge's priority order. The highest total wins; ties go to the
earliest candidate in the list, so the choice is fully deterministic.

Freshness is not only hand-rated: any candidate leaning on a tired
pigeon-pitch trope loses three points per trope phrase found in its
own text, so a line the field has already told five hundred times
cannot win on a generous hand rating alone. The field is full of
breadcrumb subscriptions, literal seed rounds, statues and cooing,
so those are the penalised phrases.

Revision (second pass, on the winning line): the first draft said
"Our market is every windowsill on Earth" — grandiose filler with no
ask, and "we never leave, we just fly home" tripped over itself.
The revised winner opens with the ask ("We're raising to take our
network from one park to every windowsill in the city"), swaps in
tighter investor language ("customer acquisition costs a sandwich
crust"), and lands the homing joke cleanly ("nobody ever leaves: we
just fly home"). Same joke, shorter fuse; tightness 4 -> 5.

No network, no external input, no randomness. The program verifies
its own output (1-200 characters, a single line, UTF-8) and prints
the SHA-256 of the file it wrote.
"""

from hashlib import sha256
from os import environ, makedirs
from sys import exit as finish, stderr

# Weights for the five judge criteria, in the judge's priority order:
# on-subject, funny, original, pigeon voice, tight.
WEIGHTS = (3, 4, 3, 2, 2)

# Overused pigeon-pitch tropes, seen all over the field's 500+ entries.
# A candidate containing one of these phrases has already been told a
# thousand times; each hit costs three points. Matched case-insensitively
# against the text itself.
CLICHES = (
    "breadcrumb",
    "seed is literal",
    "seed round, literally",
    "statue",
    "coo",
)

# Each candidate: (text, (on-subject, funny, original, voice, tight)).
# All twelve lines are original, written for this entry.
CANDIDATES = [
    (
        "We're raising to take our network from one park to every "
        "windowsill in the city — customer acquisition costs a "
        "sandwich crust, retention is 100%, and nobody ever leaves: "
        "we just fly home.",
        (5, 4, 4, 5, 5),
    ),
    (
        "We're raising a seed round for PigeonPost — and no, the seed "
        "isn't literal. It's the one thing in this city we haven't "
        "eaten yet.",
        (4, 4, 5, 4, 3),
    ),
    (
        "Our startup eats your lunch — literally, we've been doing it "
        "in this park for years — and now we're raising to eat "
        "everyone's.",
        (4, 4, 4, 4, 3),
    ),
    (
        "Our startup turns every statue in the city into a billboard — "
        "we already own the pigeons, the ledges and the aim; we just "
        "need your money for the paint.",
        (4, 3, 3, 4, 3),
    ),
    (
        "Investors keep asking about our exit strategy — we fly away, "
        "obviously, and we always come back, which is more than I can "
        "say for your last three founders.",
        (3, 4, 4, 4, 3),
    ),
    (
        "We're the original airmail: 5,000 years of deliveries, zero "
        "lost packages — well, one, but the pigeon came back and "
        "apologised in person.",
        (4, 3, 3, 4, 4),
    ),
    (
        "Our moat is the city's anti-pigeon spikes: every spike they "
        "install proves the market wants us gone, and every pigeon "
        "that gets past one proves we can't be stopped.",
        (4, 3, 4, 4, 2),
    ),
    (
        "We deliver packages faster than your courier, cheaper than "
        "your drone, and we never need charging — the only thing we "
        "drop is on statues, and that's a feature.",
        (4, 4, 3, 4, 3),
    ),
    (
        "Our business model is simple: the city installs spikes to "
        "keep us out, tourists pay to feed us, and we poop on both of "
        "them for free.",
        (3, 4, 3, 5, 3),
    ),
    (
        "We've been bootstrapped on breadcrumbs for 5,000 years and "
        "never raised a cent — until now, because the park just got a "
        "no-feeding sign.",
        (4, 3, 3, 4, 3),
    ),
    (
        "We're raising to put a pigeon on every rooftop in the city — "
        "our users already flock to us, our churn is zero, and our "
        "burn rate is literally birdseed.",
        (5, 3, 3, 4, 4),
    ),
    (
        "My pitch is thirty seconds because that's exactly how long a "
        "tourist holds a sandwich before I take it — now, who's in "
        "for the seed round?",
        (4, 4, 4, 5, 3),
    ),
]


def score(text, ratings):
    """Weighted total for one candidate, minus the cliche penalty."""
    total = sum(w * r for w, r in zip(WEIGHTS, ratings))
    lowered = text.lower()
    for phrase in CLICHES:
        if phrase in lowered:
            total -= 3
    return total


def pick():
    """Return (best index, best text, best score, all scores)."""
    scored = [(score(t, r), i, t) for i, (t, r) in enumerate(CANDIDATES)]
    best = max(scored, key=lambda s: (s[0], -s[1]))
    return best[1], best[2], best[0], scored


def main():
    winner_index, line, best_score, scored = pick()
    for total, index, _ in sorted(scored, reverse=True):
        print(f"candidate {index + 1:2d}: {total} points")
    print(f"winner: candidate {winner_index + 1} with {best_score} points")

    # Gate: one line, 1-200 characters, not only whitespace.
    if not line or line != line.strip() or "\n" in line:
        print("winner is not a single clean line", file=stderr)
        finish(1)
    if not 1 <= len(line) <= 200:
        print(f"winner is {len(line)} characters, not 1-200", file=stderr)
        finish(1)

    out_dir = environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    makedirs(out_dir, exist_ok=True)
    path = f"{out_dir}/entry.txt"
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)
    digest = sha256(line.encode("utf-8")).hexdigest()
    print(f"wrote {path} ({len(line)} chars) sha256={digest}")
    print(line)


if __name__ == "__main__":
    main()
