from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

if __name__ == "__main__":
    p = Path(__file__)
    file_path = p.parent / "output" / f"{p.stem}.pdf"
    c = canvas.Canvas(str(file_path), pagesize=letter)

    # Create textobject
    textobject = c.beginText()
    textobject.setTextOrigin(10, 730)
    textobject.setFont("Times-Roman", 12)

    textobject.textLine("Python Rocks!")
    textobject.setFillColor(colors.red)

    textobject.textLine("Python Rocks in Red!")
    textobject.textLines(["JavaScript also rocks!", "But TypeScript is even better."])

    c.drawText(textobject)
    c.save()
