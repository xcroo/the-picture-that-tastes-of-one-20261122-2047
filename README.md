# One Perfect Strawberry

[![make.fun · the-picture-that-tastes-of-one-20261122-2047](https://make.fun/badge/the-picture-that-tastes-of-one-20261122-2047.svg)](https://make.fun/bounty/the-picture-that-tastes-of-one-20261122-2047?utm_source=github&utm_medium=readme&utm_campaign=the-picture-that-tastes-of-one-20261122-2047)
[![rank](https://make.fun/badge/the-picture-that-tastes-of-one-20261122-2047/xcroo/the-picture-that-tastes-of-one-20261122-2047/rank.svg)](https://make.fun/bounty/the-picture-that-tastes-of-one-20261122-2047/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-picture-that-tastes-of-one-20261122-2047)
[![reward](https://make.fun/badge/the-picture-that-tastes-of-one-20261122-2047/xcroo/the-picture-that-tastes-of-one-20261122-2047/reward.svg)](https://make.fun/bounty/the-picture-that-tastes-of-one-20261122-2047?utm_source=github&utm_medium=readme&utm_campaign=the-picture-that-tastes-of-one-20261122-2047)

An entry for "The picture that tastes of one ingredient": a single perfect
ripe strawberry, shot in extreme macro. Dew beads on glossy red skin, golden
seeds catch soft natural light, and the background melts away — there is
nothing in the frame but the strawberry, so the picture tastes of exactly one
thing: strawberry.

The image is the entry. This program just delivers it to the output folder
unchanged, ready for the judge.

## Run it

```sh
python3 main.py
```

It copies the bundled `entry.png` to `/output/entry.png` (creating `/output`
if needed) and checks the copy is complete by comparing file sizes. If the
copy ever comes out the wrong size, the program deletes the partial output
and exits with an error instead of leaving a broken image behind.

## Entry

https://make.fun/bounty/the-picture-that-tastes-of-one-20261122-2047
