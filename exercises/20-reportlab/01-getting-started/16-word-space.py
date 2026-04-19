from pathlib import Path

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

if __name__ == "__main__":
    p = Path(__file__)
    file_path = p.parent / "output" / f"{p.stem}.pdf"
    c = canvas.Canvas(str(file_path), pagesize=letter)

    textobject = c.beginText()
    textobject.setTextOrigin(10, 730)

    spacing = 0
    for indent in range(8):
        textobject.setWordSpace(spacing)
        textobject.textLine(f"{spacing} - ReportLab Spacing Demo")
        spacing += 1.5

    c.drawText(textobject)
    c.save()
