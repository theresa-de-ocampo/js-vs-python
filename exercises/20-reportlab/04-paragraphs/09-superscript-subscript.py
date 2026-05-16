from pathlib import Path

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer


def paragraph_scripting():
    path = Path(__file__)
    output_path = path.parent / "output" / f"{path.stem}.pdf"

    doc = SimpleDocTemplate(str(output_path))

    story = []
    paragraphs = [
        "Einstein says: E = mc<super>2</super>",
        "ReportLab <super rise=12>superscript</super> and <sub>subscript</sub>",
        "ReportLab Greek Letter e: <greek>e</greek>",
    ]

    for p in paragraphs:
        story.append(Paragraph(p))
        story.append(Spacer(1, 15))

    doc.build(story)


if __name__ == "__main__":
    paragraph_scripting()
