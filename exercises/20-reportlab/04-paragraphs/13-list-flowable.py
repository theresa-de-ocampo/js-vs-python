from pathlib import Path
from string import ascii_uppercase

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import (
    ListFlowable,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
)
from reportlab.lib.styles import getSampleStyleSheet


def numbering():
    path = Path(__file__)
    output_dir = path.parent / "output"
    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / f"{path.stem}.pdf"

    doc = SimpleDocTemplate(str(output_path), pagesize=letter)
    styles = getSampleStyleSheet()
    normal = styles["Normal"]

    story = []
    story.append(Paragraph("Numbered list", styles["Heading2"]))

    list_items = [
        Paragraph("First thing", normal),
        Paragraph("Second thing", normal),
        Paragraph("Third thing", normal),
    ]
    story.append(
        ListFlowable(
            list_items,
            bulletType="1",
            start="1",
            leftIndent=0.35 * inch,
        )
    )

    story.append(Spacer(1, 0.25 * inch))
    story.append(Paragraph("Figure labels", styles["Heading2"]))

    section_number = 0
    captions = [
        "Application architecture",
        "Request flow",
        "Generated PDF output",
        "Final document",
    ]

    for index, caption in enumerate(captions):
        figure_label = f"Fig. {section_number}-{ascii_uppercase[index]}"
        story.append(Paragraph(f"{figure_label}: {caption}", normal))

    doc.build(story)


if __name__ == "__main__":
    numbering()
