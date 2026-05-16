from pathlib import Path

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.sequencer import getSequencer

# getSequencer vs ListFlowable

# getSequencer and ListFlowable solve different problems
# getSequencer is a counter system.
# It is useful when you want counters embedded inside paragraph text.
# So, it is good for figure and table labes where the number is part of a sentence or caption.
#   Fig. 0-A
#   Fig. 0-B
#   Fig. 0-C

# ListFlowable is a layout object for actual lists.
# It handles indentation, bullets, numbering, spacing, and list item layout.
# 1. First thing
# 2. Second thing
# 3. Third thing


def paragraph_numbering():
    path = Path(__file__)
    output_path = path.parent / "output" / f"{path.stem}.pdf"
    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=letter,
    )

    styles = getSampleStyleSheet()
    flowables = []

    for _ in range(1, 4):
        text = '<seq id="test"/> thing(s)'
        para = Paragraph(text, style=styles["Normal"])
        flowables.append(para)

    seq = getSequencer()

    # Numeric formatter
    seq.setFormat("Section", "1")
    seq.reset("Section", 0)

    # Letter formatter
    seq.setFormat("FigureNo", "A")
    seq.reset("FigureNo", 0)

    for _ in range(1, 4):
        text = 'Fig. <seq template="%(Section)s-%(FigureNo+)s"/>'
        para = Paragraph(text, style=styles["Normal"])
        flowables.append(para)

    doc.build(flowables)


if __name__ == "__main__":
    paragraph_numbering()
