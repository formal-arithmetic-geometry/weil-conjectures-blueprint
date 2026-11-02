"""Writes intro.md: the website's opening title as an animated SVG.

"Weil Conjectures" in Naija Easy Handwritting, its glyphs drawn as paths with
a light chalk grain, in a deep grey.  The font is an outline font, so the
pen is found by thinning each glyph to its skeleton: a mask drawn along the
skeleton, at one pen speed, reveals the glyph as it is written.  On the SVG's
own clock, which the website starts as the title appears:

  0.00-1.60 s  the title is written, stroke by stroke;
  1.60-2.20 s  still;
  2.20-3.00 s  a blackboard eraser wipes from right to left, all but the tops
               of the letters on the left, as an eraser leaves them;
  3.00-3.80 s  and from left to right over those tops, wiping them too, while
               the W turns into the W of the logo;
  3.80-4.55 s  the logo's diagonal is drawn from lower left to upper right; it
               is a mirror, and the part of the Sigma (the W's reflection) on
               the lower left of the perpendicular through its tip shows.

The website then flies the frame marked `data-intro-logo` onto the top bar's
logo (`[site.intro] hold` is the 4.55 s).  Usage, from the repository's root,
with the font file beside it:

  nix-shell -p "python3.withPackages (ps: with ps; [ fonttools numpy scikit-image ])" \\
    --run "python3 scripts/intro_title.py 'Naija Easy Handwritting Regular.ttf' > intro.md"
"""
import math
import sys

import numpy as np
from fontTools.pens.basePen import BasePen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from scipy import ndimage
from skimage.draw import polygon as fill_polygon
from skimage.morphology import skeletonize

TEXT = "Weil Conjectures"
SIZE = 100  # font size, in the SVG's units
RES = 8  # raster pixels per unit, for the skeletons
COLOR = "color-mix(in srgb, var(--fg) 76%, var(--bg))"  # a deep grey, in either theme

# The logo (site-assets/R1b-W-mirror-sigma-ink.svg), on its 64 x 64 square.
LOGO_W = [(6, 6), (6, 29), (17.5, 17.5), (29, 29), (29, 6)]
LOGO_SIGMA = [(58, 58), (35, 58), (46.5, 46.5), (35, 35), (58, 35)]
LOGO_STROKE, LOGO_DIAG_STROKE = 2.6, 1.3
DIAG = ((4, 60), (60, 4))

T_WRITE, T_STILL = 1.6, 0.6
PEN_LIFT = 0.02  # between two strokes
T_PASS = 0.8  # each pass of the eraser
T_MIRROR = 0.75
LEFT_SHARE = 0.45  # of the letters after the W, where the first pass leaves the tops
TOP_LEFT = 40  # above this the first pass leaves the letters there (SVG units)

T_E1 = T_WRITE + T_STILL
T_E2 = T_E1 + T_PASS
T_M = T_E2 + T_PASS
T_END = T_M + T_MIRROR


def n(x):
    return f"{x:.1f}".rstrip("0").rstrip(".")


def pts(ps):
    return " ".join(f"{n(x)},{n(y)}" for x, y in ps)


def poly_d(ps):
    return "M" + " L".join(f"{n(x)} {n(y)}" for x, y in ps)


def length(ps):
    return sum(math.dist(a, b) for a, b in zip(ps, ps[1:]))


class FlatPen(BasePen):
    """The glyph's contours as polygons, curves cut into short lines."""

    def __init__(self, glyphset):
        super().__init__(glyphset)
        self.contours, self.cur = [], None

    def _moveTo(self, p):
        self.cur = [p]
        self.contours.append(self.cur)

    def _lineTo(self, p):
        self.cur.append(p)

    def _qCurveToOne(self, p1, p2):
        p0 = self.cur[-1]
        for i in range(1, 13):
            t = i / 12
            self.cur.append(tuple((1 - t) ** 2 * a + 2 * (1 - t) * t * b + t * t * c
                                  for a, b, c in zip(p0, p1, p2)))

    def _curveToOne(self, p1, p2, p3):
        p0 = self.cur[-1]
        for i in range(1, 17):
            t = i / 16
            self.cur.append(tuple((1 - t) ** 3 * a + 3 * (1 - t) ** 2 * t * b + 3 * (1 - t) * t * t * c
                                  + t ** 3 * d for a, b, c, d in zip(p0, p1, p2, p3)))


def glyphs(font_path):
    """Each letter of TEXT: its path and contours, in the SVG's units (y down)."""
    f = TTFont(font_path)
    gs, cmap = f.getGlyphSet(), f.getBestCmap()
    k = SIZE / f["head"].unitsPerEm
    asc = f["hhea"].ascent * k
    x, out = 0.0, []
    for ch in TEXT:
        g = gs[cmap[ord(ch)]]
        tr = (k, 0, 0, -k, x, asc)
        pen = SVGPathPen(gs, ntos=n)
        g.draw(TransformPen(pen, tr))
        flat = FlatPen(gs)
        g.draw(TransformPen(flat, tr))
        if flat.contours:
            out.append((ch, pen.getCommands(), flat.contours))
        x += g.width * k
    return out


# ---------------------------------------------------------------- skeletons


def raster(contours):
    xs = [p[0] for c in contours for p in c]
    ys = [p[1] for c in contours for p in c]
    x0, y0 = min(xs) - 2, min(ys) - 2
    w = int((max(xs) - x0 + 2) * RES) + 1
    h = int((max(ys) - y0 + 2) * RES) + 1
    img = np.zeros((h, w), bool)
    for c in contours:  # even-odd: a counter is a contour inside another
        rr, cc = fill_polygon([(p[1] - y0) * RES for p in c], [(p[0] - x0) * RES for p in c], (h, w))
        img[rr, cc] ^= True
    return img, x0, y0


NEIGH = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def skeleton_graph(skel):
    """The skeleton as nodes (ends and junctions, each a cluster of pixels)
    and edges (pixel paths between two nodes)."""
    on = set(zip(*np.nonzero(skel)))

    def nbrs(p):
        return [(p[0] + a, p[1] + b) for a, b in NEIGH if (p[0] + a, p[1] + b) in on]

    special = {p for p in on if len(nbrs(p)) != 2}
    node_of, nodes = {}, []
    for p in special:  # touching junction pixels are one junction
        if p in node_of:
            continue
        stack, members = [p], []
        node_of[p] = len(nodes)
        while stack:
            q = stack.pop()
            members.append(q)
            for r in nbrs(q):
                if r in special and r not in node_of:
                    node_of[r] = len(nodes)
                    stack.append(r)
        nodes.append(members)
    edges, seen = [], set()
    for i, members in enumerate(nodes):
        for p in members:
            for q in nbrs(p):
                if q in node_of or (p, q) in seen:
                    continue
                path, prev, cur = [p, q], p, q
                seen.add((p, q))
                while cur not in node_of:
                    nxt = [r for r in nbrs(cur) if r != prev and r not in path[-3:]]
                    if not nxt:
                        break
                    prev, cur = cur, nxt[0]
                    path.append(cur)
                if cur in node_of:
                    seen.add((cur, path[-2]))
                    edges.append((i, node_of[cur], path))
    # A ring without ends or junctions (an o): cut it at its top.
    covered = {p for _, _, path in edges for p in path} | special
    rest = on - covered
    while rest:
        start = min(rest)
        path, prev, cur = [start], None, start
        while True:
            nxt = [r for r in nbrs(cur) if r != prev and r in rest and r not in path]
            if not nxt:
                break
            prev, cur = cur, nxt[0]
            path.append(cur)
        path.append(start)
        nodes.append([start])
        edges.append((len(nodes) - 1, len(nodes) - 1, path))
        rest -= set(path)
    return nodes, edges


def rdp(ps, eps):
    if len(ps) < 3:
        return ps
    if len(ps) > 4 and math.dist(ps[0], ps[-1]) < 1:  # a loop: in two halves
        h = len(ps) // 2
        return rdp(ps[:h + 1], eps)[:-1] + rdp(ps[h:], eps)
    a, b = np.array(ps[0], float), np.array(ps[-1], float)
    ab = b - a
    nrm = np.hypot(*ab) or 1.0
    d = [abs(ab[0] * (p[1] - a[1]) - ab[1] * (p[0] - a[0])) / nrm for p in ps[1:-1]]
    i = int(np.argmax(d)) + 1
    if d[i - 1] > eps:
        return rdp(ps[:i + 1], eps)[:-1] + rdp(ps[i:], eps)
    return [ps[0], ps[-1]]


def pen_strokes(contours):
    """The strokes a pen draws the glyph with, in order, and the pen's width
    that covers the glyph along them (SVG units)."""
    img, x0, y0 = raster(contours)
    dist = ndimage.distance_transform_edt(img)
    skel = skeletonize(img)
    radius = dist[skel].max() if skel.any() else 1.0
    labels, count = ndimage.label(skel, structure=np.ones((3, 3)))
    # The parts of the glyph, the largest first: a dot comes last.
    parts = sorted(range(1, count + 1), key=lambda i: -(labels == i).sum())
    strokes = []
    for i in parts:
        strokes += walk(labels == i, x0, y0, radius)
    # A stroke starts at its upper left end.
    key = lambda p: p[0] + 0.3 * p[1]  # noqa: E731
    strokes = [s[::-1] if key(s[-1]) < key(s[0]) - 10 else s for s in strokes]
    strokes = [rdp(s, 0.25) for s in strokes if length(s) > 0.5]
    return strokes, 2 * radius / RES + 1.5


def walk(skel, x0, y0, radius):
    """The strokes along one connected part of the skeleton."""
    nodes, edges = skeleton_graph(skel)
    deg = {}
    for a, b, _ in edges:
        deg[a] = deg.get(a, 0) + 1
        deg[b] = deg.get(b, 0) + 1
    # Spurs of the thinning: short edges to an end.
    edges = [e for e in edges if not (len(e[2]) < radius * 1.3 and (deg[e[0]] == 1 or deg[e[1]] == 1)
                                      and len(edges) > 1)]
    to_xy = lambda p: (x0 + p[1] / RES, y0 + p[0] / RES)  # noqa: E731
    centre = [tuple(np.mean([to_xy(p) for p in m], axis=0)) for m in nodes]
    used = [False] * len(edges)
    strokes, cur_node, cur = [], None, None

    def ends_of(i):
        return [e for e in range(len(edges)) if not used[e] and i in edges[e][:2]]

    while not all(used):
        if cur is None:
            free = {i for e, (a, b, _) in enumerate(edges) if not used[e] for i in (a, b)}
            ends = [i for i in free if len(ends_of(i)) == 1] or list(free)
            pos = strokes[-1][-1] if strokes else (-1e9, -1e9)
            # The next stroke: from the end nearest the pen, the first from the left top.
            cur_node = min(ends, key=lambda i: (math.dist(centre[i], pos) if strokes else
                                                centre[i][0] + 0.3 * centre[i][1]))
            cur = [centre[cur_node]]
        options = ends_of(cur_node)
        if not options:
            strokes.append(cur)
            cur = None
            continue
        if len(cur) > 1:
            dx, dy = cur[-1][0] - cur[-2][0], cur[-1][1] - cur[-2][1]

            def turn(e):
                a, b, path = edges[e]
                q = path if a == cur_node else path[::-1]
                p = to_xy(q[min(len(q) - 1, 6)])
                ex, ey = p[0] - cur[-1][0], p[1] - cur[-1][1]
                return -(dx * ex + dy * ey) / ((math.hypot(dx, dy) * math.hypot(ex, ey)) or 1)
            options.sort(key=turn)
        e = options[0]
        used[e] = True
        a, b, path = edges[e]
        q = path if a == cur_node else path[::-1]
        cur.extend(to_xy(p) for p in q[1:])
        cur.append(centre[b if a == cur_node else a])
        cur_node = b if a == cur_node else a
    if cur:
        strokes.append(cur)
    return strokes


# ---------------------------------------------------------------- the W


def along(a, b, f):
    return (a[0] + (b[0] - a[0]) * f, a[1] + (b[1] - a[1]) * f)


def resample(ps, step):
    out = [ps[0]]
    for a, b in zip(ps, ps[1:]):
        d = math.dist(a, b)
        for i in range(1, max(1, int(d / step)) + 1):
            out.append(along(a, b, i / max(1, int(d / step))))
    return out


def w_corners(main):
    """The points of the W's stroke at its top left, first valley, peak,
    second valley and top right."""
    ys = [p[1] for p in main]
    m = len(main)
    i1 = max(range(0, m // 2), key=lambda i: ys[i])
    i3 = max(range(m // 2, m), key=lambda i: ys[i])
    i2 = min(range(i1, i3 + 1), key=lambda i: ys[i])
    return [0, i1, i2, i3, m - 1]


def morph_targets(main, corners, logo):
    out = []
    for c in range(4):
        seg = main[corners[c]:corners[c + 1] + 1]
        cum = [0.0]
        for p, q in zip(seg, seg[1:]):
            cum.append(cum[-1] + math.dist(p, q))
        part = [along(logo[c], logo[c + 1], s / (cum[-1] or 1)) for s in cum]
        out.extend(part if c == 0 else part[1:])
    return out


# ---------------------------------------------------------------- the eraser


def zigzag(x0, x1, top, bottom, dx, seed):
    """Back and forth from x0 to x1; `top(x)` and `bottom(x)` bound it."""
    ps, i, step, x = [], 0, dx if x1 > x0 else -dx, x0
    while (x - x1) * (1 if step > 0 else -1) < dx:
        wob = 5 * math.sin(i * 2.3 + seed)
        ps.append((x + wob, (top(x) if i % 2 == 0 else bottom(x)) + wob))
        x += step
        i += 1
    return ps


def main(font_path):
    letters = glyphs(font_path)
    (w_ch, w_d, w_contours), rest = letters[0], letters[1:]
    if w_ch != "W":
        sys.exit("the title must start with its W")

    allpts = [p for _, _, cs in letters for c in cs for p in c]
    x_min, x_max = min(p[0] for p in allpts), max(p[0] for p in allpts)
    y_min, y_max = min(p[1] for p in allpts), max(p[1] for p in allpts)

    # The pen: each letter's strokes, at one speed for the whole title.
    pens = [pen_strokes(cs) for _, _, cs in letters]
    order = [(li, s) for li, (ss, _) in enumerate(pens) for s in ss]
    total = sum(length(s) for _, s in order)
    speed = total / (T_WRITE - PEN_LIFT * (len(order) - 1))
    t, timing = 0.0, []
    for _, s in order:
        timing.append((t, length(s) / speed))
        t += length(s) / speed + PEN_LIFT

    w_strokes, w_width = pens[0]
    main = max(w_strokes, key=length)
    main = resample(main, 1.2)
    corners = w_corners(main)
    w_top = min(p[1] for c in w_contours for p in c)
    w_bottom = max(p[1] for c in w_contours for p in c)
    k = (w_bottom - w_top) / 23  # the logo's W as tall as the font's
    cx, cy = (x_min + x_max) / 2, (w_top + w_bottom) / 2
    lx, ly = cx - 32 * k, cy - 32 * k
    top = min(ly, y_min) - 12
    bottom = max(ly + 64 * k, y_max) + 12
    vb = (x_min - 24, top, x_max - x_min + 48, bottom - top)
    box = f'x="{n(vb[0])}" y="{n(vb[1])}" width="{n(vb[2])}" height="{n(vb[3])}"'
    logo_w = [(lx + k * x, ly + k * y) for x, y in LOGO_W]
    targets = morph_targets(main, corners, logo_w)
    w_line = max(3.0, w_width * 0.55)  # the W's stroke as one line

    # Each letter, revealed through its own mask as its strokes are written.
    masks, bodies = [], []
    for li, ((ch, d, _), (strokes, width)) in enumerate(zip(letters, pens)):
        lines = []
        for (lj, s), (b, dur) in zip(order, timing):
            if lj != li:
                continue
            L = n(length(s) + width)
            lines.append(f'<path d="{poly_d(s)}" stroke-dasharray="{L} {L}" stroke-dashoffset="{L}">'
                         f'<animate attributeName="stroke-dashoffset" from="{L}" to="0" begin="{b:.3f}s" '
                         f'dur="{dur:.3f}s" fill="freeze"/></path>')
        masks.append(f'<mask id="wc-pen{li}" maskUnits="userSpaceOnUse" {box}><g fill="none" stroke="white" '
                     f'stroke-width="{n(width)}" stroke-linecap="round" stroke-linejoin="round">'
                     f'{"".join(lines)}</g></mask>')
        bodies.append(f'<path d="{d}" mask="url(#wc-pen{li})"/>')
    w_body, rest_bodies = bodies[0], "".join(bodies[1:])

    # The eraser.  First right to left over everything but the tops of the
    # letters on the left; then left to right over those tops.
    first_x = min(p[0] for _, _, cs in rest for c in cs for p in c)
    split = first_x + LEFT_SHARE * (x_max - first_x)
    band = 70
    ramp = lambda x: min(1.0, max(0.0, (x - split) / 60))  # noqa: E731
    low_top = TOP_LEFT + band / 2  # the band's top edge at TOP_LEFT
    e1 = zigzag(x_max + 10, first_x - 6,
                lambda x: low_top + (y_min + 6 - low_top) * ramp(x), lambda x: y_max - 6, 34, 0.0)
    e2 = zigzag(first_x - 6, split + 40, lambda x: y_min - 2, lambda x: TOP_LEFT + 14, 30, 1.3)

    def eraser(i, ps, width, begin):
        e = n(length(ps))
        return (f'<path id="wc-eraser{i}" d="{poly_d(ps)}" fill="none" stroke-width="{width}" '
                f'stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="{e} {e}" '
                f'stroke-dashoffset="{e}"><animate attributeName="stroke-dashoffset" from="{e}" to="0" '
                f'begin="{n(begin)}s" dur="{n(T_PASS)}s" fill="freeze"/></path>')

    def clip(c):
        # Logo coordinates: the half plane x - y <= c, lower left of the
        # perpendicular to the diagonal through its tip.
        return pts([(-200, -200 - c), (200, 200 - c), (-200, 200 - c)])

    ease = 'calcMode="spline" keyTimes="0;1" keySplines=".5 0 .3 1"'
    m, dm = f"{n(T_M)}s", f"{T_MIRROR}s"
    e2s = f"{n(T_E2)}s"

    svg = f'''<svg class="wc-title" xmlns="http://www.w3.org/2000/svg" viewBox="{" ".join(n(v) for v in vb)}" role="img" aria-label="Weil Conjectures" style="display:block;width:8.2em;max-width:94vw;height:auto;overflow:visible;color:{COLOR}" fill="currentColor">
<defs>
<filter id="wc-chalk" {box} filterUnits="userSpaceOnUse"><feTurbulence type="fractalNoise" baseFrequency=".8" numOctaves="2" seed="7" result="n"/><feColorMatrix in="n" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -2 1.95" result="g"/><feComposite in="SourceGraphic" in2="g" operator="in"/></filter>
<filter id="wc-rag" {box} filterUnits="userSpaceOnUse"><feTurbulence type="fractalNoise" baseFrequency=".05" numOctaves="2" seed="3" result="t"/><feDisplacementMap in="SourceGraphic" in2="t" scale="18" xChannelSelector="R" yChannelSelector="G"/><feGaussianBlur stdDeviation="2.5"/></filter>
<filter id="wc-dust-blur" {box} filterUnits="userSpaceOnUse"><feGaussianBlur stdDeviation="5"/></filter>
{"".join(masks)}
{eraser(1, e1, band, T_E1)}
{eraser(2, e2, 46, T_E2)}
<mask id="wc-erased" maskUnits="userSpaceOnUse" {box}><rect {box} fill="white"/><use href="#wc-eraser1" stroke="black" filter="url(#wc-rag)"/><use href="#wc-eraser2" stroke="black" filter="url(#wc-rag)"/></mask>
<mask id="wc-dust" maskUnits="userSpaceOnUse" {box}><use href="#wc-eraser1" stroke="white" filter="url(#wc-rag)"/><use href="#wc-eraser2" stroke="white" filter="url(#wc-rag)"/></mask>
<clipPath id="wc-mirror" clipPathUnits="userSpaceOnUse"><polygon points="{clip(-56)}"><animate attributeName="points" from="{clip(-56)}" to="{clip(56)}" begin="{m}" dur="{dm}" fill="freeze"/></polygon></clipPath>
<g id="wc-rest">{rest_bodies}</g>
</defs>
<g filter="url(#wc-chalk)">
<g mask="url(#wc-erased)"><use href="#wc-rest"/></g>
<g mask="url(#wc-dust)" opacity="0"><use href="#wc-rest" filter="url(#wc-dust-blur)"/><animate attributeName="opacity" values="0;.05;.03;.05;0" keyTimes="0;.25;.5;.75;1" begin="{n(T_E1)}s" dur="{n(2 * T_PASS + 0.2)}s" fill="freeze"/></g>
<g>{w_body}<animate attributeName="opacity" from="1" to="0" begin="{e2s}" dur=".15s" fill="freeze"/></g>
<polyline points="{pts(main)}" fill="none" stroke="currentColor" stroke-width="{n(w_line)}" stroke-linecap="round" stroke-linejoin="round" opacity="0"><animate attributeName="opacity" from="0" to="1" begin="{e2s}" dur=".15s" fill="freeze"/><animate attributeName="points" from="{pts(main)}" to="{pts(targets)}" begin="{e2s}" dur="{n(T_PASS)}s" fill="freeze" {ease}/><animate attributeName="stroke-width" from="{n(w_line)}" to="{n(LOGO_STROKE * k)}" begin="{e2s}" dur="{n(T_PASS)}s" fill="freeze" {ease}/></polyline>
<g transform="translate({n(lx)} {n(ly)}) scale({n(k)})" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
<rect data-intro-logo="" width="64" height="64" stroke="none"/>
<line x1="{DIAG[0][0]}" y1="{DIAG[0][1]}" x2="{DIAG[0][0]}" y2="{DIAG[0][1]}" stroke-width="{LOGO_DIAG_STROKE}" visibility="hidden"><set attributeName="visibility" to="visible" begin="{m}" fill="freeze"/><animate attributeName="x2" from="{DIAG[0][0]}" to="{DIAG[1][0]}" begin="{m}" dur="{dm}" fill="freeze"/><animate attributeName="y2" from="{DIAG[0][1]}" to="{DIAG[1][1]}" begin="{m}" dur="{dm}" fill="freeze"/></line>
<polyline points="{pts(LOGO_SIGMA)}" stroke-width="{LOGO_STROKE}" clip-path="url(#wc-mirror)"/>
</g>
</g>
</svg>'''
    # One HTML block for Markdown: no blank line inside.
    print("\n".join(line for line in svg.splitlines() if line.strip()))


if __name__ == "__main__":
    main(sys.argv[1])
