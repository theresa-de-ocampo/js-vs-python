# importlib.resources provides routines for accessing non-code resources from Python packages.
from importlib import resources
from pathlib import Path

from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


def embed_font_demo():
    p = Path(__file__)
    output_file_path = p.parent / "output" / f"{p.stem}.pdf"

    # Find the installed reportlab package and return a resource handle for that package's content
    reportlab_fonts = resources.files("reportlab").joinpath("fonts")
    vera_font_path = reportlab_fonts.joinpath("Vera.ttf")
    vera_bold_font_path = reportlab_fonts.joinpath("VeraBd.ttf")
    vera_italic_font_path = reportlab_fonts.joinpath("VeraIt.ttf")
    vera_bold_italic_font_path = reportlab_fonts.joinpath("VeraBI.ttf")

    print()

    vera_font = TTFont("Vera", vera_font_path)
    vera_bold_font = TTFont("Vera-Bold", vera_bold_font_path)
    vera_italic_font = TTFont("Vera-Italic", vera_italic_font_path)
    vera_bold_italic_font = TTFont("Vera-BoldItalic", vera_bold_italic_font_path)
    pdfmetrics.registerFont(vera_font)
    pdfmetrics.registerFont(vera_bold_font)
    pdfmetrics.registerFont(vera_italic_font)
    pdfmetrics.registerFont(vera_bold_italic_font)

    # Mostly just for metadata
    pdfmetrics.registerFontFamily(
        "Vera",
        normal="Vera",
        bold="Vera-Bold",
        italic="Vera-Italic",
        boldItalic="Vera-BoldItalic",
    )

    c = canvas.Canvas(str(output_file_path), pagesize=letter)
    c.setFont("Helvetica", 40)
    c.drawString(10, 730, "The Helvetica Font")

    # You'll get a KeyError if you try to use the font w/out registering it.
    c.setFont("Vera", 40)
    c.drawString(10, 690, "The Vera Font")

    c.setFont("Vera-Bold", 40)
    c.drawString(10, 650, "The Vera Bold Font")

    c.setFont("Vera-Italic", 40)
    c.drawString(10, 610, "The Vera Italic Font")

    c.setFont("Vera-BoldItalic", 40)
    c.drawString(10, 570, "The Vera Bold Italic Font")
    c.save()


if __name__ == "__main__":
    embed_font_demo()
