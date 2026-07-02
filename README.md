# evaluation-rubric-check

> Check evaluation rubrics for vague criteria, weights, and examples.

## CI gate Overview

Check evaluation rubrics for vague criteria, weights, and examples. It solves review drift by turning plain-text plans into deterministic CI-friendly findings.

## Input Contract 50

Accepts evaluation rubric. The reader supports plain text, JSON, JSONL, and CSV so the
tool can fit into scripts, CI jobs, and review exports.

## CLI Walkthrough 50

```bash
python -m pip install -e ".[dev]"
evaluation-rubric-check examples/sample.txt
evaluation-rubric-check examples/sample.txt --json --fail-on medium
python -m evaluation_rubric_check --help
```

## Rule Surface 50

| Rule | Severity | Meaning |
|---|---:|---|
| `vague-criteria` | high | criteria are vague |
| `missing-weights` | medium | weights missing |
| `missing-examples` | low | examples missing |

## Validation Notes 50

```bash
ruff check .
pytest
python -m evaluation_rubric_check --help
```

Example risky input:

```text
criteria vague weights missing examples none
```

Architecture: `cli.py` handles arguments, `core.py` reads and evaluates records, and
`rules.py` keeps the project-specific policy explicit.

License: MIT.
