from pathlib import Path

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def add_image(c: canvas.Canvas, image_path: str):
    c.drawImage(image_path, 30, 600, width=100, height=100, mask="auto")


if __name__ == "__main__":
    p = Path(__file__)
    file_path = p.parent / "output" / f"{p.stem}.pdf"
    c = canvas.Canvas(str(file_path), pagesize=letter)

    image_path = p.parent / "assets" / "python.png"
    add_image(c, str(image_path))
    c.save()
