"""Audit objective pre-recording readiness without inventing confirmations."""
import csv
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from app import load_record


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    checks = []
    record = load_record()
    checks.append('Frozen output matches current material inputs and analysis source.')
    visible = json.loads((ROOT / 'visible_output.json').read_text())
    for frozen, summary in zip(record['results'], visible['scenario_results']):
        for key in ('name', 'value_per_share', 'funding_net_m'):
            if frozen[key] != summary[key]:
                raise ValueError('Visible summary differs from executed output.')
        if any(abs(r['balance_gap']) > 1e-7 for r in frozen['rows']):
            raise ValueError('Unreconciled forecast balance sheet.')
    checks.append('Visible summary and scenario balance sheets reconcile to executed output.')
    snapshot = json.loads((ROOT / 'evidence/recording-snapshot.json').read_text())
    for name, expected in snapshot['files'].items():
        if sha(ROOT / name) != expected:
            raise ValueError('Stale recording snapshot: ' + name)
    checks.append('Recording snapshot matches current inputs, code and output.')
    for r in json.loads((ROOT / 'evidence/document-sources.json').read_text()):
        if sha(ROOT / r['source']) != r['source_sha256'] or sha(ROOT / r['pdf']) != r['pdf_sha256']:
            raise ValueError('Stale PDF or source: ' + r['source'])
        if sha(ROOT / r['repository_copy']) != r['pdf_sha256']:
            raise ValueError('Repository PDF differs from reviewed PDF.')
    checks.append('Three PDFs match their Markdown sources and repository copies.')
    pdfs = json.loads((ROOT / 'evidence/pdf-checks.json').read_text())
    memo = next(x for x in pdfs if x['file'] == 'Decision-Memo-DRAFT.pdf')
    if memo['pages'] > 2 or any(x['text_bounds'] != 'PASS' for x in pdfs):
        raise ValueError('PDF page limit or bounds failed.')
    checks.append('Memo is at most two pages; PDF page bounds passed.')
    lab = json.loads((ROOT / 'evidence/lab11-source-integrity.json').read_text())
    path = ROOT / 'evidence/lab11-smr/SMR_Base_Run_2026-09-29/lab10_smr_proforma.py'
    if sha(path) != lab['source_sha256_recorded']:
        raise ValueError('Preserved original Lab 11 model hash differs.')
    checks.append('Preserved Lab 11 source matches the original result hash.')
    with (ROOT / 'submission-manifest.csv').open(newline='') as file:
        rows = list(csv.DictReader(file))
    if len(rows) != 12 or sum(r['required'] == 'yes' for r in rows) != 11:
        raise ValueError('Manifest must have 12 rows, 11 required.')
    for r in rows:
        value = r['location_or_url']
        if value and not value.startswith(('https://', 'http://')):
            if not (ROOT / value).is_file():
                raise ValueError('Missing manifest file: ' + value)
            if r['frozen_or_commit_id'].startswith('sha256:') and r['frozen_or_commit_id'][7:] != sha(ROOT / value):
                raise ValueError('Stale manifest hash: ' + value)
    checks.append('Manifest local paths and hashes are valid.')
    if not (ROOT / 'RECORDING-GUIDE.md').is_file() or any(
            not (ROOT / f'docs/video-{n}-rehearsal-script.md').is_file() for n in (1,2,3)):
        raise ValueError('Missing guide or rehearsal script.')
    checks.append('Recording guide and three rehearsal scripts exist.')
    report = dict(timestamp_utc=datetime.now(timezone.utc).isoformat(),
                  automated_pre_recording_checks='PASS', checks=checks,
                  snapshot_sha256=snapshot['snapshot_sha256'],
                  pending_firsthand=['Original Lab 11 timing and actual tool boundary',
                                     'Student source/assumption review and dispositions',
                                     'Outside-user cold run if required'],
                  pending_post_recording=['Three recordings and corrected transcripts',
                                          'Video URLs/durations/indices and access checks'],
                  submission_complete=False)
    (ROOT / 'evidence/pre-recording-checks.json').write_text(json.dumps(report, indent=2) + '\n')
    print(f'PASS: {len(checks)} objective pre-recording checks.')
    print('Firsthand confirmations and post-recording artifacts remain separate.')


if __name__ == '__main__':
    main()
