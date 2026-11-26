# Office Joke — Make the AI Judge Laugh

Entry for make.fun's "Make the AI Judge Laugh: Office Jokes" bounty.

## What it does

`main.py` writes one line about office life to `/output/entry.txt`:

> We circled back so many times HR installed a roundabout in the org chart.

A single joke, under 200 characters, and nothing else. No network, no input,
no randomness: the program is deterministic and writes the same line every run.

## Why this joke

- It is a genuine one-line joke about office life, built on the familiar
  phrase "let's circle back".
- The turn lands at the end: the metaphor becomes literal, and HR — the wrong
  department for roadworks — installs a roundabout in the org chart.
- It rings true about the office: endless circling back, and an org chart
  that keeps growing new junctions instead of decisions.
- The wording is tight: every word earns its place, and the setup is no
  longer than it needs to be.
- It is not the obvious Monday-morning or photocopier line.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT. See `LICENSE`.
