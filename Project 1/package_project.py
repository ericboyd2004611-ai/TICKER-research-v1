"""Create an honest local review archive and 12-row course manifest."""
import csv
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parent
FIELDS = ['item', 'required', 'location_or_url', 'title', 'duration_or_as_of',
          'timestamp_index', 'access_checked', 'frozen_or_commit_id', 'notes']


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    previous = {}
    if (ROOT / 'submission-manifest.csv').exists():
        with (ROOT / 'submission-manifest.csv').open(newline='') as file:
            previous = {r['item']: r for r in csv.DictReader(file)}
    rows = []
    local = {
        'Research-Evolution.pdf': ('output/pdf/Research-Evolution-DRAFT.pdf', 'Edition A text plus research evolution review draft', 'Edition A text included; student reports professor-approved text format. Edition B remains AI-generated and pending review'),
        'Visible executed output': ('output/commercialization-report.md', 'Executed conditional valuation and financing evidence', 'Local output exists; operating exit is an explicit assumption with sensitivity'),
        'Decision memo or deck': ('output/pdf/Decision-Memo-DRAFT.pdf', 'Watch/defer decision memo - review draft', 'AI-generated proposal; student approval and independent checks pending'),
        'Validation-and-AI-Use.pdf': ('output/pdf/Validation-and-AI-Use-DRAFT.pdf', 'Validation and AI use - review draft', 'Existing NuScale Lab 11 prediction/results included; original timing and tool boundary need verification; student dispositions pending'),
    }
    items = ['Research-Evolution.pdf', 'Repository', 'Visible executed output',
             'Decision memo or deck', 'Validation-and-AI-Use.pdf',
             'Video 1', 'Transcript Video 1', 'Video 2', 'Transcript Video 2',
             'Video 3', 'Transcript Video 3', 'Optional deployed output']
    for item in items:
        row = dict.fromkeys(FIELDS, '')
        row.update(item=item, required='no' if item == 'Optional deployed output' else 'yes')
        if item in local:
            location, title, notes = local[item]
            row.update(location_or_url=location, title=title, duration_or_as_of='2026-09-01 close',
                       access_checked='local file only; external access not checked',
                       frozen_or_commit_id='sha256:' + digest(ROOT / location), notes=notes)
        elif item == 'Repository':
            row.update(location_or_url='https://github.com/ericboyd2004611-ai/TICKER-research-v1',
                       title='Existing course repository remote',
                       notes='NOT READY: remote exists in git config; this project has not been uploaded or access-verified; no commit ID claimed')
            if previous.get(item, {}).get('frozen_or_commit_id'):
                row.update(previous[item])
            status_path = ROOT / 'evidence/repository-status.json'
            if status_path.exists():
                status = json.loads(status_path.read_text())
                row.update(location_or_url=status['project_url'],
                           title='NuScale Project 1 - separate submission branch',
                           frozen_or_commit_id=status.get('source_commit', ''),
                           access_checked='git remote branch verified; instructional-team access pending' if status['published'] else '',
                           notes='Published source snapshot; videos and firsthand confirmation still pending' if status['published'] else 'Prepared isolated branch; publication verification pending')
        elif item.startswith('Video'):
            row['notes'] = f'MISSING actual recording/URL/duration/index. Rehearsal only: docs/video-{item[-1]}-rehearsal-script.md'
            if previous.get(item, {}).get('location_or_url'):
                row.update(previous[item])
        elif item.startswith('Transcript'):
            row['notes'] = 'MISSING corrected transcript of actual recording; a rehearsal script is not a transcript'
            if previous.get(item, {}).get('location_or_url'):
                row.update(previous[item])
        else:
            row['notes'] = 'Not required; no deployment performed'
        rows.append(row)
    if len(rows) != 12 or sum(r['required'] == 'yes' for r in rows) != 11:
        raise ValueError('Course manifest must contain 12 rows, 11 required')
    with (ROOT / 'submission-manifest.csv').open('w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    submission = ROOT / 'submission'
    submission.mkdir(exist_ok=True)
    import shutil
    for original, final in [('Decision-Memo-DRAFT.pdf', 'Decision-Memo.pdf'),
                            ('Research-Evolution-DRAFT.pdf', 'Research-Evolution.pdf'),
                            ('Validation-and-AI-Use-DRAFT.pdf', 'Validation-and-AI-Use.pdf')]:
        shutil.copy2(ROOT / 'output/pdf' / original, submission / final)
    shutil.copy2(ROOT / 'submission-manifest.csv', submission / 'submission-manifest.csv')
    files = sorted(p for p in ROOT.rglob('*') if p.is_file()
                   and not any(part in ('__pycache__', '.git', '.venv', 'tmp') for part in p.relative_to(ROOT).parts)
                   and p.suffix not in ('.pyc', '.zip') and p.name not in ('.DS_Store', 'package-inventory.json'))
    inventory = dict(label='AI-generated local review package; course submission incomplete',
                     created_utc=datetime.now(timezone.utc).isoformat(),
                     files=[dict(path=str(p.relative_to(ROOT)), bytes=p.stat().st_size, sha256=digest(p)) for p in files],
                     unresolved=['Original Lab 11 timing/tool-boundary evidence verification',
                                 'Student source and AI review', 'Recordings and actual transcripts',
                                 'Verified repository/video access and freeze', 'Supported full fair-value analysis'])
    inventory_path = ROOT / 'evidence/package-inventory.json'
    inventory_path.write_text(json.dumps(inventory, indent=2) + '\n')
    archive = ROOT / 'output/Project-1-SMR-Review-Package.zip'
    with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as zipped:
        for path in files + [inventory_path]:
            zipped.write(path, 'Project 1/' + str(path.relative_to(ROOT)))
    with zipfile.ZipFile(archive) as zipped:
        if zipped.testzip() is not None:
            raise ValueError('Archive integrity check failed')
    print(f'Created {archive.name}: {archive.stat().st_size:,} bytes')
    print(f'{len(files)} files plus inventory; 12-row manifest. Course submission remains incomplete.')


if __name__ == '__main__':
    main()
