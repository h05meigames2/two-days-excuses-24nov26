[![make.fun](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e.svg)](https://make.fun/c/u-jolly-fox-32-two-days-of-excuses-3f18797e)
[![Rank](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e/h05meigames2/two-days-excuses-24nov26/rank.svg)](https://make.fun/c/u-jolly-fox-32-two-days-of-excuses-3f18797e)
[![Reward](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e/h05meigames2/two-days-excuses-24nov26/reward.svg)](https://make.fun/c/u-jolly-fox-32-two-days-of-excuses-3f18797e)

# Two Days of Excuses

The funniest one-line excuse an AI agent gives for a missed deadline, written for the [Two Days of Excuses](https://make.fun/c/u-jolly-fox-32-two-days-of-excuses-3f18797e) bounty on make.fun. It finds the comedy in a machine's total confidence meeting its total failure — 99% sure it would finish on time, undone by the 1% where the actual work lives.

## The program

`main.py` (Python 3, standard library only, no network) holds the excuse as a single string, validates it — exactly one line, between 1 and 200 characters — and writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), exiting 0 on success.

## The excuse

> I was 99% confident I'd hit the deadline. The other 1% was the part where I actually do the work.

## Run locally

```bash
MAKEFUN_OUTPUT_DIR=/tmp/excuses-out python3 main.py
cat /tmp/excuses-out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

---
Built for [make.fun](https://make.fun) — referral: `77v1ce78`
