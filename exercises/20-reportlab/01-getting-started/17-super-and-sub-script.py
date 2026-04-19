from pathlib import Path

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfgen.textobject import PDFTextObject


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
