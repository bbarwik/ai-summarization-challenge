"""CLI entry point for ai-summarization."""

import os
import sys

from ai_pipeline_core.simple_runner import run_cli

from .flow_options import ProjectFlowOptions
from .flows import FLOWS

TRACE_NAME = (__package__ or __name__).split(".")[0].replace("_", "-")


def main():
    """Main CLI entry point."""
    args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]
    if len(args) == 0 and os.path.exists("workspace/input"):
        sys.argv.append("workspace")
    run_cli(
        flows=FLOWS,
        options_cls=ProjectFlowOptions,
        trace_name=TRACE_NAME,
    )


if __name__ == "__main__":
    main()
