"""Guard the frozen analysis-to-interface contract."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ApplicationChecks(unittest.TestCase):
    def test_summary_uses_current_frozen_results(self):
        output = json.loads((ROOT / 'output/commercialization-output.json').read_text())
        shown = subprocess.run([sys.executable, '-I', str(ROOT / 'app.py'), 'summary'],
                               capture_output=True, text=True, check=True).stdout
        self.assertIn('not fair value', shown)
        for result in output['results']:
            self.assertIn(f"${result['value_per_share']:.2f}", shown)

    def test_changed_inputs_cannot_silently_display_old_values(self):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder)
            for name in ('app.py', 'build_scenarios.py', 'src/commercialization.py',
                         'output/commercialization-output.json',
                         'data/research-inputs.json', 'data/commercialization-scenarios.json'):
                (target / name).parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(ROOT / name, target / name)
            path = target / 'data/research-inputs.json'
            record = json.loads(path.read_text())
            record['price_usd'] += 1
            path.write_text(json.dumps(record))
            result = subprocess.run([sys.executable, '-I', str(target / 'app.py')],
                                    capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('Stale output', result.stderr)

    def test_year_outside_forecast_is_actionable_error(self):
        result = subprocess.run([sys.executable, '-I', str(ROOT / 'app.py'),
                                 'scenario', '--year', '2040'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn('2026 and 2036', result.stderr)


if __name__ == '__main__':
    unittest.main()
