from pathlib import Path

from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas

if __name__ == "__main__":
    p = Path(__file__)
    file_path = p.parent / "output" / f"{p.stem}.pdf"
    c = canvas.Canvas(str(file_path))
    c.setPageSize(landscape(letter))
    c.setAuthor("Teriz De Ocampo")
    c.setTitle("Portfolio")
    c.setSubject("Summary of Skills")
    c.drawString(30, 500, "Teriz De Ocampo")
    c.save()
