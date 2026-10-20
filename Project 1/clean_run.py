"""Assistant clean-directory rehearsal; never claims a human cold-run reviewer."""
from datetime import datetime, timezone
import hashlib
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent


def main():
    lines = ['# Assistant clean-directory rehearsal', '',
             'This is an assistant-run reproducibility check, not an outside human review.',
             'Timestamp: ' + datetime.now(timezone.utc).isoformat(),
             'Python: ' + sys.version.replace('\n', ' '), '',
             'Commands run with -I -S: isolated mode, with site-package loading disabled.', '']
    with tempfile.TemporaryDirectory(prefix='smr-clean-') as folder:
        target = Path(folder)
        for path in ROOT.iterdir():
            if path.is_file() and path.suffix in ('.py', '.md', '.txt', '.json', '.csv'):
                shutil.copy2(path, target / path.name)
        for name in ('src', 'tests', 'data', 'docs'):
            shutil.copytree(ROOT / name, target / name,
                            ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
        commands = [
            ['build_scenarios.py'], ['research_bridge.py'], ['analysis.py'],
            ['prepare_drafts.py'], ['verify_project.py'], ['app.py', 'summary'],
            ['app.py', 'scenario', '--scenario', 'stronger', '--year', '2030'],
            ['app.py', 'sensitivity'], ['app.py', 'exit'], ['app.py', 'reverse'], ['app.py', 'sources'],
            ['app.py', 'monitoring'], ['app.py', 'readiness'],
        ]
        for args in commands:
            result = subprocess.run([sys.executable, '-I', '-S'] + args, cwd=target,
                                    capture_output=True, text=True)
            lines += ['## ' + 'python3 -I -S ' + ' '.join(args), '',
                      '```text', result.stdout + result.stderr, '```', '']
            if result.returncode:
                (ROOT / 'evidence/clean-run.md').write_text('\n'.join(lines))
                raise SystemExit(f'Clean run failed: {args}')
        for name in ('commercialization-output.json', 'research-bridge.json', 'downside-output.json'):
            expected = hashlib.sha256((ROOT / 'output' / name).read_bytes()).hexdigest()
            actual = hashlib.sha256((target / 'output' / name).read_bytes()).hexdigest()
            if actual != expected:
                raise SystemExit(f'Output mismatch in clean run: {name}')
        lines += ['## Result', '', 'PASS: all commands succeeded; all three JSON outputs matched byte for byte.',
                  'First clean-run failure: none. Outside-user review remains outstanding.', '']
    (ROOT / 'evidence').mkdir(exist_ok=True)
    (ROOT / 'evidence/clean-run.md').write_text('\n'.join(lines))
    print('Clean-directory rehearsal passed. evidence/clean-run.md')


if __name__ == '__main__':
    main()
