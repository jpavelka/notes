import argparse
import re
import tempfile
from pathlib import Path

from py_parsers import utils


def py_parse(text, dest_ftype):
    text = utils.add_sections(text)
    text = utils.youtube_embed(text, dest_ftype)
    text = utils.alter_eq_refs(text)
    text = utils.format_notes(text, dest_ftype)
    fpath = Path(tempfile.gettempdir()) / 'parsed.md'
    fpath.write_text(text)
    final_fpath = Path('converted/converted.' + dest_ftype)
    if dest_ftype == 'html':
        md_fpath = fpath
        fpath = Path(tempfile.gettempdir()) / 'pandoced.html'
        utils.pandoc_convert(md_fpath, fpath)
        text = fpath.read_text()
        text = utils.html_post_process(text)
        final_fpath.write_text(text)
    else:
        utils.pandoc_convert(fpath, final_fpath)
