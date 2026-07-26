#!/usr/bin/env python3
"""Deterministic build of Figure 1 (two pathways) as SVG.

The AI image generator failed this figure three times (see figures_log.md), so it is
drawn here instead, where every label is written by hand and cannot be garbled.
Hard rule: no numbers, no percentages, no data values anywhere in the output.
"""
import re

INK   = "#22323a"
LINE  = "#37505b"
TEAL  = "#4f8f8f"
TEALL = "#cfe3e2"
SAND  = "#e3c9a3"
SANDL = "#f4e8d5"
PANEL = "#f3f7f7"
PANELB= "#dae6e6"
GREY  = "#5b6b73"
FONT  = "Inter, 'Helvetica Neue', Helvetica, Arial, sans-serif"

out = []
A = out.append


def blastocyst(cx, cy, r):
    """Zona pellucida, trophectoderm rim, eccentric inner cell mass."""
    return (
        f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{TEALL}" stroke="{LINE}" stroke-width="2"/>'
        f'<circle cx="{cx}" cy="{cy}" r="{r-4.5:.1f}" fill="#ffffff" stroke="{TEAL}" '
        f'stroke-width="1.6" stroke-dasharray="{max(3.0,r*0.16):.1f} {max(2.2,r*0.11):.1f}"/>'
        f'<ellipse cx="{cx-r*0.32:.1f}" cy="{cy-r*0.28:.1f}" rx="{r*0.40:.1f}" '
        f'ry="{r*0.32:.1f}" fill="{TEAL}" stroke="{LINE}" stroke-width="1.3"/>')


def uterus(cx, cy, follicles, ov_rx, ov_ry):
    """Coronal-section uterus: fundus, cornua, triangular cavity, cervix,
    transcervical catheter depositing one embryo in the cavity."""
    s = []
    body = (f"M {cx-58},{cy-52} C {cx-64},{cy-86} {cx-30},{cy-98} {cx},{cy-96} "
            f"C {cx+30},{cy-98} {cx+64},{cy-86} {cx+58},{cy-52} "
            f"C {cx+54},{cy-6} {cx+40},{cy+28} {cx+26},{cy+54} "
            f"C {cx+22},{cy+67} {cx-22},{cy+67} {cx-26},{cy+54} "
            f"C {cx-40},{cy+28} {cx-54},{cy-6} {cx-58},{cy-52} Z")
    cavity = (f"M {cx-30},{cy-56} C {cx-24},{cy-74} {cx+24},{cy-74} {cx+30},{cy-56} "
              f"L {cx+7},{cy+42} L {cx-7},{cy+42} Z")
    tl = f"M {cx-57},{cy-58} C {cx-92},{cy-100} {cx-138},{cy-86} {cx-150},{cy-48}"
    tr = f"M {cx+57},{cy-58} C {cx+92},{cy-100} {cx+138},{cy-86} {cx+150},{cy-48}"

    s.append(f'<path d="{tl}" fill="none" stroke="{LINE}" stroke-width="6" stroke-linecap="round"/>')
    s.append(f'<path d="{tr}" fill="none" stroke="{LINE}" stroke-width="6" stroke-linecap="round"/>')
    s.append(f'<path d="{body}" fill="{SAND}" stroke="{LINE}" stroke-width="2.6" stroke-linejoin="round"/>')
    s.append(f'<path d="{cavity}" fill="{SANDL}" stroke="{LINE}" stroke-width="1.8" stroke-linejoin="round"/>')
    # cervix with canal
    s.append(f'<rect x="{cx-16}" y="{cy+50}" width="32" height="56" rx="9" '
             f'fill="{SAND}" stroke="{LINE}" stroke-width="2.4"/>')
    # ovaries
    for sgn in (-1, 1):
        ox, oy = cx + sgn*158, cy - 26
        s.append(f'<ellipse cx="{ox}" cy="{oy}" rx="{ov_rx}" ry="{ov_ry}" '
                 f'fill="{SANDL}" stroke="{LINE}" stroke-width="2.2"/>')
        pts = [(-0.50,-0.30),(0.06,-0.44),(0.54,-0.18),(-0.54,0.26),(0.00,0.10),
               (0.50,0.36),(-0.06,0.52)][:follicles]
        for fx, fy in pts:
            s.append(f'<circle cx="{ox+fx*ov_rx:.1f}" cy="{oy+fy*ov_ry:.1f}" '
                     f'r="{min(ov_rx,ov_ry)*0.30:.1f}" fill="{TEALL}" '
                     f'stroke="{TEAL}" stroke-width="1.5"/>')
    # catheter, transcervical, tip in the cavity
    s.append(f'<path d="M {cx},{cy+112} L {cx},{cy-16}" fill="none" stroke="{GREY}" '
             f'stroke-width="4.2" stroke-linecap="round"/>')
    s.append(f'<path d="M {cx},{cy+112} L {cx},{cy+72}" fill="none" stroke="{TEAL}" '
             f'stroke-width="9" stroke-linecap="round"/>')
    s.append(blastocyst(cx, cy - 36, 15))
    return "".join(s)


def arrow(x1, y1, x2, y2):
    return (f'<path d="M {x1},{y1} L {x2},{y2}" stroke="{LINE}" stroke-width="4.5" '
            f'fill="none" stroke-linecap="round" marker-end="url(#ah)"/>')


def label(x, y, txt, size=21, weight=500, anchor="middle", fill=INK):
    return (f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" '
            f'font-weight="{weight}" text-anchor="{anchor}" fill="{fill}">{txt}</text>')


W, H = 1600, 750
A(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
  f'role="img" aria-label="Fresh transfer and freeze-all pathways after one oocyte retrieval">')
A(f'<defs><marker id="ah" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="6.5" '
  f'markerHeight="6.5" orient="auto-start-reverse">'
  f'<path d="M 0 0 L 10 5 L 0 10 z" fill="{LINE}"/></marker></defs>')
A(f'<rect width="{W}" height="{H}" fill="#ffffff"/>')

# ---- shared sequence -------------------------------------------------------
oy = 318
A(f'<ellipse cx="112" cy="{oy}" rx="64" ry="48" fill="{SANDL}" stroke="{LINE}" stroke-width="2.6"/>')
for fx, fy in [(-0.52,-0.30),(0.04,-0.46),(0.54,-0.18),(-0.54,0.26),(0.02,0.14),(0.52,0.38),(-0.08,0.54)]:
    A(f'<circle cx="{112+fx*64:.1f}" cy="{oy+fy*48:.1f}" r="13" fill="{TEALL}" '
      f'stroke="{TEAL}" stroke-width="2"/>')
A(label(112, oy + 96, "Ovarian"))
A(label(112, oy + 122, "stimulation"))

A(arrow(192, oy, 240, oy))

# aspiration needle
A(f'<g transform="rotate(26 292 {oy})">'
  f'<rect x="276" y="{oy-56}" width="32" height="64" rx="8" fill="{TEALL}" stroke="{LINE}" stroke-width="2.4"/>'
  f'<path d="M 292,{oy+8} L 292,{oy+66}" stroke="{LINE}" stroke-width="3.2" stroke-linecap="round"/>'
  f'</g>')
A(label(292, oy + 96, "Oocyte"))
A(label(292, oy + 122, "retrieval"))

A(arrow(352, oy, 400, oy))

# culture dish
A(f'<path d="M 406,{oy-6} L 406,{oy+16} C 406,{oy+32} 526,{oy+32} 526,{oy+16} L 526,{oy-6}" '
  f'fill="{TEALL}" stroke="{LINE}" stroke-width="2.6"/>')
A(f'<ellipse cx="466" cy="{oy-6}" rx="60" ry="20" fill="#ffffff" stroke="{LINE}" stroke-width="2.6"/>')
for dx in (-26, 0, 26):
    A(blastocyst(466 + dx, oy - 6, 10))
A(label(466, oy + 96, "Fertilisation"))
A(label(466, oy + 122, "and culture"))

# ---- branch arrows ---------------------------------------------------------
A(f'<path d="M 540,{oy-18} C 578,{oy-18} 578,178 618,178" stroke="{LINE}" stroke-width="4.5" '
  f'fill="none" stroke-linecap="round" marker-end="url(#ah)"/>')
A(f'<path d="M 540,{oy+18} C 578,{oy+18} 578,506 618,506" stroke="{LINE}" stroke-width="4.5" '
  f'fill="none" stroke-linecap="round" marker-end="url(#ah)"/>')

# ---- upper panel: fresh ----------------------------------------------------
A(f'<rect x="636" y="30" width="936" height="292" rx="18" fill="{PANEL}" stroke="{PANELB}" stroke-width="2"/>')
A(label(666, 74, "Fresh transfer", 26, 700, "start"))
A(label(666, 103, "transfer in the stimulated cycle", 19, 400, "start", GREY))
A(blastocyst(736, 208, 30))
A(arrow(786, 208, 856, 208))
A(uterus(1190, 196, follicles=7, ov_rx=46, ov_ry=35))

# ---- lower panel: freeze all ----------------------------------------------
A(f'<rect x="636" y="346" width="936" height="376" rx="18" fill="{PANEL}" stroke="{PANELB}" stroke-width="2"/>')
A(label(666, 390, "Freeze all", 26, 700, "start"))
A(label(666, 419, "segmentation", 19, 400, "start", GREY))

# vitrification straw
A(blastocyst(716, 492, 16))
A(blastocyst(756, 492, 16))
A(f'<path d="M 720,530 L 736,548" stroke="{LINE}" stroke-width="2.6" stroke-linecap="round"/>')
A(f'<path d="M 752,530 L 736,548" stroke="{LINE}" stroke-width="2.6" stroke-linecap="round"/>')
A(f'<path d="M 722,554 L 750,554 L 750,622 L 736,640 L 722,622 Z" fill="{TEALL}" '
  f'stroke="{LINE}" stroke-width="2.4" stroke-linejoin="round"/>')
A(label(736, 676, "Vitrification", 20))

A(arrow(776, 592, 826, 592))

# dewar
A(f'<rect x="850" y="538" width="88" height="94" rx="12" fill="{TEALL}" stroke="{LINE}" stroke-width="2.6"/>')
A(f'<rect x="872" y="518" width="44" height="24" rx="7" fill="{SANDL}" stroke="{LINE}" stroke-width="2.4"/>')
for yy in (566, 586, 606):
    A(f'<path d="M 850,{yy} L 938,{yy}" stroke="{LINE}" stroke-width="1.7" opacity="0.5"/>')
A(label(894, 676, "Storage", 20))

# time break
A(f'<path d="M 984,372 L 984,696" stroke="{GREY}" stroke-width="3.4" stroke-dasharray="12 10" stroke-linecap="round"/>')
A(label(1016, 390, "Later cycle", 26, 700, "start"))
A(label(1016, 419, "unstimulated, endometrium prepared", 19, 400, "start", GREY))

# warming dish
A(f'<path d="M 1040,592 L 1040,608 C 1040,620 1124,620 1124,608 L 1124,592" '
  f'fill="{TEALL}" stroke="{LINE}" stroke-width="2.4"/>')
A(f'<ellipse cx="1082" cy="592" rx="42" ry="15" fill="#ffffff" stroke="{LINE}" stroke-width="2.4"/>')
A(blastocyst(1082, 592, 13))
A(label(1082, 664, "Warming", 20))

A(arrow(1140, 592, 1188, 592))
A(uterus(1378, 556, follicles=0, ov_rx=26, ov_ry=19))

A('</svg>')

svg = "\n".join(out)
open("fig1.svg", "w").write(svg)
open("fig1_wrapper.html", "w").write(
    f'<html><body style="margin:0;background:#fff">{svg}</body></html>')
print(f"fig1.svg written ({len(svg)} bytes)")

texts = re.findall(r'<text[^>]*>([^<]*)</text>', svg)
bad = [t for t in texts if re.search(r'\d|%', t)]
print("rendered labels:", texts)
print("LABELS CONTAINING A DIGIT OR PERCENT:", bad if bad else "none - hard rule satisfied")
