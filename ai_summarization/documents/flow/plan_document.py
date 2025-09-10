"""Flow document for report plan."""

from enum import StrEnum

from ai_pipeline_core import FlowDocument


class PlanDocument(FlowDocument):
    """Flow document containing the report plan."""

    class FILES(StrEnum):
        """File names for plan documents."""

        REPORT_PLAN = "report_plan.md"
