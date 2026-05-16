from pathlib import Path

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def paragraph_bullets():
    path = Path(__file__)
    output_dir = path.parent / "output"
    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / f"{path.stem}.pdf"

    doc = SimpleDocTemplate(str(output_path), pagesize=letter)
    styles = getSampleStyleSheet()
    normal = styles["Normal"]
    flowables = []

    p = Paragraph("I'm a cutom bulleted paragraph", style=normal, bulletText="-")
    flowables.append(p)

    p = Paragraph("This is a normal bullet", style=normal, bulletText="\u2022")
    flowables.append(p)

    p = Paragraph("<bullet>&bull;</bullet>This text uses the bullet tag", style=normal)
    flowables.append(p)

    doc.build(flowables)


if __name__ == "__main__":
    paragraph_bullets()
