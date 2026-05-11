from pathlib import Path

from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Paragraph


def landscape_orientation():
    path = Path(__file__)
    output_path = path.parent / "output" / f"{path.stem}.pdf"
    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=landscape(letter),
        leftMargin=72,
        rightMargin=72,
        topMargin=72,
        bottomMargin=72,
    )
    doc.build([Paragraph("Hi. I'm Tom Riddle.")])


if __name__ == "__main__":
    landscape_orientation()
