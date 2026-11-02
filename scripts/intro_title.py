"""Writes intro.md: the website's opening title as an animated SVG.

"Weil Conjectures" in EMS Allure, a single-stroke script (SIL OFL 1.1, a
derivative of Allura), drawn as strokes with a light chalk grain, in a deep
grey.  On the SVG's own clock, which the website starts as the title appears:

  0.0-1.6 s  the title is written, stroke by stroke, at one pen speed;
  1.6-2.2 s  still;
  2.2-3.0 s  a blackboard eraser wipes from right to left, leaving a residue;
  3.0-3.8 s  and back from left to right, wiping every letter but the W, which
             meanwhile turns into the W of the logo;
  3.8-4.8 s  the logo's diagonal is drawn from lower left to upper right; it
             is a mirror, and the part of the Sigma (the W's reflection) on
             the lower left of the perpendicular through its tip shows.

The website then flies the frame marked `data-intro-logo` onto the top bar's
logo (`[site.intro] hold` is the 4.8 s).  Usage, from the repository's root:

  curl -LO https://gitlab.com/inkscape/extensions/-/raw/master/svg_fonts/EMSAllure.svg
  python3 scripts/intro_title.py EMSAllure.svg > intro.md
"""
import math
import re
import sys
import xml.etree.ElementTree as ET

TEXT = "Weil Conjectures"
SIZE = 100  # font size, in the SVG's units
STROKE = 5.5  # the pen, in the SVG's units
COLOR = "color-mix(in srgb, var(--fg) 76%, var(--bg))"  # a deep grey, in either theme

# The logo (site-assets/R1b-W-mirror-sigma-ink.svg), on its 64 x 64 square.
LOGO_W = [(6, 6), (6, 29), (17.5, 17.5), (29, 29), (29, 6)]
LOGO_SIGMA = [(58, 58), (35, 58), (46.5, 46.5), (35, 35), (58, 35)]
LOGO_STROKE, LOGO_DIAG_STROKE = 2.6, 1.3
DIAG = ((4, 60), (60, 4))

# The W of EMS Allure is a swash and a main stroke.  The main stroke's points
# at its top, first valley, peak, second valley and top right, which go to the
# corners of the logo's W; the points after the last curl into it.
W_CORNERS = [0, 10, 20, 28, 35]

T_WRITE, T_STILL = 1.6, 0.6
PEN_LIFT = 0.02  # between two strokes
T_PASS = 0.8  # each pass of the eraser
T_MIRROR = 1.0
RESIDUE = 0.3  # what the first pass leaves

T_E1 = T_WRITE + T_STILL
T_E2 = T_E1 + T_PASS
T_M = T_E2 + T_PASS
T_END = T_M + T_MIRROR

SVG_NS = {"s": "http://www.w3.org/2000/svg"}


def n(x):
    return f"{x:.1f}".rstrip("0").rstrip(".")


def pts(ps):
    return " ".join(f"{n(x)},{n(y)}" for x, y in ps)


def length(ps):
    return sum(math.dist(a, b) for a, b in zip(ps, ps[1:]))


def strokes_of(d):
    out = []
    for cmd, args in re.findall(r"([MLml])([^MLml]*)", d):
        nums = [float(v) for v in re.findall(r"-?[\d.]+(?:e-?\d+)?", args)]
        ps = list(zip(nums[::2], nums[1::2]))
        if cmd in "Mm":
            out.append(ps)
        else:
            out[-1].extend(ps)
    return out


def glyph_strokes(font_path):
    """Each letter of TEXT as its strokes, in the SVG's units (y down)."""
    root = ET.parse(font_path).getroot()
    font = root.find(".//s:font", SVG_NS)
    face = font.find("s:font-face", SVG_NS)
    default = float(font.get("horiz-adv-x", 500))
    glyphs = {g.get("unicode"): g for g in font.findall("s:glyph", SVG_NS)}
    k = SIZE / float(face.get("units-per-em", 1000))
    asc = float(face.get("ascent", 800))
    x, out = 0.0, []
    for ch in TEXT:
        g = glyphs[ch]
        ss = [[(x + px * k, (asc - py) * k) for px, py in s] for s in strokes_of(g.get("d", ""))]
        if ss:
            out.append((ch, ss))
        x += float(g.get("horiz-adv-x", default)) * k
    return out


def along(a, b, f):
    return (a[0] + (b[0] - a[0]) * f, a[1] + (b[1] - a[1]) * f)


def morph_targets(main, logo):
    """Where each point of the W's main stroke goes on the logo's W: the
    points between two corners spread along the logo's side between them as
    they are spread along the stroke."""
    out = []
    for c in range(len(W_CORNERS) - 1):
        seg = main[W_CORNERS[c]:W_CORNERS[c + 1] + 1]
        cum = [0.0]
        for p, q in zip(seg, seg[1:]):
            cum.append(cum[-1] + math.dist(p, q))
        part = [along(logo[c], logo[c + 1], s / cum[-1]) for s in cum]
        out.extend(part if c == 0 else part[1:])
    out.extend(logo[-1] for _ in main[W_CORNERS[-1] + 1:])
    return out


def eraser_path(x0, x1, top, bottom, dx, seed):
    """Back and forth over the letters from x0 to x1, a little uneven."""
    ps, i, step = [], 0, dx if x1 > x0 else -dx
    x = x0
    while (x - x1) * (1 if step > 0 else -1) < dx:
        wob = 6 * math.sin(i * 2.3 + seed)
        ps.append((x + wob, (top if i % 2 == 0 else bottom) + wob))
        x += step
        i += 1
    return "M" + " L".join(f"{n(a)} {n(b)}" for a, b in ps), length(ps)


def main(font_path):
    letters = glyph_strokes(font_path)
    (_, (swash, w_main)), rest = letters[0], letters[1:]
    if len(w_main) <= W_CORNERS[-1]:
        sys.exit("the W is not the one W_CORNERS was read off")

    allpts = [p for _, ss in letters for s in ss for p in s]
    x_min, x_max = min(p[0] for p in allpts), max(p[0] for p in allpts)
    y_min, y_max = min(p[1] for p in allpts), max(p[1] for p in allpts)
    w_top = min(p[1] for p in w_main)
    w_bottom = max(p[1] for p in w_main)
    k = (w_bottom - w_top) / 23  # the logo's W as tall as the font's
    cx, cy = (x_min + x_max) / 2, (w_top + w_bottom) / 2
    lx, ly = cx - 32 * k, cy - 32 * k
    top = min(ly, y_min) - 12
    bottom = max(ly + 64 * k, y_max) + 12
    vb = (x_min - 24, top, x_max - x_min + 48, bottom - top)
    box = f'x="{n(vb[0])}" y="{n(vb[1])}" width="{n(vb[2])}" height="{n(vb[3])}"'
    logo_w = [(lx + k * x, ly + k * y) for x, y in LOGO_W]
    targets = morph_targets(w_main, logo_w)

    # The pen: every stroke at one speed, with a pause as the pen lifts.
    order = [swash, w_main] + [s for _, ss in rest for s in ss]
    total = sum(length(s) for s in order)
    speed = total / (T_WRITE - PEN_LIFT * (len(order) - 1))
    t, timing = 0.0, []
    for s in order:
        d = length(s) / speed
        timing.append((t, d))
        t += d + PEN_LIFT

    def written(s, i, extra=""):
        L = n(length(s) + 1)
        b, d = timing[i]
        return (f'<path d="M{" L".join(f"{n(x)} {n(y)}" for x, y in s)}" stroke-dasharray="{L} {L}" '
                f'stroke-dashoffset="{L}" visibility="hidden"{extra}>'
                f'<set attributeName="visibility" to="visible" begin="{n(b)}s" fill="freeze"/>'
                f'<animate attributeName="stroke-dashoffset" from="{L}" to="0" begin="{n(b)}s" '
                f'dur="{d:.3f}s" fill="freeze"/>')

    rest_paths = "".join(written(s, i + 2) + "</path>" for i, s in enumerate(order[2:]))
    swash_path = (written(swash, 0) + f'<animate attributeName="opacity" from="1" to="0" begin="{n(T_E2)}s" '
                  f'dur="{n(T_PASS * 0.4)}s" fill="freeze"/></path>')
    main_path = (written(w_main, 1) + f'<set attributeName="opacity" to="0" begin="{n(T_E2)}s" '
                 f'fill="freeze"/></path>')

    first_x = min(p[0] for _, ss in rest for s in ss for p in s)
    e1_d, e1_len = eraser_path(x_max + 10, first_x - 6, y_min + 4, y_max - 4, 38, 0.0)
    e2_d, e2_len = eraser_path(first_x - 6, x_max + 10, y_min + 4, y_max - 4, 38, 1.3)

    def eraser(i, d, L, begin):
        e = n(L)
        return (f'<path id="wc-eraser{i}" d="{d}" fill="none" stroke-width="72" stroke-linecap="round" '
                f'stroke-linejoin="round" stroke-dasharray="{e} {e}" stroke-dashoffset="{e}">'
                f'<animate attributeName="stroke-dashoffset" from="{e}" to="0" begin="{n(begin)}s" '
                f'dur="{n(T_PASS)}s" fill="freeze"/></path>')

    def clip(c):
        # Logo coordinates: the half plane x - y <= c, lower left of the
        # perpendicular to the diagonal through its tip.
        return pts([(-200, -200 - c), (200, 200 - c), (-200, 200 - c)])

    ease = 'calcMode="spline" keyTimes="0;1" keySplines=".5 0 .3 1"'
    m, dm = f"{n(T_M)}s", f"{n(T_MIRROR)}s"
    pen = (f'fill="none" stroke="currentColor" stroke-width="{STROKE}" stroke-linecap="round" '
           f'stroke-linejoin="round"')

    svg = f'''<svg class="wc-title" xmlns="http://www.w3.org/2000/svg" viewBox="{" ".join(n(v) for v in vb)}" role="img" aria-label="Weil Conjectures" style="display:block;width:8.2em;max-width:94vw;height:auto;overflow:visible;color:{COLOR}">
<defs>
<filter id="wc-chalk" {box} filterUnits="userSpaceOnUse"><feTurbulence type="fractalNoise" baseFrequency=".8" numOctaves="2" seed="7" result="n"/><feColorMatrix in="n" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -2 1.95" result="g"/><feComposite in="SourceGraphic" in2="g" operator="in"/></filter>
<filter id="wc-rag" {box} filterUnits="userSpaceOnUse"><feTurbulence type="fractalNoise" baseFrequency=".05" numOctaves="2" seed="3" result="t"/><feDisplacementMap in="SourceGraphic" in2="t" scale="22" xChannelSelector="R" yChannelSelector="G"/><feGaussianBlur stdDeviation="3"/></filter>
<filter id="wc-dust-blur" {box} filterUnits="userSpaceOnUse"><feGaussianBlur stdDeviation="5"/></filter>
{eraser(1, e1_d, e1_len, T_E1)}
{eraser(2, e2_d, e2_len, T_E2)}
<mask id="wc-erased" maskUnits="userSpaceOnUse" {box}><rect {box} fill="white"/><use href="#wc-eraser1" stroke="black" stroke-opacity="{1 - RESIDUE}" filter="url(#wc-rag)"/><use href="#wc-eraser2" stroke="black" filter="url(#wc-rag)"/></mask>
<mask id="wc-dust" maskUnits="userSpaceOnUse" {box}><use href="#wc-eraser1" stroke="white" filter="url(#wc-rag)"/><use href="#wc-eraser2" stroke="white" filter="url(#wc-rag)"/></mask>
<clipPath id="wc-mirror" clipPathUnits="userSpaceOnUse"><polygon points="{clip(-56)}"><animate attributeName="points" from="{clip(-56)}" to="{clip(56)}" begin="{m}" dur="{dm}" fill="freeze"/></polygon></clipPath>
<g id="wc-rest" {pen}>{rest_paths}</g>
</defs>
<g filter="url(#wc-chalk)">
<g mask="url(#wc-erased)"><use href="#wc-rest"/></g>
<g mask="url(#wc-dust)" opacity="0"><use href="#wc-rest" filter="url(#wc-dust-blur)"/><animate attributeName="opacity" values="0;.1;.05;.1;0" keyTimes="0;.25;.5;.75;1" begin="{n(T_E1)}s" dur="{n(2 * T_PASS + 0.2)}s" fill="freeze"/></g>
<g {pen}>{swash_path}{main_path}</g>
<polyline points="{pts(w_main)}" {pen} visibility="hidden"><set attributeName="visibility" to="visible" begin="{n(T_E2)}s" fill="freeze"/><animate attributeName="points" from="{pts(w_main)}" to="{pts(targets)}" begin="{n(T_E2)}s" dur="{n(T_PASS)}s" fill="freeze" {ease}/><animate attributeName="stroke-width" from="{STROKE}" to="{n(LOGO_STROKE * k)}" begin="{n(T_E2)}s" dur="{n(T_PASS)}s" fill="freeze" {ease}/></polyline>
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
