from .uuid_seq import UUIDSequenceTransformer
from .redact import RedactTransformer
from .date_fmt import DateFormatTransformer

registry = {
    'uuid_seq': UUIDSequenceTransformer,
    'redact': RedactTransformer,
    'date_fmt': DateFormatTransformer,
}