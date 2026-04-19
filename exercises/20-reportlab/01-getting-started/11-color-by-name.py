from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def color_by_name(c: canvas.Canvas):
    c.setFont("Helvetica", 10)
    x = 30

    sample_colors = [
        colors.aliceblue,
        colors.aquamarine,
        colors.lavender,
        colors.beige,
        colors.chocolate,
    ]

    for color in sample_colors:
        c.setFillColor(color)
        c.circle(x, 730, 20, fill=1)
        c.setFillColor(colors.black)
        # c.drawString(x - 10, 700, str(color))
        x += 75


if __name__ == "__main__":
    p = Path(__file__)
    file_path = p.parent / "output" / f"{p.stem}.pdf"
    c = canvas.Canvas(str(file_path), pagesize=letter)
    color_by_name(c)
    c.save()
