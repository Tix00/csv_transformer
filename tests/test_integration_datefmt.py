import sys
import subprocess
from pathlib import Path

def test_cli_date_fmt(tmp_path):
    in_csv = tmp_path / 'in.csv'
    out_csv = tmp_path / 'out.csv'
    in_csv.write_text("dt\n2025-03-23 16:54:43 CET\n")

    cmd = [
        sys.executable,
        'cli.py',
        str(in_csv),
        str(out_csv),
        '--columns', 'dt',
        '--transform', 'dt=date_fmt',
        '--tz-source', 'CET',
        '--tz-target', 'UTC',
        '--date-format', '%Y-%m-%d %H:%M:%S'
    ]
    res = subprocess.run(
        cmd,
        cwd=str(Path(__file__).parent.parent),
        capture_output=True,
        text=True
    )
    assert res.returncode == 0
    assert out_csv.read_text().splitlines()[1] == '2025-03-23 15:54:43'