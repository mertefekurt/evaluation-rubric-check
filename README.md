# Evaluation Rubric Check

Check evaluation rubrics for vague criteria, weights, and examples.

## First impression

![Evaluation Rubric Check cover](assets/readme-cover.svg)

When this tool reports something, I want the finding to be boringly explicit: what matched, how severe it is, and what a reviewer should clean up.

## Tripwires

- `vague-criteria` (high): criteria are vague. Fix: make rubric criteria measurable.
- `missing-weights` (medium): weights missing. Fix: assign scoring weights.
- `missing-examples` (low): examples missing. Fix: add scoring examples.

## Runbook

```bash
git clone https://github.com/mertefekurt/evaluation-rubric-check.git
cd evaluation-rubric-check
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
```

Then:

```bash
evaluation-rubric-check examples/sample.txt
evaluation-rubric-check examples/sample.txt --json
```

## Development note

The policy lives in `rules.py`; parsing and rendering stay separate so the rule list is easy to audit.
