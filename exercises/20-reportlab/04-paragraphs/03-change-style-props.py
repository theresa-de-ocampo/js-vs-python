from pathlib import Path

from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# Note that ReportLab does not automatically recompute leading when you mutate fontSize;
# you need to set both.

# A common rule is:
# leading = fontSize * 1.2

if __name__ == "__main__":
    path = Path(__file__)
    output_path = path.parent / "output" / f"{path.stem}.pdf"

    doc = SimpleDocTemplate(str(output_path))
    styles = getSampleStyleSheet()
    normal = styles["Normal"]
    story = []

    story.append(Paragraph("This is the default 10pt", normal))
    normal.fontSize = 20
    normal.leading = 24
    story.append(Paragraph("Now, this is using 20pt.", normal))
    normal.fontSize = 16
    normal.leading = 19.2
    story.append(Paragraph("That was too big, brought it down to 16pt.", normal))
    story.append(Paragraph("This is the sweet spot.", normal))

    doc.build(story)
