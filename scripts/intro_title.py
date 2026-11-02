"""Writes intro.md: the website's opening title as an animated SVG.

"Weil Conjectures" in Architects Daughter (SIL OFL 1.1), as paths.  On the
SVG's own clock, which the website starts once the title has grown in:

  0.0-0.5 s  still;
  0.5-1.3 s  a blackboard eraser wipes every letter but the W, leaving chalk
             dust that fades, while the W turns into the W of the logo;
  1.3-1.8 s  the logo's diagonal is drawn from lower left to upper right; it
             is a mirror, and the part of the Sigma (the W's reflection) on
             the lower left of the perpendicular through its tip shows.

The website then flies the frame marked `data-intro-logo` onto the top bar's
logo (`[site.intro] hold` is the 1.8 s).  Usage, from the repository's root:

  curl -LO https://raw.githubusercontent.com/google/fonts/main/ofl/architectsdaughter/ArchitectsDaughter-Regular.ttf
  nix-shell -p python3Packages.fonttools --run \
    "python3 scripts/intro_title.py ArchitectsDaughter-Regular.ttf > intro.md"
"""
import math
import sys

from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

TEXT = "Weil Conjectures"
SIZE = 100  # font size, in the SVG's units

# The logo (site-assets/R1b-W-mirror-sigma-ink.svg), on its 64 x 64 square.
LOGO_W = [(6, 6), (6, 29), (17.5, 17.5), (29, 29), (29, 6)]
LOGO_SIGMA = [(58, 58), (35, 58), (46.5, 46.5), (35, 35), (58, 35)]
LOGO_STROKE, LOGO_DIAG_STROKE = 2.6, 1.3
DIAG = ((4, 60), (60, 4))

# The W of the font, as the five points of its stroke, and the stroke's width
# (read off the glyph at SIZE 100).
GLYPH_W = [(6, 41), (28.5, 94), (47.5, 49), (75.5, 94), (87, 28)]
GLYPH_STROKE = 6.4

K = 3  # the logo's scale in the title: its W about as tall as the font's

T_ERASE, T_MIRROR, T_END = 0.5, 1.3, 1.8


def n(x):
    return f"{x:.1f}".rstrip("0").rstrip(".")


def pts(ps):
    return " ".join(f"{n(x)},{n(y)}" for x, y in ps)


def glyph_paths(font_path):
    f = TTFont(font_path)
    gs, cmap = f.getGlyphSet(), f.getBestCmap()
    k = SIZE / f["head"].unitsPerEm
    asc = f["hhea"].ascent * k
    x, out = 0.0, []
    for ch in TEXT:
        g = gs[cmap[ord(ch)]]
        pen = SVGPathPen(gs, ntos=n)
        g.draw(TransformPen(pen, (k, 0, 0, -k, x, asc)))
        bp = BoundsPen(gs)
        g.draw(TransformPen(bp, (k, 0, 0, -k, x, asc)))
        if bp.bounds:
            out.append((ch, pen.getCommands()))
        x += g.width * k
    return out, x


def eraser_path(x0, x1, top, bottom, dx):
    """Back and forth over the letters, left to right, a little uneven."""
    ps, x, i = [], x0, 0
    while x < x1 + dx:
        wob = 6 * math.sin(i * 2.3)
        ps.append((x + wob, (top if i % 2 == 0 else bottom) + wob))
        x += dx
        i += 1
    length = sum(math.dist(a, b) for a, b in zip(ps, ps[1:]))
    return "M" + " L".join(f"{n(a)} {n(b)}" for a, b in ps), length


def main(font_path):
    glyphs, width = glyph_paths(font_path)
    w_glyph = glyphs[0][1]
    rest = "".join(f'<path d="{d}"/>' for _, d in glyphs[1:])

    cx, cy = width / 2, 66  # the middle of the letters' bodies
    lx, ly = cx - 32 * K, cy - 32 * K  # the logo's square
    vb = (-20, ly - 10, width + 40, 64 * K + 20)
    logo_w = [(lx + K * x, ly + K * y) for x, y in LOGO_W]

    erase_d, erase_len = eraser_path(96, width - 6, 18, 138, 40)
    e = n(erase_len)

    def clip(c):
        # Logo coordinates: the half plane x - y <= c, lower left of the
        # perpendicular to the diagonal through its tip.
        return pts([(-200, -200 - c), (200, 200 - c), (-200, 200 - c)])

    mirror = f"{T_MIRROR}s"
    erase = f"{T_ERASE}s"
    dur_e = f"{n(T_MIRROR - T_ERASE)}s"
    dur_m = f"{n(T_END - T_MIRROR)}s"
    ease = 'calcMode="spline" keyTimes="0;1" keySplines=".6 0 .3 1"'
    box = f'x="{n(vb[0])}" y="{n(vb[1])}" width="{n(vb[2])}" height="{n(vb[3])}"'

    svg = f'''<svg class="wc-title" xmlns="http://www.w3.org/2000/svg" viewBox="{" ".join(n(v) for v in vb)}" role="img" aria-label="Weil Conjectures" style="display:block;width:8.6em;max-width:94vw;height:auto;overflow:visible" fill="currentColor">
<defs>
<filter id="wc-chalk" x="-2%" y="-10%" width="104%" height="120%"><feTurbulence type="fractalNoise" baseFrequency=".8" numOctaves="2" seed="7" result="n"/><feColorMatrix in="n" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -2.2 1.95" result="g"/><feComposite in="SourceGraphic" in2="g" operator="in"/></filter>
<filter id="wc-rag" {box} filterUnits="userSpaceOnUse"><feTurbulence type="fractalNoise" baseFrequency=".05" numOctaves="2" seed="3" result="t"/><feDisplacementMap in="SourceGraphic" in2="t" scale="22" xChannelSelector="R" yChannelSelector="G"/><feGaussianBlur stdDeviation="3"/></filter>
<filter id="wc-dust-blur" {box} filterUnits="userSpaceOnUse"><feGaussianBlur stdDeviation="5"/></filter>
<path id="wc-eraser" d="{erase_d}" fill="none" stroke-width="74" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="{e} {e}" stroke-dashoffset="{e}"><animate attributeName="stroke-dashoffset" from="{e}" to="0" begin="{erase}" dur="{dur_e}" fill="freeze"/></path>
<mask id="wc-erased" maskUnits="userSpaceOnUse" {box}><rect {box} fill="white"/><use href="#wc-eraser" stroke="black" filter="url(#wc-rag)"/></mask>
<mask id="wc-dust" maskUnits="userSpaceOnUse" {box}><use href="#wc-eraser" stroke="white" filter="url(#wc-rag)"/></mask>
<clipPath id="wc-mirror" clipPathUnits="userSpaceOnUse"><polygon points="{clip(-56)}"><animate attributeName="points" from="{clip(-56)}" to="{clip(56)}" begin="{mirror}" dur="{dur_m}" fill="freeze"/></polygon></clipPath>
<g id="wc-rest">{rest}</g>
</defs>
<g filter="url(#wc-chalk)">
<g mask="url(#wc-erased)"><use href="#wc-rest"/></g>
<path d="{w_glyph}"><animate attributeName="opacity" values="1;0" keyTimes="0;1" begin="{erase}" dur=".12s" fill="freeze"/></path>
</g>
<g mask="url(#wc-dust)" opacity="0"><use href="#wc-rest" filter="url(#wc-dust-blur)"/><animate attributeName="opacity" values="0;.1;0" keyTimes="0;.6;1" begin="{erase}" dur="{n(T_MIRROR - T_ERASE + 0.15)}s" fill="freeze"/></g>
<polyline points="{pts(GLYPH_W)}" fill="none" stroke="currentColor" stroke-width="{GLYPH_STROKE}" stroke-linecap="round" stroke-linejoin="round" opacity="0"><set attributeName="opacity" to="1" begin="{erase}" fill="freeze"/><animate attributeName="points" from="{pts(GLYPH_W)}" to="{pts(logo_w)}" begin="{erase}" dur="{dur_e}" fill="freeze" {ease}/><animate attributeName="stroke-width" from="{GLYPH_STROKE}" to="{n(LOGO_STROKE * K)}" begin="{erase}" dur="{dur_e}" fill="freeze" {ease}/></polyline>
<g transform="translate({n(lx)} {n(ly)}) scale({K})" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
<rect data-intro-logo="" width="64" height="64" stroke="none"/>
<line x1="{DIAG[0][0]}" y1="{DIAG[0][1]}" x2="{DIAG[0][0]}" y2="{DIAG[0][1]}" stroke-width="{LOGO_DIAG_STROKE}" visibility="hidden"><set attributeName="visibility" to="visible" begin="{mirror}" fill="freeze"/><animate attributeName="x2" from="{DIAG[0][0]}" to="{DIAG[1][0]}" begin="{mirror}" dur="{dur_m}" fill="freeze"/><animate attributeName="y2" from="{DIAG[0][1]}" to="{DIAG[1][1]}" begin="{mirror}" dur="{dur_m}" fill="freeze"/></line>
<polyline points="{pts(LOGO_SIGMA)}" stroke-width="{LOGO_STROKE}" clip-path="url(#wc-mirror)"/>
</g>
</svg>'''
    # One HTML block for Markdown: no blank line inside.
    print("\n".join(line for line in svg.splitlines() if line.strip()))


if __name__ == "__main__":
    main(sys.argv[1])
