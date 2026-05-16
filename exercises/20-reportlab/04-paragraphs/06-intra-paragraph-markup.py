from pathlib import Path

from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def intra_tags():
    path = Path(__file__)
    output_path = path.parent / "output" / f"{path.stem}.pdf"

    doc = SimpleDocTemplate(str(output_path))
    styles = getSampleStyleSheet()

    story = []

    text = (
        "This <b>text</b> is important, "
        "not <strong>strong</strong>.<br /><br />"
        "A book title should be in <i>italics</i>.<br /><br />"
        "You can also <u>underline</u> your text.<br /><br />"
        "Bad text should be <strike>struck-through</strike>!<br /><br />"
        'You can link to <a href="https://www.google.com" color="blue">Google</a> like this'
    )

    p = Paragraph(text, styles["Normal"])
    story.append(p)

    doc.build(story)


if __name__ == "__main__":
    intra_tags()
