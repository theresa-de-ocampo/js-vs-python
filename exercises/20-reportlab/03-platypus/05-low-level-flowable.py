# You won't normally use this.
# But just know that Paragraph is a Platypus Flowable.
# Flowables also have lower-level methods such as wrapOn and drawOn

# You would normally just use the higher-level layout engine: doc.build()
# Behind the scenes, doc.build() ultimately uses the same flowable protocol: wrap, split, and draw

from pathlib import Path

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def mixed():
    path = Path(__file__)
    output_path = path.parent / "output" / f"{path.stem}.pdf"
    c = canvas.Canvas(str(output_path), pagesize=letter)
    styles = getSampleStyleSheet()
    width, height = letter

    p = Paragraph("Hi. I'm Tom Riddle", style=styles["Normal"])
    p.wrapOn(c, width, height)
    p.drawOn(c, 20, 760)

    c.save()


if __name__ == "__main__":
    mixed()
