from pathlib import Path

from reportlab.pdfgen import canvas

p = Path(__file__)
file_path = p.parent / "output" / f"{p.stem}.pdf"

# You can also configure the page size from the constructor.
c = canvas.Canvas(str(file_path), bottomup=0, encrypt="secret")
c.drawString(100, 100, "Welcome to ReportLab")
c.showPage()
c.save()
