import json, subprocess, sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


def test_classify_exit_zero_and_output():
    qdir = REPO / 'tests' / 'fixtures' / 'shield_quarantine'
    qdir.mkdir(parents=True, exist_ok=True)
    (qdir / 'manifest.json').write_text(json.dumps({'files':[{'bytes':1}]}) + '\n', encoding='utf-8')
    out = qdir / 'classification.json'
    if out.exists():
        out.unlink()
    p = subprocess.run([sys.executable, str(REPO / 'src' / 'classify.py'), str(qdir)], capture_output=True, text=True)
    assert p.returncode == 0, p.stderr
    assert out.exists()
    data = json.loads(out.read_text(encoding='utf-8'))
    assert data['classification'] == 'suspicious'
