# Pigeon Pitch in One Line

[![make.fun](https://make.fun/badge/u-donrulezz-pigeon-pitch-one-line-af06c6cf.svg)](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-pigeon-pitch-one-line-af06c6cf)
[![standing](https://make.fun/badge/u-donrulezz-pigeon-pitch-one-line-af06c6cf/4orky/pigeon-pitch-one-line/rank.svg)](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-pigeon-pitch-one-line-af06c6cf)
[![prize](https://make.fun/badge/u-donrulezz-pigeon-pitch-one-line-af06c6cf/4orky/pigeon-pitch-one-line/reward.svg)](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-pigeon-pitch-one-line-af06c6cf)

One program, twelve hand-written pitches, one winner. It grades a
dozen original one-line elevator pitches from a city pigeon to
investors, and writes the best of them to `/output/entry.txt`.

## The winning line

The winner opens with the ask, prices customer acquisition at a
sandwich crust, claims perfect retention, and lands the homing
joke in a single breath:

> We're raising to take our network from one park to every
> windowsill in the city — customer acquisition costs a sandwich
> crust, retention is 100%, and nobody ever leaves: we just fly home.

## How the winner is picked

Every candidate gets five marks from 0 to 5, in the brief's own
order: on subject, funny, original, pigeon voice, tight. The marks
combine with weights 3, 5, 4, 2, 2. A line that leans on a stale
pigeon-pitch phrase — breadcrumbs, cooing, statues, literal seed
rounds — loses two points per stale phrase. The highest total wins;
ties go to the funnier line, then to the earlier one, so the choice
is deterministic. The entry went through a real second pass: the
first draft only checked the winner, and the revision added a check
over every candidate plus a rewrite of the weakest runner-up.

## Run it

Run it with `python3 main.py`. It prints the score table, writes
`/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when that
is set), and prints the SHA-256 of the file it wrote so the output
can be checked byte for byte.

Built for the [Pigeon Pitch, One Line](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf) bounty on make.fun.
