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
    os.system('pandoc citations.bibtex -s -f bibtex -t markdown > citations.md')
    cmds = [
        'pandoc',
        '-s {}'.format(fpath),
        '-o {}'.format(dest_fpath),
        '--toc',
        '--toc-depth 2',
        '--number-sections',
        '--filter pandoc-xnos',
        '--citeproc citations.md',
        '-M link-citations=true'
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
    os.system(' '.join(cmds))


def html_post_process(text):
    text = text.split('\n')
    for i, s in enumerate(text):
        if re.search('^<nav id="TOC"', s):
            text[
                i] += '\n<div id="tocTop"><div class="tocHeader">Contents</div><div><a href="javascript:void(0)" class="closeBtn" onclick="closeNav()">&times;</a></div></div>'
        if re.search('^</nav>$', s):
            text[i] += '\n<div id="main" onclick="closeNavIfSmall()">'
    text = add_citations_header(text)
    text = add_hover_footnotes(text)
    return text


def add_citations_header(text_lines):
    for i, line in enumerate(text_lines):
        if re.search('^<div id="refs"', line):
            text_lines.insert(i, '<h1 id="References">References</h1>')
            break
    return text_lines


def add_hover_footnotes(text_lines):
    final_lines = []
    removed_lines = []
    in_footnotes = False
    for line in text_lines:
        if in_footnotes:
            if re.search('^</section>$', line.strip()):
                in_footnotes = False
            removed_lines.append(line)
            continue
        if re.search('<section id="footnotes"', line):
            in_footnotes = True
            removed_lines.append(line)
            continue
        final_lines += [line]
    text = '\n'.join(final_lines)
    removed_text = ' '.join(removed_lines)
    matches = re.findall(
        '<a href=[^<]*class="footnote-ref"[^<]*><sup>[^<]*</sup></a>', text)
    for match in matches:
        id = match.split('href="#')[-1].split('"')[0]
        ref_id = match.split('id="')[-1].split('"')[0]
        li_str = f'<li id="{id}">'
        hover_text = '<p>'.join('<a'.join(re.findall(
            f'{li_str}.*?(?=<\/li>)', removed_text)[0].split('<a')[:-1]).split('<p>')[1:])
        hover_text = f'<b>Footnote {id[2:]}:</b> ' + hover_text
        hover_id = f'{id}Hover'
        match_replace_list = match.split('</sup>')
        match_replace_list.insert(1, '</sup>')
        match_replace = ''.join(match_replace_list)
        match_replace = re.sub('^<a', '<span', match_replace)
        match_replace = re.sub('a>$', 'span>', match_replace)
        match_replace = re.sub(f'href="#{id}" ', '', match_replace)
        match_replace = re.sub(
            f'<sup>', f"""<sup onclick="footnoteOnTooltipClick('{hover_id}', '{hover_text.replace('"', '@@@')}', '{ref_id}')">""", match_replace)
        text = text.replace(match, match_replace)
    return text
