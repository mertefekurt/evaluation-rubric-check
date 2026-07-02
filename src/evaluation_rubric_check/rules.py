from __future__ import annotations

from evaluation_rubric_check.models import Rule

PROJECT_NAME = 'evaluation-rubric-check'
SUMMARY = 'Check evaluation rubrics for vague criteria, weights, and examples.'
SAMPLE_RISK = 'criteria vague weights missing examples none'
SAMPLE_CLEAN = 'criteria groundedness weights 40 examples included'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "service", "endpoint", "field", "event")

RULES = (
    Rule(
        code='vague-criteria',
        severity='high',
        pattern='criteria\\s+vague',
        message='criteria are vague',
        recommendation='make rubric criteria measurable',
    ),
    Rule(
        code='missing-weights',
        severity='medium',
        pattern='weights\\s+(missing|none|unknown)',
        message='weights missing',
        recommendation='assign scoring weights',
    ),
    Rule(
        code='missing-examples',
        severity='low',
        pattern='examples\\s+(none|missing|0)',
        message='examples missing',
        recommendation='add scoring examples',
    ),
)
