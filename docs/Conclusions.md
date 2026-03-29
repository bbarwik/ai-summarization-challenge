# AI Summarization: Methodology and Results

"Without data, you’re just another person with an opinion." — W. Edwards Deming

## Reflection on the task

- Task lacks metrics defining how good report looks like. Given two reports how can we decide which is better?

## Scripts

| Script | Purpose |
|--------|---------|
| `generate_correct_info.py` | Extracts ~100 verified correct claims from input documents |
| `naive_report.py` | Generates baseline single-prompt report |
| `evaluate_reports.py` | Compares reports against 161 planted errors + correct claims |

## How to run


### Build and run pipeline with Docker (isolated network)
make docker-build
make docker-setup
make docker-run

### Generate 'Correct' claims for quality comparitions
python scripts/generate_correct_info.py \
    docs/incorrect_informations.md \
    workspace_base_line_gpt-5/input/ \
    --output docs/correct_information.md \
    --model gpt-5

### Generate reprot in single shot
    
python scripts/naive_report.py \
    workspace_base_line_gpt-5/input/
    
### Generate report iteratively

python scripts/verified_report.py workspace_verified/input/  --model_fast google/gemini-3.1-flash-lite-preview

### Generate report iteratively with scratchpad

python accumulation_report.py workspace_verified/input/  --model_fast google/gemini-3.1-flash-lite-preview

### Evaluate / Compare 2 reprots
    
python scripts/evaluate_reports.py \
    docs/incorrect_informations.md \
    workspace_base_line_gpt-5/output/final_report.md \
    workspace_naive_gpt-5/output_naive/final_report.md \
    --correct-info docs/correct_information.md \
    --output evaluation_results.json \
    --model gpt-5

    
## Evaluation Metrics (User-Defined)

The task does not define how to compare reports. I invented:

| Phase | Status | Meaning |
|-------|--------|---------|
| Error Detection | DETECTED | Correctly flagged false claim |
| | IGNORED | Didn't mention it |
| | INCLUDED | Repeated false claim as true (critical failure) |
| | PARTIAL | Mentioned but didn't flag |
| Accuracy | ACCURATE | Correctly stated verified fact |
| | CONTRADICTED | Got verified fact wrong |
| | UNVERIFIABLE | Didn't mention the fact |

## Results (gpt-5)

```
report_1 (pipeline):  DETECTED 36.0%, Accuracy 66.7%
report_2 (naive):     DETECTED 56.5%, Accuracy 68.3%
```

## Conclusions

- Single simple prompt works better than bad workflow KISS rule applies
- You can improve something you can't measure
- Practical note - just use opensource harness like opencode, you can expect much better results, do not reinvent the wheel
