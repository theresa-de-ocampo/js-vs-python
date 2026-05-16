from pathlib import Path

from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# Note that this is not the best approach.
# You would usually want to create a ParagraphStyle instead.

if __name__ == "__main__":
    path = Path(__file__)
    output_path = path.parent / "output" / f"{path.stem}.pdf"

    doc = SimpleDocTemplate(str(output_path))
    styles = getSampleStyleSheet()

    story = []
    text = "<para align=center>Hi. I'm Tom Riddle.</para>"
    p = Paragraph(text, styles["Normal"])
    story.append(p)

    doc.build(story)
