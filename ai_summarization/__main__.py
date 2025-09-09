"""CLI entry point for ai-summarization."""

from ai_pipeline_core import DocumentList, FlowOptions
from ai_pipeline_core.simple_runner import run_cli

from .flow_options import ProjectFlowOptions
from .flows import FLOW_CONFIGS, FLOWS

TRACE_NAME = (__package__ or __name__).split(".")[0].replace("_", "-")


def initialize_project(options: FlowOptions) -> tuple[str, DocumentList]:
    # TODO: Implement project initialization logic
    return "", DocumentList([])


def main():
    """Main CLI entry point."""
    run_cli(
        flows=FLOWS,
        flow_configs=FLOW_CONFIGS,
        options_cls=ProjectFlowOptions,
        initializer=initialize_project,
        trace_name=TRACE_NAME,
    )


if __name__ == "__main__":
    main()
