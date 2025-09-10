"""Pipeline flows for AI summarization."""

from .step_01_planning import PlanningFlowConfig, planning_flow
from .step_02_writing import WritingFlowConfig, writing_flow
from .step_03_review import ReviewFlowConfig, review_flow
from .step_04_rewrite import RewriteFlowConfig, rewrite_flow

# MUST export these lists
FLOW_CONFIGS = [
    PlanningFlowConfig,
    WritingFlowConfig,
    ReviewFlowConfig,
    RewriteFlowConfig,
]

FLOWS = [
    planning_flow,
    writing_flow,
    review_flow,
    rewrite_flow,
]

# MUST have same length
assert len(FLOW_CONFIGS) == len(FLOWS)

__all__ = ["FLOW_CONFIGS", "FLOWS"]
