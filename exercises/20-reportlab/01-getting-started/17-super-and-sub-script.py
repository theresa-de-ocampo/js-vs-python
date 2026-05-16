from pathlib import Path

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfgen.textobject import PDFTextObject

# PDFTextObject vs. Paragraph

# PDFTextObject
# API Level    : Low-level canvas
# Positioning  : You manuallly place it.
# Text Wrapping: Manual
# Page Breaks  : Manual
# Styling      : Imperative calls like setFont, setRise
# Best For     : Exact text positioning, custom drawing, special effects

# Paragraph
# API Level    : High-Level Platypus
# Positioning  : Document layout places it
# Text Wrapping: Automatic
# Page Breaks  : Automatic
# Styling      : ParagraphStyle plus inline markup
# Best For     : Reports, letters, flowing documents

# Does Paragraph use PDFTextObject behind the scenes?
# Broadly speaking, Paragraph eventually draws text onto the PDF Canvas using lower-level mechanisms
# But it is not accurate to think of Paragraph as just a thin wrapper around one PDFTextObject.
# The layers are roughly:
# Paragraph
#   -> parses text and markup
#   -> breaks text into fragments
#   -> calculates wrapping and line layout
#   -> handles alignment, leading, indentation, bullets, etc.
#   -> draws the result onto the canvas

# PDFTextObject: "I know exactly where and how I want to draw this text."
# Paragraph: "Here is a text plus a style. Please calculate how it should fit in the document."

# PDFTextObject is a pen for writing a specific text at specific coordinates.
# Paragraph is a layout object that decides line breaks, spacing, and positioning, then uses the canvas to draw the final text.


def apply_scripting(textobject: PDFTextObject, text, rise):
    textobject.setFont("Helvetica-Oblique", 8)
    textobject.setRise(rise)
    textobject.textOut(text)
    textobject.setFont("Helvetica-Oblique", 12)
    textobject.setRise(0)


if __name__ == "__main__":
    p = Path(__file__)
    file_path = p.parent / "output" / f"{p.stem}.pdf"
    c = canvas.Canvas(str(file_path), pagesize=letter)

    textobject = c.beginText()
    textobject.setFont("Helvetica-Oblique", 12)
    textobject.setTextOrigin(10, 730)
    textobject.textOut("ReportLab ")
    apply_scripting(textobject, "superscript", 7)
    textobject.textOut("and ")
    apply_scripting(textobject, "subscript", -7)
    c.drawText(textobject)
    c.save()
