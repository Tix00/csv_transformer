import sys
import subprocess
from pathlib import Path

def test_cli_redact(tmp_path):
    in_csv = tmp_path / 'in.csv'
    out_csv = tmp_path / 'out.csv'
    in_csv.write_text("name,email\nJohn,doe@example.com\n")

    cmd = [
        sys.executable,
        'cli.py',
        str(in_csv),
        str(out_csv),
        '--columns', 'name,email',
        '--transform', 'name=redact,email=redact'
    ]
    res = subprocess.run(
        cmd,
        cwd=str(Path(__file__).parent.parent),
        capture_output=True,
        text=True
    )
    assert res.returncode == 0

    lines = out_csv.read_text().splitlines()
    assert lines[0] == 'name,email'
    assert lines[1] != 'John,doe@example.com'