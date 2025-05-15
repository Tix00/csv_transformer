import sys
import subprocess
from pathlib import Path

def test_empty_csv(tmp_path):
    in_csv = tmp_path / 'in.csv'
    out_csv = tmp_path / 'out.csv'
    in_csv.write_text("a,b,c\n")

    cmd = [
        sys.executable,
        'cli.py',
        str(in_csv),
        str(out_csv),
        '--columns', 'a,b'
    ]
    res = subprocess.run(
        cmd,
        cwd=str(Path(__file__).parent.parent),
        capture_output=True,
        text=True
    )
    assert res.returncode == 0
    lines = out_csv.read_text().splitlines()
    assert lines[0] == 'a,b'
    assert len(lines) == 1