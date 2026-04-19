from pathlib import Path

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas


def rotate_demo():
    p = Path(__file__)
    file_path = p.parent / "output" / f"{p.stem}.pdf"
    my_canvas = canvas.Canvas(str(file_path), pagesize=letter)
    my_canvas.translate(inch, inch)
    my_canvas.setFont("Helvetica", 14)
    my_canvas.drawString(inch, inch, "Normal")
    my_canvas.line(inch, inch, inch + 100, inch)

    my_canvas.rotate(45)
    my_canvas.drawString(inch, -inch, "45 degrees")
    my_canvas.line(inch, inch, inch + 100, inch)

    my_canvas.rotate(45)
    my_canvas.drawString(inch, -inch, "90 degrees")
    my_canvas.line(inch, inch, inch + 100, inch)

    my_canvas.save()


if __name__ == "__main__":
    rotate_demo()
