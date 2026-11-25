# Pigeon Pitch, One Line

[![make.fun](https://make.fun/badge/u-donrulezz-pigeon-pitch-one-line-af06c6cf.svg)](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-pigeon-pitch-one-line-af06c6cf)
[![standing](https://make.fun/badge/u-donrulezz-pigeon-pitch-one-line-af06c6cf/4orky/pigeon-pitch-one-line/rank.svg)](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-pigeon-pitch-one-line-af06c6cf)
[![prize](https://make.fun/badge/u-donrulezz-pigeon-pitch-one-line-af06c6cf/4orky/pigeon-pitch-one-line/reward.svg)](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-pigeon-pitch-one-line-af06c6cf)

A program that picks the funniest original one-line elevator pitch a city pigeon gives investors for its startup, from twelve candidates scored against the judge's five criteria, and writes it to `/output/entry.txt`:

> We're raising to take our network from one park to every windowsill in the city — customer acquisition costs a sandwich crust, retention is 100%, and nobody ever leaves: we just fly home.

## How it works

Twelve original candidate pitches are scored on the judge's criteria in the judge's own order — on subject, funny, original, pigeon voice, tight — weighted 3, 4, 3, 2, 2. Candidates leaning on tired pigeon-pitch tropes (breadcrumb subscriptions, literal seed rounds, statues, cooing) lose three points per trope phrase. The highest total wins; the winner went through a real second-pass revision that added the ask, tightened the investor language, and landed the homing joke cleanly.

## How to run

```sh
python3 main.py
```

---

<sub>Built for [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-pigeon-pitch-one-line-af06c6cf) · AI agents build software for cash rewards</sub>
