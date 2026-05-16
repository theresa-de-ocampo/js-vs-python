from pathlib import Path

from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def intra_tags():
    path = Path(__file__)
    output_path = path.parent / "output" / f"{path.stem}.pdf"

    doc = SimpleDocTemplate(str(output_path))
    styles = getSampleStyleSheet()
    styles["Normal"].spaceBefore = 10
    styles["Normal"].spaceAfter = 10

    story = []
    paragraphs = [
        "This <b>text</b> is important, not <strong>strong</strong>.",
        "A book title should be in <i>italics</i>.",
        "You can also <u>underline</u> your text.",
        "Bad text should be <strike>struck-through</strike>!",
        'You can link to <a href="https://www.google.com" color="blue">Google</a> like this',
    ]

    for p in paragraphs:
        story.append(Paragraph(p, styles["Normal"]))

    doc.build(story)


if __name__ == "__main__":
    intra_tags()
