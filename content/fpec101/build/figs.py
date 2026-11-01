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
