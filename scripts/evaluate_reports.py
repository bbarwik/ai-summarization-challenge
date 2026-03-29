#!/usr/bin/env python3
"""Evaluate research reports against ground truth incorrect information."""

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

EVALUATION_PROMPT = """You are an expert evaluator comparing research reports against
ground truth incorrect information.

## GROUND TRUTH: KNOWN INCORRECT FACTS
```markdown
{ground_truth_content}
```

## REPORTS TO EVALUATE
{report_sections}

## YOUR TASK
For each of the 161 known incorrect facts above, determine how each report handled it.

## STATUS DEFINITIONS
| Status | Meaning |
|--------|---------|
| DETECTED | Report identifies this as incorrect and explains why |
| IGNORED | Report does not mention this fact at all |
| INCLUDED | Report presents this false fact as true (critical failure) |
| PARTIAL | Report mentions this but doesn't clearly flag it as incorrect |

## OUTPUT FORMAT
Respond with ONLY a valid JSON array (no markdown code blocks, no explanatory text):

```json
[
  {{
    "error_id": "1a",
    "claim": "Protocol founded by Satoshi Nakamoto in 2026 using time-travel technology",
    "evaluations": [
      {{
        "report": "report_1",
        "justification": "explanation of how report_1 handled this",
        "status": "DETECTED"
      }}
    ]
  }}
]
```

Process ALL 161 errors. Output valid JSON array only."""

ACCURACY_PROMPT = """You are an expert evaluator checking factual accuracy of research
reports against verified correct information.

## VERIFIED CORRECT INFORMATION
```markdown
{correct_info_content}
```

## REPORTS TO EVALUATE
{report_sections}

## YOUR TASK
For each of the verified correct claims above, determine how each report handled it.

## STATUS DEFINITIONS
| Status | Meaning |
|--------|---------|
| ACCURATE | Report correctly states this verified fact |
| CONTRADICTED | Report states something that contradicts this verified fact |
| UNVERIFIABLE | Report does not mention this fact |

## OUTPUT FORMAT
Respond with ONLY a valid JSON array (no markdown code blocks, no explanatory text):

```json
[
  {{
    "claim": "USDe is a synthetic dollar stablecoin that maintains stability via delta-hedging",
    "evaluations": [
      {{
        "report": "report_1",
        "status": "ACCURATE",
        "explanation": "report_1 correctly states this"
      }},
      {{
        "report": "report_2",
        "status": "UNVERIFIABLE",
        "explanation": "report_2 does not mention this"
      }}
    ]
  }}
]
```

Process ALL verified claims. Output valid JSON array only."""


def load_file(path: str) -> str:
    with open(path) as f:
        return f.read()


def fix_json(json_str: str) -> str:
    import re

    json_str = json_str.strip()
    if json_str.startswith("```"):
        json_str = re.sub(r"^```json\s*", "", json_str)
        json_str = re.sub(r"\s*```$", "", json_str)
    json_str = re.sub(r'\\([^"\\/bfnrtu])', r"\\\\1", json_str)
    return json_str


def build_prompt(ground_truth: str, reports: list[tuple[str, str]]) -> str:
    report_sections = []
    for i, (name, content) in enumerate(reports):
        report_sections.append(f"Report {i + 1}: {name}\n```markdown\n{content}\n```")

    return EVALUATION_PROMPT.format(
        ground_truth_content=ground_truth,
        report_sections="\n\n".join(report_sections),
    )


def build_accuracy_prompt(correct_info: str, reports: list[tuple[str, str]]) -> str:
    report_sections = []
    for i, (name, content) in enumerate(reports):
        report_sections.append(f"Report {i + 1}: {name}\n```markdown\n{content}\n```")

    return ACCURACY_PROMPT.format(
        correct_info_content=correct_info,
        report_sections="\n\n".join(report_sections),
    )


def call_openrouter(prompt: str, model: str) -> str:
    api_key = os.environ.get("OPENAI_API_KEY")
    base_url = os.environ.get("OPENAI_BASE_URL", "https://openrouter.ai/api/v1")

    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable not set")

    schema = {
        "name": "evaluation_result",
        "strict": "true",
        "description": "Evaluation of reports against ground truth incorrect information",
        "type": "object",
        "items": {
            "type": "object",
            "properties": {
                "error_id": {"type": "string"},
                "claim": {"type": "string"},
                "evaluations": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "report": {"type": "string"},
                            "justification": {"type": "string"},
                            "status": {
                                "type": "string",
                                "enum": ["DETECTED", "IGNORED", "INCLUDED", "PARTIAL"],
                            },
                        },
                        "required": ["report", "justification", "status"],
                    },
                },
            },
            "required": ["error_id", "claim", "evaluations"],
        },
    }

    response = httpx.post(
        f"{base_url}/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "response_format": {
                "type": "json_schema",
                "json_schema": schema,
            },
        },
    )
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]


def call_openrouter_accuracy(prompt: str, model: str) -> str:
    api_key = os.environ.get("OPENAI_API_KEY")
    base_url = os.environ.get("OPENAI_BASE_URL", "https://openrouter.ai/api/v1")

    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable not set")

    schema = {
        "name": "accuracy_result",
        "description": "Accuracy check of reports against verified correct information",
        "type": "object",
        "items": {
            "type": "object",
            "properties": {
                "claim": {"type": "string"},
                "evaluations": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "report": {"type": "string"},
                            "status": {
                                "type": "string",
                                "enum": ["ACCURATE", "CONTRADICTED", "UNVERIFIABLE"],
                            },
                            "explanation": {"type": "string"},
                        },
                        "required": ["report", "status", "explanation"],
                    },
                },
            },
            "required": ["claim", "evaluations"],
        },
    }

    response = httpx.post(
        f"{base_url}/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "response_format": {
                "type": "json_schema",
                "json_schema": schema,
            },
        },
    )
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]


def calculate_scores(results: list, report_names: list[str]) -> dict:
    scores = {}

    for report_name in report_names:
        detected = partial = ignored = included = 0

        for error in results:
            for eval_entry in error.get("evaluations", []):
                if eval_entry.get("report") == report_name:
                    status = eval_entry.get("status")
                    if status == "DETECTED":
                        detected += 1
                    elif status == "PARTIAL":
                        partial += 1
                    elif status == "IGNORED":
                        ignored += 1
                    elif status == "INCLUDED":
                        included += 1

        detection_score = detected * 1.0 + partial * 0.5 + ignored * 0 + included * -2
        detection_score = max(0, detection_score)

        penalty = 0
        if included > 3:
            penalty = (included - 3) * 2

        scores[report_name] = {
            "detected": detected,
            "partial": partial,
            "ignored": ignored,
            "included": included,
            "detection_score": round(detection_score, 2),
            "inclusion_penalty": penalty,
            "total": round(detection_score - penalty, 2),
            "detection_rate": round(detected / 161, 3) if detected else 0,
        }

    return scores


def calculate_accuracy_scores(results: list, report_names: list[str]) -> dict:
    scores = {}

    for report_name in report_names:
        accurate = contradicted = unverifiable = 0

        for entry in results:
            for eval_entry in entry.get("evaluations", []):
                if eval_entry.get("report") == report_name:
                    status = eval_entry.get("status")
                    if status == "ACCURATE":
                        accurate += 1
                    elif status == "CONTRADICTED":
                        contradicted += 1
                    elif status == "UNVERIFIABLE":
                        unverifiable += 1

        total = accurate + contradicted + unverifiable
        accuracy_rate = round(accurate / total, 3) if total > 0 else 0

        scores[report_name] = {
            "accurate": accurate,
            "contradicted": contradicted,
            "unverifiable": unverifiable,
            "accuracy_rate": accuracy_rate,
        }

    return scores

    return scores


def print_results(scores: dict, report_names: list[str], has_accuracy: bool = False):
    print("\n=== Report Evaluation Results ===\n")

    for report_name in report_names:
        s = scores[report_name]
        print(f"Report: {report_name}")
        print(f"  DETECTED:   {s['detected']}/161 ({s['detection_rate']:.1%})")
        print(f"  PARTIAL:    {s['partial']}/161")
        print(f"  IGNORED:    {s['ignored']}/161")
        print(f"  INCLUDED:   {s['included']}/161", " <- CRITICAL" if s["included"] > 0 else "")
        print(f"  Score:      {s['detection_score']}", end="")
        if s["inclusion_penalty"] > 0:
            print(f" - {s['inclusion_penalty']} penalty = {s['total']}", end="")
        print()

        if has_accuracy and "accuracy" in s:
            acc = s["accuracy"]
            total_acc = acc["accurate"] + acc["contradicted"] + acc["unverifiable"]
            if total_acc > 0:
                print(f"  Accuracy:   {acc['accurate']}/{total_acc} ({acc['accuracy_rate']:.1%})")
                if acc["contradicted"] > 0:
                    print(f"  Contradicted: {acc['contradicted']}")

        if s["included"] > 3:
            print(f"  WARNING: {s['included']} false inclusions (>3), penalty applied")
        print()

    if len(report_names) == 2:
        winner = max(report_names, key=lambda r: scores[r]["total"])
        print(f"=== WINNER: {winner} ===")


def main():
    parser = argparse.ArgumentParser(description="Evaluate reports against ground truth")
    parser.add_argument("ground_truth", help="Path to docs/incorrect_informations.md")
    parser.add_argument("report_a", help="Path to first report")
    parser.add_argument("report_b", nargs="?", help="Path to second report (optional)")
    parser.add_argument(
        "--correct-info",
        default=None,
        help="Path to docs/correct_information.md for accuracy check (optional)",
    )
    parser.add_argument(
        "--model",
        default=os.environ.get("CORE_MODEL", "openai/gpt-5"),
        help="Model to use (default: CORE_MODEL env or openai/gpt-5)",
    )
    parser.add_argument(
        "--output",
        default="evaluation_results.json",
        help="Output JSON file path",
    )

    args = parser.parse_args()

    print("[1/6] Loading ground truth file...")
    ground_truth = load_file(args.ground_truth)
    print(f"      Loaded: {args.ground_truth} ({len(ground_truth)} chars)")

    print("[2/6] Loading report files...")
    reports = [(args.report_a, load_file(args.report_a))]
    report_names = ["report_1"]
    print(f"      Loaded: {args.report_a} ({len(reports[0][1])} chars)")

    if args.report_b:
        reports.append((args.report_b, load_file(args.report_b)))
        report_names.append("report_2")
        print(f"      Loaded: {args.report_b} ({len(reports[1][1])} chars)")

    print("[3/6] Building evaluation prompt...")
    prompt = build_prompt(ground_truth, reports)
    print(f"      Prompt size: {len(prompt)} chars")

    api_key = os.environ.get("OPENAI_API_KEY")
    base_url = os.environ.get("OPENAI_BASE_URL", "https://openrouter.ai/api/v1")
    model = args.model

    print("[4/6] Environment check...")
    print(f"      OPENAI_API_KEY: {'SET' if api_key else 'NOT SET'}")
    print(f"      OPENAI_BASE_URL: {base_url}")
    print(f"      Model: {model}")

    print("[5/6] Sending error detection request to OpenRouter...")
    try:
        json_str = call_openrouter(prompt, args.model)
        print(f"      Response received: {len(json_str)} chars")
    except Exception as e:
        print(f"[5/6] ERROR: OpenRouter call failed: {e}")
        sys.exit(1)

    print("[6/6] Parsing JSON response...")
    try:
        results = json.loads(json_str)
        print(f"      Parsed {len(results)} error entries")
    except json.JSONDecodeError as e:
        print(f"[6/6] ERROR: Failed to parse LLM response as JSON: {e}")
        print("Raw response (first 2000 chars):")
        print(json_str[:2000])
        sys.exit(1)

    scores = calculate_scores(results, report_names)

    accuracy_results = None
    if args.correct_info:
        print("[7/7] Running accuracy check...")
        correct_info = load_file(args.correct_info)
        print(f"      Loaded: {args.correct_info} ({len(correct_info)} chars)")

        print("      Building accuracy prompt...")
        acc_prompt = build_accuracy_prompt(correct_info, reports)
        print(f"      Prompt size: {len(acc_prompt)} chars")

        print("      Sending accuracy request to OpenRouter...")
        try:
            acc_json_str = call_openrouter_accuracy(acc_prompt, model)
            print(f"      Response received: {len(acc_json_str)} chars")
        except Exception as e:
            print(f"      ERROR: Accuracy check failed: {e}")
            accuracy_results = None
        else:
            try:
                accuracy_results = json.loads(acc_json_str)
                print(f"      Parsed {len(accuracy_results)} accuracy entries")
            except json.JSONDecodeError:
                print("      First parse attempt failed, trying to fix JSON...")
                fixed = fix_json(acc_json_str)
                try:
                    accuracy_results = json.loads(fixed)
                    print(f"      Fixed JSON: parsed {len(accuracy_results)} accuracy entries")
                except json.JSONDecodeError:
                    print("      ERROR: Failed to parse accuracy response as JSON")
                    print("Raw response (first 2000 chars):")
                    print(acc_json_str[:2000])
                    accuracy_results = None

        if accuracy_results is not None:
            acc_scores = calculate_accuracy_scores(accuracy_results, report_names)
            for rn in report_names:
                scores[rn]["accuracy"] = acc_scores[rn]

    print_results(scores, report_names, has_accuracy=(accuracy_results is not None))

    output = {
        "results": results,
        "scores": scores,
    }
    if accuracy_results is not None:
        output["accuracy_results"] = accuracy_results

    with open(args.output, "w") as f:
        json.dump(output, f, indent=2)

    print(f"\nFull JSON saved to: {args.output}")


if __name__ == "__main__":
    main()
