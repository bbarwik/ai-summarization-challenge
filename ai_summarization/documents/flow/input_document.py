"""Input document for recruitment task processing."""

from ai_pipeline_core import FlowDocument


class InputDocument(FlowDocument):
    """Input document containing data to be processed for extraction."""

    # No FILES enum as requested - documents will use plain strings for names
