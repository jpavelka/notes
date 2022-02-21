import os
import re
from pathlib import Path


def add_sections(text):
    text = text.split('\n')
    for i, s in enumerate(text):
        if re.search('^\{insertSection:', s):
            sec_path = Path('md_src/' + s.split(':')[1][:-1])
            sec_text = sec_path.read_text()
            text[i] = sec_text
    return '\n'.join(text)


def youtube_embed(text, dest_ftype):
    text = text.split('\n')
    for i, s in enumerate(text):
        if re.search('^\{videoEmbedYoutube:', s):
            if dest_ftype == 'html':
                vid_id = s.split(':')[1][:-1]
                s = """
                <div class="ytEmbedContainerContainer">
                    <div class="ytEmbedContainer">
                        <iframe
                            src="https://www.youtube.com/embed/{}"
                            title="YouTube video player"
                            frameborder="0"
                            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                            allowfullscreen>
                        </iframe>
                    </div>
                </div>
                """.format(vid_id)
                text[i] = ' '.join(x.strip() for x in s.split('\n'))
                print(text[i])
            else:
                text[i] = ''
    return '\n'.join(text)


def alter_eq_refs(text):
    text = text.split('\n')
    for i, s in enumerate(text):
        if i == 0:
            continue
        if re.search('^\{#', s):
            last_line_math = re.search(
                '\$\$$', text[i - 1].strip()) is not None
            if last_line_math:
                text[i - 1] += s
                text[i] = ''
                continue
            last_lines_blank_then_math = i > 1 and (
                text[i - 1].strip() == '' and re.search('\$\$$', text[i - 2].strip()) is not None)
            if last_lines_blank_then_math:
                text[i - 2] += s
                text[i] = ''
    return '\n'.join(text)


def format_notes(text, dest_ftype):
    text = text.split('\n')
    for i, s in enumerate(text):
        if re.search('^\{noteText:', s):
            note_text = 'noteText:'.join(s.split('noteText:')[1:])[:-1].strip()
            if dest_ftype in ['md', 'html']:
                text[i] = '<details><summary>Note</summary>{}</details>'.format(
                    note_text)
            else:
                text[i] = note_text
    return '\n'.join(text)


def pandoc_convert(fpath, dest_fpath):
    fpath = Path(fpath)
    dest_fpath = Path(dest_fpath)
    dest_ftype = dest_fpath.suffix[1:]
    cmds = [
        'pandoc',
        '-s {}'.format(fpath),
        '-o {}'.format(dest_fpath),
        '--toc',
        '--number-sections',
        '--filter pandoc-xnos'
    ]
    if dest_ftype == 'html':
        cmds += [
            '--katex=https://cdn.jsdelivr.net/npm/katex@0.15.2/dist/',
            '--metadata pagetitle="{}"'.format(fpath.stem),
        ]
        for fname in os.listdir('html/header'):
            cmds.append('--include-in-header=html/header/' + fname)
        for fname in os.listdir('html/before-body'):
            cmds.append('--include-before-body=html/before-body/' + fname)
        for fname in os.listdir('html/after-body'):
            cmds.append('--include-after-body=html/after-body/' + fname)
    cmd = ' '.join(cmds)
    print(cmd)
    os.system(' '.join(cmds))


def html_post_process(text):
    text = text.split('\n')
    for i, s in enumerate(text):
        if re.search('^<nav id="TOC">', s):
            text[
                i] += '\n<div><p class="tocHeader">Contents</p><a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a></div>'
        if re.search('^</nav>$', s):
            text[i] += '\n<div id="main">'
    return '\n'.join(text)
    print()
