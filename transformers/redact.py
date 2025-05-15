from faker import Faker
from .base import Transformer

class RedactTransformer(Transformer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.fake = Faker()

    def apply(self, value):
        # Preserve length, replace letters/digits
        result = []
        for ch in value:
            if ch.isdigit():
                result.append(self.fake.random_digit())
            elif ch.isalpha():
                result.append(self.fake.random_letter())
            else:
                result.append(ch)
        return ''.join(str(c) for c in result)