# NuScale (SMR) — Project 1

Decision: watch/defer pending binding customer economics and a fundable commercialization plan.

## Run the application

Python 3.10 or later; the core model uses only the standard library. From this folder:

```sh
python3 build_scenarios.py
python3 build_methods.py
python3 app.py --serve
python3 verify_project.py
```

Open http://127.0.0.1:8765 for live driver edits, reset, checks, sensitivities and peer context. The command-line views remain available.

Views include summary, scenario, bridge, sensitivity, exit, reverse, sources, monitoring, and readiness. For example: `python3 app.py scenario --scenario central`.

## Submission files

- `submission/`: decision memo, research evolution, validation and AI-use record, and submission manifest.
- `src/`, `data/`, and `build_scenarios.py`: calculation engine, editable assumptions, and reproducible results.
- `output/`: executed statements, valuation, sensitivities, and financing diagnostics.
- `docs/`: source references, research, original Edition A text, and monitoring policy.
- `evidence/lab11-smr/`: preserved changed-input exercise evidence.
- `tests/`: financial and application checks.

Amounts are USD millions and shares in millions except per-share values. Commercial prices, margins, timing, financing, and exit multiples are assumptions. Conditional scenario results are not verified price targets. The inherited downside model is a separately dated services-only wind-down case.

AI assistance, source corrections, actual checks, and remaining personal-review items are documented in `docs/validation-and-ai-use.md`. The manifest records outstanding videos, transcripts, and access checks without treating them as completed.
