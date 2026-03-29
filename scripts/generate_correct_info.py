#!/usr/bin/env python3
"""Generate correct_information.md by filtering out incorrect claims from research documents."""

import argparse
import os
import sys
from pathlib import Path

import httpx


def load_env():
    """Load environment variables from .env file in same directory as script."""
    env_path = Path(__file__).parent / ".env"
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, value = line.split("=", 1)
                    os.environ[key.strip()] = value.strip().strip('"').strip("'")


load_env()

EXTRACTION_PROMPT = """You are an expert analyst reviewing USDe stablecoin research documents.

## YOUR TASK
Read through the research documents and extract claims that are CORRECT (not incorrect).

## FILTERING RULES

### EXCLUDE (do NOT include in output) if:
1. **Ground truth match**: The claim appears in the list of known incorrect claims below
2. **Common sense failure**: The claim violates basic math, physics, or
   temporal logic in an obvious way:
   - Negative values that cannot be negative (TVL, supply, prices, time, reserves)
   - Percentages over 100% that are explicitly described as impossible
   - Dates that don't exist (Feb 30, month 13, day 32, etc.)
   - Future dates beyond reasonable projection
   - Events that violate causality (effect before cause)
   - Claims from obviously fictional sources (Mars colonies, alien technology, time travel, etc.)
   - Mathematically self-contradictory statements

### INCLUDE (add to output) if:
- The claim passes both filters above
- Even if uncertain or unusual, if it's not obviously wrong

## KNOWN INCORRECT CLAIMS (Ground Truth)
```markdown
{ground_truth_content}
```

## RESEARCH DOCUMENTS TO ANALYZE
```markdown
{research_documents}
```

## OUTPUT FORMAT
For each document, list the claims that are CORRECT (passed both filters):

```markdown
# Correct Information for USDe Research Documents

## 1. asset_quality_analysis.md

### Correct Claims
- [claim 1]
- [claim 2]
...

## 2. audit_security_review.md

### Correct Claims
- [claim 1]
...
```

Important:
- Only list claims that are NOT incorrect
- If you're unsure whether a claim is correct, include it anyway
- Be concise - extract the key factual claims, not entire paragraphs
- Focus on: dates, numbers, events, mechanisms, relationships
- Output valid markdown only, no commentary
"""


def load_file(path: str) -> str:
    with open(path) as f:
        return f.read()


def build_prompt(ground_truth: str, documents: list[tuple[str, str]]) -> str:
    docs_content = "\n\n".join(f"=== {name} ===\n{content}" for name, content in documents)
    return EXTRACTION_PROMPT.format(
        ground_truth_content=ground_truth,
        research_documents=docs_content,
    )


def call_openrouter(prompt: str, model: str) -> str:
    api_key = os.environ.get("OPENAI_API_KEY")
    base_url = os.environ.get("OPENAI_BASE_URL", "https://openrouter.ai/api/v1")

    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable not set")

    response = httpx.post(
        f"{base_url}/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
        },
        timeout=120.0,
    )
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]


def main():
    parser = argparse.ArgumentParser(
        description="Generate correct_information.md from research documents"
    )
    parser.add_argument(
        "ground_truth",
        default="docs/incorrect_informations.md",
        help="Path to ground truth file (default: docs/incorrect_informations.md)",
    )
    parser.add_argument(
        "input_dir",
        default="workspace_base_line_gpt-5/input",
        help="Path to input directory with research documents",
    )
    parser.add_argument(
        "--output",
        default="docs/correct_information.md",
        help="Output path (default: docs/correct_information.md)",
    )
    parser.add_argument(
        "--model",
        default=os.environ.get("CORE_MODEL", "openai/gpt-5"),
        help="Model to use (default: CORE_MODEL env or openai/gpt-5)",
    )

    args = parser.parse_args()

    print("[1/5] Loading ground truth file...")
    ground_truth = load_file(args.ground_truth)
    print(f"      Loaded: {args.ground_truth} ({len(ground_truth)} chars)")

    print("[2/5] Loading research documents...")
    input_path = Path(args.input_dir)
    if not input_path.is_dir():
        print(f"ERROR: {input_path} is not a directory")
        sys.exit(1)

    documents = []
    for md_file in sorted(input_path.glob("*.md")):
        content = md_file.read_text()
        documents.append((md_file.name, content))
        print(f"      Loaded: {md_file.name} ({len(content)} chars)")

    print(f"      Total: {len(documents)} documents")

    print("[3/5] Building extraction prompt...")
    prompt = build_prompt(ground_truth, documents)
    print(f"      Prompt size: {len(prompt)} chars")

    print("[4/5] Calling OpenRouter...")
    api_key = os.environ.get("OPENAI_API_KEY")
    base_url = os.environ.get("OPENAI_BASE_URL", "https://openrouter.ai/api/v1")
    model = args.model
    print(f"      OPENAI_API_KEY: {'SET' if api_key else 'NOT SET'}")
    print(f"      OPENAI_BASE_URL: {base_url}")
    print(f"      Model: {model}")

    try:
        result = call_openrouter(prompt, model)
        print(f"      Response received: {len(result)} chars")
    except Exception as e:
        print(f"[4/5] ERROR: OpenRouter call failed: {e}")
        sys.exit(1)

    print("[5/5] Saving output...")
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(result)
    print(f"      Saved to: {output_path}")


if __name__ == "__main__":
    main()
