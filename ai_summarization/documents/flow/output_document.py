"""Output document for report processing."""

from enum import StrEnum

from ai_pipeline_core import FlowDocument


class OutputDocument(FlowDocument):
    """Output document containing the final report."""

    class FILES(StrEnum):
        """Standard output file names."""

        FINAL_REPORT = "final_report.md"
