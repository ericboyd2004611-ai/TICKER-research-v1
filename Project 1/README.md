# NuScale (SMR) - Project 1 decision component

**AI-generated review package. Read HANDOFF.md before submission.**

**Before recording:** open RECORDING-GUIDE.md for current numbers, screen and
command cues, duration limits and the recording snapshot. Run
`python3 prepare_recording.py` after any intentional model change, then regenerate
the PDFs, package and preflight checks before relying on the guide.
The `submission/` folder holds correctly named non-video PDFs and a manifest copy;
the reviewed contents still require personal review and actual video records.

The GitHub project is on the `project-1-smr-submission` branch, inside `Project 1/`.
The existing main branch is preserved. Publication/commit state is recorded in
`evidence/repository-status.json`; use the project URL there for the recording.

`python3 app.py exit` displays the operating-exit sensitivity. Objective readiness
checks are in `python3 preflight.py`; they do not invent firsthand confirmations.

## Application quick start

Python 3.10 or later. No third-party packages, network calls, accounts or API keys
are needed for the core application. From the Project 1 folder:

```sh
python3 build_scenarios.py
python3 app.py --interactive
python3 verify_project.py
```

Quit the menu with q. Other computers should use the extracted project folder.
Useful views: `python3 app.py summary`, `python3 app.py scenario --scenario central`,
`python3 app.py bridge`, `python3 app.py sensitivity`, `python3 app.py reverse`,
`python3 app.py sources`, `python3 app.py monitoring`, `python3 app.py readiness`.

The core requirements.txt intentionally has no external dependencies. Source and
input hashes protect the display from stale output. A stale-output error means
the changed assumptions must be reviewed and build_scenarios.py rerun.

## Current result and ownership boundary

Contract review corrected the first flat-fee draft. The current model applies
the payment escalation floor and replaces unsupported perpetual terminal value
with an explicit assumed operating exit. Zero/4x/6x/8x/10x sensitivities are shown.
Old values are retained only as superseded evidence. Contract pricing and exit
multiples remain assumptions; quantitative peer validation remains open.

The model also values an existing holder's terminal payoff under the fixed-price
financing assumption. This alternative does not subtract operating losses twice.
Share-capacity and modeled subscriber-value screens flag financing conditions.
It is separate from the corporate FCFF bridge, which assumes fair financing terms.

The terminal application is a locally runnable financial application component.
It reads executed results; calculation logic resides in src/commercialization.py.
Edition A is preserved from the student-supplied text under the reported
professor-approved format exception. The genuine independent exercise,
recordings, transcripts and personal source/AI dispositions remain student work.

## Complete workflow and files

Evidence flows from data/research-inputs.json and
data/commercialization-scenarios.json through src/commercialization.py to
build_scenarios.py, frozen JSON/CSV/Markdown output, then app.py.

- `python3 research_bridge.py`: cash/share arithmetic diagnostic.
- `python3 analysis.py`: separately dated inherited downside model.
- `python3 prepare_drafts.py`: matching written drafts and rehearsal scripts.
- `python3 clean_run.py`: assistant rehearsal in a fresh temporary directory.
- `python3 build_documents.py`: PDF rebuild, using requirements-docs.txt only.
- `python3 package_project.py`: local archive/inventory; never publishes/submits.

Core output is in output/commercialization-report.md and the adjacent JSON/CSV.
Read output/pdf/ for the three review PDFs. Source locators and conventions are
in docs/verified-starting-point-draft.md and docs/source-review.md. Named AI use
and actual tests are in docs/validation-and-ai-use.md. The 12-row manifest marks
missing evidence openly; planned scripts are not represented as transcripts.

The model uses USD millions, shares in millions and USD/share. It includes
economic income, balance-sheet and cash-flow schedules, with equity derived from
income and net funding rather than a plug. These are simplified economic
statements, not GAAP forecasts. Legacy nonliquid assets and liabilities are held
constant. Capex, operating commitments, leases and claims require further mapping.

The unrestricted liquidity proxy adds each asset category once; excluded
restricted cash is not deducted again. Consolidated economic interests include
exchangeable LLC units; book NCI is not deducted a second time. Options/RSUs use
a gross allowance, not treasury-stock-method dilution. Negative FCFF is already
deducted in valuation, so fixed-price issuance shares remain a separate funding
diagnostic. Assumed financing availability and year-end cash do not establish
intra-year solvency. No password or API key is needed or stored.

Work in progress. Decision user: an investment committee with no current position.
Student's starting position: watch/defer pending binding, economically specific orders,
credible commercialization economics, and acceptable dilution.

## New AI-generated research drafts

The runnable commercialization model is now available:

```sh
python3 build_scenarios.py
PYTHONPATH=src python3 -m unittest discover -s tests -v
```

Open `output/commercialization-report.md` for three scenarios, the valuation
bridge, annual cash flows, financing diagnostics, margin stress, discount/price
sensitivity and reverse valuation. Full results are in JSON and CSV beside it.
Editable assumptions are in `data/commercialization-scenarios.json`. These are
AI-generated illustrations requiring student approval and source reconciliation;
they do not yet establish a defensible fair-value range.

Start with `docs/verified-starting-point-draft.md` and
`docs/edition-b-working-draft.md`. These use a proposed September 1, 2026 close
boundary while retaining each financial observation's actual date. Run
`python3 research_bridge.py` to regenerate `output/research-bridge.json` from
`data/research-inputs.json`. This diagnostic is separate from the older model.

## Run the existing downside model

Python 3.10 or later; standard library only. From this directory:

```sh
python3 analysis.py
PYTHONPATH=src python3 -m unittest discover -s tests -v
```

Read `output/downside-report.md` without running code. Material inputs and assumptions
are in `src/smr_proforma.py` and `docs/existing-model-assumptions.md`.
This copied Week 5 model produces five annual linked statements and sensitivities.
Its residual distribution is a conditional services-only/wind-down value, not the
company's fair value, a valuation range, or a current price target.

## Dates and evidence

The existing model measures balances at December 31, 2025 using the annual report
published February 26, 2026. It is retrospective: do not describe its information
as available on December 31. Edition B uses September 1, 2026 close. The research
report also uses June 2026 data; these periods must be reconciled before combining them.

## Files

- `analysis.py`: exports existing-model results and material inputs.
- `src/smr_proforma.py`: preserved Week 5 calculation engine.
- `tests/`: existing financial safeguards.
- `output/`: generated report and machine-readable inputs/results.
- `docs/project-status.md`: outstanding analysis and submission evidence.
- `docs/validation-and-ai-use.md`: actual validation and AI-use working record.
- `submission-manifest.csv`: course template; incomplete until real files/links exist.

Original coursework is preserved. Edition A is packaged from the student-supplied
text; the student reports professor approval for that format instead of a PDF.
No separate original Edition A PDF or invented receipt is requested.
