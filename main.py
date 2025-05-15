from reader import read_csv
from writer import write_csv

class TransformerApp:
    def __init__(self, config):
        self.config = config

    def run(self):
        # Read, transform, collect rows lazily
        def gen():
            for row in read_csv(self.config.input_path):
                out = {}
                for col in self.config.columns:
                    raw = row.get(col, '')
                    tf = self.config.transforms.get(col)
                    out[col] = tf.apply(raw) if tf else raw
                yield out

        write_csv(
            self.config.output_path,
            self.config.columns,
            gen()
        )