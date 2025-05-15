import argparse
import os

from transformers import registry as transformer_registry

class Config:
    def __init__(self, input_path, output_path, columns, transforms, tz_source, tz_target, date_format):
        self.input_path = input_path
        self.output_path = output_path
        self.columns = columns
        self.transforms = transforms
        self.tz_source = tz_source
        self.tz_target = tz_target
        self.date_format = date_format

    @staticmethod
    def from_args(args):
        parser = argparse.ArgumentParser(
            description="CSV Transformer CLI"
        )
        parser.add_argument('input', help='Input CSV file path')
        parser.add_argument('output', help='Output CSV file path')
        parser.add_argument(
            '--columns', '-c',
            required=True,
            help='Comma-separated list of output column order'
        )
        parser.add_argument(
            '--transform', '-t',
            default='',
            help=('Comma-separated column=transform pairs. '
                  f"Available: {', '.join(transformer_registry.keys())}")
        )
        parser.add_argument('--tz-source', default='UTC', help='Source timezone')
        parser.add_argument('--tz-target', default='UTC', help='Target timezone')
        parser.add_argument(
            '--date-format',
            default='%Y-%m-%d',
            help='Date format for date_fmt transformer (e.g. %%Y-%%m-%%d %%H:%%M:%%S)'
        )
        parsed = parser.parse_args(args)

        if not os.path.isfile(parsed.input):
            raise FileNotFoundError(f"Input file not found: {parsed.input}")

        cols = [c.strip() for c in parsed.columns.split(',') if c.strip()]
        tx_map = {}
        if parsed.transform:
            for pair in parsed.transform.split(','):
                col, tf_name = pair.split('=', 1)
                col = col.strip(); tf_name = tf_name.strip()
                if tf_name not in transformer_registry:
                    raise ValueError(f"Unknown transform: {tf_name}")
                tx_cls = transformer_registry[tf_name]
                tx_map[col] = tx_cls(
                    tz_source=parsed.tz_source,
                    tz_target=parsed.tz_target,
                    date_format=parsed.date_format
                )

        return Config(
            input_path=parsed.input,
            output_path=parsed.output,
            columns=cols,
            transforms=tx_map,
            tz_source=parsed.tz_source,
            tz_target=parsed.tz_target,
            date_format=parsed.date_format
        )