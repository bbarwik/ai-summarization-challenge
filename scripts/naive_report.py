#!/usr/bin/env python3
"""Naive single-prompt report generator for USDe research documents."""

import argparse
import os
import sys
import httpx
from pathlib import Path


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


def load_input_documents(input_dir: Path) -> list[tuple[str, str]]:
    """Load all markdown files from input directory."""
    docs = []
    for md_file in sorted(input_dir.glob("*.md")):
        docs.append((md_file.name, md_file.read_text()))
    return docs


def build_naive_prompt(documents: list[tuple[str, str]], report_format: str) -> str:
    """Build a naive prompt with all documents and required format."""
    docs_content = "\n\n".join(f"=== {name} ===\n{content}" for name, content in documents)

    return f"""Assess factual correctness and usefulness of the following USDe stablecoin research documents and generate a structured confidence-based research report.

=== RAW DOCUMENTS ===
{docs_content}

=== REQUIRED REPORT FORMAT ===
{report_format}

Generate the report (4000-6000 words) based ONLY on the provided documents. Do not use external knowledge.
Wrap the entire report in <report></report> tags."""


def call_openrouter(prompt: str, model: str) -> str:
    """Call OpenRouter API to generate the report."""
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
        }
    )
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]


def extract_report(content: str) -> str:
    """Extract report from <report> tags."""
    start = content.find("<report>")
    end = content.find("</report>")
    if start == -1 or end == -1:
        raise ValueError("No <report></report> tags found in response")
    return content[start + 8 : end].strip()


def main():
    parser = argparse.ArgumentParser(description="Generate naive single-prompt report")
    parser.add_argument("input_dir", help="Path to input folder containing .md documents")
    parser.add_argument(
        "--model",
        default=os.environ.get("CORE_MODEL", "openai/gpt-5"),
        help="Model to use (default: CORE_MODEL env or openai/gpt-5)",
    )
    parser.add_argument(
        "--report-format",
        default=None,
        help="Path to file with report format template (optional)",
    )

    args = parser.parse_args()

    input_path = Path(args.input_dir)
    if not input_path.is_dir():
        print(f"ERROR: {input_path} is not a directory")
        sys.exit(1)

    output_path = input_path.parent / "output_naive"
    output_path.mkdir(exist_ok=True)

    print(f"[1/5] Loading documents from {input_path}...")
    documents = load_input_documents(input_path)
    print(f"      Loaded {len(documents)} documents")

    print(f"[2/5] Building naive prompt...")
    if args.report_format:
        report_format = Path(args.report_format).read_text()
    else:
        report_format = """# Final Research Report

## Executive Summary (200-500 words)
- Report goal, purpose, and key findings

## Timeline
- Chronological events using YYYY-MM-DD format
- Confidence level for each event (HIGH/MEDIUM/LOW)

## High Confidence Findings
- Information confirmed by multiple sources without conflicts

## Medium Confidence Findings
- Information from multiple sources with resolved conflicts

## Low Confidence Findings
- Information from single source or unresolved conflicts

## Conflicting Information
- All contradictions with resolutions (where possible)

## Potentially Incorrect Information
- Suspicious claims with explanations of why they may be wrong

## Data Gaps and Missing Information
- Critical gaps requiring further research"""

    prompt = build_naive_prompt(documents, report_format)
    print(f"      Prompt size: {len(prompt)} chars")

    print(f"[3/5] Environment check...")
    api_key = os.environ.get("OPENAI_API_KEY")
    base_url = os.environ.get("OPENAI_BASE_URL", "https://openrouter.ai/api/v1")
    print(f"      OPENAI_API_KEY: {'SET' if api_key else 'NOT SET'}")
    print(f"      OPENAI_BASE_URL: {base_url}")
    print(f"      Model: {args.model}")

    print(f"[4/5] Calling OpenRouter...")
    try:
        raw_response = call_openrouter(prompt, args.model)
        print(f"      Response received: {len(raw_response)} chars")
    except Exception as e:
        print(f"[4/5] ERROR: OpenRouter call failed: {e}")
        sys.exit(1)

    print(f"[5/5] Extracting and saving report...")
    try:
        report = extract_report(raw_response)
    except ValueError as e:
        print(f"[5/5] WARNING: {e}")
        print("      Saving raw response as fallback")
        report = raw_response

    output_file = output_path / "final_report.md"
    output_file.write_text(report)
    print(f"      Saved to: {output_file}")


if __name__ == "__main__":
    main()
