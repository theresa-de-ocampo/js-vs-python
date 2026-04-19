from pathlib import Path

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

if __name__ == "__main__":
    p = Path(__file__)
    file_path = p.parent / "output" / f"{p.stem}.pdf"
    c = canvas.Canvas(str(file_path), pagesize=letter)

    textobject = c.beginText()
    textobject.setTextOrigin(10, 730)

    for indent in range(4):
        textobject.textLine("ReportLab Cursor Demo")
        textobject.moveCursor(15, 15)

    c.drawText(textobject)
    c.save()
