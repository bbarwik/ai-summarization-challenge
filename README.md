# AI Pipeline Template

A production-ready starter for building sophisticated AI pipelines with **ai-pipeline-core**. It gives you a clean, opinionated foundation for async workflows, type-safe documents, and end-to-end observability.

## Why this template

* **Document‑centric** architecture (immutable Pydantic models)
* **Type‑safe flows** via `FlowConfig` with compile‑time ergonomics & runtime validation
* **Async‑first** I/O for throughput
* **Unified LLM interface** through `ai-pipeline-core.llm` (LiteLLM proxy compatible)
* **Observability** via LMNR tracing and Prefect integration

## Prerequisites

* Python **3.12+**
* Access to a LiteLLM proxy (or any OpenAI‑compatible endpoint)
* Optional: Prefect server/cloud if you want remote orchestration

## Install

```bash
# Clone and install
pip install -e .

# Dev setup (ruff, basedpyright, pre-commit, pytest)
make install-dev
```

### DevContainer Setup (Optional)

For VS Code DevContainer users who need overrides:

```bash
# Copy the example file and customize it
cp .devcontainer/docker-compose.override.yml.example .devcontainer/docker-compose.override.yml

# Edit devcontainer.json to include the override file
# Change: "dockerComposeFile": "docker-compose.yml",
# To: "dockerComposeFile": ["docker-compose.yml", "docker-compose.override.yml"],
```

The `docker-compose.override.yml` file is gitignored and can contain user-specific mounts and network configurations.

## Quick start

```bash
# Run the template pipeline with defaults
python -m ai_pipeline ./projects/my_project

# Select a flow range (indices are 1-based in this template)
python -m ai_pipeline ./projects/my_project --start 2 --end 3

# Choose models from FlowOptions
python -m ai_pipeline ./projects/my_project \
  --core-model "gpt-5" \
  --small-model "gpt-5-mini"

# Debug traces
LMNR_DEBUG=true python -m ai_pipeline ./projects/my_project
```

## Configuration

Set these environment variables (typically in a `.env` file):

```bash
# Required for LLM operations (OpenAI-compatible via LiteLLM proxy)
OPENAI_BASE_URL=http://localhost:4000
OPENAI_API_KEY=sk-...

# Optional services
PREFECT_API_URL=http://localhost:4200
PREFECT_API_KEY=pnu_...
LMNR_PROJECT_API_KEY=lmnr_...
LMNR_DEBUG=true
```

## Project layout

```
ai_pipeline/
├── documents/                    # One file = one document class
│   ├── flow/                     # Persistent documents
│   └── task/                     # Ephemeral (task-scoped) documents
├── flows/                        # Flows with colocated tasks & prompts
│   └── step_01_example/
│       ├── example_flow.py       # Flow + FlowConfig
│       └── tasks/
│           ├── process_task.py   # Task
│           └── process_task.jinja2  # Matching prompt
├── tasks/                        # Shared tasks used by multiple flows
├── prompts/                      # Shared prompts
├── flow_options.py               # ProjectFlowOptions extends FlowOptions
└── __main__.py                   # CLI entry (uses simple_runner)
```

## Everyday commands

```bash
make lint        # Ruff
make format      # Formatting
make typecheck   # basedpyright (must be 0 errors)
make test        # Unit tests
make test-cov    # Tests with coverage
make clean       # Remove build artifacts
```

## Development handbook

For detailed patterns (flows, tasks, documents, testing, prompts, logging, etc.), see **DEVELOPMENT.md**.

If you’re an AI assistant working in this repo, see **CLAUDE.md** for rules and navigation tips.

## License

MIT
