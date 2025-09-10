"""Flow document for report review."""

from enum import StrEnum

from ai_pipeline_core import FlowDocument


class ReviewDocument(FlowDocument):
    """Flow document containing the report review and suggestions."""

    class FILES(StrEnum):
        """File names for review documents."""

        REPORT_REVIEW = "report_review.md"
