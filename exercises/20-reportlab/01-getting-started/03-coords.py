from pathlib import Path

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch


def coord(x, y, height, unit):
    x, y = x * unit, height - y * unit
    return x, y


p = Path(__file__)
file_path = p.parent / "output" / f"{p.stem}.pdf"

c = canvas.Canvas(str(file_path), pagesize=letter)
width, height = letter

c.drawString(*coord(1, 1, height, inch), text="Welcome to ReportLab")
c.showPage()
c.save()
