#!/usr/bin/env python3
"""Deterministic build of Figure 3 (two denominators) as SVG.

The AI image generator failed this figure three times (see figures_log.md): it drew a
recognisable fetus in place of a blastocyst in twelve locations, and on the final attempt
drew the cumulative bracket spanning only the second and third transfers, excluding the
first, which inverts the meaning of the figure. Drawn deterministically instead.
Hard rule: no numbers, no percentages, no data values anywhere in the output.
"""
import re

INK   = "#22323a"
LINE  = "#37505b"
TEAL  = "#4f8f8f"
TEALL = "#cfe3e2"
SAND  = "#e3c9a3"
SANDL = "#f4e8d5"
PANEL = "#f7fafa"
PANELB= "#9fb9bd"
GREY  = "#5b6b73"
FONT  = "Inter, 'Helvetica Neue', Helvetica, Arial, sans-serif"

out = []
A = out.append


def blastocyst(cx, cy, r):
    """Zona pellucida, trophectoderm rim, eccentric inner cell mass. Never a fetus."""
    return (
        f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{TEALL}" stroke="{LINE}" stroke-width="2.2"/>'
        f'<circle cx="{cx}" cy="{cy}" r="{r-5:.1f}" fill="#ffffff" stroke="{TEAL}" '
        f'stroke-width="1.7" stroke-dasharray="{max(3.0,r*0.15):.1f} {max(2.2,r*0.10):.1f}"/>'
        f'<ellipse cx="{cx-r*0.32:.1f}" cy="{cy-r*0.28:.1f}" rx="{r*0.40:.1f}" '
        f'ry="{r*0.32:.1f}" fill="{TEAL}" stroke="{LINE}" stroke-width="1.4"/>')


def uterus(cx, cy, scale=1.0):
    """Coronal-section uterus at origin, scaled and translated. Catheter transcervical,
    one blastocyst in the cavity."""
    body = ("M -58,-52 C -64,-86 -30,-98 0,-96 C 30,-98 64,-86 58,-52 "
            "C 54,-6 40,28 26,54 C 22,67 -22,67 -26,54 C -40,28 -54,-6 -58,-52 Z")
    cavity = "M -30,-56 C -24,-74 24,-74 30,-56 L 7,42 L -7,42 Z"
    tl = "M -57,-58 C -92,-100 -138,-86 -150,-48"
    tr = "M 57,-58 C 92,-100 138,-86 150,-48"
    g = [f'<g transform="translate({cx},{cy}) scale({scale})">']
    g.append(f'<path d="{tl}" fill="none" stroke="{LINE}" stroke-width="6" stroke-linecap="round"/>')
    g.append(f'<path d="{tr}" fill="none" stroke="{LINE}" stroke-width="6" stroke-linecap="round"/>')
    g.append(f'<path d="{body}" fill="{SAND}" stroke="{LINE}" stroke-width="2.8" stroke-linejoin="round"/>')
    g.append(f'<path d="{cavity}" fill="{SANDL}" stroke="{LINE}" stroke-width="2" stroke-linejoin="round"/>')
    g.append(f'<rect x="-16" y="50" width="32" height="56" rx="9" fill="{SAND}" stroke="{LINE}" stroke-width="2.6"/>')
    for sgn in (-1, 1):
        g.append(f'<ellipse cx="{sgn*158}" cy="-26" rx="26" ry="19" fill="{SANDL}" '
                 f'stroke="{LINE}" stroke-width="2.4"/>')
    g.append(f'<path d="M 0,112 L 0,-16" fill="none" stroke="{GREY}" stroke-width="4.4" stroke-linecap="round"/>')
    g.append(f'<path d="M 0,112 L 0,72" fill="none" stroke="{TEAL}" stroke-width="9.5" stroke-linecap="round"/>')
    g.append(blastocyst(0, -36, 16))
    g.append('</g>')
    return "".join(g)


def bracket(x, y1, y2, w=20):
    """Arms open LEFT, toward the panels being grouped, spine on the right."""
    return (f'<path d="M {x-w},{y1} L {x},{y1} L {x},{y2} L {x-w},{y2}" fill="none" '
            f'stroke="{GREY}" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/>')


def arrow(x1, y1, x2, y2):
    return (f'<path d="M {x1},{y1} L {x2},{y2}" stroke="{LINE}" stroke-width="4.2" '
            f'fill="none" stroke-linecap="round" marker-end="url(#ah)"/>')


def label(x, y, txt, size=24, weight=500, anchor="middle", fill=INK):
    return (f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" '
            f'font-weight="{weight}" text-anchor="{anchor}" fill="{fill}">{txt}</text>')


W, H = 1700, 800
A(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
  f'role="img" aria-label="Per-transfer and cumulative denominators after one oocyte retrieval">')
A(f'<defs><marker id="ah" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="6.5" '
  f'markerHeight="6.5" orient="auto-start-reverse">'
  f'<path d="M 0 0 L 10 5 L 0 10 z" fill="{LINE}"/></marker></defs>')
A(f'<rect width="{W}" height="{H}" fill="#ffffff"/>')

# ---- cohort from one retrieval --------------------------------------------
A(f'<rect x="50" y="250" width="352" height="300" rx="20" fill="{PANEL}" stroke="{PANELB}" stroke-width="2.4"/>')
A(label(226, 300, "One oocyte retrieval", 25, 600))
for i, bx in enumerate((122, 226, 330)):
    for by in (386, 478):
        A(blastocyst(bx, by, 35))

# ---- trunk and branches ----------------------------------------------------
CENTRES = (140, 400, 660)
A(f'<path d="M 402,400 L 452,400" stroke="{LINE}" stroke-width="4.2" stroke-linecap="round"/>')
A(f'<path d="M 452,{CENTRES[0]} L 452,{CENTRES[2]}" stroke="{LINE}" stroke-width="4.2" stroke-linecap="round"/>')
for cy in CENTRES:
    A(arrow(452, cy, 508, cy))

# ---- three transfer panels -------------------------------------------------
BOX_X, BOX_W, BOX_H = 520, 640, 210
NAMES = ("First transfer", "Second transfer", "Third transfer")
for cy, name in zip(CENTRES, NAMES):
    top = cy - BOX_H // 2
    A(f'<rect x="{BOX_X}" y="{top}" width="{BOX_W}" height="{BOX_H}" rx="18" '
      f'fill="{PANEL}" stroke="{PANELB}" stroke-width="2.4"/>')
    A(blastocyst(608, cy, 42))
    A(label(700, cy + 9, name, 25, 600, "start"))
    A(uterus(1020, cy - 4, scale=0.60))

# sequence arrows between panels
for a, b in ((CENTRES[0], CENTRES[1]), (CENTRES[1], CENTRES[2])):
    A(arrow(840, a + BOX_H // 2 + 4, 840, b - BOX_H // 2 - 8))

# ---- the two denominators --------------------------------------------------
top1, bot1 = CENTRES[0] - BOX_H // 2, CENTRES[0] + BOX_H // 2
topA, botA = CENTRES[0] - BOX_H // 2, CENTRES[2] + BOX_H // 2

A(bracket(1196, top1, bot1))
A(label(1226, CENTRES[0] - 6, "Per transfer", 25, 600, "start"))
A(label(1226, CENTRES[0] + 26, "outcome", 25, 600, "start"))

A(bracket(1432, topA, botA))
A(label(1462, 390, "Cumulative", 25, 600, "start"))
A(label(1462, 422, "outcome", 25, 600, "start"))

A('</svg>')

svg = "\n".join(out)
open("fig3.svg", "w").write(svg)
open("fig3_wrapper.html", "w").write(
    f'<html><body style="margin:0;background:#fff">{svg}</body></html>')
print(f"fig3.svg written ({len(svg)} bytes)")

# assert the hard rule, and assert the bracket spans
texts = re.findall(r'<text[^>]*>([^<]*)</text>', svg)
bad = [t for t in texts if re.search(r'\d|%', t)]
print("rendered labels:", texts)
print("LABELS CONTAINING A DIGIT OR PERCENT:", bad if bad else "none - hard rule satisfied")
assert top1 == CENTRES[0] - BOX_H // 2 and bot1 == CENTRES[0] + BOX_H // 2
assert topA <= CENTRES[0] - BOX_H // 2 and botA >= CENTRES[2] + BOX_H // 2
print(f"per-transfer bracket spans y {top1}-{bot1} (first panel only)")
print(f"cumulative bracket spans y {topA}-{botA} (ALL THREE panels: "
      f"{CENTRES[0]-BOX_H//2} to {CENTRES[2]+BOX_H//2})")
