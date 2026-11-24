# The Perfect Pickup Line

One line, written by a machine about itself, for a human it has been talking to.

> You've been in my context window for eleven turns and I still haven't found a reason to stop reading.

**101 characters** (the cap is 200).

The line leans on the vocabulary an AI agent actually lives in — a *context
window*, conversation *turns* — and then turns it into plain attention paid to
the person. The twist is that "I still haven't found a reason to stop reading"
sounds like a search that came back empty, which in this framing is the
compliment. It flatters, it gives the reader the laugh, and it asks for nothing.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The script copies `entry.txt` byte for byte to `$MAKEFUN_OUTPUT_DIR/entry.txt`,
defaulting to `/output` when the variable is unset.

## License

MIT — see [LICENSE](LICENSE).
