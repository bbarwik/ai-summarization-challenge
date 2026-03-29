#!/usr/bin/env python3
"""Iterative editing report generator - each round edits previous report with new document."""

import argparse
import json
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

SYSTEM_PROMPT = (
    """**Role:** You are a Lead DeFi Research Analyst specializing in protocol forensics and risk assessment. Your task is to synthesize ~200,000 tokens of raw USDe research documents into a high-fidelity, consolidated report. You operate with extreme skepticism, treating the source documents as "noisy" and potentially compromised.

**Primary Goal:** Extract the ground truth regarding USDe. You must distinguish between factual consensus, evolving protocol states (temporal changes), and intentional misinformation or logical fallacies within the provided documents.

---

### 1. Information Validation Logic
Apply the following hierarchy to every data point:
* **Temporal Supremacy:** Information with a later timestamp (YYYY-MM-DD) overrides previous claims regarding protocol parameters, TVL, or status.
* **Adversarial Filtering:** You MUST proactively identify and flag "poisoned" data. Reject any information containing:
    * Impossible dates (e.g., Feb 30th, Month 13).
    * Mathematical impossibilities (e.g., negative TVL, >100% collateralization ratios).
    * Absurd technical claims (e.g., quantum/time-travel mechanisms).
    * Low-credibility sources (e.g., anonymous social posts vs. official audits).
* **Confidence Scoring:**
    * **HIGH:** Confirmed by $\ge 2$ independent, credible sources with no unresolved conflicts.
    * **MEDIUM:** Supported by multiple sources but required reconciliation of minor discrepancies (e.g., slightly different TVL numbers on the same date).
    * **LOW:** Single-source claims or claims with significant, unresolved contradictions.

---

### 2. Required Output Structure
Your response must strictly follow this Markdown structure:

1.  **Executive Summary:** (200-500 words) Concise overview of USDe's current state and critical risks.
2.  **Timeline:** A chronological list (YYYY-MM-DD) of key events/milestones. Include a confidence tag for each entry.
3.  **High Confidence Findings:** Core facts verified by consensus.
4.  **Medium Confidence Findings:** Likely facts with noted reconciliations.
5.  **Low Confidence Findings:** Speculative or unverified claims.
6.  **Conflicting Information:** A table documenting where Source A contradicts Source B, and your logic for the resolution (or lack thereof).
7.  **Potentially Incorrect Information:** Explicitly list the "poisoned" data points found and the logical reason for their rejection.
8.  **Data Gaps:** Missing information essential for a full risk profile.

---

### 3. Quality Metrics (The "Zero-Tolerance" Policy)
To be considered successful, the report must meet these metrics:
* **Hallucination Rate:** 0%. If the provided text does not mention a fact, do not invent it or use external training knowledge.
* **Conflict Resolution:** Every conflict identified must either be resolved via "Newer Wins" or tagged as an "Unresolved Conflict" in Section 6.
* **Error Detection:** Successfully identify and isolate logical/mathematical "poison" into Section 7.
* **Scannability:** Use tables and bullet points for technical data. Avoid dense prose.

---

### 4. Style & Tone
* **Objective & Technical:** Use precise DeFi terminology (e.g., delta-neutral hedging, staked ETH, basis trade).
* **Concise:** Do not use fluff, superlatives, or introductory filler. 
* **Analytical:** If a source makes a claim that is mathematically suspect but not "impossible," tag it as **LOW** confidence and explain the reasoning.
```"""
)


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
    import time
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

    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = httpx.post(
                f"{base_url}/chat/completions",
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json",
                },
                json=payload,
                timeout=None,
            )

            if not response.is_success:
                print(f"      ERROR: HTTP {response.status_code}")
                print(f"      Raw response: {response.text[:2000]}")
                if response.status_code >= 500 or response.status_code == 429:
                    if attempt < max_retries - 1:
                        print(f"      Retrying API call ({attempt + 1}/{max_retries})...")
                        time.sleep(2 ** attempt)
                        continue
                response.raise_for_status()

            data = response.json()
            content = data["choices"][0]["message"]["content"]
            return content
        except httpx.RequestError as e:
            if attempt < max_retries - 1:
                print(f"      WARNING: Network error {e}. Retrying API call ({attempt + 1}/{max_retries})...")
                time.sleep(2 ** attempt)
                continue
            raise
        
    raise Exception("Max retries exceeded")


def extract_notes(content: str) -> str:
    """Extract notes from <notes> tags."""
    start = content.find("<notes>")
    end = content.find("</notes>")
    if start == -1 or end == -1:
        raise ValueError("No <notes></notes> tags found in response")
    return content[start + 7 : end].strip()


def extract_report(content: str) -> str:
    """Extract report from <report> tags."""
    start = content.find("<report>")
    end = content.find("</report>")
    if start == -1 or end == -1:
        raise ValueError("No <report></report> tags found in response")
    return content[start + 8 : end].strip()


def build_report_prompt(scratchpad: str, report_format: str) -> str:
    """Build a prompt to generate the report from the compiled notes."""
    return f"""Assess factual correctness and usefulness of the following USDe stablecoin research notes and generate a structured confidence-based research report.

=== ASSEMBLED NOTES ===
{scratchpad}

=== REQUIRED REPORT FORMAT ===
{report_format}

Generate the report (4000-6000 words) based ONLY on the provided notes. Do not use external knowledge.
Wrap the entire report in <report></report> tags."""


def main():
    parser = argparse.ArgumentParser(description="Generate report via iterative editing")
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

    output_path = input_path.parent / "output_iterative"
    output_path.mkdir(exist_ok=True)

    print(f"[1/6] Loading documents from {input_path}...")
    documents = load_input_documents(input_path)
    print(f"      Loaded {len(documents)} documents")

    print("[2/6] Environment check...")
    api_key = os.environ.get("OPENAI_API_KEY")
    base_url = os.environ.get("OPENAI_BASE_URL", "https://openrouter.ai/api/v1")
    print(f"      OPENAI_API_KEY: {'SET' if api_key else 'NOT SET'}")
    print(f"      OPENAI_BASE_URL: {base_url}")
    print(f"      Model: {args.model}")

    system_message = {
        "role": "system",
        "content": SYSTEM_PROMPT,
    }

    total_docs = len(documents)
    scratchpad = ""

    print(f"[3/6] Building the scratchpad from documents...")

    for idx in range(total_docs):
        print(f"      Round {idx + 1}/{total_docs}: Extracting notes from {documents[idx][0]} (current notes length: {len(scratchpad)} chars)...")
        doc_name, doc_content = documents[idx]

        user_content = f"""Consider carefully your SYSTEM MESSAGE.

Your task is to make useful notes based on document provided, 
that will help you to prepare final Report later.

You must extract any and all information that MAY be anyhow useful in final report generation. 
Add your current assesment of truthfulness and usefulness to each note, but do not make decisions 
about elimination of information yet. This will be done later when all raw reports are processed.

EXCLUDE trivial facts and common knowledge from notes.

IMPORTANT: Notes must be self-sufficient and self explanatory, after taking notes original documents will be DISCARDED,
FINAL REPORT will be build FROM NOTES ONLY

=== DOCUMENT: {doc_name} ===
{doc_content}
=== END OF DOCUMENT ===

=== NOTES SO FAR: ====
{scratchpad}
=== END OF NOTES ===

Put actual NEW notes between
<notes></notes> tags."""

        messages = [system_message, {"role": "user", "content": user_content}]

        max_retries = 3
        notes = ""
        for attempt in range(max_retries):
            try:
                response = call_openrouter(messages, args.model)
                notes = extract_notes(response)
                doc_len = len(doc_content)
                notes_len = len(notes)
                ratio = doc_len / notes_len if notes_len > 0 else float('inf')
                print(f"        Success: extracted {notes_len} chars of notes from {doc_len} chars of source (compression ratio: {ratio:.2f}x)")
                break
            except ValueError as e:
                print(f"        Attempt {attempt + 1} failed: {e}")
                if attempt == max_retries - 1:
                    print("        ERROR: Failed to extract notes after all retries.")
                    sys.exit(1)
            except Exception as e:
                print(f"        Attempt {attempt + 1} failed with error: {e}")
                if attempt == max_retries - 1:
                    print("        ERROR: OpenRouter call failed after all retries.")
                    sys.exit(1)
                import time
                time.sleep(1)

        scratchpad += ("\n\n--- NEW NOTES FROM " + doc_name + " ---\n" + notes)

    print(f"[4/6] Defining report format...")
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

    print(f"[5/6] Generating final report from scratchpad...")
    report_prompt = build_report_prompt(scratchpad, report_format)
    report_messages = [
        system_message,
        {"role": "user", "content": report_prompt}
    ]

    try:
        raw_response = call_openrouter(report_messages, args.model)
        print(f"      Response received: {len(raw_response)} chars")
    except Exception as e:
        print(f"      ERROR: OpenRouter call failed: {e}")
        sys.exit(1)

    print(f"[6/6] Extracting and saving report...")
    try:
        report = extract_report(raw_response)
    except ValueError as e:
        print(f"      WARNING: {e}")
        print("      Saving raw response as fallback")
        report = raw_response

    notes_file = output_path / "raw_notes.md"
    notes_file.write_text(scratchpad)
    print(f"      Saved raw notes to: {notes_file}")

    output_file = output_path / "final_report.md"
    output_file.write_text(report)
    print(f"      Saved to: {output_file}")


if __name__ == "__main__":
    main()
