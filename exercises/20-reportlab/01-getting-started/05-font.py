from pathlib import Path

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def font_demo(my_canvas: canvas.Canvas, fonts):
    pos_y = 750
    for font in fonts:
        my_canvas.setFont(font, 12)
        my_canvas.drawString(30, pos_y, font)
        pos_y -= 10


if __name__ == "__main__":
    p = Path(__file__)
    file_path = p.parent / "output" / f"{p.stem}.pdf"
    my_canvas = canvas.Canvas(str(file_path), pagesize=letter)
    fonts = my_canvas.getAvailableFonts()
    font_demo(my_canvas, fonts)
    my_canvas.save()
