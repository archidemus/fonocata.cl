#!/usr/bin/env python3
"""
Genera template PPTX para presentaciones de congreso basado en el design system de fonocata.cl.

Design tokens extraídos del sitio:
- Fonts: Nunito (headings), Inter (body)  [se usan fuentes del sistema como fallback en PPTX]
- Colors: Purple (#a78bfa / #7c3aed), Blue (#93c5fd / #60a5fa), Slate (text), Pink (#f9a8d4)
- Style: Clean, rounded shapes, gradient accents, soft shadows
- Formato: 16:9 estándar (13.333" × 7.5")

Genera layouts:
1. Portada (Title Slide)
2. Índice / Agenda
3. Sección (Section Header)
4. Contenido - Título + Texto
5. Contenido - Título + 2 Columnas
6. Contenido - Título + 3 Columnas
7. Contenido - Título + 4 Cards
8. Contenido + Imagen (derecha)
9. Cita / Highlight
10. Datos / Estadísticas
11. Cierre / Contacto

Uso: python3 scripts/generate-template.py [nombre-archivo.pptx]
"""

import sys
from pathlib import Path

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn, nsmap

# ─── Design Tokens ───────────────────────────────────────────────────────

# Colores principales (desde Tailwind config del sitio)
PURPLE_400 = RGBColor(0xA7, 0x8B, 0xFA)  # #a78bfa — primary accent
PURPLE_500 = RGBColor(0x8B, 0x5C, 0xF6)  # #8b5cf6
PURPLE_600 = RGBColor(0x7C, 0x3A, 0xED)  # #7c3aed
PURPLE_300 = RGBColor(0xC4, 0xB5, 0xFD)  # #c4b5fd
PURPLE_100 = RGBColor(0xED, 0xE9, 0xFE)  # #ede9fe
PURPLE_900 = RGBColor(0x58, 0x1C, 0x87)  # #581c87

BLUE_300 = RGBColor(0x93, 0xC5, 0xFD)  # #93c5fd
BLUE_400 = RGBColor(0x60, 0xA5, 0xFA)  # #60a5fa
BLUE_100 = RGBColor(0xDB, 0xEA, 0xFE)  # #dbeafe
BLUE_50 = RGBColor(0xEF, 0xF6, 0xFF)    # #eff6ff

PINK_100 = RGBColor(0xFC, 0xE7, 0xF3)   # #fce7f3
PINK_300 = RGBColor(0xF9, 0xA8, 0xD4)   # #f9a8d4

SLATE_50 = RGBColor(0xF8, 0xFA, 0xFC)   # #f8fafc — main bg
SLATE_100 = RGBColor(0xF1, 0xF5, 0xF9)  # #f1f5f9
SLATE_200 = RGBColor(0xE2, 0xE8, 0xF0)  # #e2e8f0
SLATE_400 = RGBColor(0x94, 0xA3, 0xB8)  # #94a3b8
SLATE_500 = RGBColor(0x64, 0x74, 0x8B)  # #64748b
SLATE_600 = RGBColor(0x47, 0x55, 0x69)  # #475569
SLATE_700 = RGBColor(0x33, 0x41, 0x55)  # #334155
SLATE_800 = RGBColor(0x1E, 0x29, 0x3B)  # #1e293b
SLATE_900 = RGBColor(0x0F, 0x17, 0x2A)  # #0f172a

WHITE = RGBColor(0xFF, 0xFF, 0xFF)

# Fonts
FONT_HEADING = "Nunito"
FONT_BODY = "Inter"

# Dimensions (16:9)
SLIDE_WIDTH = Inches(13.333)
SLIDE_HEIGHT = Inches(7.5)

# Padding / Margins
MARGIN_LEFT = Inches(0.8)
MARGIN_RIGHT = Inches(0.8)
MARGIN_TOP = Inches(0.6)
CONTENT_TOP = Inches(1.6)
CONTENT_WIDTH = SLIDE_WIDTH - MARGIN_LEFT - MARGIN_RIGHT

# ─── Helpers ─────────────────────────────────────────────────────────────


def add_gradient_bg(slide, color1, color2, angle=270):
    """Add a gradient background fill to a slide."""
    bg = slide.background
    fill = bg.fill
    fill.gradient()
    fill.gradient_stops[0].color.rgb = color1
    fill.gradient_stops[0].position = 0.0
    fill.gradient_stops[1].color.rgb = color2
    fill.gradient_stops[1].position = 1.0
    # Set angle via XML
    gradFill = fill._fill._element  # the <a:gradFill> element
    lin = gradFill.find(qn('a:lin'))
    if lin is None:
        lin = gradFill.makeelement(qn('a:lin'), {})
        gradFill.append(lin)
    lin.set('ang', str(angle * 60000))  # EMUs for angle
    lin.set('scaled', '1')


def add_solid_bg(slide, color):
    """Add a solid background fill."""
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = color


def add_text_box(slide, left, top, width, height, text, font_name=FONT_BODY,
                 font_size=Pt(14), font_color=SLATE_700, bold=False, italic=False,
                 alignment=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP):
    """Add a styled text box."""
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.word_wrap = True
    tf.auto_size = None
    try:
        tf.paragraphs[0].alignment = alignment
    except:
        pass

    p = tf.paragraphs[0]
    run = p.add_run()
    run.text = text
    run.font.name = font_name
    run.font.size = font_size
    run.font.color.rgb = font_color
    run.font.bold = bold
    run.font.italic = italic

    # Vertical anchor
    txBox.text_frame._txBody.bodyPr.set('anchor', {
        MSO_ANCHOR.TOP: 't',
        MSO_ANCHOR.MIDDLE: 'ctr',
        MSO_ANCHOR.BOTTOM: 'b',
    }.get(anchor, 't'))

    return txBox


def add_rounded_rect(slide, left, top, width, height, fill_color=None,
                     line_color=None, line_width=Pt(0), corner_radius=None):
    """Add a rounded rectangle shape."""
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height
    )
    if fill_color:
        shape.fill.solid()
        shape.fill.fore_color.rgb = fill_color
    else:
        shape.fill.background()

    if line_color:
        shape.line.color.rgb = line_color
        shape.line.width = line_width
    else:
        shape.line.fill.background()

    # Adjust corner radius via XML (avLst)
    if corner_radius is not None:
        sp = shape._element
        prstGeom = sp.find(qn('a:prstGeom'))
        if prstGeom is not None:
            avLst = prstGeom.find(qn('a:avLst'))
            if avLst is None:
                avLst = prstGeom.makeelement(qn('a:avLst'), {})
                prstGeom.append(avLst)
            # Clear existing
            for gd in avLst.findall(qn('a:gd')):
                avLst.remove(gd)
            gd = avLst.makeelement(qn('a:gd'), {
                'name': 'adj',
                'fmla': f'val {corner_radius}'
            })
            avLst.append(gd)

    return shape


def add_circle(slide, left, top, size, fill_color=None, line_color=None):
    """Add a circle/oval shape."""
    shape = slide.shapes.add_shape(
        MSO_SHAPE.OVAL, left, top, size, size
    )
    if fill_color:
        shape.fill.solid()
        shape.fill.fore_color.rgb = fill_color
    else:
        shape.fill.background()

    if line_color:
        shape.line.color.rgb = line_color
    else:
        shape.line.fill.background()

    return shape


def add_line(slide, start_x, start_y, end_x, end_y, color=SLATE_200, width=Pt(1)):
    """Add a horizontal line."""
    connector = slide.shapes.add_connector(
        1, start_x, start_y, end_x, end_y  # 1 = straight
    )
    connector.line.color.rgb = color
    connector.line.width = width
    return connector


def add_footer(slide, text="Catalina Orellana M. | Fonoaudióloga | fonocata.cl"):
    """Add consistent footer bar."""
    # Thin purple line
    line = add_line(slide, Inches(0), SLIDE_HEIGHT - Inches(0.5),
                    SLIDE_WIDTH, SLIDE_HEIGHT - Inches(0.5),
                    color=PURPLE_300, width=Pt(1.5))
    # Footer text
    add_text_box(slide, MARGIN_LEFT, SLIDE_HEIGHT - Inches(0.45),
                 Inches(8), Inches(0.35), text,
                 font_size=Pt(9), font_color=SLATE_400,
                 alignment=PP_ALIGN.LEFT)


def add_slide_number(slide, num, total):
    """Add slide number in bottom right."""
    add_text_box(slide, SLIDE_WIDTH - Inches(1.2), SLIDE_HEIGHT - Inches(0.45),
                 Inches(0.8), Inches(0.35), f"{num} / {total}",
                 font_size=Pt(9), font_color=SLATE_400,
                 alignment=PP_ALIGN.RIGHT)


def add_section_badge(slide, text, left=MARGIN_LEFT, top=Inches(0.4)):
    """Add the purple eyebrow badge (like the hero's eyebrow)."""
    badge_width = Inches(len(text) * 0.12 + 0.6)
    badge_height = Inches(0.35)
    rect = add_rounded_rect(slide, left, top, badge_width, badge_height,
                            fill_color=PURPLE_100, line_color=SLATE_200,
                            line_width=Pt(0.5), corner_radius=8000)

    # Purple dot
    dot_size = Inches(0.15)
    add_circle(slide, left + Inches(0.12), top + Inches(0.1),
               dot_size, fill_color=PURPLE_400)

    # Badge text
    add_text_box(slide, left + Inches(0.35), top + Inches(0.02),
                 badge_width - Inches(0.4), badge_height,
                 text.upper(),
                 font_name=FONT_HEADING, font_size=Pt(9),
                 font_color=SLATE_500, bold=True)


def set_shape_transparency(shape, pct):
    """Set fill transparency (0-100) on a shape via XML."""
    spPr = shape._element.find(qn('p:spPr'))
    if spPr is None:
        return
    solidFill = spPr.find(qn('a:solidFill'))
    if solidFill is None:
        return
    srgbClr = solidFill.find(qn('a:srgbClr'))
    if srgbClr is not None:
        # Remove existing alpha
        for a in srgbClr.findall(qn('a:alpha')):
            srgbClr.remove(a)
        alpha_val = str(int((100 - pct) * 1000))  # pct transparency → alpha val
        alpha_el = srgbClr.makeelement(qn('a:alpha'), {'val': alpha_val})
        srgbClr.append(alpha_el)


def add_decorative_circles(slide):
    """Add subtle decorative circles in corners (like the hero blur effects)."""
    # Top right - large, very faint purple
    circle1 = add_circle(slide, SLIDE_WIDTH - Inches(3), Inches(-1),
                         Inches(4), fill_color=PURPLE_100)
    set_shape_transparency(circle1, 80)

    # Bottom left - faint blue
    circle2 = add_circle(slide, Inches(-1.5), SLIDE_HEIGHT - Inches(2.5),
                         Inches(4), fill_color=BLUE_100)
    set_shape_transparency(circle2, 85)


# ─── Slide Generators ────────────────────────────────────────────────────

TOTAL_SLIDES = 11


def make_title_slide(prs):
    """Slide 1: Portada con título del congreso."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # Blank
    add_solid_bg(slide, SLATE_50)
    add_decorative_circles(slide)

    # Large purple gradient rectangle on left
    rect_width = Inches(0.15)
    add_rounded_rect(slide, Inches(0.5), Inches(0.8), rect_width, Inches(5.8),
                     fill_color=PURPLE_400, corner_radius=50000)

    # Congress name
    add_text_box(slide, Inches(1.0), Inches(1.0), Inches(10), Inches(0.4),
                 "CONGRESO IBEROAMERICANO DE VOZ",
                 font_name=FONT_HEADING, font_size=Pt(13),
                 font_color=SLATE_500, bold=True)

    # Main title
    add_text_box(slide, Inches(1.0), Inches(1.6), Inches(10), Inches(2.5),
                 "Título de tu\nPresentación",
                 font_name=FONT_HEADING, font_size=Pt(44),
                 font_color=SLATE_800, bold=True)

    # Subtitle / description
    add_text_box(slide, Inches(1.0), Inches(4.2), Inches(8), Inches(0.8),
                 "Subtítulo o descripción breve de la presentación",
                 font_name=FONT_BODY, font_size=Pt(16),
                 font_color=SLATE_500)

    # Purple line separator
    add_line(slide, Inches(1.0), Inches(5.3), Inches(4), Inches(5.3),
             color=PURPLE_400, width=Pt(2))

    # Author info card
    card = add_rounded_rect(slide, Inches(1.0), Inches(5.6), Inches(5), Inches(1.2),
                            fill_color=WHITE, line_color=SLATE_200,
                            line_width=Pt(0.75), corner_radius=10000)

    add_text_box(slide, Inches(1.3), Inches(5.7), Inches(4.4), Inches(0.35),
                 "Catalina Orellana Molnar",
                 font_name=FONT_HEADING, font_size=Pt(14),
                 font_color=SLATE_800, bold=True)
    add_text_box(slide, Inches(1.3), Inches(6.05), Inches(4.4), Inches(0.25),
                 "Fonoaudióloga Clínica",
                 font_name=FONT_BODY, font_size=Pt(11),
                 font_color=PURPLE_500)
    add_text_box(slide, Inches(1.3), Inches(6.3), Inches(4.4), Inches(0.25),
                 "fonocata.cl | @fonocata.cl",
                 font_name=FONT_BODY, font_size=Pt(10),
                 font_color=SLATE_400)

    return slide


def make_agenda_slide(prs):
    """Slide 2: Índice / Agenda."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_solid_bg(slide, SLATE_50)
    add_decorative_circles(slide)

    add_section_badge(slide, "Agenda")
    add_text_box(slide, MARGIN_LEFT, Inches(1.0), CONTENT_WIDTH, Inches(0.8),
                 "Contenidos de la Presentación",
                 font_name=FONT_HEADING, font_size=Pt(32),
                 font_color=SLATE_800, bold=True)

    items = [
        ("01", "Introducción", "Contexto y motivación"),
        ("02", "Marco Teórico", "Fundamentos y evidencia"),
        ("03", "Metodología", "Diseño del estudio"),
        ("04", "Resultados", "Hallazgos principales"),
        ("05", "Discusión", "Análisis e implicancias"),
        ("06", "Conclusiones", "Síntesis y proyecciones"),
    ]

    col_width = Inches(5.8)
    start_y = Inches(2.0)
    row_height = Inches(0.75)

    for i, (num, title, desc) in enumerate(items):
        col = i % 2
        row = i // 2
        x = MARGIN_LEFT + col * (col_width + Inches(0.5))
        y = start_y + row * (row_height + Inches(0.15))

        # Number circle
        circle = add_circle(slide, x, y + Inches(0.05), Inches(0.45),
                            fill_color=PURPLE_100)
        add_text_box(slide, x, y + Inches(0.05), Inches(0.45), Inches(0.45),
                     num, font_name=FONT_HEADING, font_size=Pt(14),
                     font_color=PURPLE_600, bold=True,
                     alignment=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)

        # Title
        add_text_box(slide, x + Inches(0.65), y, col_width - Inches(0.65), Inches(0.35),
                     title, font_name=FONT_HEADING, font_size=Pt(16),
                     font_color=SLATE_800, bold=True)
        # Description
        add_text_box(slide, x + Inches(0.65), y + Inches(0.3), col_width - Inches(0.65), Inches(0.3),
                     desc, font_name=FONT_BODY, font_size=Pt(11),
                     font_color=SLATE_500)

    add_footer(slide)
    add_slide_number(slide, 2, TOTAL_SLIDES)
    return slide


def make_section_slide(prs):
    """Slide 3: Section Header (divisor de sección)."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_gradient_bg(slide, PURPLE_600, SLATE_900, angle=315)

    # Decorative circles
    c1 = add_circle(slide, SLIDE_WIDTH - Inches(4), Inches(-2),
                     Inches(6), fill_color=PURPLE_400)
    set_shape_transparency(c1, 85)

    c2 = add_circle(slide, Inches(-2), SLIDE_HEIGHT - Inches(3),
                     Inches(5), fill_color=BLUE_300)
    set_shape_transparency(c2, 90)

    # Section number
    add_text_box(slide, MARGIN_LEFT, Inches(2.0), Inches(2), Inches(0.6),
                 "01",
                 font_name=FONT_HEADING, font_size=Pt(36),
                 font_color=PURPLE_300, bold=True)

    # Line
    add_line(slide, MARGIN_LEFT, Inches(2.8), Inches(3), Inches(2.8),
             color=PURPLE_300, width=Pt(2))

    # Section title
    add_text_box(slide, MARGIN_LEFT, Inches(3.1), Inches(10), Inches(1.5),
                 "Título de la Sección",
                 font_name=FONT_HEADING, font_size=Pt(40),
                 font_color=WHITE, bold=True)

    # Section subtitle
    add_text_box(slide, MARGIN_LEFT, Inches(4.8), Inches(8), Inches(0.6),
                 "Descripción breve del contenido de esta sección",
                 font_name=FONT_BODY, font_size=Pt(16),
                 font_color=PURPLE_300)

    add_footer(slide, "Catalina Orellana M. | Fonoaudióloga | fonocata.cl")
    add_slide_number(slide, 3, TOTAL_SLIDES)
    return slide


def make_title_content_slide(prs):
    """Slide 4: Título + Contenido (texto)."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_solid_bg(slide, SLATE_50)
    add_decorative_circles(slide)

    add_section_badge(slide, "Sección")
    add_text_box(slide, MARGIN_LEFT, Inches(1.0), CONTENT_WIDTH, Inches(0.7),
                 "Título del Contenido",
                 font_name=FONT_HEADING, font_size=Pt(28),
                 font_color=SLATE_800, bold=True)

    # Thin line under title
    add_line(slide, MARGIN_LEFT, Inches(1.7), Inches(3), Inches(1.7),
             color=PURPLE_400, width=Pt(2))

    # Body content area
    content_y = Inches(2.0)
    content_h = Inches(4.5)
    card = add_rounded_rect(slide, MARGIN_LEFT, content_y, CONTENT_WIDTH, content_h,
                            fill_color=WHITE, line_color=SLATE_200,
                            line_width=Pt(0.5), corner_radius=8000)

    add_text_box(slide, Inches(1.1), Inches(2.3), Inches(11), Inches(3.8),
                 "Escribe aquí el contenido principal de tu diapositiva. "
                 "Puedes incluir párrafos de texto, listas o cualquier información relevante.\n\n"
                 "• Primer punto importante\n"
                 "• Segundo punto relevante\n"
                 "• Tercer punto de discusión\n\n"
                 "Texto adicional para contexto o explicación complementaria.",
                 font_name=FONT_BODY, font_size=Pt(14),
                 font_color=SLATE_700)

    add_footer(slide)
    add_slide_number(slide, 4, TOTAL_SLIDES)
    return slide


def make_two_column_slide(prs):
    """Slide 5: Título + 2 Columnas."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_solid_bg(slide, SLATE_50)
    add_decorative_circles(slide)

    add_section_badge(slide, "Sección")
    add_text_box(slide, MARGIN_LEFT, Inches(1.0), CONTENT_WIDTH, Inches(0.7),
                 "Título — Dos Columnas",
                 font_name=FONT_HEADING, font_size=Pt(28),
                 font_color=SLATE_800, bold=True)

    col_width = Inches(5.6)
    col_y = Inches(2.0)
    col_h = Inches(4.5)
    gap = Inches(0.4)

    # Column 1
    card1 = add_rounded_rect(slide, MARGIN_LEFT, col_y, col_width, col_h,
                             fill_color=WHITE, line_color=SLATE_200,
                             line_width=Pt(0.5), corner_radius=8000)
    # Purple accent bar at top
    add_rounded_rect(slide, MARGIN_LEFT + Inches(0.2), col_y + Inches(0.2),
                     Inches(0.8), Inches(0.08), fill_color=PURPLE_400,
                     corner_radius=50000)
    add_text_box(slide, MARGIN_LEFT + Inches(0.3), col_y + Inches(0.5),
                 col_width - Inches(0.6), Inches(0.4),
                 "Columna Uno",
                 font_name=FONT_HEADING, font_size=Pt(16),
                 font_color=SLATE_800, bold=True)
    add_text_box(slide, MARGIN_LEFT + Inches(0.3), col_y + Inches(1.0),
                 col_width - Inches(0.6), Inches(3.0),
                 "Contenido de la primera columna. Describe el concepto, hallazgo o idea principal.\n\n"
                 "• Punto relevante\n"
                 "• Dato importante\n"
                 "• Observación clave",
                 font_name=FONT_BODY, font_size=Pt(13),
                 font_color=SLATE_600)

    # Column 2
    x2 = MARGIN_LEFT + col_width + gap
    card2 = add_rounded_rect(slide, x2, col_y, col_width, col_h,
                             fill_color=WHITE, line_color=SLATE_200,
                             line_width=Pt(0.5), corner_radius=8000)
    # Blue accent bar
    add_rounded_rect(slide, x2 + Inches(0.2), col_y + Inches(0.2),
                     Inches(0.8), Inches(0.08), fill_color=BLUE_400,
                     corner_radius=50000)
    add_text_box(slide, x2 + Inches(0.3), col_y + Inches(0.5),
                 col_width - Inches(0.6), Inches(0.4),
                 "Columna Dos",
                 font_name=FONT_HEADING, font_size=Pt(16),
                 font_color=SLATE_800, bold=True)
    add_text_box(slide, x2 + Inches(0.3), col_y + Inches(1.0),
                 col_width - Inches(0.6), Inches(3.0),
                 "Contenido de la segunda columna. Complementa o contrasta con la primera.\n\n"
                 "• Punto relevante\n"
                 "• Dato importante\n"
                 "• Observación clave",
                 font_name=FONT_BODY, font_size=Pt(13),
                 font_color=SLATE_600)

    add_footer(slide)
    add_slide_number(slide, 5, TOTAL_SLIDES)
    return slide


def make_three_column_slide(prs):
    """Slide 6: Título + 3 Columnas."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_solid_bg(slide, SLATE_50)
    add_decorative_circles(slide)

    add_section_badge(slide, "Sección")
    add_text_box(slide, MARGIN_LEFT, Inches(1.0), CONTENT_WIDTH, Inches(0.7),
                 "Título — Tres Columnas",
                 font_name=FONT_HEADING, font_size=Pt(28),
                 font_color=SLATE_800, bold=True)

    col_width = Inches(3.6)
    col_y = Inches(2.0)
    col_h = Inches(4.5)
    gap = Inches(0.3)
    colors = [PURPLE_400, BLUE_400, PINK_300]
    bgs = [PURPLE_100, BLUE_100, PINK_100]
    titles = ["Concepto A", "Concepto B", "Concepto C"]
    icons = ["🎯", "💡", "🔬"]

    for i in range(3):
        x = MARGIN_LEFT + i * (col_width + gap)
        card = add_rounded_rect(slide, x, col_y, col_width, col_h,
                                fill_color=WHITE, line_color=SLATE_200,
                                line_width=Pt(0.5), corner_radius=8000)
        # Colored top accent
        add_rounded_rect(slide, x + Inches(0.2), col_y + Inches(0.2),
                         Inches(0.6), Inches(0.08), fill_color=colors[i],
                         corner_radius=50000)

        # Icon circle
        add_circle(slide, x + Inches(0.25), col_y + Inches(0.5),
                   Inches(0.5), fill_color=bgs[i])
        add_text_box(slide, x + Inches(0.25), col_y + Inches(0.5),
                     Inches(0.5), Inches(0.5), icons[i],
                     font_size=Pt(16), alignment=PP_ALIGN.CENTER,
                     anchor=MSO_ANCHOR.MIDDLE)

        # Title
        add_text_box(slide, x + Inches(0.25), col_y + Inches(1.2),
                     col_width - Inches(0.5), Inches(0.4),
                     titles[i],
                     font_name=FONT_HEADING, font_size=Pt(15),
                     font_color=SLATE_800, bold=True)

        # Body
        add_text_box(slide, x + Inches(0.25), col_y + Inches(1.7),
                     col_width - Inches(0.5), Inches(2.5),
                     "Describe aquí el contenido de esta columna.\n\n"
                     "• Punto uno\n• Punto dos\n• Punto tres",
                     font_name=FONT_BODY, font_size=Pt(12),
                     font_color=SLATE_600)

    add_footer(slide)
    add_slide_number(slide, 6, TOTAL_SLIDES)
    return slide


def make_four_cards_slide(prs):
    """Slide 7: Título + 4 Cards (estilo Services del sitio)."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_solid_bg(slide, WHITE)
    add_decorative_circles(slide)

    add_section_badge(slide, "Sección")
    add_text_box(slide, MARGIN_LEFT, Inches(1.0), CONTENT_WIDTH, Inches(0.7),
                 "Título — Cuatro Elementos",
                 font_name=FONT_HEADING, font_size=Pt(28),
                 font_color=SLATE_800, bold=True)

    # 2x2 grid
    card_w = Inches(5.6)
    card_h = Inches(2.1)
    gap_x = Inches(0.4)
    gap_y = Inches(0.3)
    start_y = Inches(1.9)
    colors = [PURPLE_100, BLUE_100, PINK_100, RGBColor(0xD1, 0xFA, 0xE5)]  # emerald-100
    accents = [PURPLE_400, BLUE_400, PINK_300, RGBColor(0x34, 0xD3, 0x99)]  # emerald-400
    titles = ["Elemento Uno", "Elemento Dos", "Elemento Tres", "Elemento Cuatro"]
    icons = ["🎤", "🍽️", "🧠", "💜"]

    for i in range(4):
        col = i % 2
        row = i // 2
        x = MARGIN_LEFT + col * (card_w + gap_x)
        y = start_y + row * (card_h + gap_y)

        card = add_rounded_rect(slide, x, y, card_w, card_h,
                                fill_color=colors[i], line_color=SLATE_200,
                                line_width=Pt(0.25), corner_radius=12000)

        # Icon circle
        circle = add_circle(slide, x + Inches(0.3), y + Inches(0.3),
                            Inches(0.55), fill_color=WHITE)
        add_text_box(slide, x + Inches(0.3), y + Inches(0.3),
                     Inches(0.55), Inches(0.55), icons[i],
                     font_size=Pt(18), alignment=PP_ALIGN.CENTER,
                     anchor=MSO_ANCHOR.MIDDLE)

        # Title
        add_text_box(slide, x + Inches(1.0), y + Inches(0.3),
                     card_w - Inches(1.3), Inches(0.35),
                     titles[i],
                     font_name=FONT_HEADING, font_size=Pt(14),
                     font_color=SLATE_800, bold=True)

        # Description
        add_text_box(slide, x + Inches(1.0), y + Inches(0.7),
                     card_w - Inches(1.3), Inches(1.2),
                     "Descripción breve de este elemento o concepto clave.",
                     font_name=FONT_BODY, font_size=Pt(11),
                     font_color=SLATE_600)

    add_footer(slide)
    add_slide_number(slide, 7, TOTAL_SLIDES)
    return slide


def make_content_image_slide(prs):
    """Slide 8: Contenido + Imagen (placeholder)."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_solid_bg(slide, SLATE_50)
    add_decorative_circles(slide)

    add_section_badge(slide, "Sección")
    add_text_box(slide, MARGIN_LEFT, Inches(1.0), Inches(6), Inches(0.7),
                 "Título con Imagen",
                 font_name=FONT_HEADING, font_size=Pt(28),
                 font_color=SLATE_800, bold=True)

    # Left content
    add_text_box(slide, MARGIN_LEFT, Inches(2.0), Inches(5.8), Inches(4.0),
                 "Contenido principal de la diapositiva.\n\n"
                 "• Primer punto relevante\n"
                 "• Segundo punto de discusión\n"
                 "• Tercer hallazgo importante\n\n"
                 "Texto adicional para explicar o contextualizar los puntos anteriores.",
                 font_name=FONT_BODY, font_size=Pt(14),
                 font_color=SLATE_700)

    # Right image placeholder
    img_x = Inches(7.2)
    img_y = Inches(1.6)
    img_w = Inches(5.2)
    img_h = Inches(5.0)
    img_card = add_rounded_rect(slide, img_x, img_y, img_w, img_h,
                                fill_color=SLATE_100, line_color=SLATE_200,
                                line_width=Pt(0.75), corner_radius=10000)

    # Placeholder icon + text
    add_text_box(slide, img_x, img_y + Inches(1.8), img_w, Inches(0.5),
                 "🖼️",
                 font_size=Pt(36), alignment=PP_ALIGN.CENTER,
                 anchor=MSO_ANCHOR.MIDDLE)
    add_text_box(slide, img_x + Inches(0.5), img_y + Inches(2.6),
                 img_w - Inches(1.0), Inches(0.4),
                 "Inserta tu imagen aquí",
                 font_name=FONT_BODY, font_size=Pt(12),
                 font_color=SLATE_400, alignment=PP_ALIGN.CENTER)

    add_footer(slide)
    add_slide_number(slide, 8, TOTAL_SLIDES)
    return slide


def make_quote_slide(prs):
    """Slide 9: Cita / Highlight."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_solid_bg(slide, WHITE)

    # Large decorative circle (like hero)
    c1 = add_circle(slide, SLIDE_WIDTH - Inches(5), Inches(-3),
                     Inches(8), fill_color=PURPLE_100)
    set_shape_transparency(c1, 80)

    c2 = add_circle(slide, Inches(-3), SLIDE_HEIGHT - Inches(3),
                     Inches(6), fill_color=BLUE_100)
    set_shape_transparency(c2, 85)

    # Purple accent bar left
    add_rounded_rect(slide, Inches(2.5), Inches(2.2), Inches(0.08), Inches(3.0),
                     fill_color=PURPLE_400, corner_radius=50000)

    # Quote text
    add_text_box(slide, Inches(3.0), Inches(2.2), Inches(7.5), Inches(2.5),
                 "\"Una cita o hallazgo relevante que quieras destacar en tu presentación.\"",
                 font_name=FONT_HEADING, font_size=Pt(24),
                 font_color=SLATE_800, bold=False, italic=True)

    # Attribution
    add_text_box(slide, Inches(3.0), Inches(5.0), Inches(7.5), Inches(0.4),
                 "— Autor / Fuente",
                 font_name=FONT_BODY, font_size=Pt(13),
                 font_color=PURPLE_500, bold=True)

    add_footer(slide)
    add_slide_number(slide, 9, TOTAL_SLIDES)
    return slide


def make_stats_slide(prs):
    """Slide 10: Datos / Estadísticas."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_solid_bg(slide, SLATE_50)
    add_decorative_circles(slide)

    add_section_badge(slide, "Datos")
    add_text_box(slide, MARGIN_LEFT, Inches(1.0), CONTENT_WIDTH, Inches(0.7),
                 "Datos y Resultados",
                 font_name=FONT_HEADING, font_size=Pt(28),
                 font_color=SLATE_800, bold=True)

    # 3 stat cards
    stats = [
        ("85%", "Tasa de\nMejoría", PURPLE_400, PURPLE_100),
        ("120+", "Pacientes\nAtendidos", BLUE_400, BLUE_100),
        ("4", "Áreas de\nEspecialidad", PINK_300, PINK_100),
    ]

    stat_w = Inches(3.6)
    stat_h = Inches(3.5)
    gap = Inches(0.35)
    start_x = (SLIDE_WIDTH - 3 * stat_w - 2 * gap) / 2
    stat_y = Inches(2.2)

    for i, (number, label, accent, bg) in enumerate(stats):
        x = int(start_x) + i * (stat_w + gap)
        card = add_rounded_rect(slide, x, stat_y, stat_w, stat_h,
                                fill_color=bg, line_color=SLATE_200,
                                line_width=Pt(0.25), corner_radius=12000)

        # Number
        add_text_box(slide, x, stat_y + Inches(0.6), stat_w, Inches(0.9),
                     number,
                     font_name=FONT_HEADING, font_size=Pt(44),
                     font_color=accent, bold=True,
                     alignment=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)

        # Accent line
        line_w = Inches(0.8)
        add_rounded_rect(slide, int(x) + (stat_w - line_w) // 2,
                         stat_y + Inches(1.7),
                         line_w, Inches(0.06),
                         fill_color=accent, corner_radius=50000)

        # Label
        add_text_box(slide, x, stat_y + Inches(2.0), stat_w, Inches(1.0),
                     label,
                     font_name=FONT_BODY, font_size=Pt(14),
                     font_color=SLATE_600,
                     alignment=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.TOP)

    # Additional context text
    add_text_box(slide, MARGIN_LEFT, Inches(6.0), CONTENT_WIDTH, Inches(0.5),
                 "Nota: Puedes reemplazar estos datos con tus propios resultados o estadísticas.",
                 font_name=FONT_BODY, font_size=Pt(11),
                 font_color=SLATE_400, italic=True,
                 alignment=PP_ALIGN.CENTER)

    add_footer(slide)
    add_slide_number(slide, 10, TOTAL_SLIDES)
    return slide


def make_closing_slide(prs):
    """Slide 11: Cierre / Contacto."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_gradient_bg(slide, PURPLE_600, SLATE_900, angle=315)

    # Decorative circles
    c1 = add_circle(slide, SLIDE_WIDTH - Inches(3), Inches(-2),
                     Inches(5), fill_color=PURPLE_400)
    set_shape_transparency(c1, 88)

    c2 = add_circle(slide, Inches(-2), SLIDE_HEIGHT - Inches(3),
                     Inches(4), fill_color=BLUE_300)
    set_shape_transparency(c2, 92)

    # Thank you
    add_text_box(slide, MARGIN_LEFT, Inches(1.5), Inches(10), Inches(1.2),
                 "¡Gracias!",
                 font_name=FONT_HEADING, font_size=Pt(52),
                 font_color=WHITE, bold=True)

    add_text_box(slide, MARGIN_LEFT, Inches(3.0), Inches(8), Inches(0.6),
                 "Catalina Orellana Molnar",
                 font_name=FONT_HEADING, font_size=Pt(22),
                 font_color=PURPLE_300, bold=True)

    # Line
    add_line(slide, MARGIN_LEFT, Inches(3.8), Inches(3), Inches(3.8),
             color=PURPLE_300, width=Pt(2))

    # Contact info
    contact_items = [
        "📧  catalina.orellanamol@gmail.com",
        "📱  +56 9 5632 0835 (WhatsApp)",
        "🌐  fonocata.cl",
        "📸  @fonocata.cl",
    ]
    for i, item in enumerate(contact_items):
        add_text_box(slide, MARGIN_LEFT, Inches(4.2) + i * Inches(0.4),
                     Inches(6), Inches(0.35),
                     item,
                     font_name=FONT_BODY, font_size=Pt(14),
                     font_color=WHITE)

    # Congress branding bottom right
    add_text_box(slide, SLIDE_WIDTH - Inches(5), SLIDE_HEIGHT - Inches(1.0),
                 Inches(4.2), Inches(0.5),
                 "Congreso Iberoamericano de Voz 2025",
                 font_name=FONT_BODY, font_size=Pt(10),
                 font_color=PURPLE_300,
                 alignment=PP_ALIGN.RIGHT)

    add_slide_number(slide, 11, TOTAL_SLIDES)
    return slide


# ─── Main ─────────────────────────────────────────────────────────────────


def main():
    output_name = sys.argv[1] if len(sys.argv) > 1 else "Template_Fonocata_Congreso.pptx"
    output_path = Path(__file__).parent.parent / output_name

    prs = Presentation()
    prs.slide_width = SLIDE_WIDTH
    prs.slide_height = SLIDE_HEIGHT

    print("🎨 Generando template fonocata.cl para congreso...")
    print(f"   Formato: {SLIDE_WIDTH / 914400:.1f}\" × {SLIDE_HEIGHT / 914400:.1f}\" (16:9)")

    make_title_slide(prs)
    print("   ✓ Slide 1: Portada")

    make_agenda_slide(prs)
    print("   ✓ Slide 2: Agenda")

    make_section_slide(prs)
    print("   ✓ Slide 3: Divisor de sección")

    make_title_content_slide(prs)
    print("   ✓ Slide 4: Título + Contenido")

    make_two_column_slide(prs)
    print("   ✓ Slide 5: Dos Columnas")

    make_three_column_slide(prs)
    print("   ✓ Slide 6: Tres Columnas")

    make_four_cards_slide(prs)
    print("   ✓ Slide 7: Cuatro Cards")

    make_content_image_slide(prs)
    print("   ✓ Slide 8: Contenido + Imagen")

    make_quote_slide(prs)
    print("   ✓ Slide 9: Cita / Highlight")

    make_stats_slide(prs)
    print("   ✓ Slide 10: Estadísticas")

    make_closing_slide(prs)
    print("   ✓ Slide 11: Cierre / Contacto")

    prs.save(str(output_path))
    print(f"\n✅ Template guardado en: {output_path}")
    print(f"   {len(prs.slides)} slides generados")


if __name__ == "__main__":
    main()
