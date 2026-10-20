# Video 2 rehearsal script - AI-generated draft

Target: under 5 minutes. Planned cue times, not actual recording timestamps.

0:00-0:40 | Open README and the repository folder.
This component supports an initiate, defer or decline decision. It runs locally
with Python and no API key. The terminal interface reads frozen output; the
calculation engine is separate from the display.

0:40-1:35 | Open the two JSON input files and src/commercialization.py.
Reported inputs and forecast assumptions live in separate files. The model uses
an explicit 2026 stub, delivery revenue, service revenue, operating costs,
advance milestone payments, capex and incremental working capital. Every module
price and delivery path is an analyst assumption awaiting evidence.

1:35-2:30 | Run python3 build_scenarios.py, then python3 app.py bridge.
FCFF is operating income less tax, plus depreciation, less investment and working
capital. The bridge adds opening liquidity once and includes an assumed operating
sale. Negative cash flow is already charged in value, so fixed-price financing
shares are shown as a separate diagnostic rather than deducted again.

2:30-3:35 | Run PYTHONPATH=src python3 -m unittest discover -s tests -v.
Show the cash known answer, linked statement checks and PMA escalation test.
Explain one assertion directly in the code. Tests establish financial invariants;
they cannot prove an assumed module price or future funding availability.
Show the exact actual test count from this run rather than reading an old count.

3:35-4:30 | Open the independent record and the source correction.
The designated locked exercise requires my own prediction and an AI-closed run.
Existing Lab 11 records are preserved without manufacturing timing evidence. The biggest financial limitations
are hidden contract pricing, payment timing, ownership changes and unsupported
residual value. A clean-environment rehearsal is recorded separately; another
person's cold run still requires an actual participant.

4:30-4:50 | Show output/commercialization-report.md and app summary.
The visible report can be inspected without running code. Its inputs, source
hashes and precise results are preserved in JSON, with annual statements in CSV.
