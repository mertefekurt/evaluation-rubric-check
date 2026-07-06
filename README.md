<p align="center">
  <img src="assets/readme-cover.svg" alt="Evaluation Rubric Check cover" width="100%" />
</p>

# Evaluation Rubric Check

![stack](https://img.shields.io/badge/stack-Python-0891b2?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-b45309?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-be185d?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-4b5563?style=flat-square)

Check evaluation rubrics for vague criteria, weights, and examples.

## Why it exists

Small review tasks are easy to skip when the signal lives in notes, spreadsheets, or loosely formatted exports. `evaluation-rubric-check` turns those checks into a repeatable command with plain findings and CI-friendly exit codes.

## Quick run

```bash
python -m pip install -e ".[dev]"
evaluation-rubric-check examples/sample.txt
evaluation-rubric-check examples/sample.txt --json --fail-on medium
```

## Rule set

| Rule | Severity | What it catches |
| --- | --- | --- |
| `vague-criteria` | high | criteria are vague |
| `missing-weights` | medium | weights missing |
| `missing-examples` | low | examples missing |

## Input

The reader accepts plain text, JSON, JSONL, and CSV. That keeps it useful for hand-written notes, review exports, and small automation jobs.

## Sample risky input

```text
criteria vague weights missing examples none
```

## Development

```bash
python -m pip install -e ".[dev]"
ruff check .
pytest
python -m evaluation_rubric_check --help
```

`cli.py` handles arguments, `core.py` reads and evaluates records, and `rules.py` keeps the Evaluation Rubric Check policy easy to review.
