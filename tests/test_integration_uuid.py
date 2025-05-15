import sys
import subprocess
from pathlib import Path

def test_cli_uuid_seq(tmp_path):
    in_csv = tmp_path / 'in.csv'
    out_csv = tmp_path / 'out.csv'
    in_csv.write_text("id\nUID1\nUID2\n")

    cmd = [
        sys.executable,
        'cli.py',
        str(in_csv),
        str(out_csv),
        '--columns', 'id',
        '--transform', 'id=uuid_seq'
    ]
    res = subprocess.run(
        cmd,
        cwd=str(Path(__file__).parent.parent),
        capture_output=True,
        text=True
    )
    assert res.returncode == 0

    lines = out_csv.read_text().splitlines()
    assert lines[1] == '1'
    assert lines[2] == '2'