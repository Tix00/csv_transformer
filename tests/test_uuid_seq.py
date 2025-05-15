from transformers.uuid_seq import UUIDSequenceTransformer

def test_uuid_sequence():
    t = UUIDSequenceTransformer()
    assert t.apply('x') == '1'
    assert t.apply('y') == '2'
    assert t.apply('x') == '1'