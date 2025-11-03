# ai-pipeline-core API Reference

This document is automatically generated using `make docs-build`. Do not manually edit this file.

## Navigation Guide

**For Humans:**
- Use `grep -n '^##' API.md` to list all main sections with line numbers
- Use `grep -n '^###' API.md` to list all classes and functions
- Use `grep -n '^####' API.md` to list all methods and properties
- Search for specific features: `grep -n -i "ClassName" API.md` or `grep -n -i "function_name" API.md`

**For AI Assistants:**
- Use the Grep tool with pattern `^##` to list all module sections (e.g., `^## ai_pipeline_core.module`)
- Use pattern `^###` to find all classes and functions (e.g., `### ClassName`, `### function_name`)
- Use pattern `^####` to find all methods (e.g., `#### ClassName.method_name`)
- For specific lookups, use patterns like `class AIMessages` or `def generate` with output_mode="content" and -n=true for line numbers
- Use -C flag (context lines) to see surrounding content: `pattern="AIMessages", -C=5`
- Navigate directly to line numbers using Read tool with offset parameter once you know the location


## ai_pipeline_core

AI Pipeline Core - Production-ready framework for building AI pipelines with LLMs.

AI Pipeline Core is a high-performance async framework for building type-safe AI pipelines.
It combines document processing, LLM integration, and workflow orchestration into a unified
system designed for production use.

The framework enforces best practices through strong typing (Pydantic), automatic retries,
and cost tracking. All I/O operations are async for maximum throughput.

**CRITICAL IMPORT RULE**:
Always import from the top-level package:
**CORRECT**:
from ai_pipeline_core import llm, pipeline_flow, FlowDocument, DocumentList

**WRONG** - Never import from submodules:
from ai_pipeline_core.llm import generate  # NO!
from ai_pipeline_core.documents import FlowDocument  # NO!

FRAMEWORK RULES (Use by default, unless instructed otherwise):
1. Decorators: Use @pipeline_task WITHOUT parameters, @pipeline_flow WITH config
2. Logging: Use get_pipeline_logger(__name__) - NEVER print() or logging module
3. LLM calls: Use AIMessages or str. Wrap Documents in AIMessages; do not call .text yourself
4. Options: DO NOT use options parameter - omit it entirely (defaults are optimal)
5. Documents: Create with just name and content - skip description unless needed
6. FlowConfig: OUTPUT_DOCUMENT_TYPE must differ from all INPUT_DOCUMENT_TYPES
7. Initialization: PromptManager and logger at module scope, not in functions
8. DocumentList: Use default constructor - no validation flags needed
9. setup_logging(): Only in application main(), never at import time

Messages parameter type: AIMessages or str. Do not pass Document or DocumentList directly.

Core Capabilities:
- **Document Processing**: Type-safe handling of text, JSON, YAML, PDFs, and images
- **LLM Integration**: Unified interface to any model via LiteLLM with caching
- **Structured Output**: Type-safe generation with Pydantic model validation
- **Workflow Orchestration**: Prefect-based flows and tasks with retries
- **Observability**: Built-in monitoring and debugging capabilities
- **Local Development**: Simple runner for testing without infrastructure

Quick Start:
>>> from ai_pipeline_core import (
...     pipeline_flow, FlowDocument, DocumentList, FlowOptions, FlowConfig, llm, AIMessages
... )
>>>
>>> class OutputDoc(FlowDocument):
...     '''Analysis result document.'''
>>>
>>> class MyFlowConfig(FlowConfig):
...     INPUT_DOCUMENT_TYPES = []
...     OUTPUT_DOCUMENT_TYPE = OutputDoc
>>>
>>> @pipeline_flow(config=MyFlowConfig)
>>> async def analyze_flow(
...     project_name: str,
...     documents: DocumentList,
...     flow_options: FlowOptions
... ) -> DocumentList:
...     # Messages accept AIMessages or str. Wrap documents: AIMessages([doc])
...     response = await llm.generate(
...         "gpt-5",
...         messages=AIMessages([documents[0]])
...     )
...     result = OutputDoc.create(
...         name="analysis.txt",
...         content=response.content
...     )
...     return DocumentList([result])

Environment Variables (when using LiteLLM proxy):
- OPENAI_BASE_URL: LiteLLM proxy endpoint (e.g., http://localhost:4000)
- OPENAI_API_KEY: API key for LiteLLM proxy

Note: LiteLLM proxy uses OpenAI-compatible API format, hence the OPENAI_*
variable names are correct regardless of which LLM provider you're using.

Optional Environment Variables:
- PREFECT_API_URL: Prefect server for orchestration
- PREFECT_API_KEY: Prefect API authentication key
- LMNR_PROJECT_API_KEY: Laminar (LMNR) API key for tracing
- LMNR_DEBUG: Set to "true" to enable debug-level traces


## ai_pipeline_core.exceptions

Exception hierarchy for AI Pipeline Core.

This module defines the exception hierarchy used throughout the AI Pipeline Core library.
All exceptions inherit from PipelineCoreError, providing a consistent error handling interface.

### PipelineCoreError

```python
class PipelineCoreError(Exception)
```

Base exception for all AI Pipeline Core errors.

### DocumentError

```python
class DocumentError(PipelineCoreError)
```

Base exception for document-related errors.

### DocumentValidationError

```python
class DocumentValidationError(DocumentError)
```

Raised when document validation fails.

### DocumentSizeError

```python
class DocumentSizeError(DocumentValidationError)
```

Raised when document content exceeds MAX_CONTENT_SIZE limit.

### DocumentNameError

```python
class DocumentNameError(DocumentValidationError)
```

Raised when document name contains invalid characters or patterns.

### LLMError

```python
class LLMError(PipelineCoreError)
```

Raised when LLM generation fails after all retries.

### PromptError

```python
class PromptError(PipelineCoreError)
```

Base exception for prompt template errors.

### PromptRenderError

```python
class PromptRenderError(PromptError)
```

Raised when Jinja2 template rendering fails.

### PromptNotFoundError

```python
class PromptNotFoundError(PromptError)
```

Raised when prompt template file is not found in search paths.

### MimeTypeError

```python
class MimeTypeError(DocumentError)
```

Raised when MIME type detection or validation fails.


## ai_pipeline_core.llm.model_response

Model response structures for LLM interactions.

Provides enhanced response classes that use OpenAI-compatible base types via LiteLLM
with additional metadata, cost tracking, and structured output support.

### ModelResponse

```python
class ModelResponse(ChatCompletion)
```

Response wrapper for LLM text generation.

Primary usage is adding to AIMessages for multi-turn conversations:

>>> response = await llm.generate("gpt-5", messages=messages)
>>> messages.append(response)  # Add assistant response to conversation
>>> print(response.content)  # Access generated text

The two main interactions with ModelResponse:
1. Adding to AIMessages for conversation flow
2. Accessing .content property for the generated text

Almost all use cases are covered by these two patterns. Advanced features
like token usage and cost tracking are available but rarely needed.

**Example**:

  >>> from ai_pipeline_core import llm, AIMessages
  >>>
  >>> messages = AIMessages(["Explain quantum computing"])
  >>> response = await llm.generate("gpt-5", messages=messages)
  >>>
  >>> # Primary usage: add to conversation
  >>> messages.append(response)
  >>>
  >>> # Access generated text
  >>> print(response.content)

**Notes**:

  Inherits from OpenAI's ChatCompletion for compatibility.
  Other properties (usage, model, id) should only be accessed
  when absolutely necessary.

#### ModelResponse.content

```python
@property
def content(self) -> str
```

Get the generated text content.

Primary property for accessing the LLM's response text.
This is the main property you'll use with ModelResponse.

**Returns**:

  Generated text from the model, or empty string if none.

**Example**:

  >>> response = await generate("gpt-5", messages="Hello")
  >>> text = response.content  # The generated response
  >>>
  >>> # Common pattern: add to messages then use content
  >>> messages.append(response)
  >>> if "error" in response.content.lower():
  ...     # Handle error case

#### ModelResponse.reasoning_content

```python
@property
def reasoning_content(self) -> str
```

Get the reasoning content.

**Returns**:

  The reasoning content from the model, or empty string if none.

### StructuredModelResponse

```python
class StructuredModelResponse(ModelResponse, Generic[T])
```

Response wrapper for structured/typed LLM output.

Primary usage is accessing the .parsed property for the structured data.


## ai_pipeline_core.llm.ai_messages

AI message handling for LLM interactions.

Provides AIMessages container for managing conversations with mixed content types
including text, documents, and model responses.

### AIMessageType

```python
AIMessageType = str | Document | ModelResponse
```

Type for messages in AIMessages container.

Represents the allowed types for conversation messages:
- str: Plain text messages
- Document: Structured document content
- ModelResponse: LLM generation responses

### AIMessages

```python
class AIMessages(list[AIMessageType])
```

Container for AI conversation messages supporting mixed types.

This class extends list to manage conversation messages between user
and AI, supporting text, Document objects, and ModelResponse instances.
Messages are converted to OpenAI-compatible format for LLM interactions.

Conversion Rules:
- str: Becomes {"role": "user", "content": text}
- Document: Becomes {"role": "user", "content": document_content}
(automatically handles text, images, PDFs based on MIME type)
- ModelResponse: Becomes {"role": "assistant", "content": response.content}

Note: Document conversion is automatic. Text content becomes user text messages.

VISION/PDF MODEL COMPATIBILITY WARNING:
Images require vision-capable models (e.g., gpt-4o, gemini-pro-vision, claude-3-haiku).
Non-vision models will raise ValueError when encountering image documents.
PDFs require models with document processing support - check your model's capabilities
before including PDF documents in messages. Unsupported models may fall back to
text extraction or raise errors depending on provider configuration.
LiteLLM proxy handles the specific encoding requirements for each provider.

IMPORTANT: Although AIMessages can contain Document entries, the LLM client functions
expect `messages` to be `AIMessages` or `str`. If you start from a Document or a list
of Documents, build AIMessages first (e.g., `AIMessages([doc])` or `AIMessages(docs)`).

CAUTION: AIMessages is a list subclass. Always use list construction (e.g.,
`AIMessages(["text"])`) or empty constructor with append (e.g.,
`AIMessages(); messages.append("text")`). Never pass raw strings directly to the
constructor (`AIMessages("text")`) as this will raise a TypeError to prevent
accidental character iteration.

**Example**:

  >>> from ai_pipeline_core import llm
  >>> messages = AIMessages()
  >>> messages.append("What is the capital of France?")
  >>> response = await llm.generate("gpt-5", messages=messages)
  >>> messages.append(response)  # Add the actual response

#### AIMessages.approximate_tokens_count

```python
@property
def approximate_tokens_count(self) -> int
```

Approximate tokens count for the messages.

Uses tiktoken with gpt-4 encoding to estimate total token count
across all messages in the conversation.

**Returns**:

  Approximate tokens count for all messages.

**Raises**:

- `ValueError` - If message contains unsupported type.

**Example**:

  >>> messages = AIMessages(["Hello", "World"])
  >>> messages.approximate_tokens_count  # ~2-3 tokens


## ai_pipeline_core.llm.model_types

### ModelName

```python
ModelName: TypeAlias = (
    Literal[
        # Core models
        "gemini-2.5-pro",
        "gpt-5",
        "grok-4",
        # Small models
        "gemini-2.5-flash",
        "gpt-5-mini",
        "grok-4-fast",
        # Search models
        "gemini-2.5-flash-search",
        "sonar-pro-search",
        "gpt-4o-search",
        "grok-4-fast-search",
    ]
    | str
)
```

Type-safe model name identifiers with support for custom models.

Provides IDE autocompletion for common model names while allowing any
string for custom models. The type is a union of predefined literals
and str, giving you the best of both worlds: suggestions for known
models and flexibility for custom ones.

Note: These are example common model names as of Q3 2025. Actual availability
depends on your LiteLLM proxy configuration and provider access.

Model categories:
Core models (gemini-2.5-pro, gpt-5, grok-4):
High-capability models for complex tasks requiring deep reasoning,
nuanced understanding, or creative generation.

Small models (gemini-2.5-flash, gpt-5-mini, grok-4-fast):
Efficient models optimized for speed and cost, suitable for
simpler tasks or high-volume processing.

Search models (*-search suffix):
Models with integrated web search capabilities for retrieving
and synthesizing current information.

Using custom models:
ModelName now includes str, so you can use any model name directly:
- Predefined models get IDE autocomplete and validation
- Custom models work seamlessly as strings
- No need for Union types or additional type aliases

**Example**:

  >>> from ai_pipeline_core import llm, ModelName
  >>>
  >>> # Predefined model with IDE autocomplete
  >>> model: ModelName = "gpt-5"  # IDE suggests common models
  >>> response = await llm.generate(model, messages="Hello")
  >>>
  >>> # Custom model works directly
  >>> model: ModelName = "custom-model-v2"  # Any string is valid
  >>> response = await llm.generate(model, messages="Hello")
  >>>
  >>> # Both types work seamlessly
  >>> models: list[ModelName] = ["gpt-5", "custom-llm", "gemini-2.5-pro"]

**Notes**:

  The ModelName type includes both predefined literals and str,
  allowing full flexibility while maintaining IDE support for
  common models.


## ai_pipeline_core.llm.client

LLM client implementation for AI model interactions.

This module provides the core functionality for interacting with language models
through a unified interface. It handles retries, caching, structured outputs,
and integration with various LLM providers via LiteLLM.

Key functions:
- generate(): Text generation with optional context caching
- generate_structured(): Type-safe structured output generation

### generate

```python
async def generate(model: ModelName, *, context: AIMessages | None = None, messages: AIMessages | str, options: ModelOptions | None = None) -> ModelResponse
```

Generate text response from a language model.

Main entry point for LLM text generation with smart context caching.
The context/messages split enables efficient token usage by caching
expensive static content separately from dynamic queries.

Best Practices:
1. OPTIONS: DO NOT use the options parameter - omit it entirely for production use
2. MESSAGES: Use AIMessages or str - wrap Documents in AIMessages
3. CONTEXT vs MESSAGES: Use context for static/cacheable, messages for dynamic
4. CONFIGURATION: Configure model behavior via LiteLLM proxy or environment variables

**Arguments**:

- `model` - Model to use (e.g., "gpt-5", "gemini-2.5-pro", "grok-4").
  Accepts predefined models or any string for custom models.
- `context` - Static context to cache (documents, examples, instructions).
  Defaults to None (empty context). Cached for 5 minutes by default.
- `messages` - Dynamic messages/queries. AIMessages or str ONLY.
  Do not pass Document or DocumentList directly.
  If string, converted to AIMessages internally.
- `options` - DEPRECATED - DO NOT USE. Reserved for internal framework usage only.
  Framework defaults are production-optimized (3 retries, 10s delay, 300s timeout).
  Configure model behavior centrally via LiteLLM proxy settings or environment
  variables, not per API call. Provider-specific settings should be configured
  at the proxy level.

**Returns**:

  ModelResponse containing:
  - Generated text content
  - Usage statistics
  - Cost information (if available)
  - Model metadata

**Raises**:

- `ValueError` - If model is empty or messages are invalid.
- `LLMError` - If generation fails after all retries.

  Document Handling:
  Wrap Documents in AIMessages - DO NOT pass directly or convert to .text:

  # CORRECT - wrap Document in AIMessages
  response = await llm.generate("gpt-5", messages=AIMessages([my_document]))

  # WRONG - don't pass Document directly
  response = await llm.generate("gpt-5", messages=my_document)  # NO!

  # WRONG - don't convert to string yourself
  response = await llm.generate("gpt-5", messages=my_document.text)  # NO!

  VISION/PDF MODEL COMPATIBILITY:
  When using Documents containing images or PDFs, ensure your model supports these formats:
  - Images require vision-capable models (gpt-4o, gemini-pro-vision, claude-3-sonnet)
  - PDFs require document processing support (varies by provider)
  - Non-compatible models will raise ValueError or fall back to text extraction
  - Check model capabilities before including visual/PDF content

  Context vs Messages Strategy:
- `context` - Static, reusable content for caching efficiency
  - Large documents, instructions, examples
  - Remains constant across multiple calls
  - Cached when supported by provider/proxy configuration

- `messages` - Dynamic, per-call specific content
  - User questions, current conversation turn
  - Changes with each API call
  - Never cached, always processed fresh

**Example**:

  >>> # CORRECT - No options parameter (this is the recommended pattern)
  >>> response = await llm.generate("gpt-5", messages="Explain quantum computing")
  >>> print(response.content)  # In production, use get_pipeline_logger instead of print

  >>> # With context caching for efficiency
  >>> # Context and messages are both AIMessages or str; wrap any Documents
  >>> static_doc = AIMessages([large_document, "few-shot example: ..."])
  >>>
  >>> # First call: caches context
  >>> r1 = await llm.generate("gpt-5", context=static_doc, messages="Summarize")
  >>>
  >>> # Second call: reuses cache, saves tokens!
  >>> r2 = await llm.generate("gpt-5", context=static_doc, messages="Key points?")

  >>> # Multi-turn conversation
  >>> messages = AIMessages([
  ...     "What is Python?",
  ...     previous_response,
  ...     "Can you give an example?"
  ... ])
  >>> response = await llm.generate("gpt-5", messages=messages)

  Performance:
  - Context caching saves ~50-90% tokens on repeated calls
  - First call: full token cost
  - Subsequent calls (within cache TTL): only messages tokens
  - Default cache TTL is 300s/5 minutes (production-optimized)
  - Default retry logic: 3 attempts with 10s delay (production-optimized)

  Caching:
  When enabled in your LiteLLM proxy and supported by the upstream provider,
  context messages may be cached to reduce token usage on repeated calls.
  Default TTL is 5m (optimized for production workloads). Configure caching
  behavior centrally via your LiteLLM proxy settings, not per API call.
  Savings depend on provider and payload; treat this as an optimization, not a guarantee.

  Configuration:
  All model behavior should be configured at the LiteLLM proxy level:
  - Temperature, max_tokens: Set in litellm_config.yaml model_list
  - Retry logic: Configure in proxy general_settings
  - Timeouts: Set via proxy configuration
  - Caching: Enable/configure in proxy cache settings

  This centralizes configuration and ensures consistency across all API calls.

**Notes**:

  - All models are accessed via LiteLLM proxy
  - Automatic retry with configurable delay between attempts
  - Cost tracking via response headers

### generate_structured

```python
async def generate_structured(model: ModelName, response_format: type[T], *, context: AIMessages | None = None, messages: AIMessages | str, options: ModelOptions | None = None) -> StructuredModelResponse[T]
```

Generate structured output conforming to a Pydantic model.

Type-safe generation that returns validated Pydantic model instances.
Uses OpenAI's structured output feature for guaranteed schema compliance.

IMPORTANT: Search models (models with '-search' suffix) do not support
structured output. Use generate() instead for search models.

Best Practices:
1. OPTIONS: DO NOT use the options parameter - omit it entirely for production use
2. MESSAGES: Use AIMessages or str - wrap Documents in AIMessages
3. CONFIGURATION: Configure model behavior via LiteLLM proxy or environment variables
4. See generate() documentation for more details

Context vs Messages Strategy:
context: Static, reusable content for caching efficiency
- Schemas, examples, instructions
- Remains constant across multiple calls
- Cached when supported by provider/proxy configuration

messages: Dynamic, per-call specific content
- Data to be structured, user queries
- Changes with each API call
- Never cached, always processed fresh

Complex Task Pattern:
For complex tasks like research or deep analysis, it's recommended to use
a two-step approach:
1. First use generate() with a capable model to perform the analysis
2. Then use generate_structured() with a smaller model to convert the
response into structured output

This pattern is more reliable than trying to force complex reasoning
directly into structured format:

>>> # Step 1: Research/analysis with generate() - no options parameter
>>> research = await llm.generate(
...     "gpt-5",
...     messages="Research and analyze this complex topic..."
... )
>>>
>>> # Step 2: Structure the results with generate_structured()
>>> structured = await llm.generate_structured(
...     "gpt-5-mini",  # Smaller model is fine for structuring
...     response_format=ResearchSummary,
...     messages=f"Extract key information: {research.content}"
... )

**Arguments**:

- `model` - Model to use (must support structured output).
  Search models (models with '-search' suffix) do not support structured output.
- `response_format` - Pydantic model class defining the output schema.
  The model will generate JSON matching this schema.
- `context` - Static context to cache (documents, schemas, examples).
  Defaults to None (empty AIMessages).
- `messages` - Dynamic prompts/queries. AIMessages or str ONLY.
  Do not pass Document or DocumentList directly.
- `options` - Optional ModelOptions for configuring temperature, retries, etc.
  If provided, it will NOT be mutated (a copy is created internally).
  The response_format field is set automatically from the response_format parameter.
  In most cases, leave as None to use framework defaults.
  Configure model behavior centrally via LiteLLM proxy settings when possible.

**Notes**:

  Vision/PDF model compatibility considerations:
  - Images require vision-capable models that also support structured output
  - PDFs require models with both document processing AND structured output support
  - Many models support either vision OR structured output, but not both
  - Test your specific model+document combination before production use
  - Consider two-step approach: generate() for analysis, then generate_structured()
  for formatting

**Returns**:

  StructuredModelResponse[T] containing:
  - parsed: Validated instance of response_format class
  - All fields from regular ModelResponse (content, usage, etc.)

**Raises**:

- `TypeError` - If response_format is not a Pydantic model class.
- `ValueError` - If model doesn't support structured output or no parsed content returned.
  Structured output support varies by provider and model.
- `LLMError` - If generation fails after retries.
- `ValidationError` - If response cannot be parsed into response_format.

**Example**:

  >>> from pydantic import BaseModel, Field
  >>>
  >>> class Analysis(BaseModel):
  ...     summary: str = Field(description="Brief summary")
  ...     sentiment: float = Field(ge=-1, le=1)
  ...     key_points: list[str] = Field(max_length=5)
  >>>
  >>> # CORRECT - No options parameter
  >>> response = await llm.generate_structured(
  ...     "gpt-5",
  ...     response_format=Analysis,
  ...     messages="Analyze this product review: ..."
  ... )
  >>>
  >>> analysis = response.parsed  # Type: Analysis
  >>> print(f"Sentiment: {analysis.sentiment}")
  >>> for point in analysis.key_points:
  ...     print(f"- {point}")

  Supported models:
  Structured output support varies by provider and model. Generally includes:
  - OpenAI: GPT-4 and newer models
  - Anthropic: Claude 3+ models
  - Google: Gemini Pro models

  Search models (models with '-search' suffix) do not support structured output.
  Check provider documentation for specific support.

  Performance:
  - Structured output may use more tokens than free text
  - Complex schemas increase generation time
  - Validation overhead is minimal (Pydantic is fast)

**Notes**:

  - Pydantic model is converted to JSON Schema for the API
  - The model generates JSON matching the schema
  - Validation happens automatically via Pydantic
  - Use Field() descriptions to guide generation
  - Search models (models with '-search' suffix) do not support structured output


## ai_pipeline_core.prompt_manager

Jinja2-based prompt template management system.

This module provides the PromptManager class for loading and rendering
Jinja2 templates used as prompts for language models. It implements a
smart search strategy that looks for templates in both local and shared
directories.

Search strategy:
1. Local directory (same as calling module)
2. Local 'prompts' subdirectory
3. Parent 'prompts' directories (search ascends parent packages up to the package
boundary or after 4 parent levels, whichever comes first)

Key features:
- Automatic template discovery
- Jinja2 template rendering with context
- Smart path resolution (.jinja2/.jinja extension handling)
- Clear error messages for missing templates
- Built-in global variables:
- current_date: Current date in format "03 January 2025" (string)

**Example**:

  >>> from ai_pipeline_core import PromptManager
  >>>
  >>> # Initialize at module level (not inside functions)
  >>> pm = PromptManager(__file__)
  >>>
  >>> # Render a template
  >>> prompt = pm.get(
  ...     "analyze.jinja2",
  ...     document=doc,
  ...     instructions="Extract key points"
  ... )

  Template organization:
  project/
  ├── my_module.py        # Can use local templates
  ├── analyze.jinja2      # Local template (same directory)
  └── prompts/           # Shared prompts directory
  ├── summarize.jinja2
  └── extract.jinja2

**Notes**:

  Templates should use .jinja2 or .jinja extension.
  The extension can be omitted when calling get().

### PromptManager

```python
class PromptManager
```

Manages Jinja2 prompt templates with smart path resolution.

PromptManager provides a convenient interface for loading and rendering
Jinja2 templates used as prompts for LLMs. It automatically searches for
templates in multiple locations, supporting both local (module-specific)
and shared (project-wide) templates.

Search hierarchy:
1. Same directory as the calling module (for local templates)
2. 'prompts' subdirectory in the calling module's directory
3. 'prompts' directories in parent packages (search ascends parent packages up to the
package boundary or after 4 parent levels, whichever comes first)

**Attributes**:

- `search_paths` - List of directories where templates are searched.
- `env` - Jinja2 Environment configured for prompt rendering.

**Example**:

  >>> # BEST PRACTICE: Instantiate at module scope (top level), not inside functions
  >>> # In flow/my_flow.py
  >>> from ai_pipeline_core import PromptManager
  >>> pm = PromptManager(__file__)  # Module-level initialization
  >>>
  >>> # WRONG - Don't instantiate inside handlers or hot paths:
  >>> # async def process():
  >>> #     pm = PromptManager(__file__)  # NO! Creates new instance each call
  >>>
  >>> # Uses flow/prompts/analyze.jinja2 if it exists,
  >>> # otherwise searches parent directories
  >>> prompt = pm.get("analyze", context=data)
  >>>
  >>> # Can also use templates in same directory as module
  >>> prompt = pm.get("local_template.jinja2")

  Template format:
  Templates use standard Jinja2 syntax:
    ```jinja2
    Analyze the following document:
    {{ document.name }}

    {% if instructions %}
    Instructions: {{ instructions }}
    {% endif %}

    Date: {{ current_date }}  # Current date in format "03 January 2025"
    ```

**Notes**:

  - Autoescape is disabled for prompts (raw text output)
  - Whitespace control is enabled (trim_blocks, lstrip_blocks)

  Template Inheritance:
  Templates support standard Jinja2 inheritance. Templates are searched
  in order of search_paths, so templates in earlier paths override later ones.
  Precedence (first match wins):
  1. Same directory as module
  2. Module's prompts/ subdirectory
  3. Parent prompts/ directories (nearest to farthest)
  - Templates are cached by Jinja2 for performance

#### PromptManager.__init__

```python
def __init__(self, current_file: str, prompts_dir: str = "prompts")
```

Initialize PromptManager with smart template discovery.

Sets up the Jinja2 environment with a FileSystemLoader that searches
multiple directories for templates. The search starts from the calling
module's location and extends to parent package directories.

**Arguments**:

- `current_file` - The __file__ path of the calling module. Must be
  a valid file path (not __name__). Used as the
  starting point for template discovery.
- `prompts_dir` - Name of the prompts subdirectory to search for
  in each package level. Defaults to "prompts".
  Do not pass prompts_dir='prompts' because it is already the default.

**Raises**:

- `PromptError` - If current_file is not a valid file path (e.g.,
  if __name__ was passed instead of __file__).

**Notes**:

  Search behavior - Given a module at /project/flows/my_flow.py:
  1. /project/flows/ (local templates)
  2. /project/flows/prompts/ (if exists)
  3. /project/prompts/ (if /project has __init__.py)

  Search ascends parent packages up to the package boundary or after 4 parent
  levels, whichever comes first.

**Example**:

  >>> # Correct usage
  >>> pm = PromptManager(__file__)
  >>>
  >>> # Custom prompts directory name
  >>> pm = PromptManager(__file__, prompts_dir="templates")
  >>>
  >>> # Common mistake (will raise PromptError)
  >>> pm = PromptManager(__name__)  # Wrong!

#### PromptManager.get

```python
def get(self, prompt_path: str, **kwargs: Any) -> str
```

Load and render a Jinja2 template with the given context.

Searches for the template in all configured search paths and renders
it with the provided context variables. Automatically tries adding
.jinja2 or .jinja extensions if the file is not found.

**Arguments**:

- `prompt_path` - Path to the template file, relative to any search
  directory. Can be a simple filename ("analyze")
  or include subdirectories ("tasks/summarize").
  Extensions (.jinja2, .jinja) are optional.
- `**kwargs` - Context variables passed to the template. These become
  available as variables within the Jinja2 template.

**Returns**:

  The rendered template as a string, ready to be sent to an LLM.

**Raises**:

- `PromptNotFoundError` - If the template file cannot be found in
  any search path.
- `PromptRenderError` - If the template contains errors or if
  rendering fails (e.g., missing variables,
  syntax errors).

**Notes**:

  Template resolution - Given prompt_path="analyze":
  1. Try "analyze" as-is
  2. Try "analyze.jinja2"
  3. Try "analyze.jinja"

  The first matching file is used.

**Example**:

  >>> pm = PromptManager(__file__)
  >>>
  >>> # Simple rendering
  >>> prompt = pm.get("summarize", text="Long document...")
  >>>
  >>> # With complex context
  >>> prompt = pm.get(
  ...     "analyze",
  ...     document=doc,
  ...     max_length=500,
  ...     style="technical",
  ...     options={"include_metadata": True}
  ... )
  >>>
  >>> # Nested template path
  >>> prompt = pm.get("flows/extraction/extract_entities")

  Template example:
    ```jinja2
    Summarize the following text in {{ max_length }} words:

    {{ text }}

    {% if style %}
    Style: {{ style }}
    {% endif %}
    ```

**Notes**:

  All Jinja2 features are available: loops, conditionals,
  filters, macros, inheritance, etc.


## ai_pipeline_core.flow.options

Flow options configuration for pipeline execution.

Provides base configuration settings for AI pipeline flows,
including model selection and runtime parameters.

### FlowOptions

```python
class FlowOptions(BaseSettings)
```

Base configuration settings for AI pipeline flows.

FlowOptions provides runtime configuration for pipeline flows,
including model selection and other parameters. It uses pydantic-settings
to support environment variable overrides and is immutable (frozen) by default.

This class is designed to be subclassed for flow-specific configuration:

**Example**:

  >>> class MyFlowOptions(FlowOptions):
  ...     temperature: float = Field(0.7, ge=0, le=2)
  ...     batch_size: int = Field(10, gt=0)
  ...     custom_param: str = "default"

  >>> # Use in CLI with run_cli:
  >>> run_cli(
  ...     flows=[my_flow],
  ...     options_cls=MyFlowOptions  # Will parse CLI args
  ... )

  >>> # Or create programmatically:
  >>> options = MyFlowOptions(
  ...     core_model="gemini-2.5-pro",
  ...     temperature=0.9
  ... )

**Attributes**:

- `core_model` - Primary LLM for complex tasks (default: gpt-5)
- `small_model` - Fast model for simple tasks (default: gpt-5-mini)

  Configuration:
  - Frozen (immutable) after creation
  - Extra fields ignored (not strict)
  - Can be populated from environment variables
  - Used by simple_runner.cli for command-line parsing

**Notes**:

  The base class provides model selection. Subclasses should
  add flow-specific parameters with appropriate validation.


## ai_pipeline_core.flow.config

Flow configuration system for type-safe pipeline definitions.

This module provides the FlowConfig abstract base class that enforces
type safety for flow inputs and outputs in the pipeline system.

Best Practice:
    Always finish @pipeline_flow functions with create_and_validate_output()
    to ensure type safety and proper validation of output documents.

### FlowConfig

```python
class FlowConfig(ABC)
```

Abstract base class for type-safe flow configuration.

FlowConfig defines the contract for flow inputs and outputs, ensuring
type safety and preventing circular dependencies in pipeline flows.
Each flow must have a corresponding FlowConfig subclass that specifies
its input document types and output document type.

CRITICAL RULE: OUTPUT_DOCUMENT_TYPE must NEVER be in INPUT_DOCUMENT_TYPES!
This prevents circular dependencies as flows chain together.
Each flow transforms input types to a DIFFERENT output type.

Class Variables:
INPUT_DOCUMENT_TYPES: List of FlowDocument types this flow accepts
OUTPUT_DOCUMENT_TYPE: Single FlowDocument type this flow produces

Validation Rules:
- INPUT_DOCUMENT_TYPES and OUTPUT_DOCUMENT_TYPE must be defined
- OUTPUT_DOCUMENT_TYPE cannot be in INPUT_DOCUMENT_TYPES (prevents cycles)
- Field names must be exact (common typos are detected)

Why this matters:
Flows connect in pipelines where one flow's output becomes another's input.
Same input/output types would create infinite loops or circular dependencies.

**Example**:

  >>> # CORRECT - Different output type from inputs
  >>> class ProcessingFlowConfig(FlowConfig):
  ...     INPUT_DOCUMENT_TYPES = [RawDataDocument]
  ...     OUTPUT_DOCUMENT_TYPE = ProcessedDocument  # Different type!
  >>>
  >>> # Use in @pipeline_flow - RECOMMENDED PATTERN
  >>> @pipeline_flow(config=ProcessingFlowConfig, name="processing")
  >>> async def process(
  ...     project_name: str, docs: DocumentList, flow_options: FlowOptions
  ... ) -> DocumentList:
  ...     outputs = []
  ...     # ... processing logic ...
  ...     return config.create_and_validate_output(outputs)

  >>> # WRONG - Will raise TypeError
  >>> class BadConfig(FlowConfig):
  ...     INPUT_DOCUMENT_TYPES = [DataDocument]
  ...     OUTPUT_DOCUMENT_TYPE = DataDocument  # SAME TYPE - NOT ALLOWED!

**Notes**:

  - Validation happens at class definition time
  - Helps catch configuration errors early
  - Used by simple_runner to manage document flow

#### FlowConfig.create_and_validate_output

```python
@classmethod
def create_and_validate_output(cls, output: FlowDocument | Iterable[FlowDocument] | DocumentList) -> DocumentList
```

Create and validate flow output documents.

RECOMMENDED: Always use this method at the end of @pipeline_flow functions
to ensure type safety and proper output validation.

Convenience method that wraps output in a DocumentList if needed
and validates it matches the expected OUTPUT_DOCUMENT_TYPE.

**Arguments**:

- `output` - Single document, iterable of documents, or DocumentList.

**Returns**:

  Validated DocumentList containing the output documents.

**Raises**:

- `DocumentValidationError` - If output type doesn't match OUTPUT_DOCUMENT_TYPE.

**Example**:

  >>> @pipeline_flow(config=MyFlowConfig, name="my_flow")
  >>> async def process_flow(
  ...     project_name: str, documents: DocumentList, flow_options: FlowOptions
  ... ) -> DocumentList:
  >>>     outputs = []
  >>>     # ... processing logic ...
  >>>     outputs.append(OutputDoc(...))
  >>>
  >>>     # Always finish with this validation
  >>>     return config.create_and_validate_output(outputs)

**Notes**:

  This is the recommended pattern for all @pipeline_flow functions.
  It ensures type safety and catches output errors immediately.


## ai_pipeline_core.pipeline

Pipeline decorators with Prefect integration and tracing.

Wrappers around Prefect's @task and @flow that add Laminar tracing
and enforce async-only execution for consistency.

### pipeline_task

```python
def pipeline_task(__fn: Callable[..., Coroutine[Any, Any, R_co]] | None = None, *, trace_level: TraceLevel = "always", trace_ignore_input: bool = False, trace_ignore_output: bool = False, trace_ignore_inputs: list[str] | None = None, trace_input_formatter: Callable[..., str] | None = None, trace_output_formatter: Callable[..., str] | None = None, trace_cost: float | None = None, trace_trim_documents: bool = True, name: str | None = None, description: str | None = None, tags: Iterable[str] | None = None, version: str | None = None, cache_policy: CachePolicy | type[NotSet] = NotSet, cache_key_fn: Callable[[TaskRunContext, dict[str, Any]], str | None] | None = None, cache_expiration: datetime.timedelta | None = None, task_run_name: TaskRunNameValueOrCallable | None = None, retries: int | None = None, retry_delay_seconds: int | float | list[float] | Callable[[int], list[float]] | None = None, retry_jitter_factor: float | None = None, persist_result: bool | None = None, result_storage: ResultStorage | str | None = None, result_serializer: ResultSerializer | str | None = None, result_storage_key: str | None = None, cache_result_in_memory: bool = True, timeout_seconds: int | float | None = None, log_prints: bool | None = False, refresh_cache: bool | None = None, on_completion: list[StateHookCallable] | None = None, on_failure: list[StateHookCallable] | None = None, retry_condition_fn: RetryConditionCallable | None = None, viz_return_value: bool | None = None, asset_deps: list[str | Asset] | None = None) -> _TaskLike[R_co] | Callable[[Callable[..., Coroutine[Any, Any, R_co]]], _TaskLike[R_co]]
```

Decorate an async function as a traced Prefect task.

Wraps an async function with both Prefect task functionality and
LMNR tracing. The function MUST be async (declared with 'async def').

IMPORTANT: Never combine with @trace decorator - this includes tracing automatically.
The framework will raise TypeError if you try to use both decorators together.

Best Practice - Use Defaults:
For 90% of use cases, use this decorator WITHOUT any parameters.
Only specify parameters when you have EXPLICIT requirements.

**Arguments**:

- `__fn` - Function to decorate (when used without parentheses).
- `trace_level` - When to trace ("always", "debug", "off").
  - "always": Always trace (default)
  - "debug": Only trace when LMNR_DEBUG="true"
  - "off": Disable tracing
- `trace_ignore_input` - Don't trace input arguments.
- `trace_ignore_output` - Don't trace return value.
- `trace_ignore_inputs` - List of parameter names to exclude from tracing.
- `trace_input_formatter` - Custom formatter for input tracing.
- `trace_output_formatter` - Custom formatter for output tracing.
- `trace_cost` - Optional cost value to track in metadata. When provided and > 0,
  sets gen_ai.usage.output_cost, gen_ai.usage.cost, and cost metadata.
  Also forces trace level to "always" if not already set.
- `trace_trim_documents` - Trim document content in traces to first 100 chars (default True).
  Reduces trace size with large documents.
- `name` - Task name (defaults to function name).
- `description` - Human-readable task description.
- `tags` - Tags for organization and filtering.
- `version` - Task version string.
- `cache_policy` - Caching policy for task results.
- `cache_key_fn` - Custom cache key generation.
- `cache_expiration` - How long to cache results.
- `task_run_name` - Dynamic or static run name.
- `retries` - Number of retry attempts (default 0).
- `retry_delay_seconds` - Delay between retries.
- `retry_jitter_factor` - Random jitter for retry delays.
- `persist_result` - Whether to persist results.
- `result_storage` - Where to store results.
- `result_serializer` - How to serialize results.
- `result_storage_key` - Custom storage key.
- `cache_result_in_memory` - Keep results in memory.
- `timeout_seconds` - Task execution timeout.
- `log_prints` - Capture print() statements.
- `refresh_cache` - Force cache refresh.
- `on_completion` - Hooks for successful completion.
- `on_failure` - Hooks for task failure.
- `retry_condition_fn` - Custom retry condition.
- `viz_return_value` - Include return value in visualization.
- `asset_deps` - Upstream asset dependencies.

**Returns**:

  Decorated task callable that is awaitable and has Prefect
  task methods (submit, map, etc.).

**Example**:

  >>> # RECOMMENDED - No parameters needed!
  >>> @pipeline_task
  >>> async def process_document(doc: Document) -> Document:
  ...     result = await analyze(doc)
  ...     return result
  >>>
  >>> # With parameters (only when necessary):
  >>> @pipeline_task(retries=5)  # Only for known flaky operations
  >>> async def unreliable_api_call(url: str) -> dict:
  ...     # This API fails often, needs extra retries
  ...     return await fetch_with_retry(url)
  >>>
  >>> # AVOID specifying defaults - they're already optimal:
  >>> # - Automatic task naming
  >>> # - Standard retry policy
  >>> # - Sensible timeout
  >>> # - Full observability

  Performance:
  - Task decoration overhead: ~1-2ms
  - Tracing overhead: ~1-2ms per call
  - Prefect state tracking: ~5-10ms

**Notes**:

  Tasks are automatically traced with LMNR and appear in
  both Prefect and LMNR dashboards.

**See Also**:

  - pipeline_flow: For flow-level decoration
  - trace: Lower-level tracing decorator
  - prefect.task: Standard Prefect task (no tracing)

### pipeline_flow

```python
def pipeline_flow(*, config: type[FlowConfig], trace_level: TraceLevel = "always", trace_ignore_input: bool = False, trace_ignore_output: bool = False, trace_ignore_inputs: list[str] | None = None, trace_input_formatter: Callable[..., str] | None = None, trace_output_formatter: Callable[..., str] | None = None, trace_cost: float | None = None, trace_trim_documents: bool = True, name: str | None = None, version: str | None = None, flow_run_name: Union[Callable[[], str], str] | None = None, retries: int | None = None, retry_delay_seconds: int | float | None = None, task_runner: TaskRunner[PrefectFuture[Any]] | None = None, description: str | None = None, timeout_seconds: int | float | None = None, validate_parameters: bool = True, persist_result: bool | None = None, result_storage: ResultStorage | str | None = None, result_serializer: ResultSerializer | str | None = None, cache_result_in_memory: bool = True, log_prints: bool | None = None, on_completion: list[FlowStateHook[Any, Any]] | None = None, on_failure: list[FlowStateHook[Any, Any]] | None = None, on_cancellation: list[FlowStateHook[Any, Any]] | None = None, on_crashed: list[FlowStateHook[Any, Any]] | None = None, on_running: list[FlowStateHook[Any, Any]] | None = None) -> Callable[[_DocumentsFlowCallable[FO_contra]], _FlowLike[FO_contra]]
```

Decorate an async flow for document processing.

Wraps an async function as a Prefect flow with tracing and type safety.
The decorated function MUST be async and follow the required signature.

IMPORTANT: Never combine with @trace decorator - this includes tracing automatically.
The framework will raise TypeError if you try to use both decorators together.

Best Practice - Use Defaults:
For 90% of use cases, use this decorator WITHOUT any parameters.
Only specify parameters when you have EXPLICIT requirements.

Required function signature:
async def flow_fn(
project_name: str,         # Project/pipeline identifier
documents: DocumentList,   # Input documents to process
flow_options: FlowOptions, # Configuration (or subclass)
) -> DocumentList             # Must return DocumentList

**Arguments**:

- `config` - Required FlowConfig class for document loading/saving. Enables
  automatic loading from string paths and saving outputs.
- `trace_level` - When to trace ("always", "debug", "off").
  - "always": Always trace (default)
  - "debug": Only trace when LMNR_DEBUG="true"
  - "off": Disable tracing
- `trace_ignore_input` - Don't trace input arguments.
- `trace_ignore_output` - Don't trace return value.
- `trace_ignore_inputs` - Parameter names to exclude from tracing.
- `trace_input_formatter` - Custom input formatter.
- `trace_output_formatter` - Custom output formatter.
- `trace_cost` - Optional cost value to track in metadata. When provided and > 0,
  sets gen_ai.usage.output_cost, gen_ai.usage.cost, and cost metadata.
  Also forces trace level to "always" if not already set.
- `trace_trim_documents` - Trim document content in traces to first 100 chars (default True).
  Reduces trace size with large documents.
- `name` - Flow name (defaults to function name).
- `version` - Flow version identifier.
- `flow_run_name` - Static or dynamic run name.
- `retries` - Number of flow retry attempts (default 0).
- `retry_delay_seconds` - Delay between flow retries.
- `task_runner` - Task execution strategy (sequential/concurrent).
- `description` - Human-readable flow description.
- `timeout_seconds` - Flow execution timeout.
- `validate_parameters` - Validate input parameters.
- `persist_result` - Persist flow results.
- `result_storage` - Where to store results.
- `result_serializer` - How to serialize results.
- `cache_result_in_memory` - Keep results in memory.
- `log_prints` - Capture print() statements.
- `on_completion` - Hooks for successful completion.
- `on_failure` - Hooks for flow failure.
- `on_cancellation` - Hooks for flow cancellation.
- `on_crashed` - Hooks for flow crashes.
- `on_running` - Hooks for flow start.

**Returns**:

  Decorated flow callable that maintains Prefect flow interface
  while enforcing document processing conventions.

**Example**:

  >>> from ai_pipeline_core import FlowOptions, FlowConfig
  >>>
  >>> class MyFlowConfig(FlowConfig):
  ...     INPUT_DOCUMENT_TYPES = [InputDoc]
  ...     OUTPUT_DOCUMENT_TYPE = OutputDoc
  >>>
  >>> # Standard usage with config
  >>> @pipeline_flow(config=MyFlowConfig)
  >>> async def analyze_documents(
  ...     project_name: str,
  ...     documents: DocumentList,
  ...     flow_options: FlowOptions
  >>> ) -> DocumentList:
  ...     # Process each document
  ...     results = []
  ...     for doc in documents:
  ...         result = await process(doc)
  ...         results.append(result)
  ...     return DocumentList(results)
  >>>
  >>> # With additional parameters:
  >>> @pipeline_flow(config=MyFlowConfig, retries=2)
  >>> async def critical_flow(
  ...     project_name: str,
  ...     documents: DocumentList,
  ...     flow_options: FlowOptions
  >>> ) -> DocumentList:
  ...     # Critical processing that might fail
  ...     return await process_critical(documents)
  >>>
  >>> # AVOID specifying defaults - they're already optimal:
  >>> # - Automatic flow naming
  >>> # - Standard retry policy
  >>> # - Full observability

**Notes**:

  - Flow is wrapped with both Prefect and LMNR tracing
  - Return type is validated at runtime
  - FlowOptions can be subclassed for custom configuration
  - All Prefect flow methods (.serve(), .deploy()) are available

**See Also**:

  - pipeline_task: For task-level decoration
  - FlowConfig: Type-safe flow configuration
  - FlowOptions: Base class for flow options
  - simple_runner.run_pipeline: Execute flows locally


## ai_pipeline_core.logging.logging_config

### get_pipeline_logger

```python
def get_pipeline_logger(name: str)
```

Get a logger for pipeline components.

Returns a Prefect-integrated logger with proper configuration.

**Arguments**:

- `name` - Logger name, typically __name__.

**Returns**:

  Prefect logger instance.

**Example**:

  >>> logger = get_pipeline_logger(__name__)
  >>> logger.info("Module initialized")


## ai_pipeline_core.storage

Storage module for ai_pipeline_core.


## ai_pipeline_core.settings

Core configuration settings for pipeline operations.

This module provides the Settings base class for configuration management.
Applications should inherit from Settings to create their own ProjectSettings
class with additional configuration fields.

Environment variables:
OPENAI_BASE_URL: LiteLLM proxy endpoint (e.g., http://localhost:4000)
OPENAI_API_KEY: API key for LiteLLM proxy authentication
PREFECT_API_URL: Prefect server endpoint for flow orchestration
PREFECT_API_KEY: Prefect API authentication key
LMNR_PROJECT_API_KEY: Laminar project key for observability
GCS_SERVICE_ACCOUNT_FILE: Path to GCS service account JSON file

Configuration precedence:
1. Environment variables (highest priority)
2. .env file in current directory
3. Default values (empty strings)

**Example**:

  >>> from ai_pipeline_core import Settings
  >>>
  >>> # Create your project's settings class
  >>> class ProjectSettings(Settings):
  ...     app_name: str = "my-app"
  ...     debug_mode: bool = False
  >>>
  >>> # Create singleton instance
  >>> settings = ProjectSettings()
  >>>
  >>> # Access configuration
  >>> print(settings.openai_base_url)
  >>> print(settings.app_name)

  .env file format:
  OPENAI_BASE_URL=http://localhost:4000
  OPENAI_API_KEY=sk-1234567890
  PREFECT_API_URL=http://localhost:4200/api
  PREFECT_API_KEY=pnu_abc123
  LMNR_PROJECT_API_KEY=lmnr_proj_xyz
  GCS_SERVICE_ACCOUNT_FILE=/path/to/service-account.json
  APP_NAME=production-app
  DEBUG_MODE=false

**Notes**:

  Settings are loaded once at initialization and frozen. There is no
  built-in reload mechanism - the process must be restarted to pick up
  changes to environment variables or .env file. This is by design to
  ensure consistency during execution.

### Settings

```python
class Settings(BaseSettings)
```

Base configuration class for AI Pipeline applications.

Settings is designed to be inherited by your application's configuration
class. It provides core AI Pipeline settings and type-safe configuration
management with automatic loading from environment variables and .env files.
All settings are immutable after initialization.

Inherit from Settings to add your application-specific configuration:

>>> from ai_pipeline_core import Settings
>>>
>>> class ProjectSettings(Settings):
...     # Your custom settings
...     app_name: str = "my-app"
...     max_retries: int = 3
...     enable_cache: bool = True
>>>
>>> # Create singleton instance for your app
>>> settings = ProjectSettings()

Core Attributes:
openai_base_url: LiteLLM proxy URL for OpenAI-compatible API.
Required for all LLM operations. Usually
http://localhost:4000 for local development.

openai_api_key: Authentication key for LiteLLM proxy. Required
for LLM operations. Format depends on proxy config.

prefect_api_url: Prefect server API endpoint. Required for flow
deployment and remote execution. Leave empty for
local-only execution.

prefect_api_key: Prefect API authentication key. Required only
when connecting to Prefect Cloud or secured server.

lmnr_project_api_key: Laminar (LMNR) project API key for observability.
Optional but recommended for production monitoring.

lmnr_debug: Debug mode flag for Laminar. Set to "true" to
enable debug-level logging. Empty string by default.

gcs_service_account_file: Path to GCS service account JSON file.
Used for authenticating with Google Cloud Storage.
Optional - if not set, default credentials will be used.

Configuration sources:
- Environment variables (highest priority)
- .env file in current directory
- Default values in class definition

**Notes**:

  Empty strings are used as defaults to allow optional services.
  Check for empty values before using service-specific settings.


## ai_pipeline_core.documents.task_document

Task-specific document base class for temporary pipeline data.

This module provides the TaskDocument abstract base class for documents
that exist only during Prefect task execution and are not persisted.

### TaskDocument

```python
class TaskDocument(Document)
```

Abstract base class for temporary documents within task execution.

TaskDocument is used for intermediate data that exists only during
the execution of a Prefect task and is not persisted to disk. These
documents are ideal for temporary processing results, transformations,
and data that doesn't need to survive beyond the current task.

Key characteristics:
- Not persisted to file system
- Exists only during task execution
- Garbage collected after task completes
- Used for intermediate processing results
- Reduces persistent I/O for temporary data

Creating TaskDocuments:
Same as Document - use `create()` for automatic conversion, `__init__` for bytes.
See Document.create() for detailed usage examples.

Use Cases:
- Intermediate transformation results
- Temporary buffers during processing
- Task-local cache data
- Processing status documents

**Notes**:

  - Cannot instantiate TaskDocument directly - must subclass
  - Not saved by simple_runner utilities
  - Reduces I/O overhead for temporary data
  - No additional abstract methods to implement


## ai_pipeline_core.documents.document

Document abstraction layer for AI pipeline flows.

This module provides the core document abstraction for working with various types of data
in AI pipelines. Documents are immutable Pydantic models that wrap binary content with metadata.

### Document

```python
class Document(BaseModel, ABC)
```

Abstract base class for all documents in the AI Pipeline Core system.

Document is the fundamental data abstraction for all content flowing through
pipelines. It provides automatic encoding, MIME type detection, serialization,
and validation. All documents must be subclassed from FlowDocument or TaskDocument
based on their persistence requirements.

VALIDATION IS AUTOMATIC - Do not add manual validation!
Size validation, name validation, and MIME type detection are built-in.
The framework handles all standard validations internally.

# WRONG - These checks already happen automatically:
if document.size > document.MAX_CONTENT_SIZE:
raise DocumentSizeError(...)  # NO! Already handled
document.validate_file_name(document.name)  # NO! Automatic

Best Practices:
- Use create() classmethod for automatic type conversion (default preferred)
- Omit description parameter unless truly needed for metadata
- When using LLM functions, pass AIMessages or str. Wrap any Document values
in AIMessages([...]). Do not call .text yourself

Standard Usage:
>>> # CORRECT - minimal parameters
>>> doc = MyDocument.create(name="data.json", content={"key": "value"})

>>> # AVOID - unnecessary description
>>> doc = MyDocument.create(
...     name="data.json",
...     content={"key": "value"},
...     description="This is data"  # Usually not needed!
... )

Key features:
- Immutable by default (frozen Pydantic model)
- Automatic MIME type detection
- Content size validation
- SHA256 hashing for deduplication
- Support for text, JSON, YAML, PDF, and image formats
- Conversion utilities between different formats
- Source provenance tracking via sources field
- Document type conversion via model_convert() method
- Standard Pydantic model_copy() for same-type copying

Class Variables:
MAX_CONTENT_SIZE: Maximum allowed content size in bytes (default 25MB)

**Attributes**:

- `name` - Document filename (validated for security)
- `description` - Optional human-readable description
- `content` - Raw document content as bytes
- `sources` - List of source references tracking document provenance

  Creating Documents:
  **Use the `create` classmethod** for most use cases. It accepts various
  content types (str, dict, list, BaseModel) and converts them automatically.
  Only use __init__ directly when you already have bytes content.

  >>> # RECOMMENDED: Use create for automatic conversion
  >>> doc = MyDocument.create(name="data.json", content={"key": "value"})
  >>>
  >>> # Direct constructor: Only for bytes
  >>> doc = MyDocument(name="data.bin", content=b"\x00\x01\x02")

**Warnings**:

  - Document subclasses should NOT start with 'Test' prefix (pytest conflict)
  - Cannot instantiate Document directly - must subclass FlowDocument or TaskDocument
  - Cannot add custom fields - only name, description, content, sources are allowed
  - Document is an abstract class and cannot be instantiated directly

  Metadata Attachment Patterns:
  Since custom fields are not allowed, use these patterns for metadata:
  1. Use the 'description' field for human-readable metadata
  2. Embed metadata in content (e.g., JSON with data + metadata fields)
  3. Create a separate MetadataDocument type to accompany data documents
  4. Use document naming conventions (e.g., "data_v2_2024.json")
  5. Store metadata in flow_options

  FILES Enum Best Practice:
  When defining a FILES enum, NEVER use magic strings to reference files.
  Always use the enum values to maintain type safety and refactorability.

  WRONG - Magic strings/numbers:
  doc = ConfigDocument.create(name="config.yaml", content=data)  # NO!
  doc = docs.get_by("settings.json")  # NO! Magic string
  files = ["config.yaml", "settings.json"]  # NO! Magic strings

  CORRECT - Use enum references:
  doc = ConfigDocument.create(
  name=ConfigDocument.FILES.CONFIG,  # YES! Type-safe
  content=data
  )
  doc = docs.get_by(ConfigDocument.FILES.SETTINGS)  # YES!
  files = [
  ConfigDocument.FILES.CONFIG,
  ConfigDocument.FILES.SETTINGS
  ]  # YES! Refactorable

  Pydantic Model Interaction:
  Documents provide DIRECT support for Pydantic models. Use the built-in
  methods instead of manual JSON conversion.

  WRONG - Manual JSON conversion:
  # Don't do this - manual JSON handling
  json_str = doc.text
  json_data = json.loads(json_str)
  model = MyModel(**json_data)  # NO! Use as_pydantic_model

  # Don't do this - manual serialization
  json_str = model.model_dump_json()
  doc = MyDocument.create(name="data.json", content=json_str)  # NO!

  CORRECT - Direct Pydantic interaction:
  # Reading Pydantic model from document
  model = doc.as_pydantic_model(MyModel)  # Direct conversion
  models = doc.as_pydantic_model(list[MyModel])  # List support

  # Creating document from Pydantic model
  doc = MyDocument.create(
  name="data.json",
  content=model  # Direct BaseModel support
  )

  # Round-trip is seamless
  original_model = MyModel(field="value")
  doc = MyDocument.create(name="data.json", content=original_model)
  restored = doc.as_pydantic_model(MyModel)
  assert restored == original_model  # Perfect round-trip

**Example**:

  >>> from enum import StrEnum
  >>> from pydantic import BaseModel
  >>>
  >>> # Simple document:
  >>> class MyDocument(FlowDocument):
  ...     pass
  >>>
  >>> # Document with file restrictions:
  >>> class ConfigDocument(FlowDocument):
  ...     class FILES(StrEnum):
  ...         CONFIG = "config.yaml"
  ...         SETTINGS = "settings.json"
  >>>
  >>> # CORRECT FILES usage - no magic strings:
  >>> doc = ConfigDocument.create(
  ...     name=ConfigDocument.FILES.CONFIG,  # Use enum
  ...     content={"key": "value"}
  ... )
  >>>
  >>> # CORRECT Pydantic usage:
  >>> class Config(BaseModel):
  ...     key: str
  >>>
  >>> # Direct creation from Pydantic model
  >>> config_model = Config(key="value")
  >>> doc = MyDocument.create(name="data.json", content=config_model)
  >>>
  >>> # Direct extraction to Pydantic model
  >>> restored = doc.as_pydantic_model(Config)
  >>> print(restored.key)  # "value"
  >>>
  >>> # Track document provenance with sources
  >>> source_doc = MyDocument.create(name="input.txt", content="raw data")
  >>> processed = MyDocument.create(
  ...     name="output.txt",
  ...     content="processed data",
  ...     sources=[source_doc.sha256]  # Reference source document
  ... )
  >>> processed.has_source(source_doc)  # True
  >>>
  >>> # Document copying and type conversion:
  >>> # Standard Pydantic model_copy (doesn't validate updates)
  >>> copied = doc.model_copy(update={"name": "new_name.json"})
  >>> # Type conversion with validation via model_convert
  >>> task_doc = MyTaskDoc.create(name="temp.json", content={"data": "value"})
  >>> flow_doc = task_doc.model_convert(MyFlowDoc)  # Convert to FlowDocument
  >>> flow_doc.is_flow  # True

#### Document.MAX_CONTENT_SIZE

```python
MAX_CONTENT_SIZE: ClassVar[int] = 25 * 1024 * 1024
```

Maximum allowed content size in bytes (default 25MB).

#### Document.create

```python
@classmethod
def create(cls, *, name: str, content: str | bytes | dict[str, Any] | list[Any] | BaseModel, description: str | None = None, sources: list[str] | None = None) -> Self
```

Create a Document with automatic content type conversion (recommended).

This is the **recommended way to create documents**. It accepts various
content types and automatically converts them to bytes based on the file
extension. Use the `parse` method to reverse this conversion.

Best Practice (by default, unless instructed otherwise):
Only provide name and content. The description parameter is RARELY needed.

**Arguments**:

- `name` - Document filename (required, keyword-only).
  Extension determines serialization:
  - .json → JSON serialization
  - .yaml/.yml → YAML serialization
  - .md → Markdown list joining (for list[str])
  - Others → UTF-8 encoding (for str)
- `content` - Document content in various formats (required, keyword-only):
  - bytes: Used directly without conversion
  - str: Encoded to UTF-8 bytes
  - dict[str, Any]: Serialized to JSON (.json) or YAML (.yaml/.yml)
  - list[str]: Joined automatically for .md (validates format compatibility),
  else JSON/YAML
  - list[BaseModel]: Serialized to JSON or YAML based on extension
  - BaseModel: Serialized to JSON or YAML based on extension
- `description` - Optional description - USUALLY OMIT THIS (defaults to None).
  Only use when meaningful metadata helps downstream processing
- `sources` - Optional list of source strings (document SHA256 hashes or references).
  Used to track what sources contributed to creating this document.
  Can contain document SHA256 hashes (for referencing other documents)
  or arbitrary reference strings (URLs, file paths, descriptions).
  Defaults to empty list

**Returns**:

  New Document instance with content converted to bytes

**Raises**:

- `ValueError` - If content type is not supported for the file extension,
  or if markdown list format is incompatible
- `DocumentNameError` - If filename violates validation rules
- `DocumentSizeError` - If content exceeds MAX_CONTENT_SIZE

**Notes**:

  All conversions are reversible using the `parse` method.
  For example: MyDocument.create(name="data.json", content={"key": "value"}).parse(dict)
  returns the original dictionary {"key": "value"}.

**Example**:

  >>> # CORRECT - no description needed (by default, unless instructed otherwise)
  >>> doc = MyDocument.create(name="test.txt", content="Hello World")
  >>> doc.content  # b'Hello World'
  >>> doc.parse(str)  # "Hello World"

  >>> # CORRECT - Dictionary to JSON, no description
  >>> doc = MyDocument.create(name="config.json", content={"key": "value"})
  >>> doc.content  # b'{"key": "value", ...}'
  >>> doc.parse(dict)  # {"key": "value"}

  >>> # AVOID unless description adds real value
  >>> doc = MyDocument.create(
  ...     name="config.json",
  ...     content={"key": "value"},
  ...     description="Config file"  # Usually redundant!
  ... )

  >>> # Pydantic model to YAML
  >>> from pydantic import BaseModel
  >>> class Config(BaseModel):
  ...     host: str
  ...     port: int
  >>> config = Config(host="localhost", port=8080)
  >>> doc = MyDocument.create(name="config.yaml", content=config)
  >>> doc.parse(Config)  # Returns Config instance

  >>> # List to Markdown
  >>> items = ["Section 1", "Section 2"]
  >>> doc = MyDocument.create(name="sections.md", content=items)
  >>> doc.parse(list)  # ["Section 1", "Section 2"]

  >>> # Document with sources for provenance tracking
  >>> source_doc = MyDocument.create(name="source.txt", content="original")
  >>> derived = MyDocument.create(
  ...     name="result.txt",
  ...     content="processed",
  ...     sources=[source_doc.sha256, "https://api.example.com/data"]
  ... )
  >>> derived.get_source_documents()  # [source_doc.sha256]
  >>> derived.get_source_references()  # ["https://api.example.com/data"]

#### Document.__init__

```python
def __init__(self, *, name: str, content: bytes, description: str | None = None, sources: list[str] | None = None) -> None
```

Initialize a Document instance with raw bytes content.

Important:
**Most users should use the `create` classmethod instead of __init__.**
The create method provides automatic content conversion for various types
(str, dict, list, Pydantic models) while __init__ only accepts bytes.

This constructor accepts only bytes content for type safety. It prevents
direct instantiation of the abstract Document class.

**Arguments**:

- `name` - Document filename (required, keyword-only)
- `content` - Document content as raw bytes (required, keyword-only)
- `description` - Optional human-readable description (keyword-only)
- `sources` - Optional list of source strings for provenance tracking.
  Can contain document SHA256 hashes (for referencing other documents)
  or arbitrary reference strings (URLs, file paths, descriptions).
  Defaults to empty list

**Raises**:

- `TypeError` - If attempting to instantiate Document directly.

**Example**:

  >>> # Direct constructor - only for bytes content:
  >>> doc = MyDocument(name="test.txt", content=b"Hello World")
  >>> doc.content  # b'Hello World'

  >>> # RECOMMENDED: Use create for automatic conversion:
  >>> doc = MyDocument.create(name="text.txt", content="Hello World")
  >>> doc = MyDocument.create(name="data.json", content={"key": "value"})
  >>> doc = MyDocument.create(name="config.yaml", content=my_model)
  >>> doc = MyDocument.create(name="items.md", content=["item1", "item2"])

#### Document.id

```python
@final
@property
def id(self) -> str
```

Get a short unique identifier for the document.

This ID is crucial for LLM interactions. When documents are provided to
LLMs via generate() or generate_structured(), their IDs are included,
allowing the LLM to reference documents in prompts by either name or ID.
The ID is content-based (derived from SHA256 hash of content only),
so the same content always produces the same ID. Changing the name or
description does NOT change the ID.

**Returns**:

  6-character base32-encoded string (uppercase, e.g., "A7B2C9").
  This is the first 6 chars of the full base32 SHA256, NOT hex.

  Collision Rate:
  With base32 encoding (5 bits per char), 6 chars = 30 bits.
  Expect collisions after ~32K documents (birthday paradox).
  For higher uniqueness requirements, use the full sha256 property.

**Notes**:

  While shorter than full SHA256, this provides
  reasonable uniqueness for most use cases.

#### Document.sha256

```python
@final
@cached_property
def sha256(self) -> str
```

Get the full SHA256 hash of the document content.

Computes and caches the SHA256 hash of the content,
encoded in base32 (uppercase). Used for content
deduplication and integrity verification.

**Returns**:

  Full SHA256 hash as base32-encoded uppercase string.

  Why Base32 Instead of Hex:
  - Base32 is case-insensitive, avoiding issues with different file systems
  and AI interactions where casing might be inconsistent
  - More compact than hex (52 chars vs 64 chars for SHA-256)
  - Contains more information per character than hex (5 bits vs 4 bits)
  - Safe for URLs without encoding
  - Compatible with case-insensitive file systems
  - Avoids confusion in AI interactions where models might change casing
  - Not base64 because we want consistent uppercase for all uses

**Notes**:

  This is computed once and cached for performance.
  The hash is deterministic based on content only.

#### Document.size

```python
@final
@property
def size(self) -> int
```

Get the size of the document content.

**Returns**:

  Size of content in bytes.

**Notes**:

  Useful for monitoring document sizes and
  ensuring they stay within limits.

#### Document.mime_type

```python
@property
def mime_type(self) -> str
```

Get the document's MIME type.

Primary property for accessing MIME type information.
Automatically detects MIME type based on file extension and content.

**Returns**:

  MIME type string (e.g., "text/plain", "application/json").

**Notes**:

  MIME type detection uses extension-based detection for known
  text formats and content analysis for binary formats.

#### Document.is_text

```python
@property
def is_text(self) -> bool
```

Check if document contains text content.

**Returns**:

  True if MIME type indicates text content
  (text/*, application/json, application/x-yaml, text/yaml, etc.),
  False otherwise.

**Notes**:

  Used to determine if text property can be safely accessed.

#### Document.is_pdf

```python
@property
def is_pdf(self) -> bool
```

Check if document is a PDF file.

**Returns**:

  True if MIME type is application/pdf, False otherwise.

**Notes**:

  PDF documents require special handling and are
  supported by certain LLM models.

#### Document.is_image

```python
@property
def is_image(self) -> bool
```

Check if document is an image file.

**Returns**:

  True if MIME type starts with "image/", False otherwise.

**Notes**:

  Image documents are automatically encoded for
  vision-capable LLM models.

#### Document.text

```python
@property
def text(self) -> str
```

Get document content as UTF-8 text string.

Decodes the bytes content as UTF-8 text. Only available for
text-based documents (check is_text property first).

**Returns**:

  UTF-8 decoded string.

**Raises**:

- `ValueError` - If document is not text (is_text == False).

**Example**:

  >>> doc = MyDocument.create(name="data.txt", content="Hello ✨")
  >>> if doc.is_text:
  ...     print(doc.text)  # "Hello ✨"

  >>> # Binary document raises error:
  >>> binary_doc = MyDocument(name="image.png", content=png_bytes)
  >>> binary_doc.text  # Raises ValueError

#### Document.approximate_tokens_count

```python
@property
def approximate_tokens_count(self) -> int
```

Approximate tokens count for the document content.

Uses tiktoken with gpt-4 encoding to estimate token count.
For text documents, encodes the actual text. For non-text
documents (images, PDFs, etc.), returns a fixed estimate of 1024 tokens.

**Returns**:

  Approximate number of tokens for this document.

**Example**:

  >>> doc = MyDocument.create(name="data.txt", content="Hello world")
  >>> doc.approximate_tokens_count  # ~2 tokens

#### Document.as_pydantic_model

```python
def as_pydantic_model(self, model_type: type[TModel] | type[list[TModel]]) -> TModel | list[TModel]
```

Parse document content as Pydantic model with validation.

Parses JSON or YAML content and validates it against a Pydantic model.
Automatically detects format based on MIME type. Supports both single
models and lists of models.

**Arguments**:

- `model_type` - Pydantic model class to validate against.
  Can be either:
  - type[Model] for single model
  - type[list[Model]] for list of models

**Returns**:

  Validated Pydantic model instance or list of instances.

**Raises**:

- `ValueError` - If document is not text or type mismatch.
- `ValidationError` - If data doesn't match model schema.
- `JSONDecodeError/YAMLError` - If content parsing fails.

**Example**:

  >>> from pydantic import BaseModel
  >>>
  >>> class User(BaseModel):
  ...     name: str
  ...     age: int
  >>>
  >>> # Single model
  >>> doc = MyDocument.create(name="user.json",
  ...     content={"name": "Alice", "age": 30})
  >>> user = doc.as_pydantic_model(User)
  >>> print(user.name)  # "Alice"
  >>>
  >>> # List of models
  >>> doc2 = MyDocument.create(name="users.json",
  ...     content=[{"name": "Bob", "age": 25}, {"name": "Eve", "age": 28}])
  >>> users = doc2.as_pydantic_model(list[User])
  >>> print(len(users))  # 2

#### Document.as_markdown_list

```python
def as_markdown_list(self) -> list[str]
```

Parse document as markdown-separated list of sections.

Splits text content automatically using markdown section separators.
Designed for markdown documents with multiple sections.

**Returns**:

  List of string sections (preserves whitespace within sections).

**Raises**:

- `ValueError` - If document is not text-based.

**Example**:

  >>> # Using create with list
  >>> sections = ["# Chapter 1\nIntroduction", "# Chapter 2\nDetails"]
  >>> doc = MyDocument.create(name="book.md", content=sections)
  >>> doc.as_markdown_list()  # Returns original sections

  >>> # Round-trip conversion works automatically
  >>> sections = ["Part 1", "Part 2", "Part 3"]
  >>> doc2 = MyDocument.create(name="parts.md", content=sections)
  >>> doc2.as_markdown_list()  # ['Part 1', 'Part 2', 'Part 3']

#### Document.parse

```python
def parse(self, type_: type[Any]) -> Any
```

Parse document content to original type (reverses create conversion).

This method reverses the automatic conversion performed by the `create`
classmethod. It intelligently parses the bytes content based on the
document's file extension and converts to the requested type.

Designed for roundtrip conversion:
>>> original = {"key": "value"}
>>> doc = MyDocument.create(name="data.json", content=original)
>>> restored = doc.parse(dict)
>>> assert restored == original  # True

**Arguments**:

- `type_` - Target type to parse content into. Supported types:
  - bytes: Returns raw content (no conversion)
  - str: Decodes UTF-8 text
  - dict: Parses JSON (.json) or YAML (.yaml/.yml)
  - list: Splits markdown (.md) or parses JSON/YAML
  - BaseModel subclasses: Validates JSON/YAML into model

**Returns**:

  Content parsed to the requested type.

**Raises**:

- `ValueError` - If type is unsupported or parsing fails.

  Extension Rules:
  - .json → JSON parsing for dict/list/BaseModel
  - .yaml/.yml → YAML parsing for dict/list/BaseModel
  - .md + list → Split automatically into sections
  - Any + str → UTF-8 decode
  - Any + bytes → Raw content

**Example**:

  >>> # String content
  >>> doc = MyDocument(name="test.txt", content=b"Hello")
  >>> doc.parse(str)
  'Hello'

  >>> # JSON content
  >>> doc = MyDocument.create(name="data.json", content={"key": "value"})
  >>> doc.parse(dict)  # Returns {'key': 'value'}

  >>> # Markdown list
  >>> items = ["Item 1", "Item 2"]
  >>> doc = MyDocument.create(name="list.md", content=items)
  >>> doc.parse(list)
  ['Item 1', 'Item 2']

#### Document.model_convert

```python
@final
def model_convert(self, new_type: type[TDocument], *, update: dict[str, Any] | None = None, deep: bool = False) -> TDocument
```

Convert document to a different Document type with optional updates.

Creates a new document of a different type, preserving all attributes
while allowing updates. This is useful for converting between document
types (e.g., TaskDocument to FlowDocument) while maintaining data integrity.

**Arguments**:

- `new_type` - Target Document class for conversion. Must be a concrete
  subclass of Document (not abstract classes like Document,
  FlowDocument, or TaskDocument).
- `update` - Dictionary of attributes to update. Supports any attributes
  that the Document constructor accepts (name, content,
  description, sources).
- `deep` - Whether to perform a deep copy of mutable attributes.

**Returns**:

  New Document instance of the specified type.

**Raises**:

- `TypeError` - If new_type is not a subclass of Document, is an abstract
  class, or if update contains invalid attributes.
- `DocumentNameError` - If the name violates the target type's FILES enum.
- `DocumentSizeError` - If content exceeds MAX_CONTENT_SIZE.

**Example**:

  >>> # Convert TaskDocument to FlowDocument
  >>> task_doc = MyTaskDoc.create(name="temp.json", content={"data": "value"})
  >>> flow_doc = task_doc.model_convert(MyFlowDoc)
  >>> assert flow_doc.is_flow
  >>> assert flow_doc.content == task_doc.content
  >>>
  >>> # Convert with updates
  >>> updated = task_doc.model_convert(
  ...     MyFlowDoc,
  ...     update={"name": "permanent.json", "description": "Converted"}
  ... )
  >>>
  >>> # Track document lineage
  >>> derived = doc.model_convert(
  ...     ProcessedDoc,
  ...     update={"sources": [doc.sha256]}
  ... )


## ai_pipeline_core.documents

Document abstraction system for AI pipeline flows.

The documents package provides immutable, type-safe data structures for handling
various content types in AI pipelines, including text, images, PDFs, and other
binary data with automatic MIME type detection.


## ai_pipeline_core.documents.flow_document

Flow-specific document base class for persistent pipeline data.

This module provides the FlowDocument abstract base class for documents
that need to persist across Prefect flow runs and between pipeline steps.

### FlowDocument

```python
class FlowDocument(Document)
```

Abstract base class for documents that persist across flow runs.

FlowDocument is used for data that needs to be saved between pipeline
steps and across multiple flow executions. These documents are typically
written to the file system using the simple_runner utilities.

Key characteristics:
- Persisted to file system between pipeline steps
- Survives across multiple flow runs
- Used for flow inputs and outputs
- Saved in directories organized by the document's type/name

Creating FlowDocuments:
Same as Document - use `create()` for automatic conversion, `__init__` for bytes.
See Document.create() for detailed usage examples.

Persistence:
Documents are saved under an output directory path associated with the document's type/name.
For example: output/my_doc/data.json

**Notes**:

  - Cannot instantiate FlowDocument directly - must subclass
  - Used with FlowConfig to define flow input/output types
  - No additional abstract methods to implement


## ai_pipeline_core.documents.document_list

Type-safe list container for Document objects.

### DocumentList

```python
class DocumentList(list[Document])
```

Type-safe container for Document objects.

Specialized list with validation and filtering for documents.

Best Practice: Use default constructor by default, unless instructed otherwise.
Only enable validate_same_type or validate_duplicates when you explicitly need them.

**Example**:

  >>> # RECOMMENDED - default constructor for most cases
  >>> docs = DocumentList([doc1, doc2])
  >>> # Or empty initialization
  >>> docs = DocumentList()
  >>> docs.append(MyDocument(name="file.txt", content=b"data"))
  >>>
  >>> # Only use validation flags when specifically needed:
  >>> docs = DocumentList(validate_same_type=True)  # Rare use case
  >>> doc = docs.get_by("file.txt")  # Get by name

#### DocumentList.__init__

```python
def __init__(self, documents: list[Document] | None = None, validate_same_type: bool = False, validate_duplicates: bool = False, frozen: bool = False) -> None
```

Initialize DocumentList.

**Arguments**:

- `documents` - Initial list of documents.
- `validate_same_type` - Enforce same document type.
- `validate_duplicates` - Prevent duplicate filenames.
- `frozen` - If True, list is immutable from creation.

#### DocumentList.filter_by

```python
def filter_by(self, arg: str | type[Document] | Iterable[type[Document]] | Iterable[str]) -> "DocumentList"
```

Filter documents by name(s) or type(s).

ALWAYS returns a DocumentList (which may be empty), never raises an exception
for no matches. Use this when you want to process all matching documents.

**Arguments**:

- `arg` - Can be one of:
  - str: Single document name to filter by
  - type[Document]: Single document type to filter by (includes subclasses)
  - Iterable[type[Document]]: Multiple document types to filter by
  (list, tuple, set, generator, or any iterable)
  - Iterable[str]: Multiple document names to filter by
  (list, tuple, set, generator, or any iterable)

**Returns**:

  New DocumentList with filtered documents (may be empty).
  - Returns ALL matching documents
  - Empty DocumentList if no matches found

**Raises**:

- `TypeError` - If arg is not a valid type (not str, type, or iterable),
  or if iterable contains mixed types (strings and types together).
- `AttributeError` - If arg is expected to be iterable but doesn't support iteration.

**Example**:

  >>> # Returns list with all matching documents
  >>> matching_docs = docs.filter_by("file.txt")  # May be empty
  >>> for doc in matching_docs:
  ...     process(doc)
  >>>
  >>> # Filter by type - returns all instances
  >>> config_docs = docs.filter_by(ConfigDocument)
  >>> print(f"Found {len(config_docs)} config documents")
  >>>
  >>> # Filter by multiple names
  >>> important_docs = docs.filter_by(["config.yaml", "settings.json"])
  >>> if not important_docs:  # Check if empty
  ...     print("No important documents found")

#### DocumentList.get_by

```python
def get_by(self, arg: str | type[Document], required: bool = True) -> Document | None
```

Get EXACTLY ONE document by name or type.

IMPORTANT: This method expects to find exactly one matching document.
- If no matches and required=True: raises ValueError
- If no matches and required=False: returns None
- If multiple matches: ALWAYS raises ValueError (ambiguous)

When required=True (default), you do NOT need to check for None:
>>> doc = docs.get_by("config.yaml")  # Will raise if not found
>>> # No need for: if doc is not None  <- This is redundant!
>>> print(doc.content)  # Safe to use directly

**Arguments**:

- `arg` - Document name (str) or document type.
- `required` - If True (default), raises ValueError when not found.
  If False, returns None when not found.

**Returns**:

  The single matching document, or None if not found and required=False.

**Raises**:

- `ValueError` - If required=True and document not found, OR if multiple
  documents match (ambiguous result).
- `TypeError` - If arg is not a string or Document type.

**Example**:

  >>> # CORRECT - No need to check for None when required=True (default)
  >>> doc = docs.get_by("file.txt")  # Raises if not found
  >>> print(doc.content)  # Safe to use directly
  >>>
  >>> # When using required=False, check for None
  >>> doc = docs.get_by("optional.txt", required=False)
  >>> if doc is not None:
  ...     print(doc.content)
  >>>
  >>> # Will raise if multiple documents have same type
  >>> # Use filter_by() instead if you want all matches
  >>> try:
  ...     doc = docs.get_by(ConfigDocument)  # Error if 2+ configs
  >>> except ValueError as e:
  ...     configs = docs.filter_by(ConfigDocument)  # Get all instead
