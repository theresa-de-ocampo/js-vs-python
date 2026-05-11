from pathlib import Path

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Paragraph, Frame


def frame_demo():
    path = Path(__file__)
    output_path = path.parent / "output" / f"{path.stem}.pdf"
    c = Canvas(str(output_path), pagesize=letter)

    styles = getSampleStyleSheet()
    normal = styles["Normal"]
    heading = styles["Heading1"]

    flowables = []
    flowables.append(Paragraph("Heading #1", heading))
    flowables.append(Paragraph("Paragraph #1", normal))

    right_flowables = []
    right_flowables.append(Paragraph("Heading #2", heading))
    right_flowables.append(Paragraph("Ipsum Lorem", normal))

    left_frame = Frame(inch, inch, width=3 * inch, height=9 * inch, showBoundary=1)
    right_frame = Frame(4 * inch, inch, width=3 * inch, height=9 * inch, showBoundary=1)

    left_frame.addFromList(flowables, c)
    right_frame.addFromList(right_flowables, c)

    c.save()


if __name__ == "__main__":
    frame_demo()
