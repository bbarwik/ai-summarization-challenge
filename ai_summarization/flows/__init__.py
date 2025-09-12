"""Pipeline flows for AI summarization."""

from .step_01_planning import planning_flow
from .step_02_writing import writing_flow
from .step_03_review import review_flow
from .step_04_rewrite import rewrite_flow

# MUST export FLOWS list
FLOWS = [
    planning_flow,
    writing_flow,
    review_flow,
    rewrite_flow,
]

__all__ = ["FLOWS"]
