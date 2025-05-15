#!/usr/bin/env python3
import sys
from config import Config
from main import TransformerApp

def main():
    try:
        cfg = Config.from_args(sys.argv[1:])
        app = TransformerApp(cfg)
        app.run()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()