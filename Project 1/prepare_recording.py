"""Prepare an exact, data-driven guide and snapshot for the three recordings."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main():
    p = json.loads((ROOT / 'output/commercialization-output.json').read_text())
    strong = p['results'][2]
    low = p['margin_stress'][2]
    grid = {x['exit_multiple']: x['value_per_share'] for x in p['exit_sensitivity'] if x['name'] == strong['name']}
    files = ['data/research-inputs.json', 'data/commercialization-scenarios.json',
             'src/commercialization.py', 'build_scenarios.py', 'app.py',
             'output/commercialization-output.json', 'visible_output.json']
    hashes = {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in files}
    freeze = hashlib.sha256(json.dumps(hashes, sort_keys=True).encode()).hexdigest()
    snapshot = dict(created_utc=datetime.now(timezone.utc).isoformat(),
                    snapshot_sha256=freeze, files=hashes,
                    scope='Current recording inputs/code/output; not an original Lab 11 prediction timestamp')
    (ROOT / 'evidence/recording-snapshot.json').write_text(json.dumps(snapshot, indent=2) + '\n')
    guide = f'''# Start here before recording

Use this guide with the matching PDFs and output. Snapshot ID: `{freeze[:16]}`.
This freezes the current presentation evidence, not the historical lab prediction.

## One consistent decision

WATCH / DEFER: keep SMR on the watchlist and request verified contract economics
and a fundable cash plan before initiation. This is conditional analysis using
an explicit September 1, 2026 close boundary, not a current live-price call.

The three default DCF results are $0.00, $0.00 and ${strong['value_per_share']:.2f}/share.
They assume a six-times operating exit and unverified commercial economics.
A modeled zero is the limited-liability floor, not proof the stock is worthless.
Delayed and central financing assumptions fail the share-capacity and modeled
subscription-value checks. Do not describe those paths as fundable base cases.

## Numbers to understand, not memorize blindly

| Item | Current model result |
|---|---:|
| Stronger execution, default 6x exit | ${strong['value_per_share']:.2f}/share |
| Same case, zero operating exit | ${grid[0.0]:.2f}/share |
| Same case, 4x / 8x / 10x | ${grid[4.0]:.2f} / ${grid[8.0]:.2f} / ${grid[10.0]:.2f} |
| Stronger case, 5-point lower module margin | ${low['value_per_share']:.2f}/share |
| Stronger net funding, base / margin stress | ${strong['funding_net_m']:.1f}m / ${low['funding_net_m']:.1f}m |
| Reverse supplier-price hurdle, central schedule | ${p['reverse_scenario']['solved_module_price_m']:.1f}m per module in 2026-base dollars |

The reverse price is not a sourced selling price. The 6x exit is not an observed
peer multiple. The $50m cash buffer and 25% margin of safety are analyst rules.
PMA fee escalation is a source-based contractual feature; future CPI and invoice
timing still create uncertainty. Full sources are in docs/source-review.md.

## Open these files before starting

1. output/pdf/Research-Evolution-DRAFT.pdf and docs/lab11-evidence-map.md.
2. README.md, src/commercialization.py, and the two data JSON files.
3. output/pdf/Decision-Memo-DRAFT.pdf and output/commercialization-report.md.
4. A terminal in this project folder. Keep the commands below ready.

## Terminal rehearsal

```sh
python3 app.py summary
python3 app.py scenario --scenario central
python3 app.py bridge --scenario stronger
python3 app.py sensitivity
python3 app.py exit
python3 app.py reverse
python3 verify_project.py
```

Do not edit assumptions or regenerate outputs during a presentation unless you
intend to explain and refreeze that version. Keep the actual output on screen.

## Video 1 - research ownership, maximum 3:00

Use docs/video-1-rehearsal-script.md. Show Edition A, Edition B and the A-to-B
table. Explain the initial watch/defer thesis and the evidence that now conditions
it. Show the assistant's original flat-fee claim, the actual PMA escalation clause,
and the corrected calculation. State your actual accept/modify/reject decision
after reviewing it. Existing Lab 11 records are preserved; do not invent a lock time.

## Video 2 - technical ownership, maximum 5:00

Use docs/video-2-rehearsal-script.md. Show the actual submitted repository version,
input files, src/commercialization.py and one meaningful assertion in the tests.
Demonstrate the command that produces the frozen output. Explain FCFF, equity
roll-forward, advance milestone fees, and why equity funding is not counted twice.
Show the tests running and describe what a pass does and does not establish.

## Video 3 - committee decision and live demonstration, maximum 5:00

Use docs/video-3-rehearsal-script.md. Lead with watch/defer and the committee ask.
Make the live app the main delivery: summary, one annual schedule, sensitivity,
exit and monitoring. Explain that a 10x exit can materially change the stronger
case, so no mechanical target or guaranteed downside is claimed. End with the
observable conditions that could change the recommendation.

## Recording and submission mechanics

Include clear audio, readable screen text and a small webcam view unless an
approved accommodation provides another format. Aim below each maximum.
Keep three separate recordings. Upload Unlisted or Public, or use an approved
Purdue-hosted equivalent; never Private. Correct substantive caption errors.
After recording, save the actual corrected transcripts as
docs/transcript-video-1.txt, docs/transcript-video-2.txt and
docs/transcript-video-3.txt. Scripts are rehearsal material, not transcripts.

Add actual URLs, titles, durations and evidence timestamps to the manifest.
Retain the exact submitted recordings unchanged after the deadline.

## Before calling the package submission-complete

- Confirm which original Lab 11 record establishes prediction timing and tool use.
- Personally review the recommendation, source correction and material assumptions.
- Verify repository access and record the actual submitted commit/branch.
- Record a genuine outside-user cold run if required by the assignment.
- Add the recordings, corrected transcripts and actual access checks.

Those are firsthand or post-recording facts. The assistant's successful clean
run and the existing source hash do not fabricate them.
'''
    (ROOT / 'RECORDING-GUIDE.md').write_text(guide)
    print('Prepared RECORDING-GUIDE.md and recording snapshot ' + freeze[:16])


if __name__ == '__main__':
    main()
