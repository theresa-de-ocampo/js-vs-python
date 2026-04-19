from pathlib import Path

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def gray_color_demo(c: canvas.Canvas):
    c.setFont("Helvetica", 10)
    x = 30

    grays = [0, 0.25, 0.5, 0.75, 1]

    for gray in grays:
        c.setFillGray(gray)
        c.circle(x, 730, 20, fill=1)
        c.setFillGray(0)
        c.drawString(x - 10, 700, f"Gray={gray}")
        x += 75


if __name__ == "__main__":
    p = Path(__file__)
    file_path = p.parent / "output" / f"{p.stem}.pdf"
    c = canvas.Canvas(str(file_path), pagesize=letter)
    gray_color_demo(c)
    c.save()
