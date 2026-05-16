from pathlib import Path

from reportlab.platypus import SimpleDocTemplate, Paragraph

if __name__ == "__main__":
    path = Path(__file__)
    output_path = path.parent / "output" / f"{path.stem}.pdf"
    doc = SimpleDocTemplate(str(output_path))

    story = []
    story.append(Paragraph('Welcome to <font color="blue">ReportLab</font>!'))

    doc.build(story)
