# AI Summarization Pipeline — Recruitment Task

A practical challenge for candidates experienced with LLMs and prompt engineering.
You’ll design an AI pipeline that converts **~200k tokens** of input documents into a **concise, detailed report** while keeping API **costs under $2** and **without preprocessing** (see definition below).

This repository includes a working but intentionally simple **4-step baseline**:
**Planning → Writing → Review → Rewrite.**
It runs end-to-end and demonstrates the mechanics, but it’s **not very efficient** and will often produce **duplicated** or **incorrect** information. Your goal is to propose and/or implement a **better approach** that yields a more faithful, compact report.

> Framework: This project uses **[ai-pipeline-core](https://github.com/bbarwik/ai-pipeline-core)** for async, typed, document-centric AI workflows.
> Agents: Designed to work smoothly with **Claude Code** by default, but it should also work well with other AI coding agents.

## What you’re solving

In my main project we repeatedly need to **rewrite many long documents into a shorter one**
(e.g., **~200k tokens → ~40k tokens**). Much of the input is **duplicated**, so compression is possible, but dealing with **very large contexts** is tricky. Two recurring problems must be addressed:

1. **Duplication & Coverage**
   - The output should **remove redundancy** while **preserving all important information**.
   - Even when content is repeated across files, the consolidated report should include it **once**, with sufficient detail.

2. **Fact Consistency & Temporal Accuracy**
   - Models frequently **mix up facts** across sources.
   - Newer documents should **override** older ones (e.g., a **2025** update supersedes a **2023** claim).
   - The pipeline should **prefer the latest source** when conflicts arise and avoid stale statements.

You **do not** need to fully solve these challenges here—it’s a hard problem that can take days.
The aim is to **show that you understand the problem** and to present **credible ideas and techniques** to tackle it under the constraints.

## Constraints (read carefully)

- **No preprocessing.**
  _What this means here:_
  - ❌ No offline chunking/splitting, embeddings, vector DBs, RAG pipelines, or external ETL.
  - ❌ No external retrieval from the web or tools not included in this repo.
  - ✅ You **may** use **multi-step prompting**, message/content routing **within** the LLM calls, provider **caching** (where available), and structured outputs.
  - ✅ You **may** reorganize prompts/flows and use intermediate drafts/plans inside the pipeline—those are still **direct LLM transformations**.

- **Cost cap:** keep **total LLM interactions under $2** for the full run on the supplied input set.
- **Immutability of inputs:** you can refactor anything in the project **except** the files in `workspace/input/`.
- **Output:** a **detailed, accurate** report at `workspace/output/final_report.md`, with **minimal duplication** and **correct, up-to-date facts**.

## Baseline provided (intentionally simple)

The repo ships with a four-stage pipeline:

1. **Planning** — draft a report outline from all inputs
2. **Writing** — produce the first full draft following the plan
3. **Review** — critique the draft and identify gaps/inaccuracies
4. **Rewrite** — generate a polished final report incorporating the review

This works as a teaching scaffold but is **not optimized** for:
- Large-context efficiency,
- De-duplication,
- Temporal conflict resolution,
- Cost control under the **$2** cap.

Your task is to **redesign prompts/flow/tasks** to improve these aspects while respecting **No preprocessing**.

## Helper script

There’s a handy script to snapshot the project tree:
```bash
scripts/list_all_files.sh > files.log
```

You can then **upload content of `files.log` to any AI model** (e.g., gpt-5) to help it navigate the repo.

## Evaluation

We’re looking for:

* **Prompt & pipeline design** for large contexts (plans, selective conditioning, citation-style grounding within the allowed rules).
* **De-duplication strategies** that preserve critical information while cutting redundancy.
* **Temporal accuracy techniques** (e.g., encouraging date extraction, conflict detection, “newer wins” rules).
* **Cost awareness**—staying under **\$2** with reasonable quality.
* **Code clarity**—minimal, typed, async code that’s easy to reason about.

> You can change anything you want except the `workspace/input` documents. The shipped solution is only a template to demonstrate a simple approach.

## 📁 Project Structure

The project uses a 4-stage pipeline architecture:

```
workspace/
├── input/          # Source documents (~200k tokens)
├── plan/           # Stage 1: Report structure planning
├── draft/          # Stage 2: Initial report draft
├── review/         # Stage 3: Quality review and feedback
└── output/         # Stage 4: Final polished report

ai_summarization/
├── flows/
│   ├── step_01_planning/    # Creates report outline
│   ├── step_02_writing/     # Writes initial draft
│   ├── step_03_review/      # Reviews and provides feedback
│   └── step_04_rewrite/     # Produces final report
├── documents/               # Document type definitions
├── prompts/                 # Shared prompt templates
└── flow_options.py         # Task configuration
```

## 🚀 Quick Start

### Option 1: GitHub Codespaces (Recommended)
1. Click "Code" → "Codespaces" → "Create codespace on main"
2. Wait for environment setup
3. Configure `.env` file (see below)
4. Run the pipeline

### Option 2: DevContainer (VS Code)
1. Clone the repository
2. Open in VS Code with DevContainer extension
3. Reopen in container when prompted
4. Configure `.env` file (see below)
5. Run the pipeline

### Option 3: Local Setup
```bash
# Clone repository
git clone <repository-url>
cd ai-summarization

# Install dependencies
pip install -e .

# Or for development
make install-dev
```

## Configuration

Create a `.env` file in the project root:

```bash
# Required: OpenAI-compatible API endpoint
# Recommended: Use OpenRouter for model variety
OPENAI_BASE_URL=https://openrouter.ai/api/v1
OPENAI_API_KEY=your-openrouter-api-key

# Optional but recommended: LLM observability
# Sign up free at https://laminar.sh/
LMNR_PROJECT_API_KEY=your-laminar-key
LMNR_DEBUG=false

# Note: Prefect configuration is NOT needed in .env
```

### Getting API Keys

1. **OpenRouter** (https://openrouter.ai/):
   - Sign up for free account
   - Add credits ($5 minimum)
   - Copy API key from dashboard
   - Access to 100+ models including GPT-4, Claude, Gemini, etc.

2. **Laminar** (https://laminar.sh/) - Optional but recommended:
   - Sign up for free account
   - Create new project
   - Copy project API key
   - Provides detailed LLM usage tracking and cost monitoring

## 🏃 Running the Pipeline

### Full Pipeline Execution
```bash
# Process all documents through all 4 stages
python -m ai_summarization workspace/
```

### Partial Execution
```bash
# Run specific stages (1-indexed)
python -m ai_summarization workspace/ --start 2 --end 3

# Run only planning stage
python -m ai_summarization workspace/ --start 1 --end 1
```

### Model Selection
```bash
# Use specific models (check OpenRouter for available models)
python -m ai_summarization workspace/ \
  --core-model "google/gemini-2.5-pro" \
  --small-model "gpt-5-mini"
```

### Debug Mode
```bash
# Enable detailed tracing
LMNR_DEBUG=true python -m ai_summarization workspace/
```

## Current Approach

The pipeline implements a simple 4-stage approach:

1. **Planning Stage** (`step_01_planning`)
   - Analyzes all input documents
   - Creates structured report outline
   - Identifies key themes and companies
   - Output: `workspace/plan/report_plan.md`

2. **Writing Stage** (`step_02_writing`)
   - Uses the plan to write initial draft
   - Processes documents in context
   - Generates comprehensive content
   - Output: `workspace/draft/report_draft.md`

3. **Review Stage** (`step_03_review`)
   - Evaluates draft quality
   - Identifies gaps and improvements
   - Provides structured feedback
   - Output: `workspace/review/report_review.md`

4. **Rewrite Stage** (`step_04_rewrite`)
   - Incorporates review feedback
   - Polishes and refines content
   - Produces final report
   - Output: `workspace/output/final_report.md`

## 🧪 Development

### Testing
```bash
make test           # Run tests
make test-cov      # Run with coverage
```

### Code Quality
```bash
make lint          # Run linting
make format        # Auto-format code
make typecheck     # Type checking
```

### Pre-commit Hooks
```bash
make install-dev   # Installs pre-commit hooks
```

## 📊 Task Details

The pipeline processes research documents about AI assistant companies and generates a comprehensive report including:

- **Company Introductions**: Detailed overview of each AI assistant project
- **Project Status**: Current development stage and availability
- **Timeline & Milestones**: Key achievements and historical context
- **Future Plans**: Roadmap and upcoming features
- **Comparative Analysis**: Strengths and weaknesses of each solution
- **Market Positioning**: How projects compare to each other

The report uses only the provided input documents without external knowledge, ensuring objectivity and accuracy based on the supplied research materials.

## 🎓 Evaluation Criteria

Your solution will be evaluated on:

1. **Prompt Engineering**: Quality and efficiency of prompts
2. **Cost Efficiency**: Staying under $2 while maintaining quality
3. **Output Quality**: Comprehensiveness and accuracy of the final report
4. **Code Quality**: Clean, maintainable pipeline implementation
5. **Innovation**: Creative approaches to the token/cost constraints

## 🤝 Support

- **Framework Documentation**: See `dependencies_docs/ai-pipeline-core.md`
- **Development Guide**: See `DEVELOPMENT.md` for detailed patterns
- **Claude Integration**: See `CLAUDE.md` for AI assistant guidelines

## 📌 Important Notes

- The project is designed to work out-of-the-box with DevContainers or Codespaces
- All you need is to configure the `.env` file with your API keys
- The pipeline is fully async for optimal performance
- Prefect orchestration is built-in but requires no configuration
- The `--start` and `--end` indices are 1-based (1-4 for the 4 flows)
