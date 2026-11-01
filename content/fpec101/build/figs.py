"""SVG diagram library for the FPEC 101 course.

Plot coordinates are 0..100 on both axes (origin bottom-left), mapped to the
plot area of a 380 x 270 viewBox. Colours come from CSS classes so diagrams
follow light/dark mode on the site (.ax .gd .l1 .l2 .l3 .l4 .pt .t1 .t2 .t3 .t4 .fl .fl2).
"""
import math, re

X0, X1, Y0, Y1 = 55, 350, 222, 22
FIGS = {}

def px(x): return X0 + (X1 - X0) * x / 100.0
def py(y): return Y0 - (Y0 - Y1) * y / 100.0
def f(v): return ('%.1f' % v).rstrip('0').rstrip('.')

def smooth(pts):
    """Catmull-Rom spline through the points -> SVG path."""
    P = [(px(x), py(y)) for x, y in pts]
    if len(P) == 2:
        return 'M%s %s L%s %s' % (f(P[0][0]), f(P[0][1]), f(P[1][0]), f(P[1][1]))
    d = 'M%s %s' % (f(P[0][0]), f(P[0][1]))
    for i in range(len(P) - 1):
        p0 = P[i - 1] if i else P[i]; p1 = P[i]; p2 = P[i + 1]; p3 = P[i + 2] if i + 2 < len(P) else P[i + 1]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += ' C%s %s %s %s %s %s' % (f(c1[0]), f(c1[1]), f(c2[0]), f(c2[1]), f(p2[0]), f(p2[1]))
    return d

def arrow(x1, y1, x2, y2, cls='l3'):
    a = math.atan2(y2 - y1, x2 - x1); L = 8
    h1 = (x2 - L * math.cos(a - .45), y2 - L * math.sin(a - .45)); h2 = (x2 - L * math.cos(a + .45), y2 - L * math.sin(a + .45))
    return ('<line class="%s" x1="%s" y1="%s" x2="%s" y2="%s"/><path class="%s" d="M%s %s L%s %s L%s %s" fill="none"/>'
            % (cls, f(x1), f(y1), f(x2), f(y2), cls, f(h1[0]), f(h1[1]), f(x2), f(y2), f(h2[0]), f(h2[1])))

def plot(key, xl, yl, items, cap, capb, label=None, ticks=None):
    o = ['<svg viewBox="0 0 380 270" role="img" aria-label="%s">' % (label or cap.replace('"', "'"))]
    o.append('<line class="ax" x1="%d" y1="%d" x2="%d" y2="%d"/><line class="ax" x1="%d" y1="%d" x2="%d" y2="%d"/>' % (X0, Y0, X1 + 8, Y0, X0, Y0, X0, Y1 - 8))
    o.append('<text x="%d" y="258" text-anchor="middle">%s</text>' % ((X0 + X1) // 2, xl))
    o.append('<text x="16" y="%d" transform="rotate(-90 16 %d)" text-anchor="middle">%s</text>' % ((Y0 + Y1) // 2, (Y0 + Y1) // 2, yl))
    o += render(items)
    o.append('</svg>')
    FIGS[key] = (''.join(o), cap, capb)

def render(items):
    o = []
    for it in items:
        k = it[0]
        if k == 'ln':
            _, x1, y1, x2, y2, cls = it[:6]; dash = ' stroke-dasharray="6 4"' if len(it) > 6 and it[6] else ''
            o.append('<line class="%s" x1="%s" y1="%s" x2="%s" y2="%s"%s/>' % (cls, f(px(x1)), f(py(y1)), f(px(x2)), f(py(y2)), dash))
        elif k == 'cu':
            _, pts, cls = it[:3]; dash = ' stroke-dasharray="6 4"' if len(it) > 3 and it[3] else ''
            o.append('<path class="%s" d="%s"%s/>' % (cls, smooth(pts), dash))
        elif k == 'poly':  # straight segments (for kinked curves)
            _, pts, cls = it[:3]
            o.append('<polyline class="%s" points="%s" fill="none"/>' % (cls, ' '.join('%s,%s' % (f(px(x)), f(py(y))) for x, y in pts)))
        elif k == 'area':
            _, pts, cls = it
            o.append('<polygon class="%s" points="%s"/>' % (cls, ' '.join('%s,%s' % (f(px(x)), f(py(y))) for x, y in pts)))
        elif k == 'pt':
            o.append('<circle class="pt" cx="%s" cy="%s" r="4.5"/>' % (f(px(it[1])), f(py(it[2]))))
        elif k == 'gd':  # dashed guides from a point to both axes
            _, x, y = it[:3]
            o.append('<line class="gd" x1="%s" y1="%s" x2="%s" y2="%s"/><line class="gd" x1="%s" y1="%s" x2="%s" y2="%s"/>' % (
                f(px(x)), f(py(y)), f(px(x)), f(Y0), f(px(x)), f(py(y)), f(X0), f(py(y))))
        elif k == 'gx':  # vertical guide only
            o.append('<line class="gd" x1="%s" y1="%s" x2="%s" y2="%s"/>' % (f(px(it[1])), f(py(it[2])), f(px(it[1])), f(Y0)))
        elif k == 'gy':  # horizontal guide only
            o.append('<line class="gd" x1="%s" y1="%s" x2="%s" y2="%s"/>' % (f(X0), f(py(it[2])), f(px(it[1])), f(py(it[2]))))
        elif k == 'tx':
            _, x, y, s = it[:4]; cls = it[4] if len(it) > 4 else ''; anc = it[5] if len(it) > 5 else 'start'
            o.append('<text x="%s" y="%s"%s text-anchor="%s">%s</text>' % (f(px(x)), f(py(y)), (' class="%s"' % cls) if cls else '', anc, s))
        elif k == 'xt':  # tick label on x axis
            o.append('<text x="%s" y="%s" text-anchor="middle" class="tk">%s</text>' % (f(px(it[1])), f(Y0 + 16), it[2]))
        elif k == 'yt':  # tick label on y axis
            o.append('<text x="%s" y="%s" text-anchor="end" class="tk">%s</text>' % (f(X0 - 5), f(py(it[1]) + 4), it[2]))
        elif k == 'ar':
            _, x1, y1, x2, y2 = it[:5]; cls = it[5] if len(it) > 5 else 'l3'
            o.append(arrow(px(x1), py(y1), px(x2), py(y2), cls))
        else:
            raise ValueError(k)
    return o

def plot2(key, panels, cap, capb, h=270):
    """Side-by-side panels: each (title, xlabel, ylabel, items)."""
    global X0, X1, Y0, Y1
    save = (X0, X1, Y0, Y1)
    o = ['<svg viewBox="0 0 380 %d" role="img" aria-label="%s">' % (h, cap.replace('"', "'"))]
    w = 380 / len(panels)
    for i, (title, xl, yl, items) in enumerate(panels):
        X0, X1, Y0, Y1 = int(i * w + 42), int((i + 1) * w - 12), h - 48, 34
        o.append('<text x="%d" y="16" text-anchor="middle" font-weight="700">%s</text>' % ((X0 + X1) // 2, title))
        o.append('<line class="ax" x1="%d" y1="%d" x2="%d" y2="%d"/><line class="ax" x1="%d" y1="%d" x2="%d" y2="%d"/>' % (X0, Y0, X1 + 6, Y0, X0, Y0, X0, Y1 - 6))
        o.append('<text x="%d" y="%d" text-anchor="middle" class="sm">%s</text>' % ((X0 + X1) // 2, h - 10, xl))
        o.append('<text x="%d" y="%d" transform="rotate(-90 %d %d)" text-anchor="middle" class="sm">%s</text>' % (X0 - 32, (Y0 + Y1) // 2, X0 - 32, (Y0 + Y1) // 2, yl))
        o += render(items)
    X0, X1, Y0, Y1 = save
    o.append('</svg>')
    FIGS[key] = (''.join(o), cap, capb)

def raw(key, svg, cap, capb):
    FIGS[key] = (svg, cap, capb)

def get(key):
    if key not in FIGS: raise SystemExit('unknown figure %s' % key)
    return FIGS[key]

def keys(): return sorted(FIGS)

STYLE = ('<style>svg{font:12px sans-serif;fill:#1d2622;background:#fff}.ax{stroke:#5c6a63;stroke-width:1.5;fill:none}'
         '.gd{stroke:#5c6a63;stroke-width:1;stroke-dasharray:3 3}.l1{stroke:#1f7a5c;stroke-width:2.5;fill:none}'
         '.l2{stroke:#c4862a;stroke-width:2.5;fill:none}.l3{stroke:#a63d3d;stroke-width:2;fill:none}.l4{stroke:#2f5c9a;stroke-width:2.5;fill:none}'
         '.pt{fill:#a63d3d}.t1{fill:#1f7a5c;font-weight:700}.t2{fill:#8a5512;font-weight:700}.t3{fill:#a63d3d;font-weight:700}.t4{fill:#2f5c9a;font-weight:700}'
         '.fl{fill:#1f7a5c;fill-opacity:.15;stroke:none}.fl2{fill:#c4862a;fill-opacity:.2;stroke:none}.fl3{fill:#a63d3d;fill-opacity:.15;stroke:none}'
         '.bx{fill:#e7f2ec;stroke:#1f7a5c;stroke-width:1.5}.bx2{fill:#fbf1e1;stroke:#c4862a;stroke-width:1.5}.tk{font-size:10.5px;fill:#5c6a63}.sm{font-size:10.5px}</style>')

def standalone(key):
    svg = FIGS[key][0]
    svg = svg.replace('<svg ', '<svg xmlns="http://www.w3.org/2000/svg" width="570" height="405" ', 1)
    return svg.replace('>', '>' + STYLE, 1)

# =====================================================================
# Lecture 1 — scarcity and the PPC
# =====================================================================
PPC = [(0, 80), (30, 74), (55, 60), (72, 42), (82, 22), (86, 0)]
plot('ppc', 'Capital goods', 'Consumer goods', [
    ('cu', PPC, 'l1'), ('pt', 55, 60), ('tx', 57, 63, 'Optimum (on the curve)', 't1'),
    ('pt', 30, 35), ('tx', 14, 28, 'Attainable but inefficient', 't2'),
    ('pt', 82, 74), ('tx', 62, 82, 'Unattainable', 't3'),
    ('tx', 88, 4, 'PPC', 't1')],
    'Points ON the PPC = optimum (full use of resources). Points INSIDE = attainable but wasteful (unemployment). Points OUTSIDE = unattainable with today\'s resources.',
    'PPC-র **ওপরে** বিন্দু = সর্বোত্তম (সব সম্পদ কাজে লাগছে)। **ভেতরে** বিন্দু = সম্ভব কিন্তু অপচয় (বেকারত্ব)। **বাইরে** বিন্দু = আজকের সম্পদে অসম্ভব।')

plot('ppc_cost', 'Capital goods', 'Consumer goods', [
    ('cu', [(0, 90), (20, 86), (40, 76), (60, 58), (75, 34), (85, 0)], 'l1'),
    ('gd', 20, 86), ('gd', 40, 76), ('gd', 60, 58), ('gd', 75, 34),
    ('ar', 22, 92, 22, 87, 'l3'), ('tx', 24, 93, 'give up 4', 't3'),
    ('ar', 62, 70, 62, 59, 'l3'), ('tx', 64, 69, 'give up 18', 't3'),
    ('xt', 20, '+20'), ('xt', 40, '+20'), ('xt', 60, '+20'), ('xt', 75, '+15')],
    'Bowed-out (concave) PPC: every extra 20 units of capital goods costs MORE consumer goods than the last — increasing opportunity cost.',
    'বাইরের দিকে বাঁকা PPC: প্রতিবার ২০ একক মূলধনী দ্রব্য বাড়াতে আগের চেয়ে **বেশি** ভোগ্যপণ্য ছাড়তে হয় — ক্রমবর্ধমান সুযোগ ব্যয়।')

plot('ppc_shift', 'Capital goods', 'Consumer goods', [
    ('cu', [(0, 62), (25, 57), (45, 45), (58, 28), (64, 0)], 'l1'),
    ('cu', [(0, 84), (32, 78), (60, 62), (78, 38), (86, 0)], 'l2'),
    ('ar', 40, 50, 52, 64, 'l3'), ('tx', 66, 4, 'PPC1', 't1'), ('tx', 88, 4, 'PPC2', 't2'),
    ('tx', 30, 92, 'More resources or better technology', 't3')],
    'Economic growth: more or better resources (or new technology) shift the PPC outward. Losing resources (war, disaster) shifts it inward.',
    'অর্থনৈতিক প্রবৃদ্ধি: সম্পদ বাড়লে বা প্রযুক্তি উন্নত হলে PPC বাইরের দিকে সরে। সম্পদ হারালে (যুদ্ধ, দুর্যোগ) ভেতরের দিকে সরে।')

plot('ppc_growth', 'Capital goods', 'Consumer goods', [
    ('cu', [(0, 60), (25, 55), (45, 43), (58, 26), (63, 0)], 'l1'),
    ('cu', [(0, 68), (28, 62), (50, 49), (65, 29), (71, 0)], 'l2', True),
    ('cu', [(0, 82), (34, 76), (62, 60), (80, 36), (88, 0)], 'l4'),
    ('tx', 30, 97, 'B: capital goods focus → big shift', 't4'), ('tx', 3, 36, 'A: consumer focus', 't2'), ('tx', 3, 28, '→ small shift (dashed)', 't2'),
    ('tx', 40, 6, 'today', 't1')],
    'Today\'s choice decides tomorrow\'s PPC: a nation that invests in capital goods (machines, roads) grows faster than one that consumes everything now.',
    'আজকের পছন্দ আগামীর PPC ঠিক করে: যে দেশ মূলধনী দ্রব্যে (যন্ত্র, রাস্তা) বিনিয়োগ করে, সে সব এখনই ভোগ করা দেশের চেয়ে দ্রুত বাড়ে।')

# =====================================================================
# Lecture 2 — circular flow
# =====================================================================
def box(x, y, w, h, t, cls='bx', sub=''):
    s = '<rect class="%s" x="%d" y="%d" width="%d" height="%d" rx="8"/><text x="%d" y="%d" text-anchor="middle" font-weight="700">%s</text>' % (
        cls, x, y, w, h, x + w // 2, y + h // 2 + (0 if sub else 4), t)
    if sub: s += '<text x="%d" y="%d" text-anchor="middle" class="sm">%s</text>' % (x + w // 2, y + h // 2 + 14, sub)
    return s

def arr(x1, y1, x2, y2, cls): return arrow(x1, y1, x2, y2, cls)

def harrow(y, x1, x2, cls, dash=False):
    d = ' stroke-dasharray="6 4"' if dash else ''
    return '<line class="%s" x1="%d" y1="%d" x2="%d" y2="%d"%s/>' % (cls, x1, y, x2, y, d) + arrow(x2 - (8 if x2 > x1 else -8), y, x2, y, cls)

raw('circ',
    '<svg viewBox="0 0 380 270" role="img" aria-label="Simple circular flow of income">'
    + box(8, 20, 84, 222, 'FIRMS', sub='(businesses)') + box(288, 20, 84, 222, 'HOUSE-', sub='HOLDS', cls='bx2')
    + '<text x="190" y="44" text-anchor="middle" class="t2 sm">(a) productive resources →firms</text>' + harrow(54, 286, 94, 'l2', True)
    + '<text x="190" y="88" text-anchor="middle" class="t1 sm">(b) factor income: wages, rent,</text><text x="190" y="100" text-anchor="middle" class="t1 sm">interest, profit → households</text>' + harrow(110, 94, 286, 'l1')
    + '<text x="190" y="160" text-anchor="middle" class="t4 sm">(c) spending on goods &amp; services → firms</text>' + harrow(170, 286, 94, 'l4')
    + '<text x="190" y="204" text-anchor="middle" class="t3 sm">(d) goods &amp; services (output) → households</text>' + harrow(214, 94, 286, 'l3', True)
    + '<text x="190" y="262" text-anchor="middle" class="sm">solid = money flow · dashed = real flow</text></svg>',
    'The slide 16 picture: money flows (solid) go one way, real flows (dashed: resources and goods) go the opposite way.',
    'স্লাইড ১৬-এর ছবি: টাকার প্রবাহ (সলিড) এক দিকে, আসল প্রবাহ (ড্যাশ: সম্পদ ও পণ্য) উল্টো দিকে ঘোরে।')

raw('circ2',
    '<svg viewBox="0 0 460 300" role="img" aria-label="Circular flow with resource market and product market"><g transform="translate(40 0)">'
    + box(140, 8, 100, 44, 'RESOURCE', sub='MARKET') + box(140, 248, 100, 44, 'PRODUCT', sub='MARKET')
    + box(4, 128, 96, 44, 'BUSINESSES') + box(280, 128, 96, 44, 'HOUSEHOLDS', cls='bx2')
    + '<path class="l1" d="M140 22 Q60 30 50 128"/>' + arr(53, 118, 50, 128, 'l1')
    + '<path class="l2" d="M58 128 Q72 56 140 40"/>' + arr(130, 42, 140, 40, 'l2')
    + '<path class="l2" d="M330 128 Q320 30 240 22"/>' + arr(250, 23, 240, 22, 'l2')
    + '<path class="l1" d="M240 40 Q306 56 322 128"/>' + arr(320, 118, 322, 128, 'l1')
    + '<path class="l2" d="M50 172 Q60 270 140 278"/>' + arr(130, 278, 140, 278, 'l2')
    + '<path class="l1" d="M140 260 Q72 246 58 172"/>' + arr(60, 182, 58, 172, 'l1')
    + '<path class="l1" d="M322 172 Q306 246 240 260"/>' + arr(250, 258, 240, 260, 'l1')
    + '<text x="56" y="56" class="t1 sm" text-anchor="end">costs</text><text x="98" y="92" class="t2 sm">resources</text>'
    + '<text x="324" y="56" class="t2 sm">land, labour,</text><text x="324" y="68" class="t2 sm">capital, entrep.</text><text x="282" y="96" class="t1 sm" text-anchor="end">money income</text>'
    + '<text x="56" y="248" class="t2 sm" text-anchor="end">goods &amp;</text><text x="56" y="260" class="t2 sm" text-anchor="end">services</text><text x="98" y="214" class="t1 sm">revenue</text>'
    + '<text x="330" y="248" class="t1 sm">consumption</text><text x="330" y="260" class="t1 sm">spending</text><text x="282" y="210" class="t2 sm" text-anchor="end">goods &amp; services</text>'
    + '<path class="l2" d="M240 278 Q320 270 330 172"/>' + arr(329, 182, 330, 172, 'l2')
    + '<text x="190" y="146" text-anchor="middle" class="sm">green = money</text><text x="190" y="160" text-anchor="middle" class="sm">gold = real things</text></g></svg>',
    'The slide 17 picture (McConnell & Brue, Fig 2.2): two markets. Households sell resources in the resource market and buy products in the product market; businesses do the opposite.',
    'স্লাইড ১৭-এর ছবি (ম্যাককনেল ও ব্রু, চিত্র ২.২): দুটি বাজার। পরিবার সম্পদ বাজারে সম্পদ বিক্রি করে ও পণ্য বাজারে পণ্য কেনে; ব্যবসা করে ঠিক উল্টোটা।')

# =====================================================================
# Lecture 3 — demand, supply, equilibrium, government intervention
# =====================================================================
D0 = ((10, 90), (90, 10)); S0 = ((10, 10), (90, 90))
def clip(x1, y1, x2, y2, lo=0.0, hi=98.0):
    """Clip a segment to the plot box (Liang-Barsky)."""
    dx, dy = x2 - x1, y2 - y1; t0, t1 = 0.0, 1.0
    for p_, q_ in ((-dx, x1 - lo), (dx, hi - x1), (-dy, y1 - lo), (dy, hi - y1)):
        if p_ == 0:
            if q_ < 0: return None
            continue
        r = q_ / p_
        if p_ < 0: t0 = max(t0, r)
        else: t1 = min(t1, r)
    if t0 > t1: return None
    return x1 + t0 * dx, y1 + t0 * dy, x1 + t1 * dx, y1 + t1 * dy

def ln(seg, cls, name, dx=0, dy=0, dash=False, lab_at=1):
    (x1, y1), (x2, y2) = seg
    x1, y1, x2, y2 = clip(x1 + dx, y1 + dy, x2 + dx, y2 + dy, 2, 94); dx = dy = 0
    it = [('ln', x1 + dx, y1 + dy, x2 + dx, y2 + dy, cls, dash)]
    lx, ly = (x2 + dx, y2 + dy) if lab_at else (x1 + dx, y1 + dy)
    it.append(('tx', lx + 1.5, ly + 1, name, 't' + cls[-1]))
    return it

# demand schedule for computers (slide 8/9): P 2000..1200, Q 1000..5000
pts = [(1000, 2000), (2000, 1800), (3000, 1600), (4000, 1400), (5000, 1200)]
def mq(q): return q / 60.0
def mp(p): return (p - 1000) / 12.0
items = [('cu', [(mq(q), mp(p)) for q, p in pts], 'l1'), ('tx', mq(5000) + 1, mp(1200) - 4, 'D', 't1')]
for q, p in pts:
    items += [('pt', mq(q), mp(p)), ('gd', mq(q), mp(p)), ('xt', mq(q), '%d' % q), ('yt', mp(p), '$%d' % p)]
plot('dcurve', 'Quantity of computers demanded per week', 'Price ($)', items,
     'The demand schedule (slide 8) plotted as a demand curve: each row of the table is one point. Higher price → lower quantity demanded.',
     'চাহিদা সূচি (স্লাইড ৮) চাহিদা রেখায় আঁকা: ছকের প্রতিটি সারি একটি বিন্দু। দাম বেশি → চাহিদার পরিমাণ কম।')

plot('dmove', 'Quantity', 'Price', ln(D0, 'l1', 'D') + [
    ('pt', 30, 70), ('gd', 30, 70), ('tx', 32, 73, 'A', 't3'), ('pt', 60, 40), ('gd', 60, 40), ('tx', 62, 43, 'B', 't3'),
    ('ar', 34, 66, 56, 44), ('xt', 30, 'Q1'), ('xt', 60, 'Q2'), ('yt', 70, 'P1'), ('yt', 40, 'P2')],
    'Movement ALONG the demand curve: only the good\'s own price changes (P1 → P2), so quantity demanded changes (Q1 → Q2). The curve itself stays put.',
    'চাহিদা রেখা **বরাবর** চলাচল: শুধু পণ্যের নিজের দাম বদলায় (P1 → P2), তাই চাহিদার পরিমাণ বদলায় (Q1 → Q2)। রেখা নিজে সরে না।')

plot('dshift', 'Quantity', 'Price', ln(D0, 'l1', 'D') + ln(D0, 'l2', 'D1', dx=18) + ln(D0, 'l3', 'D2', dx=-16) + [
    ('gy', 68, 50), ('pt', 34, 50), ('pt', 50, 50), ('pt', 68, 50), ('ar', 52, 56, 64, 56, 'l2'), ('ar', 48, 44, 36, 44, 'l3'),
    ('yt', 50, 'P'), ('xt', 34, 'Q2'), ('xt', 50, 'Q'), ('xt', 68, 'Q1'), ('gx', 34, 50), ('gx', 50, 50), ('gx', 68, 50)],
    'SHIFT of demand: something other than price changes. D → D1 (right) = increase: more bought at the same price. D → D2 (left) = decrease.',
    'চাহিদার **সরণ**: দাম ছাড়া অন্য কিছু বদলায়। D → D1 (ডানে) = বৃদ্ধি: একই দামে বেশি কেনা হয়। D → D2 (বাঁয়ে) = হ্রাস।')

plot('scurve', 'Quantity supplied', 'Price', ln(S0, 'l2', 'S') + [
    ('pt', 30, 30), ('gd', 30, 30), ('pt', 70, 70), ('gd', 70, 70), ('ar', 34, 34, 66, 66, 'l3'),
    ('xt', 30, 'Q1'), ('xt', 70, 'Q2'), ('yt', 30, 'P1'), ('yt', 70, 'P2')],
    'Law of supply: the supply curve slopes UP. A higher price (P1 → P2) brings a larger quantity supplied (Q1 → Q2): a movement along S.',
    'যোগানের নিয়ম: যোগান রেখা **ওপরের দিকে** ওঠে। দাম বাড়লে (P1 → P2) যোগানের পরিমাণ বাড়ে (Q1 → Q2): S বরাবর চলাচল।')

plot('sshift', 'Quantity', 'Price', ln(S0, 'l2', 'S') + ln(S0, 'l1', 'S1', dx=18) + ln(S0, 'l3', 'S2', dx=-16) + [
    ('gy', 68, 50), ('pt', 34, 50), ('pt', 50, 50), ('pt', 68, 50), ('ar', 52, 46, 64, 46, 'l1'), ('ar', 48, 54, 36, 54, 'l3'),
    ('yt', 50, 'P'), ('xt', 34, 'Q2'), ('xt', 50, 'Q'), ('xt', 68, 'Q1'), ('gx', 34, 50), ('gx', 50, 50), ('gx', 68, 50)],
    'SHIFT of supply: S → S1 (right) = increase in supply (more offered at the same price); S → S2 (left) = decrease.',
    'যোগানের **সরণ**: S → S1 (ডানে) = যোগান বৃদ্ধি (একই দামে বেশি বিক্রির প্রস্তাব); S → S2 (বাঁয়ে) = হ্রাস।')

plot('eq', 'Quantity', 'Price', ln(D0, 'l4', 'D') + ln(S0, 'l2', 'S') + [
    ('pt', 50, 50), ('gd', 50, 50), ('tx', 53, 52, 'E', 't3'), ('yt', 50, 'Pe = 3'), ('xt', 50, 'Qe = 60')],
    'Equilibrium (slide 25): demand = supply at point E. The market-clearing price is 3 and quantity is 60. No shortage, no surplus, no tendency to change.',
    'ভারসাম্য (স্লাইড ২৫): E বিন্দুতে চাহিদা = যোগান। বাজার-পরিষ্কারক দাম ৩, পরিমাণ ৬০। ঘাটতি নেই, উদ্বৃত্ত নেই, বদলের প্রবণতা নেই।')

plot('diseq', 'Quantity', 'Price', ln(D0, 'l4', 'D') + ln(S0, 'l2', 'S') + [
    ('pt', 50, 50), ('tx', 53, 50, 'E', 't3'), ('gy', 70, 70), ('gy', 70, 30), ('ln', 30, 70, 70, 70, 'l3'), ('ln', 30, 30, 70, 30, 'l1'),
    ('tx', 32, 74, 'Excess supply (surplus)', 't3'), ('ar', 50, 76, 50, 58, 'l3'),
    ('tx', 32, 22, 'Excess demand (shortage)', 't1'), ('ar', 50, 24, 50, 42, 'l1'), ('yt', 70, 'high P'), ('yt', 30, 'low P')],
    'Disequilibrium (slide 26): above E, quantity supplied > quantity demanded → surplus pushes price DOWN. Below E, demand > supply → shortage pushes price UP.',
    'ভারসাম্যহীনতা (স্লাইড ২৬): E-র ওপরে যোগান > চাহিদা → উদ্বৃত্ত দামকে **নামায়**। E-র নিচে চাহিদা > যোগান → ঘাটতি দামকে **ওঠায়**।')

plot('ceiling', 'Quantity of wheat', 'Price of wheat', ln(D0, 'l4', 'D') + ln(S0, 'l2', 'S') + [
    ('pt', 50, 50), ('gd', 50, 50), ('ln', 0, 32, 96, 32, 'l3'), ('tx', 70, 34, 'Price ceiling P1', 't3'),
    ('gx', 32, 32), ('gx', 68, 32), ('ln', 32, 27, 68, 27, 'l1'), ('tx', 36, 21, '← shortage (excess demand) →', 't1'),
    ('yt', 50, 'Pe'), ('yt', 32, 'P1'), ('xt', 32, 'Qs'), ('xt', 50, 'Qe'), ('xt', 68, 'Qd')],
    'Price ceiling (maximum price) set BELOW equilibrium: buyers want Qd but sellers offer only Qs → a persistent shortage, queues, rationing, black markets.',
    'দামের সর্বোচ্চ সীমা (price ceiling) ভারসাম্যের **নিচে**: ক্রেতা চায় Qd, বিক্রেতা দেয় শুধু Qs → স্থায়ী ঘাটতি, লাইন, রেশনিং, কালোবাজার।')

plot('floor', 'Quantity of wheat', 'Price of wheat', ln(D0, 'l4', 'D') + ln(S0, 'l2', 'S') + [
    ('pt', 50, 50), ('gd', 50, 50), ('ln', 0, 68, 96, 68, 'l3'), ('tx', 2, 71, 'Price floor P2', 't3'),
    ('gx', 32, 68), ('gx', 68, 68), ('ln', 32, 74, 68, 74, 'l1'), ('tx', 34, 77, '← surplus (excess supply) →', 't1'),
    ('yt', 50, 'Pe'), ('yt', 68, 'P2'), ('xt', 32, 'Qd'), ('xt', 50, 'Qe'), ('xt', 68, 'Qs')],
    'Price floor (minimum price) set ABOVE equilibrium: sellers offer Qs but buyers take only Qd → a persistent surplus the government must buy, store or destroy.',
    'দামের সর্বনিম্ন সীমা (price floor) ভারসাম্যের **ওপরে**: বিক্রেতা দেয় Qs, ক্রেতা নেয় শুধু Qd → স্থায়ী উদ্বৃত্ত, যা সরকারকে কিনতে, মজুদ বা নষ্ট করতে হয়।')

def shiftfig(key, which, up, cap, capb):
    if which == 'D':
        new = ln(D0, 'l3', 'D1', dx=24 if up else -24)
        e1 = (62, 62) if up else (38, 38)
        base = ln(D0, 'l4', 'D') + ln(S0, 'l2', 'S')
    else:
        new = ln(S0, 'l3', 'S1', dx=24 if up else -24)
        e1 = (62, 38) if up else (38, 62)
        base = ln(D0, 'l4', 'D') + ln(S0, 'l2', 'S')
    it = base + new + [('pt', 50, 50), ('gd', 50, 50), ('tx', 52, 54, 'E', 't3'), ('pt', e1[0], e1[1]), ('gd', e1[0], e1[1]), ('tx', e1[0] + 2, e1[1] + 4, 'E1', 't3'),
                       ('yt', 50, 'P'), ('yt', e1[1], 'P1'), ('xt', 50, 'Q'), ('xt', e1[0], 'Q1')]
    plot(key, 'Quantity', 'Price', it, cap, capb)

shiftfig('d_inc', 'D', True, 'Demand increases (D → D1): at the old price P there is excess demand, so price rises to P1 and quantity rises to Q1. Both P and Q go UP.',
         'চাহিদা বাড়ে (D → D1): পুরোনো দাম P-তে অতিরিক্ত চাহিদা, তাই দাম P1-এ ও পরিমাণ Q1-এ ওঠে। P ও Q দুটোই **বাড়ে**।')
shiftfig('d_dec', 'D', False, 'Demand decreases (D → D1): at P there is excess supply, so price falls to P1 and quantity falls to Q1. Both P and Q go DOWN.',
         'চাহিদা কমে (D → D1): P-তে অতিরিক্ত যোগান, তাই দাম P1-এ ও পরিমাণ Q1-এ নামে। P ও Q দুটোই **কমে**।')
shiftfig('s_inc', 'S', True, 'Supply increases (S → S1): at P there is excess supply, so price FALLS to P1 and quantity RISES to Q1.',
         'যোগান বাড়ে (S → S1): P-তে অতিরিক্ত যোগান, তাই দাম P1-এ **নামে** আর পরিমাণ Q1-এ **বাড়ে**।')
shiftfig('s_dec', 'S', False, 'Supply decreases (S → S1): at P there is excess demand, so price RISES to P1 and quantity FALLS to Q1.',
         'যোগান কমে (S → S1): P-তে অতিরিক্ত চাহিদা, তাই দাম P1-এ **ওঠে** আর পরিমাণ Q1-এ **নামে**।')

# =====================================================================
# Lecture 4 — double shifts and price elasticity of demand
# =====================================================================
def dbl(key, ddx, sdx, cap, capb):
    # D: x + y = 100 + ddx ; S: y = x - sdx  -> E1 x = (100 + ddx + sdx)/2
    x1 = (100 + ddx + sdx) / 2.0; y1 = x1 - sdx
    it = ln(D0, 'l4', 'D') + ln(S0, 'l2', 'S') + ln(D0, 'l4', 'D1', dx=ddx, dash=True) + ln(S0, 'l2', 'S1', dx=sdx, dash=True) + [
        ('pt', 50, 50), ('gd', 50, 50), ('tx', 52, 54, 'E', 't3'), ('pt', x1, y1), ('gd', x1, y1), ('tx', x1 + 2, y1 + 4, 'E1', 't3'),
        ('yt', 50, 'P'), ('yt', y1, 'P1'), ('xt', 50, 'Q'), ('xt', x1, 'Q1')]
    plot(key, 'Quantity', 'Price', it, cap, capb)

dbl('dbl_up_up', 10, 30, 'Demand ↑ and supply ↑ (here supply rises more): quantity rises for sure; price falls because the supply increase is bigger. If demand rose more, price would rise.',
    'চাহিদা ↑ ও যোগান ↑ (এখানে যোগান বেশি বাড়ে): পরিমাণ নিশ্চিতভাবে বাড়ে; যোগান বৃদ্ধি বড় বলে দাম কমে। চাহিদা বেশি বাড়লে দাম বাড়ত।')
dbl('dbl_dn_dn', -10, -30, 'Demand ↓ and supply ↓ (here supply falls more): quantity falls for sure; price rises because the supply decrease is bigger.',
    'চাহিদা ↓ ও যোগান ↓ (এখানে যোগান বেশি কমে): পরিমাণ নিশ্চিতভাবে কমে; যোগান হ্রাস বড় বলে দাম বাড়ে।')
dbl('dbl_up_dn', 26, -14, 'Demand ↑ and supply ↓: price rises for sure. Quantity depends on which change is bigger (here the demand increase is bigger, so Q rises a little).',
    'চাহিদা ↑ ও যোগান ↓: দাম নিশ্চিতভাবে বাড়ে। পরিমাণ নির্ভর করে কোন পরিবর্তন বড় তার ওপর (এখানে চাহিদা বৃদ্ধি বড়, তাই Q একটু বাড়ে)।')
dbl('dbl_dn_up', -26, 14, 'Demand ↓ and supply ↑: price falls for sure. Quantity depends on which change is bigger (here the demand decrease is bigger, so Q falls a little).',
    'চাহিদা ↓ ও যোগান ↑: দাম নিশ্চিতভাবে কমে। পরিমাণ নির্ভর করে কোন পরিবর্তন বড় তার ওপর (এখানে চাহিদা হ্রাস বড়, তাই Q একটু কমে)।')

plot('elastic', 'Quantity demanded', 'Price (£)', [
    ('area', [(0, 0), (0, 70), (17, 70), (17, 0)], 'fl2'), ('area', [(0, 0), (0, 49), (68, 49), (68, 0)], 'fl'),
    ('ln', 0, 79, 90, 40, 'l4'), ('tx', 91, 40, 'D', 't4'), ('pt', 17, 70), ('pt', 68, 49), ('gd', 17, 70), ('gd', 68, 49),
    ('yt', 70, '10'), ('yt', 49, '7'), ('xt', 17, '5'), ('xt', 68, '20'), ('tx', 30, 80, 'Flat curve: elastic, |E| > 1', 't4')],
    'Elastic demand (slide 16): price falls a little (£10 → £7, −30%) but quantity jumps (5 → 20, +300%). The curve is FLAT; total revenue rises (green area > gold area).',
    'স্থিতিস্থাপক চাহিদা (স্লাইড ১৬): দাম সামান্য কমে (£১০ → £৭, −৩০%) কিন্তু পরিমাণ লাফ দেয় (৫ → ২০, +৩০০%)। রেখা **চ্যাপ্টা**; মোট আয় বাড়ে (সবুজ অংশ > সোনালি অংশ)।')

plot('inelastic', 'Quantity demanded', 'Price (£)', [
    ('area', [(0, 0), (0, 80), (40, 80), (40, 0)], 'fl2'), ('area', [(0, 0), (0, 40), (48, 40), (48, 0)], 'fl'),
    ('ln', 36, 96, 52, 16, 'l4'), ('tx', 53, 14, 'D', 't4'), ('pt', 40, 80), ('pt', 48, 40), ('gd', 40, 80), ('gd', 48, 40),
    ('yt', 80, '10'), ('yt', 40, '5'), ('xt', 40, '5'), ('xt', 48, '6'), ('tx', 56, 70, 'Steep: inelastic, |E| < 1', 't4')],
    'Inelastic demand (slide 17): price halves (£10 → £5, −50%) but quantity hardly moves (5 → 6, +20%). The curve is STEEP; total revenue falls when price falls.',
    'অস্থিতিস্থাপক চাহিদা (স্লাইড ১৭): দাম অর্ধেক হয় (£১০ → £৫, −৫০%) কিন্তু পরিমাণ প্রায় নড়ে না (৫ → ৬, +২০%)। রেখা **খাড়া**; দাম কমলে মোট আয় কমে।')

def mini(ox, title, body):
    return '<g transform="translate(%d 0)"><line class="ax" x1="14" y1="160" x2="118" y2="160"/><line class="ax" x1="14" y1="160" x2="14" y2="22"/>%s<text x="66" y="182" text-anchor="middle" class="sm">%s</text></g>' % (ox, body, title)
raw('ped_extremes',
    '<svg viewBox="0 0 380 200" role="img" aria-label="Perfectly inelastic, unit elastic and perfectly elastic demand">'
    + mini(0, '(a) Perfectly inelastic, E = 0', '<line class="l4" x1="60" y1="30" x2="60" y2="160"/><text x="64" y="36" class="t4">D</text>')
    + mini(126, '(b) Unit elastic, E = 1', '<path class="l4" d="M24 30 Q40 120 112 140"/><text x="96" y="132" class="t4">D</text>')
    + mini(252, '(c) Perfectly elastic, E = ∞', '<line class="l4" x1="14" y1="80" x2="118" y2="80"/><text x="100" y="74" class="t4">D</text>')
    + '<text x="190" y="198" text-anchor="middle" class="sm">vertical axis = Price · horizontal axis = Quantity</text></svg>',
    'The three special (extreme/unit) cases on slide 18: vertical D (E = 0), rectangular-hyperbola D (E = 1), horizontal D (E = ∞).',
    'স্লাইড ১৮-এর তিনটি বিশেষ ক্ষেত্র: খাড়া D (E = ০), আয়তাকার পরাবৃত্ত D (E = ১), আনুভূমিক D (E = ∞)।')

# =====================================================================
# Lecture 5 — PES, total revenue, cross and income elasticity
# =====================================================================
plot('es', 'Quantity supplied', 'Price (£)', [
    ('area', [(0, 0), (0, 56), (20, 56), (20, 0)], 'fl'), ('area', [(0, 0), (0, 80), (48, 80), (48, 0)], 'fl2'),
    ('ln', 12, 52, 60, 84, 'l2'), ('tx', 61, 85, 'S', 't2'), ('pt', 20, 56), ('pt', 48, 80), ('gd', 20, 56), ('gd', 48, 80),
    ('yt', 80, '10'), ('yt', 56, '7'), ('xt', 20, '5'), ('xt', 48, '12'), ('tx', 55, 50, 'Flat S: elastic, E > 1', 't2')],
    'Elastic supply (slide 8): price rises £7 → £10 (+43%), quantity supplied jumps 5 → 12 (+140%). Flat supply curve.',
    'স্থিতিস্থাপক যোগান (স্লাইড ৮): দাম £৭ → £১০ (+৪৩%), যোগানের পরিমাণ ৫ → ১২ (+১৪০%)। চ্যাপ্টা যোগান রেখা।')
plot('is_', 'Quantity supplied', 'Price (£)', [
    ('area', [(0, 0), (0, 40), (20, 40), (20, 0)], 'fl'), ('area', [(0, 0), (0, 80), (28, 80), (28, 0)], 'fl2'),
    ('ln', 16, 20, 31, 95, 'l2'), ('tx', 32, 92, 'S', 't2'), ('pt', 20, 40), ('pt', 28, 80), ('gd', 20, 40), ('gd', 28, 80),
    ('yt', 80, '10'), ('yt', 40, '5'), ('xt', 20, '5'), ('xt', 28, '7'), ('tx', 40, 60, 'Steep S: inelastic, E < 1', 't2')],
    'Inelastic supply (slide 9): price doubles £5 → £10 (+100%), quantity supplied rises only 5 → 7 (+40%). Steep supply curve.',
    'অস্থিতিস্থাপক যোগান (স্লাইড ৯): দাম দ্বিগুণ £৫ → £১০ (+১০০%), যোগানের পরিমাণ মাত্র ৫ → ৭ (+৪০%)। খাড়া যোগান রেখা।')
raw('pes_extremes',
    '<svg viewBox="0 0 380 200" role="img" aria-label="Perfectly inelastic, unit elastic and perfectly elastic supply">'
    + mini(0, '(a) Perfectly inelastic, E = 0', '<line class="l2" x1="60" y1="30" x2="60" y2="160"/><text x="64" y="36" class="t2">S</text>')
    + mini(126, '(b) Unit elastic, E = 1', '<line class="l2" x1="14" y1="160" x2="104" y2="40"/><text x="106" y="44" class="t2">S</text>')
    + mini(252, '(c) Perfectly elastic, E = ∞', '<line class="l2" x1="14" y1="80" x2="118" y2="80"/><text x="100" y="74" class="t2">S</text>')
    + '<text x="190" y="198" text-anchor="middle" class="sm">vertical axis = Price · horizontal axis = Quantity</text></svg>',
    'Slide 10: vertical S (E = 0, supply does not change), straight S through the origin (E = 1), horizontal S (E = ∞).',
    'স্লাইড ১০: খাড়া S (E = ০, যোগান বদলায় না), মূলবিন্দু দিয়ে যাওয়া সরল S (E = ১), আনুভূমিক S (E = ∞)।')

plot('tr_elastic', 'Quantity demanded (Qd)', 'Price', [
    ('ln', 4, 84, 92, 44, 'l4'), ('tx', 93, 42, 'D', 't4'),
    ('area', [(30, 72.2), (30, 58), (0, 58), (0, 72.2)], 'fl3'), ('area', [(30, 58), (62, 58), (62, 0), (30, 0)], 'fl'),
    ('pt', 30, 72.2), ('pt', 62, 57.6), ('gd', 30, 72.2), ('gd', 62, 57.6), ('yt', 72, 'P'), ('yt', 57.6, 'P1'), ('xt', 30, 'Qd'), ('xt', 62, 'Qd1'),
    ('tx', 4, 63, '(−) lost', 't3'), ('tx', 38, 30, '(+) gained', 't1')],
    'Elastic demand (slide 14): cutting price P → P1 loses the small red area (−) but gains the big green area (+). Total revenue RISES, so to increase TR, decrease price.',
    'স্থিতিস্থাপক চাহিদা (স্লাইড ১৪): দাম P → P1 কমালে ছোট লাল অংশ (−) হারায় কিন্তু বড় সবুজ অংশ (+) পায়। মোট আয় **বাড়ে** — তাই TR বাড়াতে দাম কমাও।')
plot('tr_inelastic', 'Quantity demanded (Qd)', 'Price', [
    ('ln', 30, 94, 50, 14, 'l4'), ('tx', 51, 12, 'D', 't4'),
    ('area', [(0, 50), (0, 70), (36, 70), (36, 50)], 'fl'), ('area', [(36, 50), (41, 50), (41, 0), (36, 0)], 'fl3'),
    ('pt', 36, 70), ('pt', 41, 50), ('gd', 36, 70), ('gd', 41, 50), ('yt', 70, 'P1'), ('yt', 50, 'P'), ('xt', 34, 'Qd1'), ('xt', 43, 'Qd'),
    ('tx', 3, 59, '(+) gained', 't1'), ('tx', 44, 22, '(−) lost', 't3'), ('tx', 56, 84, 'Raise price → TR ↑', 't4')],
    'Inelastic demand (slide 15): raising price P → P1 gains the big green area (+) and loses only the thin red strip (−). Total revenue RISES when price rises.',
    'অস্থিতিস্থাপক চাহিদা (স্লাইড ১৫): দাম P → P1 বাড়ালে বড় সবুজ অংশ (+) পায়, হারায় শুধু সরু লাল ফালি (−)। দাম বাড়ালে মোট আয় **বাড়ে**।')

def two(key, left, right, cap, capb, xl, yl):
    def panel(ox, title, body):
        return ('<g transform="translate(%d 0)"><line class="ax" x1="30" y1="170" x2="170" y2="170"/><line class="ax" x1="30" y1="170" x2="30" y2="30"/>'
                '<text x="100" y="22" text-anchor="middle" font-weight="700">%s</text>%s<text x="100" y="190" text-anchor="middle" class="sm">%s</text>'
                '<text x="12" y="100" transform="rotate(-90 12 100)" text-anchor="middle" class="sm">%s</text></g>') % (ox, title, body, xl, yl)
    raw(key, '<svg viewBox="0 0 380 200" role="img" aria-label="%s">' % cap.replace('"', "'") + panel(0, *left) + panel(190, *right) + '</svg>', cap, capb)

two('xed', ('Substitutes (XED +)', '<line class="l1" x1="40" y1="160" x2="160" y2="50"/>'),
    ('Complements (XED −)', '<line class="l3" x1="40" y1="50" x2="160" y2="160"/>'),
    'Cross elasticity (slide 22): for substitutes, a higher price of Y raises the quantity demanded of X (upward line); for complements it lowers it (downward line).',
    'আড়াআড়ি স্থিতিস্থাপকতা (স্লাইড ২২): বিকল্প পণ্যে Y-এর দাম বাড়লে X-এর চাহিদার পরিমাণ বাড়ে (ঊর্ধ্বমুখী রেখা); পরিপূরকে কমে (নিম্নমুখী রেখা)।',
    'Price of Y (Py)', 'Quantity of X (Qx)')
two('yed', ('Normal good (YED +)', '<line class="l1" x1="40" y1="160" x2="160" y2="50"/>'),
    ('Inferior good (YED −)', '<line class="l3" x1="40" y1="50" x2="160" y2="160"/>'),
    'Income elasticity (slide 25): for a normal good, quantity demanded rises with income; for an inferior good it falls as income rises. (The slide puts income on the vertical axis; the direction of the relationship is what matters.)',
    'আয় স্থিতিস্থাপকতা (স্লাইড ২৫): স্বাভাবিক পণ্যে আয় বাড়লে চাহিদার পরিমাণ বাড়ে; নিকৃষ্ট পণ্যে আয় বাড়লে কমে। (স্লাইডে আয় খাড়া অক্ষে; সম্পর্কের দিকটাই আসল।)',
    'Quantity demanded', 'Income')

# =====================================================================
# Lecture 6 — production and short-run costs
# =====================================================================
TPd = [0, 10, 25, 45, 60, 70, 75, 75, 70]
MPd = [10, 15, 20, 15, 10, 5, 0, -5]
APd = [10, 12.5, 15, 15, 14, 12.5, 10.71, 8.75]
def lx(l): return l * 11.0
items = [('cu', [(lx(i), t * 1.15) for i, t in enumerate(TPd)], 'l1'), ('tx', lx(8) + 1, 70 * 1.15 - 6, 'TP', 't1')]
for i, t in enumerate(TPd):
    items += [('pt', lx(i), t * 1.15), ('xt', lx(i), str(i))]
for v in (25, 50, 75): items.append(('yt', v * 1.15, str(v)))
items += [('gx', lx(3), 45 * 1.15), ('gx', lx(6.5), 75 * 1.15),
          ('tx', 2, 98, 'increasing MP', 't2'), ('tx', 36, 98, 'diminishing MP', 't2'), ('tx', 73, 98, 'negative MP', 't3')]
plot('tp', 'Units of labour', 'Total product (TP)', items,
     'Total product (McConnell & Brue Table 20.1): TP rises fast (workers 1–3), then more slowly (4–6), is maximum at 75 when MP = 0, then falls (worker 8).',
     'মোট উৎপাদন (ম্যাককনেল ও ব্রু ছক ২০.১): TP দ্রুত বাড়ে (শ্রমিক ১–৩), তারপর ধীরে (৪–৬), MP = ০ হলে সর্বোচ্চ ৭৫, তারপর কমে (শ্রমিক ৮)।')

def my(v): return (v + 6) * 3.6
items = [('ln', 0, my(0), 98, my(0), 'gd'), ('yt', my(0), '0'), ('yt', my(10), '10'), ('yt', my(20), '20'),
         ('cu', [(lx(i + 0.5) , my(m)) for i, m in enumerate(MPd)], 'l3'), ('cu', [(lx(i + 1), my(a)) for i, a in enumerate(APd)], 'l4'),
         ('tx', lx(7.5) + 1, my(-5) + 2, 'MP', 't3'), ('tx', lx(8) + 1, my(8.75) + 2, 'AP', 't4'),
         ('pt', lx(3.5), my(15)), ('tx', lx(3.5) + 1, my(15) + 4, 'MP = AP (AP max)', 't3')]
for i in range(1, 9): items.append(('xt', lx(i), str(i)))
plot('mpap', 'Units of labour', 'MP and AP', items,
     'MP rises, peaks at the 3rd worker, then falls (diminishing returns) and becomes negative. AP rises while MP > AP and falls while MP < AP; MP cuts AP at AP\'s maximum.',
     'MP বাড়ে, তৃতীয় শ্রমিকে সর্বোচ্চ, তারপর কমে (ক্রমহ্রাসমান প্রতিদান) ও ঋণাত্মক হয়। MP > AP থাকলে AP বাড়ে, MP < AP হলে কমে; AP-র সর্বোচ্চ বিন্দুতে MP, AP-কে কাটে।')

plot('fvtc', 'Quantity / output', 'Costs', [
    ('ln', 0, 30, 96, 30, 'l2'), ('tx', 85, 33, 'FC', 't2'),
    ('cu', [(0, 0), (25, 18), (50, 30), (75, 46), (92, 68)], 'l4'), ('tx', 93, 66, 'VC', 't4'),
    ('cu', [(0, 30), (25, 48), (50, 60), (75, 76), (92, 98)], 'l1'), ('tx', 70, 98, 'TC = FC+VC', 't1'),
    ('ar', 60, 36, 60, 64, 'l3'), ('tx', 62, 50, 'gap = FC', 't3')],
    'FC is flat (it does not change with output). VC starts at zero and rises. TC = FC + VC, so TC has the same shape as VC but starts at the level of FC; the vertical gap between TC and VC is always FC.',
    'FC সমতল (উৎপাদনের সাথে বদলায় না)। VC শূন্য থেকে শুরু হয়ে বাড়ে। TC = FC + VC, তাই TC-র আকৃতি VC-র মতোই কিন্তু FC-র স্তর থেকে শুরু; TC ও VC-র মধ্যকার খাড়া দূরত্ব সবসময় FC।')

AFCp = [(6, 92), (15, 40), (30, 20), (50, 12), (70, 8.5), (94, 6.5)]
AVCp = [(8, 64), (30, 42), (50, 35), (70, 41), (92, 62)]
ATCp = [(10, 96), (30, 62), (45, 53), (60, 50), (75, 56), (92, 70)]
MCp = [(10, 52), (25, 34), (36, 30), (50, 35), (60, 50), (70, 68), (78, 92)]
plot('afc', 'Quantity / output', 'Costs', [('cu', AFCp, 'l2'), ('tx', 86, 12, 'AFC', 't2'), ('tx', 30, 60, 'AFC = TFC ÷ Q keeps falling', 't2')],
     'AFC = TFC ÷ Q falls continuously as output rises: the same overhead is spread over more units. It is the only short-run cost that always falls.',
     'AFC = TFC ÷ Q উৎপাদন বাড়লে অবিরাম কমে: একই স্থির খরচ বেশি এককে ভাগ হয়। স্বল্পমেয়াদে এটাই একমাত্র ব্যয় যা সবসময় কমে।')
plot('avc', 'Quantity / output', 'Costs', [('cu', AVCp, 'l4'), ('tx', 92, 64, 'AVC', 't4'), ('pt', 50, 35), ('tx', 42, 26, 'minimum AVC', 't4')],
     'AVC is U-shaped: it falls while marginal product is rising (increasing returns), reaches a minimum, then rises when diminishing returns set in.',
     'AVC ইংরেজি U আকৃতির: প্রান্তিক উৎপাদন বাড়ার সময় কমে (ক্রমবর্ধমান প্রতিদান), সর্বনিম্নে পৌঁছায়, তারপর ক্রমহ্রাসমান প্রতিদান শুরু হলে বাড়ে।')
plot('atc_u', 'Quantity / output', 'Costs', [('cu', ATCp, 'l1'), ('tx', 92, 72, 'ATC', 't1'), ('pt', 60, 50), ('gx', 60, 50),
     ('tx', 52, 40, 'optimum (lowest ATC)', 't3'), ('tx', 4, 76, '← falling ATC', 't1'), ('tx', 66, 80, 'rising ATC →', 't1')],
     'ATC is U-shaped. Its lowest point is the optimum (most efficient) output. (Slide 30 labels the two sides "economies" and "diseconomies"; those words strictly belong to the long run, Lecture 7.)',
     'ATC ইংরেজি U আকৃতির। এর সর্বনিম্ন বিন্দুই সর্বোত্তম (সবচেয়ে দক্ষ) উৎপাদন। (স্লাইড ৩০ দুই পাশকে "economies" ও "diseconomies" বলেছে; শব্দ দুটি আসলে দীর্ঘমেয়াদের, লেকচার ৭।)')
plot('costs_all', 'Quantity / output', 'Costs per unit', [
    ('cu', AFCp, 'l2'), ('cu', AVCp, 'l4'), ('cu', ATCp, 'l1'), ('cu', MCp, 'l3'),
    ('tx', 88, 12, 'AFC', 't2'), ('tx', 92, 58, 'AVC', 't4'), ('tx', 92, 74, 'ATC', 't1'), ('tx', 79, 92, 'MC', 't3'),
    ('pt', 50, 35), ('pt', 60, 50), ('ln', 84, 52, 84, 64, 'l3'), ('tx', 60, 28, 'gap ATC − AVC = AFC', 't3')],
    'All four together (McConnell & Brue p. 386): ATC = AFC + AVC, so the gap between ATC and AVC is AFC and it shrinks as output grows. MC cuts AVC and ATC at their MINIMUM points.',
    'চারটি একসাথে (ম্যাককনেল ও ব্রু পৃ. ৩৮৬): ATC = AFC + AVC, তাই ATC ও AVC-র মাঝের ফাঁক হলো AFC, যা উৎপাদন বাড়লে ছোট হয়। MC, AVC ও ATC-কে তাদের **সর্বনিম্ন** বিন্দুতে কাটে।')
plot('mc', 'Quantity / output', 'Costs', [('cu', MCp, 'l3'), ('tx', 79, 92, 'MC', 't3'), ('pt', 36, 30), ('tx', 26, 20, 'MP is at its maximum here', 't3')],
     'MC first falls (marginal product rising), reaches a minimum where MP is highest, then rises as diminishing returns set in: MC is the mirror image of MP.',
     'MC প্রথমে কমে (প্রান্তিক উৎপাদন বাড়ছে), MP সর্বোচ্চ যেখানে সেখানে সর্বনিম্ন, তারপর ক্রমহ্রাসমান প্রতিদানে বাড়ে: MC হলো MP-র আয়নার প্রতিচ্ছবি।')

# =====================================================================
# Lecture 7 — cost table plotted, long-run ATC, economies of scale
# =====================================================================
CQ = list(range(1, 11))
AFCv = [100, 50, 33.33, 25, 20, 16.67, 14.29, 12.5, 11.11, 10]
AVCv = [90, 85, 80, 75, 74, 75, 77.14, 81.25, 86.67, 93]
ATCv = [190, 135, 113.33, 100, 94, 91.67, 91.43, 93.75, 97.78, 103]
MCv = [90, 80, 70, 60, 70, 80, 90, 110, 130, 150]
def cq(q): return q * 9.0
def cc(c): return c / 2.0
items = [('cu', [(cq(q), cc(v)) for q, v in zip(CQ, AFCv)], 'l2'), ('cu', [(cq(q), cc(v)) for q, v in zip(CQ, AVCv)], 'l4'),
         ('cu', [(cq(q), cc(v)) for q, v in zip(CQ, ATCv)], 'l1'), ('cu', [(cq(q - 0.5), cc(v)) for q, v in zip(CQ, MCv)], 'l3'),
         ('tx', cq(10) + 1, cc(10), 'AFC', 't2'), ('tx', cq(10) + 1, cc(93) - 4, 'AVC', 't4'), ('tx', cq(10) + 1, cc(103) + 1, 'ATC', 't1'), ('tx', cq(9.5) + 1, cc(150), 'MC', 't3'),
         ('pt', cq(5), cc(74)), ('pt', cq(7), cc(91.43))]
for q in CQ: items.append(('xt', cq(q), str(q)))
for c in (50, 100, 150): items.append(('yt', cc(c), '$%d' % c))
plot('mb_costs', 'Quantity (Q)', 'Costs ($)', items,
     'The slide table plotted (McConnell & Brue p. 388): MC falls to $60 then rises; it cuts AVC at its minimum ($74 at Q = 5) and ATC at its minimum ($91.43 at Q = 7). AFC keeps falling. (MC is plotted between quantities.)',
     'স্লাইডের ছক আঁকা (ম্যাককনেল ও ব্রু পৃ. ৩৮৮): MC নেমে $৬০, তারপর বাড়ে; AVC-কে সর্বনিম্নে কাটে (Q = ৫-এ $৭৪) আর ATC-কে সর্বনিম্নে (Q = ৭-এ $৯১.৪৩)। AFC কমতেই থাকে। (MC দুই পরিমাণের মাঝখানে আঁকা।)')

def u(cx, cy, w=12, h=22):
    return [(cx - w, cy + h), (cx - w / 2, cy + h * 0.3), (cx, cy), (cx + w / 2, cy + h * 0.3), (cx + w, cy + h)]
centers = [(14, 62), (32, 50), (50, 44), (68, 50), (86, 62)]
items = []
for i, (cx, cy) in enumerate(centers, 1):
    items += [('cu', u(cx, cy), 'l4'), ('tx', cx - 4, cy + 25, 'ATC-%d' % i, 't4')]
items += [('cu', [(4, 70), (14, 62), (23, 58), (32, 50), (41, 49), (50, 44), (59, 49), (68, 50), (77, 58), (86, 62), (94, 70)], 'l1', True),
          ('tx', 40, 14, 'dashed = LRATC', 't1')]
plot('lratc_seg', 'Output', 'Average total cost', items,
     'Five possible plant sizes, each with its own short-run ATC. For every output the firm picks the plant with the lowest cost; joining those lowest segments gives the long-run ATC curve.',
     'পাঁচটি সম্ভাব্য কারখানার আকার, প্রত্যেকটির নিজস্ব স্বল্পমেয়াদি ATC। প্রতিটি উৎপাদনে ফার্ম সবচেয়ে কম ব্যয়ের কারখানা বেছে নেয়; সেই সর্বনিম্ন অংশগুলো জুড়লে দীর্ঘমেয়াদি ATC রেখা পাওয়া যায়।')

plot('lratc_env', 'Output', 'Long-run average cost', [
    ('cu', [(4, 88), (20, 60), (40, 42), (52, 40), (64, 40), (80, 52), (94, 76)], 'l1'), ('tx', 90, 80, 'LRATC', 't1'),
    ('gx', 40, 42), ('gx', 64, 40), ('xt', 40, 'MES'), ('ar', 6, 24, 34, 24, 'l1'), ('tx', 2, 14, 'Economies of scale', 't1'),
    ('tx', 43, 30, 'Constant', 't2'), ('tx', 43, 24, 'returns', 't2'), ('ar', 70, 24, 94, 24, 'l3'), ('tx', 70, 14, 'Diseconomies', 't3')],
    'With unlimited plant sizes, LRATC is a smooth curve that "envelops" all the short-run ATCs. It falls (economies of scale), may stay flat (constant returns), then rises (diseconomies). MES = the smallest output at which LRATC reaches its minimum.',
    'অসীম সংখ্যক কারখানার আকারে LRATC একটি মসৃণ রেখা যা সব স্বল্পমেয়াদি ATC-কে "ঘিরে" রাখে। এটা কমে (বৃহদায়তনের সুবিধা), সমতল থাকতে পারে (স্থির প্রতিদান), তারপর বাড়ে (অসুবিধা)। MES = সবচেয়ে কম যে উৎপাদনে LRATC সর্বনিম্নে পৌঁছায়।')

# =====================================================================
# Lecture 8 — perfect competition
# =====================================================================
plot2('pc_demand', [
    ('Industry', 'Output', 'Price', ln(D0, 'l4', 'D') + ln(S0, 'l2', 'S') + [('pt', 50, 50), ('gy', 50, 50), ('yt', 50, 'P')]),
    ('Firm (price taker)', 'Output', 'Price, AR, MR', [('ln', 0, 50, 94, 50, 'l1'), ('tx', 30, 56, 'D = P = AR = MR', 't1'), ('yt', 50, 'P')])],
    'Slide 11: the industry\'s demand and supply set the price P. Each firm must accept P, so the firm\'s demand curve is a horizontal line: perfectly elastic, with P = AR = MR.',
    'স্লাইড ১১: শিল্পের চাহিদা ও যোগান দাম P ঠিক করে। প্রতিটি ফার্মকে P মেনে নিতে হয়, তাই ফার্মের চাহিদা রেখা আনুভূমিক: পূর্ণ স্থিতিস্থাপক, P = AR = MR।')

TCp = [(0, 18), (15, 28), (35, 36), (55, 44), (70, 58), (82, 76), (92, 96)]
plot('trtc', 'Quantity', 'TR, TC ($)', [
    ('ln', 0, 0, 96, 92, 'l1'), ('tx', 84, 86, 'TR', 't1'), ('cu', TCp, 'l3'), ('tx', 90, 97, 'TC', 't3'),
    ('pt', 23, 22), ('tx', 25, 16, 'break-even (TR = TC)', 't2'), ('pt', 85, 81.5), ('tx', 50, 92, 'break-even', 't2'),
    ('ln', 60, 57.5, 60, 47.5, 'l4'), ('tx', 26, 64, 'max profit: biggest gap', 't4'), ('ar', 46, 63, 58, 54, 'l4')],
    'TR–TC approach (slide 13): TR is a straight line (constant price). Profit = TR − TC is greatest where the vertical gap between TR (above) and TC (below) is largest. Where the curves meet, TR = TC: break-even (normal profit).',
    'TR–TC পদ্ধতি (স্লাইড ১৩): TR সরলরেখা (দাম স্থির)। মুনাফা = TR − TC সবচেয়ে বেশি যেখানে TR (ওপরে) আর TC (নিচে)-র খাড়া ফাঁক সবচেয়ে বড়। যেখানে রেখা মেলে সেখানে TR = TC: সমতা বিন্দু (স্বাভাবিক মুনাফা)।')

def pcfig(key, p, q, atc_at, avc_at, area_cls, label, cap, capb, show_avc=True):
    it = [('cu', ATCp, 'l1'), ('cu', MCp, 'l3'), ('ln', 0, p, 96, p, 'l4'), ('tx', 46, p + 3, 'P = AR = MR', 't4'),
          ('tx', 92, 72, 'ATC', 't1'), ('tx', 79, 92, 'MC', 't3')]
    if show_avc: it += [('cu', AVCp, 'l2'), ('tx', 92, 58, 'AVC', 't2')]
    if area_cls: it.insert(0, ('area', [(0, p), (q, p), (q, atc_at), (0, atc_at)], area_cls))
    if q: it += [('pt', q, p), ('gx', q, p), ('xt', q, 'Q (MR = MC)')]
    if label: it.append(('tx', 6, (p + atc_at) / 2 - 2, label, 't3' if area_cls == 'fl3' else 't1'))
    plot(key, 'Output', 'Cost and revenue', it, cap, capb)

pcfig('pc_profit', 70, 69, 54, 41, 'fl', 'Economic profit',
      'Short-run profit (slide 16): the firm produces where MR = MC. Price is above ATC there, so it earns an economic (supernormal) profit = the green rectangle (P − ATC) × Q.',
      'স্বল্পমেয়াদি মুনাফা (স্লাইড ১৬): ফার্ম MR = MC-তে উৎপাদন করে। সেখানে দাম ATC-র ওপরে, তাই অর্থনৈতিক (অতিস্বাভাবিক) মুনাফা = সবুজ আয়তক্ষেত্র (P − ATC) × Q।')
pcfig('pc_loss', 44, 56, 50.6, 36, 'fl3', 'Loss',
      'Short-run loss (slide 17): at MR = MC, price is below ATC (loss = red area) but above AVC, so the firm keeps producing: it covers all variable cost and part of its fixed cost.',
      'স্বল্পমেয়াদি লোকসান (স্লাইড ১৭): MR = MC-তে দাম ATC-র নিচে (লোকসান = লাল অংশ) কিন্তু AVC-র ওপরে, তাই ফার্ম উৎপাদন চালিয়ে যায়: সব পরিবর্তনশীল ব্যয় ও স্থির ব্যয়ের কিছু অংশ মেটে।')
pcfig('pc_shutdown', 28, 0, 0, 0, None, None,
      'Shutdown (slide 18): price is below the minimum of AVC, so the firm cannot even cover its variable costs. It loses less by closing (losing only its fixed costs).',
      'বন্ধ (স্লাইড ১৮): দাম AVC-র সর্বনিম্নেরও নিচে, তাই ফার্ম পরিবর্তনশীল ব্যয়ও মেটাতে পারে না। বন্ধ করলে কম হারায় (শুধু স্থির ব্যয়)।')

items = [('cu', ATCp, 'l1'), ('cu', AVCp, 'l2'), ('cu', MCp, 'l3', True), ('cu', [(50, 35), (60, 50), (70, 68), (78, 92)], 'l3'),
         ('tx', 92, 72, 'ATC', 't1'), ('tx', 92, 58, 'AVC', 't2'), ('tx', 40, 96, 'MC above AVC = supply', 't3')]
for i, (pp, qq) in enumerate([(35, 50), (50, 60), (62, 66.5), (80, 74)]):
    items += [('ln', 0, pp, qq, pp, 'gd'), ('pt', qq, pp), ('yt', pp, 'P%d' % (i + 2)), ('xt', qq, 'Q%d' % (i + 2))]
items += [('tx', 4, 26, 'below P2 (min AVC): produce nothing', 't3')]
plot('pc_supply', 'Output', 'Costs and revenues ($)', items,
     'Slides 19–23: at each price the firm produces where P = MC. So the part of the MC curve ABOVE minimum AVC is the firm\'s short-run supply curve; below P2 it shuts down.',
     'স্লাইড ১৯–২৩: প্রতিটি দামে ফার্ম P = MC-তে উৎপাদন করে। তাই সর্বনিম্ন AVC-র **ওপরের** MC অংশই ফার্মের স্বল্পমেয়াদি যোগান রেখা; P2-এর নিচে বন্ধ।')

def firm_panel(p_lines):
    it = [('cu', [(10, 80), (25, 58), (40, 50), (55, 58), (70, 80)], 'l1'), ('cu', [(16, 30), (28, 36), (40, 50), (50, 64), (58, 82), (63, 94)], 'l3'),
          ('tx', 4, 84, 'ATC', 't1'), ('tx', 66, 94, 'MC', 't3')]
    for pp, lab, cls in p_lines: it += [('ln', 0, pp, 94, pp, cls), ('yt', pp, lab)]
    return it
plot2('pc_entry', [
    ('Firm (price taker)', 'Q', 'P', firm_panel([(64, '$60', 'l4'), (50, '$50', 'gd')]) + [('area', [(0, 64), (50, 64), (50, 55), (0, 55)], 'fl'), ('tx', 3, 68, 'profit', 't1')]),
    ('Industry', 'Q', 'P', ln(D0, 'l4', 'D1') + ln(D0, 'l4', 'D2', dx=14) + ln(S0, 'l2', 'S1') + ln(S0, 'l2', 'S2', dx=14, dash=True) +
     [('pt', 50, 50), ('pt', 57, 57), ('pt', 64, 50), ('yt', 57, '$60'), ('yt', 50, '$50')])],
    'Entry eliminates profit (slides 25–26): demand rises (D1 → D2), price rises to $60 and firms earn economic profit. New firms enter, supply rises (S1 → S2), and price falls back to $50 = minimum ATC: only normal profit remains.',
    'প্রবেশ মুনাফা দূর করে (স্লাইড ২৫–২৬): চাহিদা বাড়ে (D1 → D2), দাম $৬০ হয়, ফার্মগুলো অর্থনৈতিক মুনাফা পায়। নতুন ফার্ম ঢোকে, যোগান বাড়ে (S1 → S2), দাম আবার $৫০ = সর্বনিম্ন ATC: শুধু স্বাভাবিক মুনাফা থাকে।')
plot2('pc_exit', [
    ('Firm (price taker)', 'Q', 'P', firm_panel([(36, '$40', 'l4'), (50, '$50', 'gd')]) + [('area', [(0, 56), (28, 56), (28, 36), (0, 36)], 'fl3'), ('tx', 3, 28, 'loss', 't3')]),
    ('Industry', 'Q', 'P', ln(D0, 'l4', 'D1') + ln(D0, 'l4', 'D2', dx=-14) + ln(S0, 'l2', 'S1') + ln(S0, 'l2', 'S3', dx=-14, dash=True) +
     [('pt', 50, 50), ('pt', 43, 43), ('pt', 36, 50), ('yt', 43, '$40'), ('yt', 50, '$50')])],
    'Exit eliminates losses (slides 27–28): demand falls (D1 → D2), price falls to $40 and firms make losses. Some firms leave, supply falls (S1 → S3), and price returns to $50: the remaining firms earn normal profit.',
    'প্রস্থান লোকসান দূর করে (স্লাইড ২৭–২৮): চাহিদা কমে (D1 → D2), দাম $৪০, ফার্মের লোকসান। কিছু ফার্ম বেরিয়ে যায়, যোগান কমে (S1 → S3), দাম আবার $৫০: বাকি ফার্মগুলো স্বাভাবিক মুনাফা পায়।')

plot2('lr_supply', [
    ('Constant cost', 'Q', 'P', [('ln', 4, 50, 94, 50, 'l1'), ('tx', 60, 56, 'LRS', 't1')]),
    ('Increasing cost', 'Q', 'P', [('ln', 4, 30, 94, 80, 'l1'), ('tx', 70, 82, 'LRS', 't1')]),
    ('Decreasing cost', 'Q', 'P', [('ln', 4, 80, 94, 30, 'l1'), ('tx', 70, 40, 'LRS', 't1')])],
    'Long-run industry supply (slide 29): horizontal in a constant-cost industry, upward-sloping in an increasing-cost industry, downward-sloping in a decreasing-cost industry.',
    'দীর্ঘমেয়াদি শিল্প যোগান (স্লাইড ২৯): স্থির-ব্যয়ের শিল্পে আনুভূমিক, ক্রমবর্ধমান-ব্যয়ের শিল্পে ঊর্ধ্বমুখী, ক্রমহ্রাসমান-ব্যয়ের শিল্পে নিম্নমুখী।', h=200)

# =====================================================================
# Lecture 9 — pure monopoly (McConnell & Brue numbers)
# =====================================================================
def mx(q): return q * 9.0
def my_(p): return p / 2.0
Dm = [(mx(q), my_(172 - 10 * q)) for q in (0, 10)]
MRm = [(mx(q), my_(172 - 20 * q)) for q in (0, 8.6)]
MCm = [(mx(q - 0.5), my_(v)) for q, v in zip(range(1, 11), MCv)]
ATCm = [(mx(q), my_(v)) for q, v in zip(range(1, 11), ATCv)]
plot('mono_profit', 'Quantity (Q)', 'Price, costs ($)', [
    ('area', [(0, my_(122)), (mx(5), my_(122)), (mx(5), my_(94)), (0, my_(94))], 'fl'),
    ('ln', Dm[0][0], Dm[0][1], Dm[1][0], Dm[1][1], 'l4'), ('tx', mx(10) - 2, my_(72) + 3, 'D = AR', 't4'),
    ('ln', MRm[0][0], MRm[0][1], MRm[1][0], MRm[1][1], 'l2'), ('tx', mx(8.2), 4, 'MR', 't2'),
    ('cu', MCm, 'l3'), ('tx', mx(9.5) + 1, my_(150) - 3, 'MC', 't3'), ('cu', ATCm, 'l1'), ('tx', mx(10) + 1, my_(103) + 1, 'ATC', 't1'),
    ('pt', mx(4.9), my_(76)), ('pt', mx(5), my_(122)), ('gd', mx(5), my_(122)), ('gy', mx(5), my_(94)),
    ('yt', my_(122), '$122'), ('yt', my_(94), '$94'), ('xt', mx(5), '5'), ('tx', 3, my_(110), 'Profit $140', 't1')],
    'Profit maximisation (slides 18–20): the monopolist produces Q = 5 where MR = MC, then goes UP to the demand curve to set the price, $122. ATC there is $94, so profit = (122 − 94) × 5 = $140.',
    'মুনাফা সর্বোচ্চকরণ (স্লাইড ১৮–২০): একচেটিয়া ফার্ম MR = MC যেখানে সেই Q = ৫ উৎপাদন করে, তারপর চাহিদা রেখা পর্যন্ত **ওপরে** গিয়ে দাম ঠিক করে: $১২২। সেখানে ATC $৯৪, তাই মুনাফা = (১২২ − ৯৪) × ৫ = $১৪০।')

plot2('mono_mr', [
    ('Demand and MR', 'Q', 'Price', [('ln', 0, 90, 90, 0, 'l4'), ('tx', 70, 22, 'D = AR', 't4'), ('ln', 0, 90, 45, 0, 'l2'), ('tx', 40, 10, 'MR', 't2'),
        ('gx', 45, 45), ('tx', 6, 60, 'elastic', 't1'), ('tx', 52, 50, 'inelastic', 't3'), ('tx', 30, 96, 'MR < P after 1st unit', 't2')]),
    ('Total revenue', 'Q', 'TR', [('cu', [(0, 0), (22, 70), (45, 92), (68, 70), (90, 0)], 'l1'), ('gx', 45, 92), ('tx', 30, 98, 'TR max (MR = 0)', 't1'),
        ('tx', 2, 40, 'MR +', 't1'), ('tx', 72, 40, 'MR −', 't3')])],
    'McConnell & Brue Fig. 22.3: MR lies below demand. Where MR is positive, TR rises (elastic demand); where MR = 0, TR is at its maximum (unit elastic); where MR is negative, TR falls (inelastic demand). A monopolist always stays in the elastic part.',
    'ম্যাককনেল ও ব্রু চিত্র ২২.৩: MR চাহিদার নিচে। যেখানে MR ধনাত্মক, TR বাড়ে (স্থিতিস্থাপক); MR = ০ হলে TR সর্বোচ্চ (একক); MR ঋণাত্মক হলে TR কমে (অস্থিতিস্থাপক)। একচেটিয়া ফার্ম সবসময় স্থিতিস্থাপক অংশে থাকে।', h=230)

plot('natmono', 'Quantity (millions)', 'Revenue / cost ($)', [
    ('cu', [(6, 92), (20, 55), (40, 36), (60, 28), (90, 22)], 'l1'), ('tx', 88, 26, 'ATC', 't1'),
    ('ln', 4, 80, 70, 4, 'l4'), ('tx', 66, 10, 'D', 't4'), ('tx', 26, 92, 'ATC falls over all of demand', 't1')],
    'Natural monopoly (slide 8): ATC keeps falling over the whole range of market demand, so one big firm can supply the market more cheaply than several small ones.',
    'প্রাকৃতিক একচেটিয়া (স্লাইড ৮): পুরো বাজার চাহিদার পরিসরজুড়ে ATC কমতেই থাকে, তাই একটি বড় ফার্ম কয়েকটি ছোট ফার্মের চেয়ে সস্তায় পুরো বাজারে যোগান দিতে পারে।')

plot('mono_loss', 'Quantity', 'Price, costs', [
    ('area', [(0, 46), (40, 46), (40, 56), (0, 56)], 'fl3'),
    ('ln', 0, 70, 90, 16, 'l4'), ('tx', 86, 20, 'D = AR', 't4'), ('ln', 0, 70, 58, 0, 'l2'), ('tx', 50, 6, 'MR', 't2'),
    ('cu', [(8, 90), (25, 64), (40, 56), (60, 54), (80, 62), (92, 74)], 'l1'), ('tx', 92, 78, 'ATC', 't1'),
    ('cu', [(10, 66), (30, 46), (45, 41), (65, 46), (85, 60)], 'l2', True), ('tx', 86, 62, 'AVC', 't2'),
    ('cu', [(12, 44), (25, 30), (40, 22), (52, 30), (62, 50), (70, 76)], 'l3'), ('tx', 70, 80, 'MC', 't3'),
    ('pt', 40, 46), ('gx', 40, 46), ('xt', 40, 'Qm'), ('yt', 46, 'Pm'), ('yt', 56, 'A'), ('tx', 4, 50, 'loss', 't3')],
    'Loss minimisation (slide 21): if demand falls (changing tastes) or costs rise, P can be below ATC at the MR = MC output. The monopolist still produces in the short run if P > AVC; if losses continue in the long run it moves its resources to other industries.',
    'লোকসান কমানো (স্লাইড ২১): চাহিদা কমলে (রুচি বদলালে) বা খরচ বাড়লে MR = MC উৎপাদনে P, ATC-র নিচে হতে পারে। P > AVC হলে একচেটিয়া ফার্ম স্বল্পমেয়াদে উৎপাদন চালায়; দীর্ঘমেয়াদে লোকসান চললে সম্পদ অন্য শিল্পে সরায়।')

plot('mono_vs_pc', 'Quantity', 'Price', [
    ('ln', 0, 90, 90, 0, 'l4'), ('tx', 86, 6, 'D', 't4'), ('ln', 0, 90, 45, 0, 'l2'), ('tx', 42, 4, 'MR', 't2'),
    ('ln', 0, 20, 90, 65, 'l3'), ('tx', 82, 66, 'S = MC', 't3'),
    ('pt', 46.7, 43.3), ('gd', 46.7, 43.3), ('xt', 46.7, 'Qc'), ('yt', 43.3, 'Pc'),
    ('pt', 28, 62), ('gd', 28, 62), ('xt', 28, 'Qm'), ('yt', 62, 'Pm'), ('pt', 28, 34),
    ('tx', 30, 80, 'Monopoly: fewer units, higher price', 't3')],
    'Slides 24–25: a competitive industry would produce Qc at Pc, where P = MC. The monopolist produces only Qm (where MR = MC) and charges the higher Pm. Pm > MC and Pm > minimum ATC: inefficient.',
    'স্লাইড ২৪–২৫: প্রতিযোগী শিল্প P = MC-তে Pc দামে Qc উৎপাদন করত। একচেটিয়া ফার্ম শুধু Qm (MR = MC যেখানে) উৎপাদন করে, বেশি দাম Pm নেয়। Pm > MC ও Pm > সর্বনিম্ন ATC: অদক্ষ।')
