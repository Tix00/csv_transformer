from reader import read_csv
from writer import write_csv

def test_reader_writer_roundtrip(tmp_path):
    data = tmp_path / 'in.csv'
    out = tmp_path / 'out.csv'
    data.write_text("a,b,c\n1,2,3\n")

    rows = list(read_csv(str(data)))
    assert rows == [{'a': '1', 'b': '2', 'c': '3'}]

    write_csv(str(out), ['a', 'b', 'c'], rows)
    assert '1,2,3' in out.read_text()