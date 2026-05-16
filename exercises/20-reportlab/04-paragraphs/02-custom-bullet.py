from pathlib import Path

from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# Notice that the normal style have the ff. properties even though it is not a list-related style.
#   bulletAnchor = 10
#   bulletFontName = Helvetica
#   bulletFontSize = 10
# This is because Normal is a ParagraphStyle, and ReportLab paragraphs can have bullet text
# even when they are not part of a formal ListFlowable.

if __name__ == "__main__":
    path = Path(__file__)
    output_path = path.parent / "output" / f"{path.stem}.pdf"

    doc = SimpleDocTemplate(str(output_path))
    story = []
    styles = getSampleStyleSheet()
    normal = styles["Normal"]

    story.append(Paragraph("Milk", normal, bulletText="-"))
    story.append(Paragraph("Eggs", normal, bulletText="-"))
    doc.build(story)
