"""Flow options configuration for ai-pipeline."""

from ai_pipeline_core import FlowOptions, ModelName
from pydantic import Field


class ProjectFlowOptions(FlowOptions):
    """Options to be provided to each flow in the ai-pipeline pipeline.

    Extends the base FlowOptions with project-specific configuration.
    """

    # Optionally override defaults from base class
    core_model: ModelName = Field(default="gpt-5")
    small_model: ModelName = Field(default="gpt-5-mini")
