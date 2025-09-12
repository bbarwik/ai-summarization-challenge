# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

ai-summarization is an AI-powered document summarization project built with the ai-pipeline-core framework, providing async AI pipeline orchestration with strong typing and efficient batch processing. This project processes ~200k tokens of research documents about AI assistant companies into a comprehensive report.

### Key Components
- **ai-pipeline-core**: The foundational framework providing async AI pipeline orchestration
- **Prefect**: Workflow orchestration for managing pipelines (accessed via pipeline decorators)
- **FlowOptions**: Configuration system for model selection and flow parameters
- **4-Stage Pipeline**: Planning → Writing → Review → Rewrite flows for document processing

### Technology Stack
- **Python 3.12+** (required for modern type hints)
- **ai-pipeline-core>=0.2.0** as the core framework (v0.2.0 introduces mandatory FlowConfig)
- **Pydantic** for data validation and immutable models
- **httpx** for async HTTP operations (never use requests)

## Project Structure

### Flow-Centric Organization

The project follows a flow-centric architecture where each workflow is self-contained with its tasks and templates.

**Note**: The examples below show the general structure. Actual implementations may vary based on project needs.

```
ai_summarization/
├── documents/                      # Document type definitions
│   ├── flow/                      # Flow documents (persistent across flows)
│   │   └── example_document.py    # ExampleDocument(FlowDocument)
│   └── task/                      # Task documents (temporary within tasks)
│       └── draft_document.py      # DraftDocument(TaskDocument)
│
├── flows/                          # Pipeline flows with colocated tasks
│   ├── __init__.py                # MUST export FLOWS and FLOW_CONFIGS lists
│   └── step_01_example/           # Example flow
│       ├── __init__.py
│       ├── example_flow.py        # Flow definition with FlowConfig
│       └── tasks/                 # Flow-specific tasks
│           ├── __init__.py
│           ├── process_task.py    # Task implementation
│           └── process_task.jinja2  # Colocated prompt template (matching name)
│
├── tasks/                          # Shared tasks (used by multiple flows)
│   └── validate.py                # Example shared task
│
├── prompts/                        # Shared prompt templates
│   └── common.jinja2
│
├── flow_options.py                # ProjectFlowOptions extends FlowOptions
└── __main__.py                    # CLI entry point with run_cli
```

### Key Organizational Rules

1. **Flow-specific tasks** live in `flows/{flow_name}/tasks/`
2. **Jinja2 templates** are colocated with their task files and MUST have matching names (e.g., `process_task.py` with `process_task.jinja2`)
3. **Shared tasks** (used by 2+ flows) go directly in `tasks/` directory (e.g., `tasks/validate.py`)
4. **Shared prompts** go in `prompts/` directory
5. **Each flow** is self-contained with all dependencies
6. **flows/__init__.py** MUST export FLOWS list
7. **One file = one document class** in `documents/` directory
8. **Pydantic models** used by documents should be defined in the same file

## Project Policy

### Model and Document Conventions

- **FILES enum**: Use FILES enum when filename identity matters across steps. Documents that accept any file (like InputDocument) don't need FILES enum since filenames aren't pre-defined.
- **Models**: Always use type `ModelName` for model parameters and variables; always pass models coming from flow_options (e.g., `flow_options.core_model`).
- **Vision and structured-output**: Assume all models support documents/vision; search models (`*-search`) do not support structured output.
- **FlowOptions fields**: The `task_description` field in ProjectFlowOptions is project-specific and appropriate for this AI summarization task.

## Core Principles

### 1. Minimalism Above All

Every line of code must justify its existence:

```python
# BAD: Defensive programming for unlikely scenarios
def process_data(data: list[str]) -> str:
    if not data:
        return "No data provided"  # Unnecessary defense
    if len(data) > 1000:
        raise ValueError("Too much data")  # Over-engineering

# GOOD: Trust the types and framework
def process_data(data: list[str]) -> str:
    return "\n".join(data)  # Simple and clear
```

### 2. Everything Async

ALL I/O operations must be async - no blocking calls allowed:

```python
# BAD: Blocking I/O
import requests
import time

def fetch_data(url: str) -> dict:
    response = requests.get(url)  # BLOCKING!
    time.sleep(1)  # BLOCKING!
    return response.json()

# GOOD: Async I/O
import httpx
import asyncio

async def fetch_data(url: str) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        await asyncio.sleep(1)
        return response.json()
```

### 3. Strong Typing with Pydantic

Every data structure must be a Pydantic model with complete type hints:

```python
from pydantic import BaseModel, Field
from pydantic import ConfigDict

class ResearchPlan(BaseModel):
    """Immutable research plan model."""
    model_config = ConfigDict(frozen=True)

    queries: list[str] = Field(description="Search queries")
    max_depth: int = Field(default=2, ge=1, le=5)
```

### 4. Self-Documenting Code

Code must be clear without comments:

```python
# BAD: Unclear naming
def proc(d):
    r = []
    for i in d:
        if i > 0:
            r.append(i * 2)
    return r

# GOOD: Self-documenting
def double_positive_numbers(numbers: list[int]) -> list[int]:
    return [num * 2 for num in numbers if num > 0]
```

## Critical Import Rules

### Required Import Restrictions

**CRITICAL**: The following imports are banned and must use ai_pipeline_core wrappers:

```python
# BANNED: Direct imports
import logging  # ❌
from prefect import task, flow  # ❌
from lmnr import trace  # ❌
from prefect.logging import get_logger  # ❌

# CORRECT: Import from TOP LEVEL ai_pipeline_core ONLY
from ai_pipeline_core import get_pipeline_logger  # ✅
from ai_pipeline_core import pipeline_task, pipeline_flow  # ✅
from ai_pipeline_core import FlowDocument, TaskDocument  # ✅
from ai_pipeline_core import llm, AIMessages  # ✅
from ai_pipeline_core import disable_run_logger  # ✅ For testing
from ai_pipeline_core import prefect_test_harness  # ✅ For testing
```

These restrictions are enforced by ruff linting rules in `pyproject.toml`.

### Import Convention

```python
# Within same package - relative imports
from .document import Document
from .utils import helper

# Cross-package - absolute imports from TOP LEVEL ONLY
from ai_pipeline_core import FlowDocument, DocumentList
from ai_pipeline_core import llm, AIMessages

# NEVER use parent imports (..)
# NEVER import from submodules like ai_pipeline_core.llm
# NEVER use lazy imports or if TYPE_CHECKING
# NEVER use try/except for imports - no optional imports allowed
```

### No Optional Imports Pattern

```python
# BAD: Optional imports with try/except
try:
    import optional_library
    HAS_OPTIONAL = True
except ImportError:
    HAS_OPTIONAL = False

# BAD: Conditional imports
if TYPE_CHECKING:
    from typing import SomeType

# GOOD: All imports are required
from required_library import function
from ai_pipeline_core import FlowDocument
```

## Flow Development Pattern

### Flow Definition (MUST follow exactly)

```python
# NOTE: These are example patterns. Actual implementation details may vary.
from ai_pipeline_core import DocumentList, FlowConfig, pipeline_flow
from ai_summarization.flow_options import ProjectFlowOptions
from ai_summarization.documents.flow import InputDocument, PlanDocument
from .tasks import planning_task

class PlanningFlowConfig(FlowConfig):
    """Configuration for planning flow."""

    # CRITICAL: Each flow MUST have a unique OUTPUT_DOCUMENT_TYPE!
    # The OUTPUT_DOCUMENT_TYPE should NOT be in INPUT_DOCUMENT_TYPES
    # to prevent circular dependencies between flows.
    INPUT_DOCUMENT_TYPES = [InputDocument]
    OUTPUT_DOCUMENT_TYPE = PlanDocument  # Must be a different class

@pipeline_flow(config=PlanningFlowConfig)  # Config parameter is REQUIRED in v0.2.0+
async def planning_flow(
    project_name: str,
    documents: DocumentList,
    flow_options: ProjectFlowOptions,
) -> DocumentList:
    """Process documents through planning flow."""

    # STEP 1: Validate and get input documents
    input_docs = documents.filter_by(*PlanningFlowConfig.INPUT_DOCUMENT_TYPES)

    # STEP 2: Process with tasks
    # If task returns a document, use it directly
    result_doc = await planning_task(
        documents=input_docs,
        model=flow_options.core_model,  # Pass models from flow_options
        task_description=flow_options.task_description,  # Project-specific field
    )

    # STEP 3: MUST use create_and_validate_output
    # If task returns the correct document type, pass it directly
    return PlanningFlowConfig.create_and_validate_output([result_doc])
```

### Flow Registration (flows/__init__.py)

```python
# Example from actual ai-summarization project
from .step_01_planning import planning_flow
from .step_02_writing import writing_flow
from .step_03_review import review_flow
from .step_04_rewrite import rewrite_flow

# MUST export FLOWS list (v0.2.0+ configs are attached via decorators)
FLOWS = [planning_flow, writing_flow, review_flow, rewrite_flow]

__all__ = ["FLOWS"]
```

## Task Development Pattern

### Context vs Messages Split

**Important**: Split static and dynamic content for caching benefits:
- **context**: Static context like schemas, examples, or persistent configuration (sent first to LLM, cached by provider)
- **messages**: Dynamic content including the main prompt and per-call data (sent after context)

In practice, the prompt often goes in messages while static instructions go in context. This pattern reduces token usage and costs through provider caching.

### Logging Guidelines

1. **Use debug level** for custom logging: `logger.debug("message")`
2. **Avoid meaningless logs** like "Starting task" or "Completed" - tasks have built-in logging
3. **Only log important information** that helps with debugging
4. **Tasks and flows automatically log** their start/end, no need to add these

### Prompt File Guidelines

1. **Single-line prompts**: Use inline strings directly in Python
2. **Multi-line prompts**: Use Jinja2 files with matching names
3. **File naming**: `process_task.py` MUST use `process_task.jinja2` (matching names)
4. **One prompt per task**: Each task should have at most one Jinja2 template
5. **Extension optional**: PromptManager.get("process_task") searches with/without extension

### Basic Task Pattern

```python
from ai_pipeline_core import (
    AIMessages, DocumentList, ModelName,
    PromptManager, get_pipeline_logger,
    llm, pipeline_task
)

# Module-level initialization (NOT in functions!)
prompt_manager = PromptManager(__file__)
logger = get_pipeline_logger(__name__)

@pipeline_task  # No parameters!
async def process_task(
    documents: DocumentList,
    model: ModelName,  # NO DEFAULTS! Must come from FlowOptions
) -> AnalysisDocument:
    """Process documents using LLM."""

    # For multi-line prompts, use Jinja2 file with matching name
    prompt = prompt_manager.get(
        "process_task",  # Extension optional, MUST match task file name!
        task_description="specific task requirements"
    )

    # For single-line prompts, use inline string
    # prompt = "Analyze this document and provide a summary."

    # Build messages from prompt and documents
    # NOTE: In practice, prompt often goes in messages (dynamic)
    # while static schemas/examples go in context
    messages = AIMessages([prompt] + documents.to_list())

    # Optional: Static context for schemas/examples (cached)
    # context = AIMessages([static_schema])  # If you have static content

    # Call LLM
    result = await llm.generate(
        model=model,
        # context=context,  # Optional: static content (sent first, cached)
        messages=messages  # Dynamic prompt and documents
    )

    # Create and return document
    return AnalysisDocument.create(
        name="analysis.json",  # Plain string OK when not used for routing
        content=result.content
    )
```

### Structured Output Pattern

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
    score: int = Field(ge=1, le=10)

@pipeline_task
async def structured_analysis(
    documents: DocumentList,
    model: ModelName,  # Always use ModelName type
) -> AnalysisDocument:
    """Generate structured analysis."""

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
    analysis = result.parsed  # Type: AnalysisResult
    logger.debug(f"Analysis score: {analysis.score}")  # Use debug for logging

    return AnalysisDocument.create(
        name="analysis.json",
        content=analysis  # Pass BaseModel directly, no model_dump()!
    )
```

### Parallel Execution Pattern

```python
import asyncio

@pipeline_flow(config=ParallelFlowConfig)
async def parallel_flow(
    project_name: str,
    documents: DocumentList,
    flow_options: ProjectFlowOptions,
) -> DocumentList:
    input_docs = documents.filter_by(*ParallelFlowConfig.INPUT_DOCUMENT_TYPES)

    # Run tasks in parallel
    results = await asyncio.gather(
        task_one(documents=input_docs, model=flow_options.core_model),
        task_two(documents=input_docs, model=flow_options.small_model),
        task_three(documents=input_docs, model=flow_options.core_model),
    )

    return ParallelFlowConfig.create_and_validate_output(results)
```

## Document System

### Document Organization Rules

1. **One file = one document class** - Each .py file should contain exactly one document class
2. **Pydantic models in same file** - If a document uses a Pydantic model, define it in the same file
3. **FILES enum only what's needed** - Only add file names that are actually used
4. **Proper __init__.py exports** - Each directory needs proper imports and exports

### __init__.py Examples

```python
# documents/__init__.py - Example
from .flow import InputDocument, PlanDocument, DraftDocument, ReviewDocument, OutputDocument
# Note: task/ directory may be empty if no task-scoped documents are used

__all__ = ["InputDocument", "PlanDocument", "DraftDocument", "ReviewDocument", "OutputDocument"]
```

```python
# documents/flow/__init__.py - Example from ai-summarization
from .input_document import InputDocument
from .plan_document import PlanDocument
from .draft_document import DraftDocument
from .review_document import ReviewDocument
from .output_document import OutputDocument

__all__ = ["InputDocument", "PlanDocument", "DraftDocument", "ReviewDocument", "OutputDocument"]
```

```python
# flows/step_01_planning/__init__.py - Example
from .planning_flow import PlanningFlowConfig, planning_flow

__all__ = ["PlanningFlowConfig", "planning_flow"]
```

```python
# flows/step_01_planning/tasks/__init__.py - Example
from .create_plan_task import create_plan_task

__all__ = ["create_plan_task"]
```

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

# If document uses Pydantic model, define it in same file
class AnalysisData(BaseModel):
    """Data structure for analysis document."""
    summary: str
    score: int

# Task documents are temporary within tasks
class DraftDocument(TaskDocument):
    """Temporary draft used during processing."""
    pass
```

### Document Creation Patterns

```python
# CORRECT: Use create() for automatic conversion
doc = AnalysisDocument.create(
    name="analysis.json",
    content={"key": "value"}  # Auto-converts to JSON bytes
)

# PREFERRED: Use FILES enum when filename identity matters
doc = AnalysisDocument.create(
    name=AnalysisDocument.FILES.ANALYSIS,
    content=data
)

# ALSO OK: Plain strings when filename not used for routing
doc = AnalysisDocument.create(
    name="analysis.json",  # OK if not referenced elsewhere
    content=data
)

# Creating from Pydantic model
model = MyModel(field="value")
doc = MyDocument.create(
    name="data.json",
    content=model  # Direct BaseModel support
)

# Round-trip with Pydantic
restored = doc.as_pydantic_model(MyModel)
```

### DocumentList Operations

```python
# Filter by type (returns DocumentList)
analysis_docs = documents.filter_by(AnalysisDocument)

# Get specific document (raises if not found by default)
doc = documents.get_by(AnalysisDocument.FILES.ANALYSIS)

# Optional get (returns None if not found)
doc = documents.get_by("optional.txt", required=False)
# Plain string OK here because filename is not used downstream for routing
if doc is not None:
    process(doc)

# Create DocumentList (use default constructor)
docs = DocumentList([doc1, doc2])  # No validation flags needed
```

## Configuration

### FlowOptions Pattern

```python
# ai_summarization/flow_options.py
from ai_pipeline_core import FlowOptions, ModelName
from pydantic import Field

class ProjectFlowOptions(FlowOptions):
    """Project-specific flow configuration."""

    # Override defaults from base class if needed
    core_model: ModelName = Field(default="gpt-5")
    small_model: ModelName = Field(default="gpt-5-mini")

    # Project-specific fields are allowed when needed for the task
    # Example: task_description for AI summarization project
    task_description: str = Field(
        default="...",  # Project-specific task description
        description="Main task for report generation"
    )
```

### CLI Entry Point

```python
# ai_summarization/__main__.py
from ai_pipeline_core import DocumentList, FlowOptions
from ai_pipeline_core.simple_runner import run_cli
from .flow_options import ProjectFlowOptions
from .flows import FLOWS

TRACE_NAME = "ai-summarization"

def initialize_project(options: FlowOptions) -> tuple[str, DocumentList]:
    # Initialize project with input documents
    # This is optional - can be omitted if not needed
    return "workspace", DocumentList([])

def main():
    run_cli(
        flows=FLOWS,  # Flow configs are now attached via decorators in v0.2.0+
        options_cls=ProjectFlowOptions,
        initializer=initialize_project,  # Optional parameter
        trace_name=TRACE_NAME,
    )

if __name__ == "__main__":
    main()
```

## Testing Patterns

### Test Fixtures (conftest.py)

```python
import pytest
from ai_pipeline_core import disable_run_logger, prefect_test_harness

@pytest.fixture(autouse=True, scope="session")
def prefect_test_fixture():
    """Isolate tests from main Prefect database."""
    with prefect_test_harness():
        yield

@pytest.fixture(autouse=True, scope="session")
def disable_prefect_logging():
    """Prevent RuntimeError from missing flow context."""
    with disable_run_logger():
        yield
```

### Unit Test Pattern

```python
import pytest
from ai_pipeline_core import DocumentList
from ai_summarization.documents.flow import SampleDocument
from ai_summarization.flows.step_01_example.tasks import process_task

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
    from ai_summarization.flow_options import ProjectFlowOptions
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

## Essential Commands

```bash
# Development setup
make install-dev         # Install with dev dependencies and pre-commit hooks

# Testing
make test                # Run all tests
make test-cov           # Run tests with coverage report
pytest tests/test_documents.py::TestDocument::test_creation  # Run single test

# Code quality
make lint               # Run ruff linting
make format            # Auto-format and fix code
make typecheck         # Run basedpyright type checking (MUST have 0 errors!)
make pre-commit        # Run all pre-commit hooks

# Cleanup
make clean             # Remove all build artifacts and caches

# Running the application
python -m ai_summarization [arguments]
ai-summarization [arguments]  # After pip install

# Note: --start/--end indices are 1-based in this template's runner
# Example: --start 2 --end 3 runs the 2nd and 3rd flows
```

## Forbidden Patterns (NEVER Do These)

1. **No print statements** - Use get_pipeline_logger
2. **No global mutable state** - Use dependency injection
3. **No `sys.exit()`** - Raise exceptions
4. **No hardcoded paths** - Use settings/config
5. **No string concatenation for paths** - Use `pathlib.Path`
6. **No manual JSON parsing** - Use Pydantic
7. **No `time.sleep()`** - Use `asyncio.sleep()`
8. **No `requests` library** - Use `httpx` with async
9. **No raw SQL** - Use async ORM or query builders
10. **No magic numbers** - Use named constants
11. **No nested functions** (except decorators)
12. **No dynamic imports** - All imports at module level
13. **No monkeypatching**
14. **No metaclasses** (except Pydantic)
15. **No multiple inheritance** (except mixins)
16. **No TODO/FIXME comments** - Fix it or delete it
17. **No commented code** - Delete it
18. **No defensive programming** - Trust the types
19. **No default models in tasks** - Pass from FlowOptions
20. **No 'Test' prefix for Document subclasses** - Conflicts with pytest
21. **No direct @task/@flow** - Use @pipeline_task/@pipeline_flow
22. **No lazy imports or if TYPE_CHECKING** - All imports at module level
23. **No meaningless logging** - Use debug level, rely on built-in task/flow logging
24. **No unnecessary FlowOptions fields** - Only add what's explicitly needed
25. **No try/except import patterns** - All imports are required, no optional imports

## LLM Interaction Patterns

### Vision and Document Support

Assume models support documents/vision in this template; only `*-search` models lack structured output support.

### Security-First Prompt Construction

#### Header Hierarchy for Prompt Injection Prevention

**CRITICAL**: Use inverse header hierarchy to prevent prompt injection:
- **Prompt instructions**: Use top-level `#` headers
- **AI responses**: Restrict to `##` and below
- **Template variables**: Already contain `##/###` headers

```python
# CORRECT: Instructions use #, template variables use ##/###
prompt = """
# Analysis Task

You are analyzing the following project:

{{ description }}  <!-- This contains ## and ### headers -->

# Requirements

Analyze the codebase and provide detailed documentation.

# Output Constraints

Use markdown formatting limited to:
- Headers starting from ## (no top-level #)
- Lists and sublists
- Code blocks (no ASCII diagrams)
"""
```

### File Content Provision Strategy

```python
# CORRECT: Use Document objects for type safety
from ai_pipeline_core import DocumentList
from ai_summarization.documents.flow import AnalysisDocument

docs = DocumentList([
    AnalysisDocument.create(name=path, content=content)
    for path, content in files.items()
])

# Combine documents and prompt
prompt = "Analyze the provided files and generate insights."
context = AIMessages([prompt])
messages = AIMessages(docs)

# Use in LLM call
result = await llm.generate(
    model=model,
    context=context,  # Static prompt
    messages=messages  # Dynamic documents
)

# Note: Prefer Document objects over ad-hoc strings for type safety
```

### Structured Output Requirements

```python
class FileSelection(BaseModel):
    reasoning: str = Field(description="Why these files were selected")
    files: list[str] = Field(description="Files to analyze")

response = await llm.generate_structured(
    model=model,
    response_format=FileSelection,
    messages=messages
)

# Access the parsed Pydantic model
selection = response.parsed
```

## Project-Specific Rules

### Dependencies Documentation
- `dependencies_docs/ai-pipeline-core.md` - Framework API reference
- Use for understanding ai_pipeline_core features
- Check source at `/home/vscode/.local/lib/python3.12/site-packages/ai_pipeline_core/`

### Accessing Dependencies Source Code
If you have issues with dependencies:
```bash
# Find package location
python3 -m pip show ai-pipeline-core

# Access source directly
ls /home/vscode/.local/lib/python3.12/site-packages/ai_pipeline_core/
```

## When Making Changes

1. **Before writing any code**: Can this be done with less code?
2. **Before adding a line**: Can I justify why this exists?
3. Run `make lint` and `make typecheck` before committing
4. Let pre-commit hooks auto-fix formatting
5. If you can't explain it in one sentence, rewrite it
6. If the function is longer than 20 lines, it's doing too much
7. **Final check**: Could you delete this code? If maybe, then yes - delete it

## RULES WHICH MUST BE FOLLOWED

- Do what has been asked; nothing more, nothing less
- NEVER create files unless they're absolutely necessary
- ALWAYS prefer editing an existing file to creating a new one
- NEVER proactively create documentation files (*.md) or README files
- Always validate python code with basedpyright (0 errors required!)
- If you have issues with 3rd party dependencies, check the source code directly
- Always use module-level PromptManager and logger initialization
- Never combine @pipeline_task/@pipeline_flow with @trace
- Always use @pipeline_flow with config parameter (REQUIRED in v0.2.0+)
- Always use create_and_validate_output() at the end of flows
- Never specify default models in tasks - pass from FlowOptions
- Always wrap documents in AIMessages for LLM calls
- FILES enum is for pre-defined filenames; documents accepting any file don't need it
- Document subclasses should NOT start with 'Test' prefix (pytest conflict)
- If task returns the correct document type, use it directly (don't recreate)
- Each flow must have a unique OUTPUT_DOCUMENT_TYPE class
- Prompt files must match task file names exactly
- Use debug level for logging, avoid meaningless logs
- Project-specific FlowOptions fields are acceptable when needed (e.g., task_description)
- All imports are required - no try/except import patterns
- Context is for static content (sent first), messages for dynamic content including prompts
- The initializer parameter in run_cli is optional
- Examples in documentation are illustrative and may differ from actual implementation

## Final Rule

**The best code is no code. The second best is minimal, clear, typed, async code that does exactly what's needed and nothing more.**

If you're unsure whether to add code, don't add it.
