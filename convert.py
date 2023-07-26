import argparse
from pathlib import Path

from py_parsers.parse import py_parse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dest_ftype', default='html')
    parser.add_argument('--dest_fname', default='converted')
    args = parser.parse_args()
    text = Path('md_src/src.md').read_text()
    py_parse(text, args.dest_ftype, args.dest_fname)
