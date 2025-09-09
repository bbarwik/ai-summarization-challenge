"""Flow modules for the ai-pipeline pipeline."""

from typing import Any, Callable

from ai_pipeline_core import FlowConfig

FLOW_CONFIGS: list[type[FlowConfig]] = []

FLOWS: list[Callable[..., Any]] = []

assert len(FLOW_CONFIGS) == len(FLOWS)

__all__ = [
    "FLOW_CONFIGS",
    "FLOWS",
]
