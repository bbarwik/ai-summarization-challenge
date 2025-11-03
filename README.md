# AI Summarization Challenge — Recruitment Task

A practical challenge for candidates experienced with LLMs and prompt engineering.
You'll design an AI pipeline that analyzes **USDe stablecoin research documents** (~200k tokens) and produces a **structured confidence-based research report** while keeping API **costs under $1** and **without preprocessing** (see definition below).

This repository includes a working but intentionally simple **4-step baseline**:
**Planning → Writing → Review → Rewrite.**
It runs end-to-end and demonstrates the mechanics, but it's **not very efficient** and will often produce **duplicated**, **conflicting**, or **incorrect** information. Your goal is to propose and/or implement a **better approach** that yields a more accurate, well-structured report with proper confidence scoring.

## Useful Resources

These articles provide valuable insights for tackling long-context challenges:

- **[Long Context Handling in LLMs](https://nrehiew.github.io/blog/long_context/)** - Discusses context rot, effective benchmarking, and the gap between advertised vs. actual context window capabilities. Key insight: models claiming 1M tokens often function effectively only within 32K-128K tokens.

- **[Fiction.liveBench](https://fiction.live/stories/Fiction-liveBench-Feb-21-2025/oQdzQvKHw8JyXbN87)** - Benchmark for evaluating long-context performance.

> Framework: This project uses **[ai-pipeline-core](https://github.com/bbarwik/ai-pipeline-core)** for async, typed, document-centric AI workflows.
> Agents: Designed to work smoothly with **Claude Code** by default, but it should also work well with other AI coding agents.

## What you're solving

This pipeline analyzes multiple research documents about **USDe stablecoin** and produces a structured final research report. The input documents contain overlapping information, conflicting claims, and varying levels of reliability. You need to consolidate this into a **confidence-scored analysis** that addresses several challenges:

1. **Information Validation & Confidence Scoring**
   - Classify findings by confidence level (HIGH, MEDIUM, LOW) based on source agreement
   - HIGH: Multiple sources confirm without conflicts
   - MEDIUM: Multiple sources with resolved conflicts
   - LOW: Single source or unresolved conflicts

2. **Conflict Detection & Resolution**
   - Identify where sources disagree
   - Resolve conflicts when possible (e.g., using temporal ordering, source reliability)
   - Explicitly document unresolved conflicts

3. **Temporal Accuracy & Timeline Construction**
   - Extract dates and build an accurate timeline of events
   - Newer information should supersede older claims
   - Assign confidence levels to each timeline entry

4. **Information Quality Assessment**
   - Flag potentially incorrect information with reasoning
   - Identify critical data gaps requiring further research
   - Avoid hallucination and unsupported claims

You **do not** need to perfectly solve these challenges—it's complex work that can take days.
The aim is to **show that you understand the problem** and to present **credible techniques** to tackle it under the $1 cost constraint.

## Expected Output Structure

The final report at `workspace/output/final_report.md` should contain:

1. **Executive Summary** (200-500 words)
   - Report goal, purpose, and key findings

2. **Timeline**
   - Chronological events using YYYY-MM-DD format
   - Confidence level for each event (HIGH, MEDIUM, LOW)

3. **High Confidence Findings**
   - Information confirmed by multiple sources without conflicts

4. **Medium Confidence Findings**
   - Information from multiple sources with resolved conflicts

5. **Low Confidence Findings**
   - Information from single source or unresolved conflicts

6. **Conflicting Information**
   - All contradictions with resolutions (where possible)

7. **Potentially Incorrect Information**
   - Suspicious claims with explanations of why they may be wrong

8. **Data Gaps and Missing Information**
   - Critical gaps requiring further research

The report must use **only** the provided USDe research documents without external knowledge or hallucination.

## Constraints (read carefully)

- **No preprocessing.**
  _What this means here:_
  - ❌ No offline chunking/splitting, embeddings, vector DBs, RAG pipelines, or external ETL.
  - ❌ No external retrieval from the web or tools not included in this repo.
  - ✅ You **may** use **multi-step prompting**, message/content routing **within** the LLM calls, provider **caching** (where available), and structured outputs.
  - ✅ You **may** reorganize prompts/flows and use intermediate drafts/plans inside the pipeline—those are still **direct LLM transformations**.

- **Cost cap:** keep **total LLM interactions under $1** for the full run on the USDe research documents.
- **Immutability of inputs:** you can refactor anything in the project **except** the files in `workspace/input/`.
- **Output:** a **detailed, accurate** report at `workspace/output/final_report.md`.

> You can change anything you want except the `workspace/input` documents. The shipped solution is only a template to demonstrate a simple approach.

## Baseline provided (intentionally simple)

The repo ships with a four-stage pipeline:

1. **Planning** — analyzes documents, creates timeline, identifies conflicts
2. **Writing** — produces first draft with confidence-based structure
3. **Review** — verifies confidence levels and conflict resolution
4. **Rewrite** — generates polished final report

This works as a teaching scaffold but is **not optimized** for:
- Large-context efficiency
- Confidence-based information validation
- Conflict detection and resolution
- Temporal accuracy and timeline construction
- Cost control under the **$1** cap

Your task is to **redesign prompts/flow/tasks** to improve these aspects while respecting **No preprocessing**.

## 📁 Project Structure

```
workspace/
├── input/          # USDe research documents (~200k tokens)
├── plan/           # Stage 1: Analysis and planning
├── draft/          # Stage 2: Initial report draft
├── review/         # Stage 3: Quality review and feedback
└── output/         # Stage 4: Final polished report

ai_summarization/
├── flows/
│   ├── step_01_planning/    # Document analysis and planning
│   ├── step_02_writing/     # Initial draft generation
│   ├── step_03_review/      # Quality verification
│   └── step_04_rewrite/     # Final report production
├── documents/               # Document type definitions
├── prompts/                 # Shared prompt templates
└── flow_options.py         # Configuration
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
pip install -e .
```

## Configuration

Create a `.env` file in the project root:

```bash
# Required: OpenAI-compatible API endpoint
OPENAI_BASE_URL=https://openrouter.ai/api/v1
OPENAI_API_KEY=your-openrouter-api-key

# Optional but recommended: LLM observability
LMNR_PROJECT_API_KEY=your-laminar-key
LMNR_DEBUG=false
```

**Getting API Keys:**
- **OpenRouter** (https://openrouter.ai/): Access to 100+ models including GPT-4, Claude, Gemini
- **Laminar** (https://laminar.sh/): Optional - provides LLM usage tracking and cost monitoring

## 🏃 Running the Pipeline

### Full Pipeline Execution
```bash
# Process all documents through all 4 stages
python -m ai_summarization workspace/
```

### Partial Execution
```bash
# Run specific stages (1-indexed, 1-4)
python -m ai_summarization workspace/ --start 2 --end 3

# Run only planning stage
python -m ai_summarization workspace/ --start 1 --end 1
```

### Model Selection
```bash
# Use specific models (check OpenRouter for available models)
python -m ai_summarization workspace/ --core-model "x-ai/grok-4-fast"
```

### Debug Mode
```bash
# Enable detailed tracing
LMNR_DEBUG=true python -m ai_summarization workspace/
```

## 🎓 Evaluation Criteria

Your solution will be evaluated on:

1. **Prompt & Pipeline Design**
   - Quality and efficiency of prompts for large contexts
   - Effective confidence-based analysis approach
   - Information validation strategies based on source agreement

2. **Conflict Detection & Resolution**
   - Techniques to identify and handle contradictory information
   - Temporal accuracy (date extraction, timeline construction, "newer wins" rules)

3. **Cost Efficiency**
   - Staying under **$1** while maintaining quality
   - Creative approaches to the token/cost constraints

4. **Output Quality**
   - Comprehensiveness and accuracy of the final report
   - Proper confidence level assignments
   - Minimal duplication and correct facts

## 📌 Important Notes

- The project is designed to work out-of-the-box with DevContainers or Codespaces
- The pipeline is fully async for optimal performance
- Framework documentation is available in `dependencies_docs/ai-pipeline-core.md`
- The `--start` and `--end` indices are 1-based (1-4 for the 4 flows)
