from pathlib import Path

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def draw_shapes(c: canvas.Canvas):
    c.setStrokeColorRGB(0.2, 0.5, 0.3)
    c.rect(10, 700, 100, 80, stroke=1, fill=0)
    c.ellipse(10, 680, 100, 630, stroke=1, fill=1)
    c.wedge(10, 600, 100, 550, 45, 90, stroke=1, fill=0)
    c.circle(300, 600, 50)


if __name__ == "__main__":
    p = Path(__file__)
    file_path = p.parent / "output" / f"{p.stem}.pdf"
    c = canvas.Canvas(str(file_path), pagesize=letter)
    draw_shapes(c)
    c.save()
