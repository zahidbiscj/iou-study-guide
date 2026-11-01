#!/usr/bin/env python3
"""Build the FPEC 101 midterm course (Lectures 1-15).

Inputs
  content/fpec101/source/modNN.txt   raw slide text extracted from the PPTX files
  content/fpec101/build/modNN.py     tutor content for module NN (written by hand)
  content/fpec101/build/figs.py      diagram library (SVG)
Outputs
  fpec/index.js                      list of modules (FPEC_MODS)
  fpec/modNN.js                      one lazily-loaded file per module (FPEC_REG)
  content/fpec101/modNN.md           printable study note per module
  content/fpec101/fig/*.svg          diagrams as standalone files (used by the .md notes)
  content/fpec101/COVERAGE.md        proof that every slide is covered

The build FAILS if a built module misses or repeats a slide, if any step has no
Bangla, or if a module quiz does not have exactly 5 questions.

Run:  python3 content/fpec101/build/build.py
"""
import json, os, re, sys, html

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
SRC = os.path.join(ROOT, 'content', 'fpec101', 'source')
OUT_JS = os.path.join(ROOT, 'fpec')
OUT_MD = os.path.join(ROOT, 'content', 'fpec101')
OUT_FIG = os.path.join(OUT_MD, 'fig')
PDF_URL = 'slides/Principles%20of%20Economics%20(FPEC%20101)/pdf/FPEC(mod{p}).pdf'

sys.path.insert(0, HERE)
import figs  # noqa: E402

TITLES = [
    (1, 'Nature of Economics, Scarcity & the PPC', 'অর্থনীতির প্রকৃতি, দুষ্প্রাপ্যতা ও উৎপাদন সম্ভাবনা রেখা'),
    (2, 'Economic Systems & the Circular Flow', 'অর্থনৈতিক ব্যবস্থা ও আয়ের বৃত্তাকার প্রবাহ'),
    (3, 'Demand, Supply & Market Equilibrium', 'চাহিদা, যোগান ও বাজার ভারসাম্য'),
    (4, 'Government Intervention & Price Elasticity of Demand', 'সরকারি হস্তক্ষেপ ও চাহিদার দাম স্থিতিস্থাপকতা'),
    (5, 'PED & Total Revenue, Elasticity of Supply, Income & Cross Elasticity', 'PED ও মোট আয়, যোগানের স্থিতিস্থাপকতা, আয় ও আড়াআড়ি স্থিতিস্থাপকতা'),
    (6, 'Economic Costs & Short-Run Production', 'অর্থনৈতিক ব্যয় ও স্বল্পমেয়াদি উৎপাদন'),
    (7, 'Short-Run & Long-Run Costs, Economies of Scale', 'স্বল্প ও দীর্ঘমেয়াদি ব্যয়, বৃহদায়তন উৎপাদনের সুবিধা'),
    (8, 'Pure (Perfect) Competition', 'পূর্ণ প্রতিযোগিতা'),
    (9, 'Pure Monopoly', 'বিশুদ্ধ একচেটিয়া কারবার'),
    (10, 'Monopoly (cont.) & Monopolistic Competition', 'একচেটিয়া (চলমান) ও একচেটিয়া প্রতিযোগিতা'),
    (11, 'Oligopoly', 'অলিগোপলি (স্বল্প বিক্রেতার বাজার)'),
    (12, 'Competition Policy & Regulation', 'প্রতিযোগিতা নীতি ও নিয়ন্ত্রণ'),
    (13, 'Wage Determination', 'মজুরি নির্ধারণ'),
    (14, 'Income Inequality, Poverty & Discrimination', 'আয় বৈষম্য, দারিদ্র্য ও বৈষম্যমূলক আচরণ'),
    (15, 'Government & Market Failure', 'সরকার ও বাজার ব্যর্থতা'),
]

BND = '০১২৩৪৫৬৭৮৯'
def bnum(n): return ''.join(BND[int(c)] if c.isdigit() else c for c in str(n))

# ---------------------------------------------------------------- source slides
def read_source(n):
    path = os.path.join(SRC, 'mod%02d.txt' % n)
    slides, cur = {}, None
    for line in open(path, encoding='utf-8').read().split('\n'):
        m = re.match(r'^=== Slide (\d+)', line)
        if m:
            cur = int(m.group(1)); slides[cur] = {'lines': [], 'notes': '', 'meta': ''}; continue
        if cur is None: continue
        if line.startswith('[pics='): slides[cur]['meta'] = line; continue
        if line.startswith('[NOTES] '): slides[cur]['notes'] = line[8:]; continue
        if not line.strip(): continue
        lvl = (len(line) - len(line.lstrip(' '))) // 2
        t = line.strip()
        if t.startswith('- '): t = t[2:]
        t = re.sub(r'\s{2,}|\t+', ' ', t).strip()
        if t: slides[cur]['lines'].append((lvl, t))
    return slides

# ---------------------------------------------------------------- tiny markdown
def esc_lt(s):
    # allow real tags, escape comparison signs such as "PED < 1" or "<=".
    return re.sub(r'<(?=[\s\d=$])', '&lt;', s)

def inline(s):
    s = esc_lt(s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'(?<![\w*])_(.+?)_(?![\w*])', r'<i>\1</i>', s)
    return s

def md(text, first_label=None):
    """Very small markdown: blank-line paragraphs, '- ' lists, '1. ' lists, '### ' headings, raw HTML blocks."""
    out = []
    blocks = [b for b in re.split(r'\n\s*\n', text.strip('\n')) if b.strip()]
    for i, b in enumerate(blocks):
        lines = [l.rstrip() for l in b.strip('\n').split('\n')]
        st = lines[0].lstrip()
        if st.startswith('<'):
            out.append('\n'.join(lines)); continue
        if st.startswith('### '):
            out.append('<h3>%s</h3>' % inline(st[4:]))
            if len(lines) > 1: out.append(md('\n'.join(lines[1:])))
            continue
        if all(l.lstrip().startswith('- ') for l in lines):
            out.append('<ul>' + ''.join('<li>%s</li>' % inline(l.lstrip()[2:]) for l in lines) + '</ul>'); continue
        if all(re.match(r'^\s*\d+\. ', l) for l in lines):
            out.append('<ol>' + ''.join('<li>%s</li>' % inline(re.sub(r'^\s*\d+\. ', '', l)) for l in lines) + '</ol>'); continue
        out.append('<p>%s</p>' % inline(' '.join(l.strip() for l in lines)))
    return '\n'.join(out)

def labelled(cls, label, text):
    """First paragraph gets the label; the rest continue."""
    h = md(text)
    if h.startswith('<p>'):
        return '<p class="lab %s"><b>%s</b> %s' % (cls, label, h[3:])
    return '<p class="lab %s"><b>%s</b></p>\n%s' % (cls, label, h)

# ---------------------------------------------------------------- module DSL
class Module:
    def __init__(self, n):
        self.n = n; self.meta = {}; self.steps = []; self.src = read_source(n)
        self.nslides = len(self.src); self.figs_used = []; self.qs = []

    # ---- helpers exposed to module files
    def MOD(self, qs=(), t=None, tb=None):
        self.qs = list(qs)
        if t: self.meta['t'] = t
        if tb: self.meta['tb'] = tb

    def _pair(self, en, bn):
        return ('<div class="pair">\n<div class="en"><span class="tag">English</span>\n%s</div>\n'
                '<div class="bn-box"><span class="tag">বাংলা</span>\n%s</div></div>') % (en, bn)

    def _fig(self, key):
        if not key: return ''
        keys = key if isinstance(key, (list, tuple)) else [key]
        out = []
        for k in keys:
            svg, cap, capb = figs.get(k)
            self.figs_used.append(k)
            out.append('<figure class="fig">%s<figcaption>%s<span class="mq-bn"><br>%s</span></figcaption></figure>' % (svg, inline(cap), inline(capb)))
        return '\n'.join(out)

    def CONCEPT(self, en, bn, fig=None):
        self.steps.append(dict(id='concept', k='concept', t='Big picture — what is this lecture about?', tb='বড় ছবি — এই লেকচারে কী শিখব?', sl=[],
                               h=self._fig(fig) + self._pair(md(en), md(bn)), md=(en, bn), fig=fig))

    def WORDS(self, rows, intro='Learn these words first — the slides use them again and again.', introb='আগে এই শব্দগুলো শিখে নাও — স্লাইডে বারবার আসবে।'):
        def table(lang):
            if lang == 'en':
                head = '<tr><th>Term</th><th>Meaning</th><th>Tiny example</th></tr>'
                body = ''.join('<tr><td><b>%s</b></td><td>%s</td><td>%s</td></tr>' % (inline(r[0]), inline(r[1]), inline(r[3])) for r in rows)
            else:
                head = '<tr><th>শব্দ</th><th>বাংলা অর্থ</th><th>ছোট উদাহরণ</th></tr>'
                body = ''.join('<tr><td><b>%s</b></td><td>%s</td><td>%s</td></tr>' % (inline(r[0]), inline(r[2]), inline(r[4] if len(r) > 4 else r[3])) for r in rows)
            return '<div class="tbl"><table><thead>%s</thead><tbody>%s</tbody></table></div>' % (head, body)
        self.steps.append(dict(id='words', k='words', t='Key words of this lecture', tb='এই লেকচারের মূল শব্দ', sl=[],
                               h=self._pair('<p>%s</p>%s' % (intro, table('en')), '<p>%s</p>%s' % (introb, table('bn'))), rows=rows))

    def SLIDE(self, sl, t, tb, bn, ex, exb, eg=None, egb=None, tip=None, tipb=None, fig=None, txt=None, note=None, noteb=None, warn=None, warnb=None):
        if isinstance(sl, int): sl = [sl]
        for s in sl:
            if s not in self.src: raise SystemExit('Module %d: slide %d does not exist' % (self.n, s))
        if not bn or not exb: raise SystemExit('Module %d slides %s: Bangla missing' % (self.n, sl))
        # slide text (English): from the source unless overridden
        en_txt = []
        for s in sl:
            lines = txt.get(s) if isinstance(txt, dict) and s in txt else None
            if lines is None and isinstance(txt, list) and len(sl) == 1: lines = txt
            if lines is None:
                lines = [('&nbsp;' * 4 * lvl) + ('• ' if lvl else '') + html.escape(t_) for lvl, t_ in self.src[s]['lines']]
            if not lines: lines = ['(no text on this slide)']
            en_txt.append((s, lines, self.src[s]['notes']))
        bn_lines = bn if isinstance(bn, list) else [bn]

        def quote(lang):
            if lang == 'en':
                parts = []
                for s, lines, notes in en_txt:
                    head = ('<p><b>Slide %d</b></p>' % s) if len(sl) > 1 else ''
                    parts.append(head + ''.join('<p>%s</p>' % l for l in lines) + (('<p><b>Speaker note:</b> %s</p>' % html.escape(notes)) if notes else ''))
                return '<blockquote class="slidetext"><span class="sl">Slide text</span>%s</blockquote>' % ''.join(parts)
            return '<blockquote class="slidetext"><span class="sl">স্লাইডের লেখা (বাংলা অনুবাদ)</span>%s</blockquote>' % ''.join('<p>%s</p>' % inline(l) for l in bn_lines)

        en = quote('en') + labelled('lab-T', 'Tutor explains:', ex)
        bnh = quote('bn') + labelled('lab-T', 'টিউটর বুঝিয়ে বলছেন:', exb)
        if eg: en += labelled('lab-E', 'Real-life example:', eg)
        if egb: bnh += labelled('lab-E', 'বাস্তব উদাহরণ:', egb)
        if note: en += labelled('lab-N', "Tutor's note (not on the slide):", note)
        if noteb: bnh += labelled('lab-N', 'টিউটরের নোট (স্লাইডে নেই):', noteb)
        if warn: en += labelled('lab-W', 'Common mistake:', warn)
        if warnb: bnh += labelled('lab-W', 'সাধারণ ভুল:', warnb)
        if tip: en += labelled('lab-K', 'Exam tip:', tip)
        if tipb: bnh += labelled('lab-K', 'পরীক্ষার টিপস:', tipb)
        a, b = sl[0], sl[-1]
        rng = ('Slide %d of %d · স্লাইড %s / %s' % (a, self.nslides, bnum(a), bnum(self.nslides))) if a == b else \
              ('Slides %d–%d of %d · স্লাইড %s–%s / %s' % (a, b, self.nslides, bnum(a), bnum(b), bnum(self.nslides)))
        bar = '<p class="slidebar"><span>📑 %s</span><a href="%s#page=%d" target="_blank" rel="noopener">Open original slide (page %d) ↗</a></p>' % (
            rng, PDF_URL.format(p='%02d' % self.n), a, a)
        self.steps.append(dict(id='s%02d' % a, k='slide', t=t, tb=tb, sl=sl, h=bar + self._fig(fig) + self._pair(en, bnh),
                               md=dict(en_txt=en_txt, bn=bn_lines, ex=ex, exb=exb, eg=eg, egb=egb, tip=tip, tipb=tipb, note=note, noteb=noteb, warn=warn, warnb=warnb), fig=fig))

    def CHECK(self, items):
        prev = self.steps[-1]['id']
        self.steps.append(dict(id='c' + prev[1:], k='check', t='Quick check', tb='দ্রুত যাচাই', sl=[], h='', z=dict(t='Quick check', tb='দ্রুত যাচাই', items=items)))

    def TOGETHER(self, en, bn, fig=None):
        self.steps.append(dict(id='together', k='together', t='Put it together — tables, graphs and numbers', tb='সব একসাথে — ছক, গ্রাফ ও হিসাব', sl=[],
                               h=self._fig(fig) + self._pair(md(en), md(bn)), md=(en, bn), fig=fig))

    def MIDTERM(self, en, bn):
        self.steps.append(dict(id='midterm', k='midterm', t='Midterm connection — model answers', tb='মিডটার্ম সংযোগ — মডেল উত্তর', sl=[],
                               h=self._pair(md(en), md(bn)), md=(en, bn)))

    def QUIZ(self, items):
        if len(items) != 5: raise SystemExit('Module %d: quiz must have 5 questions, has %d' % (self.n, len(items)))
        self.steps.append(dict(id='quiz', k='quiz', t='Module quiz — 5 questions', tb='মডিউল কুইজ — ৫টি প্রশ্ন', sl=[], h='', z=dict(t='Module quiz', tb='মডিউল কুইজ', items=items)))

    def SUMMARY(self, en, bn):
        self.steps.append(dict(id='summary', k='summary', t='Lecture summary — revise in 3 minutes', tb='লেকচারের সারসংক্ষেপ — ৩ মিনিটে রিভিশন', sl=[],
                               h=self._pair(md(en), md(bn)), md=(en, bn)))

def Q(q, qbn, opts, ans, exp, expbn):
    for o in opts:
        if ' · ' not in o: raise SystemExit('Quiz option needs "English · বাংলা": %s' % o)
    return dict(q=q, qbn=qbn, opts=opts, ans=ans, exp=exp, expbn=expbn)

# ---------------------------------------------------------------- checks
def check(mod):
    seen = []
    for st in mod.steps:
        if st['k'] == 'slide': seen += st['sl']
    dup = sorted(set(s for s in seen if seen.count(s) > 1))
    missing = sorted(set(range(1, mod.nslides + 1)) - set(seen))
    errs = []
    if dup: errs.append('duplicated slides %s' % dup)
    if missing: errs.append('missing slides %s' % missing)
    kinds = [s['k'] for s in mod.steps]
    for k in ('concept', 'words', 'together', 'midterm', 'quiz', 'summary'):
        if k not in kinds: errs.append('missing part %s' % k)
    for st in mod.steps:
        if st.get('z'):
            for it in st['z']['items']:
                if not (it['qbn'] and it['expbn']): errs.append('quiz item without Bangla: %s' % it['q'])
                if not 0 <= it['ans'] < len(it['opts']): errs.append('bad answer index: %s' % it['q'])
        elif 'bn-box' not in st['h']: errs.append('step %s without Bangla' % st['id'])
    ids = [s['id'] for s in mod.steps]
    if len(ids) != len(set(ids)): errs.append('duplicate step ids')
    if errs: raise SystemExit('Module %d FAILED: %s' % (mod.n, '; '.join(errs)))
    return len(seen)

# ---------------------------------------------------------------- markdown note
def strip_tags(s):
    s = re.sub(r'<br\s*/?>', '\n', s)
    s = re.sub(r'</?(b|strong)>', '**', s)
    s = re.sub(r'</?i>', '_', s)
    s = re.sub(r'&nbsp;', ' ', s)
    return html.unescape(re.sub(r'<[^>]+>', '', s))

def fig_md(key):
    if not key: return ''
    keys = key if isinstance(key, (list, tuple)) else [key]
    out = ''
    for k in keys:
        _, cap, capb = figs.get(k)
        out += '\n![%s](fig/%s.svg)\n\n_%s_  \n_%s_\n' % (strip_tags(cap), k, strip_tags(cap), strip_tags(capb))
    return out

def write_md(mod, title, titleb):
    L = ['# FPEC 101 · Module %d — %s' % (mod.n, title), '## মডিউল %s — %s' % (bnum(mod.n), titleb), '',
         '_Lecture %d · %d slides · Midterm questions: %s_' % (mod.n, mod.nslides, ', '.join('Q%d' % q for q in mod.qs) or '—'), '',
         '> Printable study note generated from the website. Each slide: slide text → Bangla translation → tutor explanation → example → exam tip.', '']
    for st in mod.steps:
        if st['k'] in ('concept', 'together', 'midterm', 'summary'):
            en, bn = st['md']
            L += ['---', '', '## %s · %s' % (st['t'], st['tb']), fig_md(st.get('fig')), '### English', '', strip_tags(en).strip(), '', '### বাংলা', '', strip_tags(bn).strip(), '']
        elif st['k'] == 'words':
            L += ['---', '', '## Key words · মূল শব্দ', '', '| Term | Meaning | বাংলা অর্থ | Example |', '|---|---|---|---|']
            for r in st['rows']:
                L.append('| %s | %s | %s | %s |' % tuple(strip_tags(inline(x)).replace('|', '/') for x in (r[0], r[1], r[2], r[3])))
            L.append('')
        elif st['k'] == 'slide':
            d = st['md']; sl = st['sl']
            rng = 'Slide %d' % sl[0] if len(sl) == 1 else 'Slides %d–%d' % (sl[0], sl[-1])
            L += ['---', '', '## %s · %s' % (rng, st['t']), '### %s' % st['tb'], fig_md(st.get('fig'))]
            for s, lines, notes in d['en_txt']:
                if len(sl) > 1: L.append('> **Slide %d**' % s)
                L += ['> %s' % strip_tags(l).strip() for l in lines]
                if notes: L.append('> _Speaker note:_ %s' % notes)
                L.append('>')
            L += ['', '**বাংলা অনুবাদ:**', ''] + ['> %s' % strip_tags(inline(l)) for l in d['bn']] + ['']
            for key, lab in (('ex', 'Tutor explains'), ('exb', 'টিউটরের ব্যাখ্যা'), ('eg', 'Real-life example'), ('egb', 'বাস্তব উদাহরণ'),
                             ('note', "Tutor's note (not on the slide)"), ('noteb', 'টিউটরের নোট'), ('warn', 'Common mistake'), ('warnb', 'সাধারণ ভুল'),
                             ('tip', 'Exam tip'), ('tipb', 'পরীক্ষার টিপস')):
                if d.get(key): L += ['**%s:** %s' % (lab, strip_tags(md(d[key])).strip()), '']
        elif st['k'] in ('check', 'quiz'):
            L += ['---', '', '## %s · %s' % (st['t'], st['tb']), '']
            for i, it in enumerate(st['z']['items'], 1):
                L += ['%d. %s  ' % (i, it['q']), '   %s' % it['qbn'], '']
                for j, o in enumerate(it['opts']): L.append('   - %s) %s' % ('ABCDE'[j], o))
                L += ['', '   **Answer: %s** — %s  ' % ('ABCDE'[it['ans']], strip_tags(it['exp'])), '   %s' % strip_tags(it['expbn']), '']
    txt = '\n'.join(L)
    txt = re.sub(r'\n{3,}', '\n\n', txt)
    open(os.path.join(OUT_MD, 'mod%02d.md' % mod.n), 'w', encoding='utf-8').write(txt)

# ---------------------------------------------------------------- main
def main():
    os.makedirs(OUT_JS, exist_ok=True); os.makedirs(OUT_FIG, exist_ok=True)
    index, cov = [], []
    for n, t, tb in TITLES:
        src_n = len(read_source(n))
        path = os.path.join(HERE, 'mod%02d.py' % n)
        if not os.path.exists(path):
            index.append(dict(n=n, t=t, tb=tb, slides=src_n, ready=False))
            cov.append((n, t, False, 0, src_n, 0, '', ''))
            continue
        mod = Module(n)
        ns = {k: getattr(mod, k) for k in ('MOD', 'CONCEPT', 'WORDS', 'SLIDE', 'CHECK', 'TOGETHER', 'MIDTERM', 'QUIZ', 'SUMMARY')}
        ns['Q'] = Q
        exec(compile(open(path, encoding='utf-8').read(), path, 'exec'), ns)
        covered = check(mod)
        t = mod.meta.get('t', t); tb = mod.meta.get('tb', tb)
        steps = [{k: v for k, v in st.items() if k in ('id', 'k', 't', 'tb', 'sl', 'h', 'z')} for st in mod.steps]
        data = dict(n=n, t=t, tb=tb, slides=mod.nslides, pdf='FPEC(mod%02d).pdf' % n, steps=steps)
        js = 'FPEC_REG(%d,%s);\n' % (n, json.dumps(data, ensure_ascii=False, separators=(',', ':')))
        open(os.path.join(OUT_JS, 'mod%02d.js' % n), 'w', encoding='utf-8').write(js)
        write_md(mod, t, tb)
        nq = sum(len(s['z']['items']) for s in mod.steps if s['k'] == 'check')
        index.append(dict(n=n, t=t, tb=tb, slides=mod.nslides, ready=True))
        cov.append((n, t, True, covered, mod.nslides, len(mod.steps), '5 + %d quick' % nq, ', '.join('Q%d' % q for q in mod.qs)))
        print('module %2d ok: %d/%d slides, %d steps, %d KB' % (n, covered, mod.nslides, len(mod.steps), len(js.encode()) // 1024))
    for k in figs.keys():
        open(os.path.join(OUT_FIG, k + '.svg'), 'w', encoding='utf-8').write(figs.standalone(k))
    open(os.path.join(OUT_JS, 'index.js'), 'w', encoding='utf-8').write('var FPEC_MODS=%s;\n' % json.dumps(index, ensure_ascii=False, separators=(',', ':')))
    L = ['# FPEC 101 — Midterm coverage report', '',
         'Generated by `content/fpec101/build/build.py`. The build **fails** if a built module misses or repeats a slide, if any step has no Bangla, or if a module quiz does not have exactly 5 questions.', '',
         '| Module | Topic | Status | Slides covered | Steps | Quiz (module + inline) | Midterm questions |', '|---|---|---|---|---|---|---|']
    for n, t, ok, c, tot, st, qz, qs in cov:
        L.append('| %d | %s | %s | %d / %d | %s | %s | %s |' % (n, t, '✅ built' if ok else '⏳ pending', c, tot, st or '–', qz or '–', qs or '–'))
    tot_c = sum(c[3] for c in cov); tot_s = sum(c[4] for c in cov)
    L += ['', '**Total: %d / %d slides covered.**' % (tot_c, tot_s), '',
          'Raw slide text: `content/fpec101/source/` · Lecture slides: `slides/Principles of Economics (FPEC 101)/` (PPTX originals, PDF copies in `pdf/`).', '']
    open(os.path.join(OUT_MD, 'COVERAGE.md'), 'w', encoding='utf-8').write('\n'.join(L))
    print('total %d/%d slides' % (tot_c, tot_s))

if __name__ == '__main__':
    main()
