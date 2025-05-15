import sys
import subprocess
from pathlib import Path

def test_cli_combined(tmp_path):
    in_csv = tmp_path / 'in.csv'
    out_csv = tmp_path / 'out.csv'
    in_csv.write_text("id,name,dt\nX,John,2025-01-01T00:00:00Z\n")

    cmd = [
        sys.executable,
        'cli.py',
        str(in_csv),
        str(out_csv),
        '--columns', 'id,name,dt',
        '--transform', 'id=uuid_seq,name=redact,dt=date_fmt',
        '--tz-source', 'UTC',
        '--tz-target', 'UTC',
        '--date-format', '%Y-%m-%d'
    ]
    res = subprocess.run(
        cmd,
        cwd=str(Path(__file__).parent.parent),
        capture_output=True,
        text=True
    )
    assert res.returncode == 0
    parts = out_csv.read_text().splitlines()[1].split(',')
    assert parts[0] == '1'
    assert parts[2] == '2025-01-01'