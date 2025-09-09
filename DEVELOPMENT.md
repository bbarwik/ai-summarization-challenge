# Development Guide

A production-ready template for building sophisticated AI-powered pipelines using the ai-pipeline-core framework.

## Introduction

This template demonstrates how to build production AI pipelines using ai-pipeline-core. The framework provides a robust foundation for orchestrating multi-agent AI workflows with type safety, immutability, and comprehensive observability.

### Key Framework Features

- **Document-centric architecture** with immutable Pydantic models
- **Type-safe workflow definitions** through FlowConfig validation
- **Built-in retry logic and cost tracking** for LLM operations
- **Unified logging and tracing** with LMNR integration
- **Async-first design** for maximum performance
- **Flow-centric organization** with colocated tasks

### Technology Stack

- **Python 3.12+** (required for modern type hints)
- **ai-pipeline-core>=0.1.14** as the core framework
- **Prefect** for workflow orchestration
- **Pydantic** for data validation
- **httpx** for async HTTP operations

### Project Policy

- **FILES enum**: Prefer FILES enum when filename identity matters across steps; otherwise plain strings are fine.
- **Models**: Always use type `ModelName` for model parameters and variables; always pass models from flow_options (e.g., `flow_options.core_model`).
- **Vision and structured-output**: Assume all models support documents/vision; search models (`*-search`) do not support structured output.

## Quick Start

### Installation

```bash
# Install the package
pip install -e .

# For development
make install-dev
```

### Running the Pipeline

```bash
# Full pipeline with defaults
python -m ai_pipeline ./projects/my_project

# Specific flows (by index, 1-based)
python -m ai_pipeline ./projects/my_project --start 2 --end 3
# Note: --start/--end indices are 1-based in this template's runner
# Example: --start 2 --end 3 runs the 2nd and 3rd flows

# With custom models
python -m ai_pipeline ./projects/my_project \
    --core-model "gpt-5" \
    --small-model "gpt-5-mini"

# Debug mode
LMNR_DEBUG=true python -m ai_pipeline ./projects/my_project
```

## Project Structure

### Flow-Centric Organization

The template follows a flow-centric architecture where each workflow is self-contained:

```
ai_pipeline/
├── documents/                      # Document type definitions
│   ├── flow/                      # Flow documents (persistent across flows)
│   │   └── example_document.py    # ExampleDocument(FlowDocument)
│   └── task/                      # Task documents (temporary within tasks)
│       └── draft_document.py      # DraftDocument(TaskDocument)
│
├── flows/                          # Pipeline flows with colocated tasks
│   ├── __init__.py                # Exports FLOWS and FLOW_CONFIGS lists
│   └── step_01_example/           # Example flow
│       ├── __init__.py
│       ├── example_flow.py        # Flow definition with FlowConfig
│       └── tasks/                 # Flow-specific tasks
│           ├── __init__.py
│           ├── process_task.py    # Task implementation
│           └── process_task.jinja2 # Colocated prompt template (matching name)
│
├── tasks/                         # Shared tasks (used by multiple flows)
│   └── validate/                  # Folder for the validate shared task
│       └── validate.py            # Example shared task
│       └── validate.jinja2        # Prompt used by example shared task
│
├── prompts/                        # Shared prompt templates
│   └── common.jinja2
│
├── flow_options.py                # ProjectFlowOptions configuration
└── __main__.py                    # CLI entry point
```

### Key Organizational Rules

1. **Flow-specific tasks** live in `flows/{flow_name}/tasks/`
2. **Jinja2 templates** are colocated with their task files and MUST have matching names
3. **Shared tasks** (used by 2+ flows) go directly in `tasks/{task_category}` directory
4. **Shared prompts** go in `prompts/` directory
5. **Each flow** is self-contained with all dependencies
6. **flows/__init__.py** must export FLOWS and FLOW_CONFIGS lists
7. **One file = one document class** in `documents/` directory
8. **Pydantic models** used by documents should be defined in the same file

## Core Development Patterns

### Flow Definition Pattern

Every flow follows this exact pattern:

```python
from ai_pipeline_core import DocumentList, FlowConfig, pipeline_flow
from ai_pipeline.flow_options import ProjectFlowOptions
from ai_pipeline.documents.flow import InputDocument, OutputDocument
from .tasks import process_task

class MyFlowConfig(FlowConfig):
    """Configuration for my flow."""

    # CRITICAL: Each flow MUST have a unique OUTPUT_DOCUMENT_TYPE!
    # The OUTPUT_DOCUMENT_TYPE should NOT be in INPUT_DOCUMENT_TYPES
    # to prevent circular dependencies between flows.
    INPUT_DOCUMENT_TYPES = [InputDocument]
    OUTPUT_DOCUMENT_TYPE = OutputDocument  # Must be a different class

@pipeline_flow
async def my_flow(
    project_name: str,
    documents: DocumentList,
    flow_options: ProjectFlowOptions,
) -> DocumentList:
    """Process documents through my flow."""

    # Step 1: Get input documents (validates types automatically)
    input_docs = documents.filter_by(*MyFlowConfig.INPUT_DOCUMENT_TYPES)

    # Step 2: Process with tasks
    # If task returns a document, use it directly
    result_doc = await process_task(
        documents=input_docs,
        model=flow_options.core_model,
    )

    # Step 3: MUST use create_and_validate_output
    # If task returns the correct document type, pass it directly
    return MyFlowConfig.create_and_validate_output([result_doc])
```

### Task Implementation Pattern

Every task follows this structure:

```python
from ai_pipeline_core import (
    AIMessages, DocumentList, ModelName,
    PromptManager, get_pipeline_logger,
    llm, pipeline_task
)

# Module-level initialization (NOT inside functions!)
prompt_manager = PromptManager(__file__)  # Must be at module scope
logger = get_pipeline_logger(__name__)  # Must be at module scope

@pipeline_task  # No parameters!
async def process_task(
    documents: DocumentList,
    model: ModelName,  # NO DEFAULTS! Must come from FlowOptions
) -> AnalysisDocument:
    """Process documents using LLM."""

    # Wrap documents in AIMessages
    messages = AIMessages(documents)

    # For multi-line prompts, use Jinja2 file with matching name
    prompt = prompt_manager.get(
        "process_task",  # Extension optional, MUST match task file name!
        context="specific instructions"
    )

    # For single-line prompts, use inline string
    # prompt = "Analyze this document and provide a summary."

    # Build static context from prompt (cached)
    static_context = AIMessages([prompt])

    # Dynamic per-call content
    dynamic_messages = AIMessages(documents)

    # Call LLM with context and messages split for caching
    result = await llm.generate(
        model=model,
        context=static_context,  # Static instructions (cached)
        messages=dynamic_messages  # Dynamic content
    )

    # Create and return document
    return AnalysisDocument.create(
        name="analysis.json",  # Plain string OK when not used for routing
        content=result.content
    )
```

### Structured Output Pattern

For tasks requiring structured data:

```python
from pydantic import BaseModel, Field
from ai_pipeline_core import (
    AIMessages, DocumentList, ModelName,
    get_pipeline_logger, llm, pipeline_task
)

logger = get_pipeline_logger(__name__)

class AnalysisResult(BaseModel):
    """Structured analysis output."""
    summary: str = Field(description="Executive summary")
    score: int = Field(ge=1, le=10, description="Score")

@pipeline_task
async def structured_analysis(
    documents: DocumentList,
    model: ModelName,  # Always use ModelName type
) -> AnalysisDocument:
    """Generate structured analysis."""

    # Optional: Add prompt for context
    # prompt = "Analyze and score the following content."
    # context = AIMessages([prompt])

    messages = AIMessages(documents)

    # Use generate_structured for type-safe output
    # Note: Search models (*-search) do not support structured output
    result = await llm.generate_structured(
        model=model,
        # context=context,  # Optional static context
        messages=messages,
        response_format=AnalysisResult
    )

    # Access the parsed Pydantic model
    analysis = result.parsed
    logger.debug(f"Analysis score: {analysis.score}")  # Use debug for logging

    return AnalysisDocument.create(
        name="analysis.json",
        content=analysis  # Pass BaseModel directly, no model_dump()!
    )
```

## Document System

### Document Type Hierarchy

```python
from enum import StrEnum
from ai_pipeline_core import FlowDocument, TaskDocument

# Flow documents persist across flows
# One file = one document class rule
class AnalysisDocument(FlowDocument):
    """Analysis results that flow between pipeline stages."""

    class FILES(StrEnum):
        """Only add file names that are actually used."""
        ANALYSIS = "analysis.json"  # Only add what you need

# Task documents are temporary within tasks
class DraftDocument(TaskDocument):
    """Temporary draft used during processing."""
    pass
```

### Document Operations

```python
# PREFERRED: Use FILES enum when filename identity matters
doc = AnalysisDocument.create(
    name=AnalysisDocument.FILES.ANALYSIS,
    content=data
)

# ALSO OK: Plain strings when filename not used for routing
doc = AnalysisDocument.create(
    name="analysis.json",  # OK if not referenced elsewhere
    content={"key": "value"}
)

# DocumentList operations
analysis_docs = documents.filter_by(AnalysisDocument)
specific_doc = documents.get_by(AnalysisDocument.FILES.ANALYSIS)

# Plain string OK when filename not used downstream for routing
optional_doc = documents.get_by("optional.txt", required=False)
```

## Configuration

### Flow Options

```python
# ai_pipeline/flow_options.py
from ai_pipeline_core import FlowOptions, ModelName
from pydantic import Field

class ProjectFlowOptions(FlowOptions):
    """Project-specific flow configuration."""

    # Override defaults from base class if needed
    core_model: ModelName = Field(default="gpt-5")
    small_model: ModelName = Field(default="gpt-5-mini")

    # ONLY add project-specific fields if explicitly required
    # Don't add fields unless the project needs them
```

### CLI Entry Point

The template includes a ready-to-use CLI:

```python
# ai_pipeline/__main__.py
from ai_pipeline_core import DocumentList, FlowOptions
from ai_pipeline_core.simple_runner import run_cli
from .flow_options import ProjectFlowOptions
from .flows import FLOW_CONFIGS, FLOWS

TRACE_NAME = "ai-pipeline"

def initialize_project(options: FlowOptions) -> tuple[str, DocumentList]:
    # TODO: Implement project initialization
    return "", DocumentList([])

def main():
    run_cli(
        flows=FLOWS,
        flow_configs=FLOW_CONFIGS,
        options_cls=ProjectFlowOptions,
        initializer=initialize_project,
        trace_name=TRACE_NAME,
    )
```

## Development

### Essential Commands

```bash
# Development setup
make install-dev         # Install with dev dependencies and pre-commit hooks

# Code Quality
make lint               # Run ruff linting
make format            # Auto-format and fix code
make typecheck         # Run basedpyright type checking
make pre-commit        # Run all pre-commit hooks

# Testing
make test               # Run all tests
make test-cov          # Run tests with coverage report
pytest -m "not integration"  # Skip integration tests

# Cleanup
make clean             # Remove all build artifacts and caches
```

### Testing Strategy

```python
import pytest
from ai_pipeline_core import DocumentList
from ai_pipeline.documents.flow import SampleDocument
from ai_pipeline.flows.step_01_example.tasks import process_task

@pytest.mark.asyncio
async def test_process_task():
    """Test processing task."""
    # Arrange
    sample_doc = SampleDocument.create(
        name="sample.txt",
        content="Sample data"
    )
    documents = DocumentList([sample_doc])

    # Use FlowOptions for model selection
    from ai_pipeline.flow_options import ProjectFlowOptions
    options = ProjectFlowOptions()

    # Act
    result = await process_task(
        documents=documents,
        model=options.small_model,  # ModelName from FlowOptions
    )

    # Assert
    assert isinstance(result, SampleDocument)
    assert "processed" in result.content.lower()
```

## Best Practices

### Import Rules

```python
# CORRECT: Import from top-level ai_pipeline_core
from ai_pipeline_core import (
    FlowDocument, DocumentList,
    pipeline_task, pipeline_flow,
    llm, AIMessages
)

# WRONG: Never import from submodules
from ai_pipeline_core.llm import generate  # NO!
from ai_pipeline_core.documents import FlowDocument  # NO!

# NEVER use parent imports (..)
# NEVER use lazy imports or if TYPE_CHECKING
# NEVER use try/except for imports - no optional imports
```

### Context vs Messages Split

**Important**: Split static and dynamic content for caching benefits:
- **context**: Static instructions, schemas, examples (cached by LLM provider)
- **messages**: Per-call dynamic data (not cached)

This pattern reduces token usage and costs through provider caching.

### Common Patterns

1. **Always use `create_and_validate_output()`** at the end of flows
2. **Never specify default models in tasks** - pass from FlowOptions
3. **Initialize PromptManager at module level**, not in functions
4. **Wrap documents in AIMessages** for LLM calls
5. **Use DocumentList default constructor** unless validation needed
6. **Colocate templates with tasks** with matching file names
7. **No 'Test' prefix for Document subclasses** - conflicts with pytest
8. **If task returns correct document type**, use it directly (don't recreate)
9. **Each flow must have unique OUTPUT_DOCUMENT_TYPE** class
10. **Use debug level for logging**, avoid meaningless logs
11. **Only add FlowOptions fields** that are explicitly needed

## Environment Variables

```bash
# Required for LLM operations
OPENAI_BASE_URL=http://localhost:4000  # API endpoint (eg. openrouter)
OPENAI_API_KEY=sk-...                  # API key

# Optional
PREFECT_API_URL=http://localhost:4200  # Prefect server
LMNR_PROJECT_API_KEY=lmnr_...          # Observability
LMNR_DEBUG=false                       # Debug tracing
```

## Getting Help

- Review `dependencies_docs/ai-pipeline-core.md` for framework details
- Check the test suite for usage examples
- Follow patterns in existing flows and tasks

## License

MIT
