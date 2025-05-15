import sys
import subprocess
from pathlib import Path

def test_cli_unknown_transform(tmp_path):
    in_csv = tmp_path / 'in.csv'
    out_csv = tmp_path / 'out.csv'
    in_csv.write_text("a\n1\n")

    cmd = [
        sys.executable,
        'cli.py',
        str(in_csv),
        str(out_csv),
        '--columns', 'a',
        '--transform', 'a=bad_tf'
    ]
    res = subprocess.run(
        cmd,
        cwd=str(Path(__file__).parent.parent),
        capture_output=True,
        text=True
    )
    assert res.returncode != 0
    assert 'Unknown transform' in res.stderr