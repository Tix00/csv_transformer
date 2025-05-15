from dateutil import parser as date_parser
from zoneinfo import ZoneInfo
from .base import Transformer

class DateFormatTransformer(Transformer):
    def __init__(self, tz_source='UTC', tz_target='UTC', date_format='%Y-%m-%d', **kwargs):
        super().__init__(**kwargs)
        self.src = ZoneInfo(tz_source)
        self.tgt = ZoneInfo(tz_target)
        self.date_format = date_format
        self.tzinfos = {
            'CET': ZoneInfo('Europe/Paris'),  # or another appropriate CET-mapped zone
            'CEST': ZoneInfo('Europe/Paris'),
            'UTC': ZoneInfo('UTC'),
        }

    def apply(self, value):
        dt = date_parser.parse(value, tzinfos=self.tzinfos)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=self.src)
        dt = dt.astimezone(self.tgt)
        return dt.strftime(self.date_format)
