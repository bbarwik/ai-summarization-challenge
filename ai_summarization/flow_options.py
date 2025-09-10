"""Flow options configuration for ai-summarization."""

from ai_pipeline_core import FlowOptions, ModelName
from pydantic import Field


class ProjectFlowOptions(FlowOptions):
    """Options to be provided to each flow in the ai-summarization pipeline.

    Extends the base FlowOptions with project-specific configuration.
    """

    # Optionally override defaults from base class
    core_model: ModelName = Field(default="gpt-5")
    small_model: ModelName = Field(default="gpt-5-mini")

    # Task description used across all flows
    task_description: str = Field(
        default=(
            "Write a very detailed research report about companies developing AI assistants. "
            "Start report with detailed introduction to each project working on AI assistants. "
            "Each project should have status, timeline, key milestones, history and future plans. "
            "Then compare them with each other, explain strengths and weaknesses of each project. "
            "Use only provided documents to write the report, do not use your internal knowledge. "
        ),
        description="The main task description used for report generation",
    )
