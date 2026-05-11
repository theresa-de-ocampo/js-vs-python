from pathlib import Path

from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak
from reportlab.platypus import Frame, PageTemplate, NextPageTemplate, Spacer


def alternate_orientations():
    path = Path(__file__)
    output_path = path.parent / "output" / f"{path.stem}.pdf"
    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=letter,
        leftMargin=72,
        rightMargin=72,
        topMargin=72,
        bottomMargin=72,
    )
    styles = getSampleStyleSheet()
    normal = styles["Normal"]

    portrait_width, portrait_height = letter
    landscape_width, landscape_heigt = landscape(letter)

    portrait_frame = Frame(
        doc.leftMargin,
        doc.bottomMargin,
        portrait_width - doc.leftMargin - doc.rightMargin,
        portrait_height - doc.topMargin - doc.bottomMargin,
        id="portrait_frame",
    )

    landscape_frame = Frame(
        doc.leftMargin,
        doc.rightMargin,
        landscape_width - doc.leftMargin - doc.rightMargin,
        landscape_heigt - doc.topMargin - doc.bottomMargin,
        id="landscape_frame",
    )

    portrait_template = PageTemplate(
        id="portrait", frames=[portrait_frame], pagesize=letter
    )
    landscape_template = PageTemplate(
        id="landscape", frames=[landscape_frame], pagesize=landscape(letter)
    )
    doc.addPageTemplates([portrait_template, landscape_template])

    story = []
    story.append(Paragraph("This is a page in portrait orientation", normal))

    # Change to landscape
    story.append(NextPageTemplate("landscape"))
    story.append(PageBreak())
    story.append(Paragraph("This is a page in landscape orientation", normal))

    # Change back to portrait
    story.append((NextPageTemplate("portrait")))
    story.append(PageBreak())
    story.append(Paragraph("Now we're back in portrait mode again", normal))

    doc.build(story)


if __name__ == "__main__":
    alternate_orientations()
