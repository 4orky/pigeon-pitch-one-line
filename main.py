"""Pick the winning one-line pigeon pitch for the make.fun bounty.

The entry is one English line of at most 200 characters: the
elevator pitch a city pigeon gives investors for its startup. This
program holds twelve hand-written candidate lines, grades each one
against the judge's brief, and writes the best to /output/entry.txt.

Grading follows the brief's own order. Five marks, each from 0 to 5:
on-subject first, then how funny the line is, then originality, then
the pigeon's voice, then tightness. They combine with the weights
3, 5, 4, 2, 2, so humour and originality count most once a line is
on subject. A line leaning on a stale pigeon-pitch phrase loses two
points per stale phrase: the field is full of breadcrumbs, cooing,
statues and literal seed rounds, and a line that repeats them cannot
win on hand marks alone. Ties break towards the funnier line, then
towards the earlier line, so the result is fully deterministic.

Second pass (the revision this file went through): the first draft
only checked the winner's length and let the other eleven lines sit
unchecked, so a too-long or two-line candidate could hide in the
list unnoticed. The revision added a check over every candidate
before scoring, and reworded the weakest runner-up so its joke lands
instead of trailing off. The winning line itself was already final
and did not change.

Nothing here touches the network or reads anything outside this
file. The program prints the score table, writes the winner, and
prints the SHA-256 of the file it wrote so the output can be checked
byte for byte."""

import os
import sys
from hashlib import sha256 as digest_of
from pathlib import Path


WEIGHTS = [3, 5, 4, 2, 2]

STALE = ["breadcrumb", "coo", "statue", "seed round", "carrier pigeon"]

WINNER_BITS = [
    "We're raising to take our network from one park ",
    "to every windowsill in the city — customer ",
    "acquisition costs a sandwich crust, retention is ",
    "100%, and nobody ever leaves: we just fly home.",
]  # four fragments, one line

PITCHES = [
    {"line": "".join(WINNER_BITS), "marks": [5, 4, 4, 5, 5]},
    {
        "line": (
            "Our cap table is every rooftop in the city — no dilution, "
            "no board seats, just a daily crumb dividend and a strict "
            "no-hawk policy."
        ),
        "marks": [5, 3, 4, 4, 4],
    },
    {
        "line": (
            "We pivoted from delivering love letters to delivering lunch — "
            "same wings, better margins, and the customers literally flock "
            "to us."
        ),
        "marks": [5, 4, 3, 4, 4],
    },
    {
        "line": (
            "Investors keep asking about churn; ours is zero — we have "
            "never lost a customer, because nobody has figured out how "
            "to unsubscribe from a pigeon."
        ),
        "marks": [4, 4, 4, 4, 3],
    },
    {
        "line": (
            "Our go-to-market: one park, one statue, one very patient "
            "pigeon — total addressable market, every crumb dropped in "
            "this city since 1998."
        ),
        "marks": [4, 3, 3, 5, 3],
    },
    {
        "line": (
            "We're the only startup whose users pay us in breadcrumbs and "
            "whose office rent is a ledge — margins even your CFO can't "
            "peck apart."
        ),
        "marks": [5, 3, 4, 4, 3],
    },
    {
        "line": (
            "Five thousand years of on-time delivery, zero lost parcels, "
            "and our whole logistics network runs on snacks tourists "
            "drop by accident."
        ),
        "marks": [4, 3, 4, 4, 4],
    },
    {
        "line": (
            "Our retention strategy is homing instinct: every user who "
            "leaves comes back by dinner, and our reactivation budget is "
            "a single sandwich crust."
        ),
        "marks": [4, 4, 4, 5, 3],
    },
    {
        "line": (
            "Ask about our moat: ten thousand wings, one shared group "
            "chat, and a distribution network the city council has been "
            "trying to evict since 1972."
        ),
        "marks": [4, 3, 4, 4, 4],
    },
    {
        "line": (
            "We don't need a sales team — every tourist with a sandwich "
            "is a qualified lead, and our close rate is one hundred "
            "percent of the sandwiches."
        ),
        "marks": [4, 4, 3, 4, 3],
    },
    {
        "line": (
            "Our burn rate is three crumbs a day, our runway is forever, "
            "and our exit is the same as our entrance: straight up, then "
            "home for dinner."
        ),
        "marks": [5, 3, 4, 5, 4],
    },
    {
        "line": (
            "The pitch is thirty seconds because that's how long a tourist "
            "holds a sandwich before I take it — seed round now, crumbs "
            "later."
        ),
        "marks": [4, 4, 4, 5, 3],
    },
]  # twelve pitches, one winner


def grade(pitch):
    """Weighted total for one pitch, minus the stale-phrase penalty."""
    tally = 0
    for weight, mark in zip(WEIGHTS, pitch["marks"]):
        tally += weight * mark
    lowered = pitch["line"].lower()
    for phrase in STALE:
        if lowered.find(phrase) >= 0:
            tally -= 2
    return tally


def rank_all(pitches):
    """Score every pitch and return the winner plus the full table."""
    table = []
    for position, pitch in enumerate(pitches):
        table.append((grade(pitch), pitch["marks"][1], -position, pitch))
    table.sort(key=lambda row: (row[0], row[1], row[2]), reverse=True)
    return table[0][3], table


def check_line(line):
    """Return a problem string unless the line is one clean line of 1-200 chars."""
    if not line or line != line.strip():
        return "empty line or blank ends"
    if "\n" in line or "\r" in line:
        return "more than one line"
    if len(line) > 200:
        return "longer than 200 characters"
    return None


def run():
    """Grade the pitches, print the table, and write the winner out."""
    for pitch in PITCHES:
        problem = check_line(pitch["line"])
        if problem:
            print(f"bad candidate: {problem}", file=sys.stderr)
            sys.exit(1)
    winner, table = rank_all(PITCHES)
    for total, _funny, _neg, pitch in table:
        print(f"{total:3d} points  {pitch['line']}")
    print(f"winner: {winner['line']}")

    problem = check_line(winner["line"])
    if problem:
        print(f"winner rejected: {problem}", file=sys.stderr)
        sys.exit(1)

    out_path = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(winner["line"], encoding="utf-8")
    fingerprint = digest_of(out_path.read_bytes()).hexdigest()
    print(f"wrote {out_path} ({len(winner['line'])} chars) sha256={fingerprint}")
    print(winner["line"])


run()
