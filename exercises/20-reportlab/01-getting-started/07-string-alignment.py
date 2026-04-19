from pathlib import Path

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


def string_alignment(c: canvas.Canvas):
    width, height = letter
    c.drawString(80, 700, "Standard String")
    c.drawRightString(80, 680, "Right String")

    numbers = [987.15, 42, -1, 234.56, (456.78)]
    y = 650
    for number in numbers:
        c.drawAlignedString(80, y, str(number))
        y -= 20

    c.drawCentredString(width / 2, height / 2, "Centered String")

    c.showPage()


if __name__ == "__main__":
    p = Path(__file__)
    file_path = p.parent / "output" / f"{p.stem}.pdf"
    c = canvas.Canvas(str(file_path))
    string_alignment(c)
    c.save()
