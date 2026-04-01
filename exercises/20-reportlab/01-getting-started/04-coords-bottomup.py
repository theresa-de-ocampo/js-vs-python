from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from pathlib import Path


def coord(x, y, unit):
    x, y = x * unit, y * unit
    return x, y


file_path = Path(__file__).parent / "output" / f"{Path(__file__).stem}.pdf"

c = canvas.Canvas(str(file_path), pagesize=letter, bottomup=0)

c.drawString(*coord(1, 1, inch), text="Welcome to ReportLab")
c.showPage()
c.save()
