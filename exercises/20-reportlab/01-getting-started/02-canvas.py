from reportlab.pdfgen import canvas
from pathlib import Path

file_path = Path(__file__).parent / "output" / f"{Path(__file__).stem}.pdf"

# You can also configure the page size from the constructor.
c = canvas.Canvas(str(file_path), bottomup=0, encrypt="secret")
c.drawString(100, 100, "Welcome to ReportLab")
c.showPage()
c.save()
