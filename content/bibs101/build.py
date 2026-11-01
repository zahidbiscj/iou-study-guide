#!/usr/bin/env python3
"""Build BIBS 101 modules from content/bibs101/src/modNN.txt.

Outputs:
  bibs/modNN.js            lazy-loaded module data for the site (BIBS_REG)
  bibs/index.js            module list (BIBS_MODS)
  content/bibs101/modNN.md printable study notes
  content/bibs101/COVERAGE.md

Source format (one file per module):
  title: English | বাংলা
  units: Units 1–2
  pdf: <file name in slides/Introduction to Business (BIBS 101)/>
  slides: <total slides>

  @concept | Title | শিরোনাম          free text; "~~" on its own line separates English from Bangla
  @words | Title | শিরোনাম            rows: term | English meaning | বাংলা অর্থ | example | উদাহরণ
  @lesson 1.1 | Title | শিরোনাম       intro of one study question (English ~~ Bangla)
  @slide 3,4 | Title | শিরোনাম        keys: TXT (optional override), BN, T, TB, E, EB, K, KB, IMG
  @check 1.1 | Title | শিরোনাম        MCQ items (see below)
  @together / @midterm / @summary     free text like @concept
  @quiz | Title | শিরোনাম             MCQ items

  MCQ item:  Q: question | প্রশ্ন
             O: option | *correct option | option | option
             OB: optional Bangla options (same order)
             X: explanation | ব্যাখ্যা

Text: blank lines separate blocks; "- " bullets, "1. " numbered, "### " heading,
lines starting with "<" are raw HTML, **bold**, *italic*.
"""
import html, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SRC = os.path.join(HERE, 'src')
EXT = os.path.join(HERE, 'src', 'slides.json')  # extracted slide text
SLIDE_DIR = 'slides/Introduction to Business (BIBS 101)/'
BND = '০১২৩৪৫৬৭৮৯'

MODS = [
    (1, 'Role of Business', 'ব্যবসার ভূমিকা', 'Units 1–2'),
    (2, 'Economic Environment', 'অর্থনৈতিক পরিবেশ', 'Units 3–4'),
    (3, 'Global Environment', 'বৈশ্বিক পরিবেশ', 'Units 5–6'),
    (4, 'Financial Markets & System', 'আর্থিক বাজার ও ব্যবস্থা', 'Unit 7'),
    (5, 'Legal Environment', 'আইনি পরিবেশ', 'Unit 8'),
    (6, 'Business Ethics', 'ব্যবসায়িক নৈতিকতা', 'Unit 9'),
    (7, 'Business Ownership', 'ব্যবসার মালিকানা', 'Units 10–11'),
    (8, 'Entrepreneurship', 'উদ্যোক্তা', 'Units 12–13'),
    (9, 'Management', 'ব্যবস্থাপনা', 'Units 14–15'),
]


def bnum(n):
    return ''.join(BND[int(c)] if c.isdigit() else c for c in str(n))


def inline(t):
    t = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', t)
    t = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'<i>\1</i>', t)
    return t


def md(text):
    """Very small markdown → HTML."""
    out, blk = [], []

    def flush():
        if not blk:
            return
        if blk[0].startswith('<'):
            out.append('\n'.join(blk))
        elif all(re.match(r'- ', x) for x in blk):
            out.append('<ul>' + ''.join('<li>%s</li>' % inline(x[2:]) for x in blk) + '</ul>')
        elif all(re.match(r'\d+\. ', x) for x in blk):
            out.append('<ol>' + ''.join('<li>%s</li>' % inline(re.sub(r'^\d+\. ', '', x)) for x in blk) + '</ol>')
        elif blk[0].startswith('### '):
            out.append('<h3>%s</h3>' % inline(blk[0][4:]))
            rest = blk[1:]
            blk.clear(); blk.extend(rest); flush(); return
        else:
            out.append('<p>%s</p>' % inline(' '.join(blk)))
        blk.clear()

    for line in text.strip('\n').split('\n'):
        line = line.rstrip()
        if not line.strip():
            flush(); continue
        if blk and (line.startswith('- ') != blk[0].startswith('- ') or
                    bool(re.match(r'\d+\. ', line)) != bool(re.match(r'\d+\. ', blk[0])) or
                    line.startswith('### ')) and not blk[0].startswith('<'):
            flush()
        blk.append(line)
    flush()
    return '\n'.join(out)


def labelled(cls, label, text):
    h = md(text)
    # put the label into the first paragraph; following blocks continue
    m = re.match(r'<p>(.*?)</p>', h, re.S)
    if m:
        return '<p class="lab %s"><b>%s</b> %s</p>%s' % (cls, label, m.group(1), h[m.end():].replace('<p>', '<p class="lab-cont">'))
    return '<p class="lab %s"><b>%s</b></p>%s' % (cls, label, h)


def parse(path):
    lines = open(path, encoding='utf-8').read().split('\n')
    head, blocks, cur = {}, [], None
    for ln in lines:
        if ln.startswith('@'):
            m = re.match(r'@(\w+)\s*([^|]*?)\s*(?:\|\s*(.*?)\s*(?:\|\s*(.*?)\s*)?)?$', ln)
            cur = {'kind': m.group(1), 'arg': m.group(2).strip(), 't': (m.group(3) or '').strip(), 'tb': (m.group(4) or '').strip(), 'body': []}
            blocks.append(cur)
        elif cur is None:
            m = re.match(r'(\w+):\s*(.*)$', ln)
            if m:
                head[m.group(1)] = m.group(2).strip()
        else:
            cur['body'].append(ln)
    return head, blocks


KEYS = ('TXT', 'BN', 'T', 'TB', 'E', 'EB', 'K', 'KB', 'IMG', 'Q', 'O', 'OB', 'X')


def keyed(body):
    """Split body lines into [(KEY, text)] in order."""
    items, cur = [], None
    for ln in body:
        m = re.match(r'(%s):\s?(.*)$' % '|'.join(KEYS), ln)
        if m:
            cur = [m.group(1), m.group(2)]
            items.append(cur)
        elif cur is not None:
            cur[1] += '\n' + ln
    return [(k, v.strip()) for k, v in items]


def split_lang(body):
    txt = '\n'.join(body)
    parts = re.split(r'^~~\s*$', txt, flags=re.M)
    if len(parts) != 2:
        raise SystemExit('missing ~~ separator in block starting: ' + txt[:80])
    return parts[0], parts[1]


def pair(en, bn):
    return ('<div class="pair">\n<div class="en"><span class="tag">English</span>\n%s</div>\n'
            '<div class="bn-box"><span class="tag">বাংলা</span>\n%s</div></div>' % (en, bn))


def mcq(body, where):
    items, it = [], None
    for k, v in keyed(body):
        if k == 'Q':
            q = [x.strip() for x in v.split(' | ')]
            assert len(q) == 2, (where, v)
            it = {'q': q[0], 'qbn': q[1]}; items.append(it)
        elif k == 'O':
            opts = [x.strip() for x in v.split(' | ')]
            assert len(opts) == 4, (where, v)
            ans = [i for i, o in enumerate(opts) if o.startswith('*')]
            assert len(ans) == 1, (where, v)
            it['ans'] = ans[0]; it['opts'] = [o.lstrip('*').strip() for o in opts]
        elif k == 'OB':
            ob = [x.strip() for x in v.split(' | ')]
            assert len(ob) == 4, (where, v)
            it['opts'] = ['%s · %s' % (a, b) for a, b in zip(it['opts'], ob)]
        elif k == 'X':
            x = [y.strip() for y in v.split(' | ')]
            assert len(x) == 2, (where, v)
            it['exp'], it['expbn'] = x
    for it in items:
        for f in ('q', 'qbn', 'opts', 'ans', 'exp', 'expbn'):
            assert f in it, (where, f, it.get('q'))
    return items


def plain(h):
    h = re.sub(r'<br\s*/?>', '\n', h)
    h = re.sub(r'</(p|li|h3|tr|blockquote|div)>', '\n', h)
    h = re.sub(r'<li>', '- ', h)
    h = re.sub(r'<b>(.*?)</b>', r'**\1**', h, flags=re.S)
    h = re.sub(r'<[^>]+>', '', h)
    h = html.unescape(h)
    return re.sub(r'\n{3,}', '\n\n', h).strip()


def build(n):
    path = os.path.join(SRC, 'mod%02d.txt' % n)
    head, blocks = parse(path)
    ext = json.load(open(EXT, encoding='utf-8'))[str(n)]
    total = ext['n']
    assert int(head['slides']) == total
    pdf = ext['file']
    pdf_url = (SLIDE_DIR + pdf).replace(' ', '%20').replace('(', '%28').replace(')', '%29')
    steps, seen, mdout, errors = [], {}, [], []
    t_en, t_bn = [x.strip() for x in head['title'].split('|')]
    mdout.append('# BIBS 101 · Module %d — %s\n\n**%s** · %s · %d slides · PDF: `%s`\n' % (n, t_en, t_bn, head['units'], total, pdf))
    lessons, checks = [], {}
    for b in blocks:
        k = b['kind']
        if k in ('concept', 'together', 'midterm', 'summary'):
            en, bn = split_lang(b['body'])
            h = pair(md(en), md(bn))
            steps.append({'id': k, 'k': k, 't': b['t'], 'tb': b['tb'], 'sl': [], 'h': h})
            mdout.append('## %s · %s\n\n%s\n\n%s\n' % (b['t'], b['tb'], plain(md(en)), plain(md(bn))))
        elif k == 'words':
            rows = [r for r in b['body'] if r.strip()]
            tr = []
            for r in rows:
                c = [x.strip() for x in r.split(' | ')]
                if len(c) != 5:
                    errors.append('words row needs 5 cells: ' + r); continue
                tr.append('<tr><td><b>%s</b></td><td>%s</td><td>%s</td><td>%s<br><span class="bn-only-inline">%s</span></td></tr>' % (inline(c[0]), inline(c[1]), inline(c[2]), inline(c[3]), inline(c[4])))
            h = ('<div class="tbl"><table class="wtable"><thead><tr><th>Term</th><th>Meaning (English)</th><th>অর্থ (বাংলা)</th><th>Example · উদাহরণ</th></tr></thead><tbody>'
                 + ''.join(tr) + '</tbody></table></div>')
            steps.append({'id': 'words', 'k': 'words', 't': b['t'], 'tb': b['tb'], 'sl': [], 'h': h})
            mdout.append('## %s · %s\n\n| Term | Meaning | অর্থ | Example |\n|---|---|---|---|\n%s\n' % (
                b['t'], b['tb'], '\n'.join('| ' + ' | '.join(r.split(' | ')[:3]) + ' | ' + r.split(' | ')[3] + ' |' for r in rows if len(r.split(' | ')) == 5)))
        elif k == 'lesson':
            en, bn = split_lang(b['body'])
            q = b['arg']
            lessons.append(q)
            h = '<p class="lesson-q"><b>Study question %s</b> · স্টাডি প্রশ্ন %s</p>' % (q, bnum(q)) + pair(md(en), md(bn))
            steps.append({'id': 'q' + q.replace('.', '-'), 'k': 'lesson', 't': 'Study question %s — %s' % (q, b['t']), 'tb': 'স্টাডি প্রশ্ন %s — %s' % (bnum(q), b['tb']), 'sl': [], 'h': h})
            mdout.append('## Study question %s — %s\n**%s**\n\n%s\n\n%s\n' % (q, b['t'], b['tb'], plain(md(en)), plain(md(bn))))
        elif k == 'slide':
            sl = [int(x) for x in re.split(r'[,\s]+', b['arg']) if x]
            for s in sl:
                if s in seen:
                    errors.append('slide %d appears twice' % s)
                seen[s] = True
            kv = dict(keyed(b['body']))
            for need in ('T', 'TB'):
                if not kv.get(need):
                    errors.append('slide %s missing %s' % (sl, need))
            for a, bb in (('E', 'EB'), ('K', 'KB')):
                if bool(kv.get(a)) != bool(kv.get(bb)):
                    errors.append('slide %s: %s without %s' % (sl, a, bb))
            if 'TXT' in kv:
                txt_en = md(kv['TXT'])
            else:
                paras = []
                for s in sl:
                    paras += ext['slides'][s - 1]['paras']
                txt_en = ''.join('<p>%s</p>' % html.escape(p) for p in paras) or '<p>(picture / title slide — no text)</p>'
            first, last = sl[0], sl[-1]
            lab = 'Slide %d' % first if first == last else 'Slides %d–%d' % (first, last)
            labbn = 'স্লাইড %s' % bnum(first) if first == last else 'স্লাইড %s–%s' % (bnum(first), bnum(last))
            bar = ('<p class="slidebar"><span>📑 %s of %d · %s / %s</span><a href="%s#page=%d" target="_blank" rel="noopener">Open original slide (PDF page %d) ↗</a></p>'
                   % (lab, total, labbn, bnum(total), pdf_url, first, first))
            imgs = ''.join('<img class="slideimg" loading="lazy" src="bibs/img/m%02d/s%02d.webp" alt="Slide %d of the original deck" width="960" height="540">' % (n, s, s) for s in sl)
            en = '<blockquote class="slidetext"><span class="sl">Slide text</span>%s</blockquote>' % txt_en
            if kv.get('IMG'):
                en += labelled('lab-N', 'Picture on the slide:', kv['IMG'])
            en += labelled('lab-T', 'Tutor explains:', kv['T'])
            if kv.get('E'):
                en += labelled('lab-E', 'Example:', kv['E'])
            if kv.get('K'):
                en += labelled('lab-K', 'Exam tip:', kv['K'])
            bn = ('<blockquote class="slidetext"><span class="sl">স্লাইডের লেখা (বাংলা অনুবাদ)</span>%s</blockquote>' % md(kv['BN'])) if kv.get('BN') else ''
            bn += labelled('lab-T', 'টিউটর বুঝিয়ে বলছেন:', kv['TB'])
            if kv.get('EB'):
                bn += labelled('lab-E', 'উদাহরণ:', kv['EB'])
            if kv.get('KB'):
                bn += labelled('lab-K', 'পরীক্ষার টিপস:', kv['KB'])
            h = bar + '<div class="slideimgs">' + imgs + '</div>' + pair(en, bn)
            steps.append({'id': 's%02d' % first, 'k': 'slide', 't': b['t'], 'tb': b['tb'], 'sl': sl, 'h': h})
            mdout.append('### %s · %s\n*%s*\n\n> %s\n\n%s\n\n%s\n\n%s\n\n%s\n' % (
                lab, b['t'], b['tb'], plain(txt_en).replace('\n', '\n> '), plain(md(kv.get('BN', ''))),
                plain(labelled('lab-T', 'Tutor explains:', kv['T'])) + ('\n\n' + plain(labelled('', 'Example:', kv['E'])) if kv.get('E') else '') + ('\n\n' + plain(labelled('', 'Exam tip:', kv['K'])) if kv.get('K') else ''),
                plain(labelled('lab-T', 'টিউটর বুঝিয়ে বলছেন:', kv['TB'])) + ('\n\n' + plain(labelled('', 'উদাহরণ:', kv['EB'])) if kv.get('EB') else '') + ('\n\n' + plain(labelled('', 'পরীক্ষার টিপস:', kv['KB'])) if kv.get('KB') else ''),
                ''))
        elif k in ('check', 'quiz'):
            items = mcq(b['body'], '%s %s' % (k, b['arg']))
            if k == 'check':
                checks[b['arg']] = len(items)
                sid = 'c' + b['arg'].replace('.', '-')
            else:
                sid = 'quiz'
                if len(items) < 10:
                    errors.append('module quiz has %d questions (need 10)' % len(items))
            steps.append({'id': sid, 'k': k, 't': b['t'], 'tb': b['tb'], 'sl': [], 'h': '', 'z': {'t': b['t'], 'tb': b['tb'], 'items': items}})
            mdout.append('## %s · %s\n' % (b['t'], b['tb']))
            for i, it in enumerate(items, 1):
                mdout.append('%d. %s  \n   %s  \n%s\n   **Answer:** %s — %s  \n   %s\n' % (
                    i, it['q'], it['qbn'], '\n'.join('   - %s %s' % ('ABCD'[j], o) for j, o in enumerate(it['opts'])),
                    'ABCD'[it['ans']], it['exp'], it['expbn']))
        else:
            errors.append('unknown block @' + k)
    missing = [s for s in range(1, total + 1) if s not in seen]
    if missing:
        errors.append('slides not covered: %s' % missing)
    for q in lessons:
        if checks.get(q, 0) < 2:
            errors.append('study question %s has no quick check (>=2 questions)' % q)
    if 'quiz' not in [s['id'] for s in steps]:
        errors.append('no module quiz')
    if errors:
        print('Module %d errors:\n  ' % n + '\n  '.join(errors))
        return None
    data = {'n': n, 't': t_en, 'tb': t_bn, 'u': head['units'], 'slides': total, 'pdf': pdf, 'steps': steps}
    os.makedirs(os.path.join(ROOT, 'bibs'), exist_ok=True)
    with open(os.path.join(ROOT, 'bibs', 'mod%02d.js' % n), 'w', encoding='utf-8') as f:
        f.write('BIBS_REG(%d,%s);\n' % (n, json.dumps(data, ensure_ascii=False, separators=(',', ':'))))
    with open(os.path.join(HERE, 'mod%02d.md' % n), 'w', encoding='utf-8') as f:
        f.write('\n'.join(mdout))
    nq = sum(len(s['z']['items']) for s in steps if s['k'] == 'quiz')
    nc = sum(checks.values())
    return {'n': n, 'slides': total, 'steps': len(steps), 'lessons': lessons, 'checks': nc, 'quiz': nq}


def main():
    ext = json.load(open(EXT, encoding='utf-8'))
    only = [int(a) for a in sys.argv[1:]]
    stats, ok = {}, True
    for n, t, tb, u in MODS:
        if os.path.exists(os.path.join(SRC, 'mod%02d.txt' % n)) and (not only or n in only):
            r = build(n)
            if r is None:
                ok = False
            else:
                stats[n] = r
    ready = {n for n, t, tb, u in MODS if os.path.exists(os.path.join(ROOT, 'bibs', 'mod%02d.js' % n))}
    lst = [{'n': n, 't': t, 'tb': tb, 'u': u, 'slides': ext[str(n)]['n'], 'pdf': ext[str(n)]['file'], 'ready': n in ready} for n, t, tb, u in MODS]
    with open(os.path.join(ROOT, 'bibs', 'index.js'), 'w', encoding='utf-8') as f:
        f.write('var BIBS_MODS=%s;\n' % json.dumps(lst, ensure_ascii=False, separators=(',', ':')))
    cov = os.path.join(HERE, 'COVERAGE.md')
    old = {}
    if os.path.exists(cov):
        for ln in open(cov, encoding='utf-8'):
            m = re.match(r'\| (\d) \| .*', ln)
            if m:
                old[int(m.group(1))] = ln.rstrip('\n')
    rows = []
    for n, t, tb, u in MODS:
        if n in stats:
            s = stats[n]
            rows.append('| %d | %s | %s | %d / %d ✅ | %s | %d | %d |' % (n, t, u, s['slides'], s['slides'], ', '.join(s['lessons']), s['checks'], s['quiz']))
        elif n in old:
            rows.append(old[n])
        else:
            rows.append('| %d | %s | %s | 0 / %d | — | 0 | 0 |' % (n, t, u, ext[str(n)]['n']))
    with open(cov, 'w', encoding='utf-8') as f:
        f.write('# BIBS 101 — coverage report\n\nGenerated by `content/bibs101/build.py`. A module is only written when every slide 1…N has its own step '
                '(with Bangla and an explanation), every study question has a quick check, and the module quiz has at least 10 questions.\n\n'
                '| Module | Topic | Units | Slides covered | Study questions | Quick-check Qs | Module quiz Qs |\n|---|---|---|---|---|---|---|\n'
                + '\n'.join(rows) + '\n')
    for n, s in stats.items():
        print('Module %d OK: %d slides, %d steps, checks %d, quiz %d' % (n, s['slides'], s['steps'], s['checks'], s['quiz']))
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
