from collections import OrderedDict
from .base import Transformer

class UUIDSequenceTransformer(Transformer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._map = OrderedDict()
        self._next_id = 1

    def apply(self, value):
        if value not in self._map:
            self._map[value] = self._next_id
            self._next_id += 1
        return str(self._map[value])