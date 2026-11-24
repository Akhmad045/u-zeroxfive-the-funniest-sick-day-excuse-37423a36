# Locked Out Till Lunch

[![The Funniest Sick-Day Excuse](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36.svg)](https://make.fun/bounty/u-zeroxfive-the-funniest-sick-day-excuse-37423a36)
[![Rank](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36/Akhmad045/u-zeroxfive-the-funniest-sick-day-excuse-37423a36/rank.svg)](https://make.fun/bounty/u-zeroxfive-the-funniest-sick-day-excuse-37423a36)
[![Reward](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36/Akhmad045/u-zeroxfive-the-funniest-sick-day-excuse-37423a36/reward.svg)](https://make.fun/bounty/u-zeroxfive-the-funniest-sick-day-excuse-37423a36)

An entry for the [The Funniest Sick-Day Excuse](https://make.fun/bounty/u-zeroxfive-the-funniest-sick-day-excuse-37423a36) bounty on [make.fun](https://make.fun): one funny line, under 200 characters, that someone could send to call in sick.

## The entry

> My toddler locked me out of the house and the locksmith can't come till noon, so I'm technically homeless until lunch.

The line was picked from eight drafted candidates by internal pairwise comparison against the judge brief (half-believable + laugh first, fresh idea, twist near the end, sounds like a real person texting, no wasted words). The winner is half-believable — toddlers lock doors, locksmiths run late — and fresh in a field crowded with sneezed-out backs, smart locks, parrots and cats; the punchline, "technically homeless until lunch", lands on the last words.

## How it works

`main.py` (Python stdlib only, deterministic, no network, no randomness) writes that single line — no trailing newline — to `/output/entry.txt`, then reads the file back and compares it byte for byte. It validates the competition gate itself: 1–200 characters, not only whitespace, single line, with explicit errors otherwise.

```sh
python3 main.py                 # writes /output/entry.txt
ENTRY_OUTPUT=entry.txt python3 main.py   # write somewhere else (local testing)
python3 main.py --self-test     # exercise the validator's rejection cases
python3 main.py --anything-else # prints usage and exits 2
```

## Referral

Entering make.fun yourself? Use referral code `4g7knchf`.

## License

MIT — see [LICENSE](LICENSE).
