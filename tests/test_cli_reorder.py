import sys
import subprocess
from pathlib import Path

def test_cli_reorder(tmp_path):
    in_csv = tmp_path / 'in.csv'
    out_csv = tmp_path / 'out.csv'
    # Write header and one row
    in_csv.write_text("a,b,c\n1,2,3\n")

    cmd = [
        sys.executable,
        'cli.py',
        str(in_csv),
        str(out_csv),
        '--columns', 'c,b,a'
    ]
    res = subprocess.run(
        cmd,
        cwd=str(Path(__file__).parent.parent),
        capture_output=True,
        text=True
    )
    assert res.returncode == 0

    lines = out_csv.read_text().splitlines()
    assert lines[0] == 'c,b,a'
    assert lines[1] == '3,2,1'