from pathlib import Path

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def draw_lines(c: canvas.Canvas):
    c.setLineWidth(0.3)

    start_y = 710
    c.line(30, start_y, 580, start_y)

    for x in range(10):
        start_y -= 10
        c.line(30, start_y, 580, start_y)


if __name__ == "__main__":
    p = Path(__file__)
    file_path = p.parent / "output" / f"{p.stem}.pdf"
    c = canvas.Canvas(str(file_path), pagesize=letter)
    draw_lines(c)
    c.save()
