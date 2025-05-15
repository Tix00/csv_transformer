from transformers.redact import RedactTransformer

def test_redact_preserves_length_and_type():
    t = RedactTransformer()
    orig = 'A1!'
    out = t.apply(orig)
    assert len(out) == len(orig)
    for o, r in zip(orig, out):
        if o.isalpha(): assert r.isalpha()
        if o.isdigit(): assert r.isdigit()
        if not o.isalnum(): assert r == o