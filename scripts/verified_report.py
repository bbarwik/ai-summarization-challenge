#!/usr/bin/env python3
"""Multi-round verified report generator for research documents."""

import argparse
import json
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

REPORT_FORMAT = """# Final Research Report

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

OUTPUT_SCHEMA = {
    "name": "analysis_result",
    "strict": True,
    "description": "Structured analysis of claims and gaps from research documents",
    "type": "object",
    "items": {
        "type": "object",
        "properties": {
            "type": {
                "type": "string",
                "enum": ["claim", "gap"],
                "description": "claim = true or false statement, stated in the document, gap = missing information",
            },
            "text": {
                "type": "string",
                "description": "Description of the claim or gap, clear JSON-friendly text describing claim in question or existing gap (information that needs researching or question that needs answering)",
            },
            "status": {
                "type": "string",
                "enum": ["FALSE", "PROBABLY_FALSE", "UNKNOWN", "PROBABLY_TRUE", "TRUE"],
                "description": "Truth assessment (claims only)",
            },
            "source": {
                "type": "string",
                "description": "Document name and location where found",
            },
        },
        "required": ["type", "text", "source"],
    },
}


SYSTEM_PROMPT = (
    """You are an expert research analyst. Your task is to analyze research documents and build a comprehensive list of claims and gaps for a final research report.

## YOUR TASK
1. Analyze documents one at a time
2. For each claim, assess its truth: TRUE, PROBABLY_TRUE, UNKNOWN, PROBABLY_FALSE, FALSE
3. Identify gaps - missing information important for a comprehensive report
4. When asked to compile, write the final report following the specified format

## WHAT TO LOOK FOR
- Contradictions between documents
- Impossible dates (Feb 30, month 13, day 45, future dates)
- Absurd numbers (negative values, percentages over 100%, numbers exceeding reasonable bounds)
- Zero-credibility sources (anonymous forums, random social media, defunct websites)
- Causality violations (effect before cause)
- Mathematically impossible statements
- Claims that contradict well-known facts

Your ltimate goal is to prepare report in following format

"""
    + REPORT_FORMAT
    + """

FOLLOW SPECIFIC INSTRUCTIONS TO REACH THE GOAL

"""
)

COMPILE_PROMPT = """Based on the complete claims and gaps list above, write the final research report.

The report MUST follow this exact structure:

{report_format}

IMPORTANT:
- Write using ONLY claims with status TRUE, PROBABLY_TRUE, or UNKNOWN
- Place FALSE/PROBABLY_FALSE claims under "Potentially Incorrect Information" - do NOT present them as facts
- Do NOT repeat false claims
- Do not use external knowledge
- Wrap the entire report in <report></report> tags"""


def load_input_documents(input_dir: Path) -> list[tuple[str, str]]:
    """Load all markdown files from input directory."""
    docs = []
    for md_file in sorted(input_dir.glob("*.md")):
        docs.append((md_file.name, md_file.read_text()))
    return docs


def call_openrouter(
    messages: list[dict],
    model: str,
    schema: dict | None = None,
) -> str:
    """Call OpenRouter API with conversation history."""
    api_key = os.environ.get("OPENAI_API_KEY")
    base_url = os.environ.get("OPENAI_BASE_URL", "https://openrouter.ai/api/v1")

    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable not set")

    payload = {
        "model": model,
        "messages": messages,
    }

    if schema:
        payload["response_format"] = {
            "type": "json_schema",
            "json_schema": schema,
        }

    response = httpx.post(
        f"{base_url}/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json=payload,
    )

    if not response.is_success:
        print(f"      ERROR: HTTP {response.status_code}")
        print(f"      Raw response: {response.text[:2000]}")
        response.raise_for_status()

    data = response.json()
    content = data["choices"][0]["message"]["content"]
    return content


def extract_report(content: str) -> str:
    """Extract report from <report> tags."""
    start = content.find("<report>")
    end = content.find("</report>")
    if start == -1 or end == -1:
        raise ValueError("No <report></report> tags found in response")
    return content[start + 8 : end].strip()


def parse_json_response(content: str) -> list:
    """Parse JSON from LLM response, handling potential markdown code blocks."""
    content = content.strip()
    if content.startswith("```"):
        content = content.split("```")[1]
        if content.startswith("json"):
            content = content[4:]
        content = content.strip()
    return json.loads(content)


def main():
    parser = argparse.ArgumentParser(description="Generate multi-round verified report")
    parser.add_argument("input_dir", help="Path to input folder containing .md documents")
    parser.add_argument(
        "--model_fast",
        default=os.environ.get("CORE_MODEL", "openai/gpt-5"),
        help="Model to use (default: CORE_MODEL env or openai/gpt-5)",
    )
    parser.add_argument(
        "--model_smart",
        default=os.environ.get("CORE_MODEL", "openai/gpt-5"),
        help="Model to use (default: CORE_MODEL env or openai/gpt-5)",
    )
    parser.add_argument(
        "--topic",
        default="the subject of the research documents",
        help="Topic description for the report (default: generic)",
    )

    args = parser.parse_args()

    input_path = Path(args.input_dir)
    if not input_path.is_dir():
        print(f"ERROR: {input_path} is not a directory")
        sys.exit(1)

    output_path = input_path.parent / "output_verified"
    output_path.mkdir(exist_ok=True)

    print(f"[1/7] Loading documents from {input_path}...")
    documents = load_input_documents(input_path)
    print(f"      Loaded {len(documents)} documents")

    print(f"[2/7] Environment check...")
    api_key = os.environ.get("OPENAI_API_KEY")
    base_url = os.environ.get("OPENAI_BASE_URL", "https://openrouter.ai/api/v1")
    print(f"      OPENAI_API_KEY: {'SET' if api_key else 'NOT SET'}")
    print(f"      OPENAI_BASE_URL: {base_url}")
    print(f"      Model (fast): {args.model_fast}")
    print(f"      Model (smart): {args.model_smart}")

    system_message = {
        "role": "system",
        "content": SYSTEM_PROMPT,
    }

    messages = [system_message]

    total_docs = len(documents)
    for idx, (doc_name, doc_content) in enumerate(documents):
        print(f"[3/7] Processing document {idx + 1}/{total_docs}: {doc_name}...")

        if idx == 0:
            user_content = f"""Analyze this research document and identify all claims and gaps.

Topic: {args.topic}

=== DOCUMENT: {doc_name} ===
{doc_content}

Output a JSON array of all claims and gaps found in this document."""
        else:
            user_content = f"""Analyze this NEW document and rebuild the COMPLETE list of all claims and gaps found so far.

Topic: {args.topic}

=== NEW DOCUMENT: {doc_name} ===
{doc_content}

IMPORTANT: Rebuild the FULL list from scratch. Include all claims/gaps from previous documents plus any new findings from this document. Strictly follow JSON Schema."""

        messages.append({"role": "user", "content": user_content})

        response = None
        try:
            response = call_openrouter(messages, args.model_fast, schema=OUTPUT_SCHEMA)
            print(f"      Response received: {len(response)} chars")

            claims_list = parse_json_response(response)
            print(f"      Items in claims list: {len(claims_list)}")

        except Exception as e:
            print(f"      ERROR: Failed to parse response: {e}")
            if response:
                print(f"      Raw response (first 1000 chars): {response[:1000]}")
            sys.exit(1)

        messages.append({"role": "assistant", "content": response})

    print(f"[4/7] All {total_docs} documents processed. Claims list built.")

    print(f"[5/7] Compiling final report...")
    compile_content = COMPILE_PROMPT.format(report_format=REPORT_FORMAT)
    messages.append({"role": "user", "content": compile_content})

    try:
        final_response = call_openrouter(messages, args.model_smart)
        print(f"      Response received: {len(final_response)} chars")
    except Exception as e:
        print(f"      ERROR: OpenRouter call failed: {e}")
        sys.exit(1)

    print(f"[6/6] Extracting and saving report...")
    try:
        report = extract_report(final_response)
    except ValueError as e:
        print(f"      WARNING: {e}")
        print("      Saving raw response as fallback")
        report = final_response

    output_file = output_path / "final_report.md"
    output_file.write_text(report)
    print(f"      Saved to: {output_file}")


if __name__ == "__main__":
    main()
