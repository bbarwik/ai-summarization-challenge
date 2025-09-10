"""Flow document for report draft."""

from enum import StrEnum

from ai_pipeline_core import FlowDocument


class DraftDocument(FlowDocument):
    """Flow document containing the initial report draft."""

    class FILES(StrEnum):
        """File names for draft documents."""

        REPORT_DRAFT = "report_draft.md"
