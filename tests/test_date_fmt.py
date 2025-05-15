from transformers.date_fmt import DateFormatTransformer

def test_date_fmt_default():
    t = DateFormatTransformer(tz_source='UTC', tz_target='UTC')
    assert t.apply('2025-05-15T13:45:00Z') == '2025-05-15'

def test_date_fmt_custom_format():
    t = DateFormatTransformer(
        tz_source='UTC',
        tz_target='UTC',
        date_format='%d/%m/%Y %H:%M'
    )
    assert t.apply('2025-05-15T13:45:00Z') == '15/05/2025 13:45'