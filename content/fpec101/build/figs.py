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
            o.append('<text x="%s" y="238" text-anchor="middle" class="tk">%s</text>' % (f(px(it[1])), it[2]))
        elif k == 'yt':  # tick label on y axis
            o.append('<text x="%s" y="%s" text-anchor="end" class="tk">%s</text>' % (f(X0 - 5), f(py(it[1]) + 4), it[2]))
        elif k == 'ar':
            _, x1, y1, x2, y2 = it[:5]; cls = it[5] if len(it) > 5 else 'l3'
            o.append(arrow(px(x1), py(y1), px(x2), py(y2), cls))
        else:
            raise ValueError(k)
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
