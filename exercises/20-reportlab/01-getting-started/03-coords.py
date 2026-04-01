from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from pathlib import Path


def coord(x, y, height, unit):
    x, y = x * unit, height - y * unit
    return x, y


file_path = Path(__file__).parent / "output" / f"{Path(__file__).stem}.pdf"

c = canvas.Canvas(str(file_path), pagesize=letter)
width, height = letter

c.drawString(*coord(1, 1, height, inch), text="Welcome to ReportLab")
c.showPage()
c.save()
