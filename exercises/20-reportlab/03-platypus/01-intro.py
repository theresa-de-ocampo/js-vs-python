from pathlib import Path

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def basic_platypus_demo():
    path = Path(__file__)
    output_file_path = path.parent / "output" / f"{path.stem}.pdf"
    doc = SimpleDocTemplate(
        str(output_file_path),
        pagesize=letter,
        leftMargin=72,
        rightMargin=72,
        topMargin=72,
        bottomMargin=18,
    )

    # styles is a runtime object, not a statically typed dictionary with known literal keys
    # That's why you don't get any intellisense
    styles = getSampleStyleSheet()
    built_in_styles = styles.byName.keys()

    # Normal
    # BodyText
    # Italic
    # Heading1
    # Title
    # Heading2
    # Heading3
    # Heading4
    # Heading5
    # Heading6
    # Bullet
    # Definition - Indented
    # Code - Indented
    # UnorderedList
    # OrderedList

    flowables = []

    for style in built_in_styles:
        if style not in ["Bullet", "UnorderedList", "OrderedList"]:
            p = Paragraph(style, style=styles[style])
            flowables.append(p)

    doc.build(flowables)


if __name__ == "__main__":
    basic_platypus_demo()
