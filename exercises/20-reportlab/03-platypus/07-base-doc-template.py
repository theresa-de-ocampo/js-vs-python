from datetime import datetime
from pathlib import Path

from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    Image,
    PageTemplate,
    Paragraph,
    Spacer,
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

# When you use SimpleDocTemplate, ReportLab automatically gives you a basic page template and frame
# based on the margins.

# BaseDocTemplate is the lower-level version. It starts with no PageTemplate.
# So if you call doc.build(flowables) without setting up a frame, it will throw:
#   IndexError: list index out of range
# because there were no page templates in doc.pageTemplates

# Typical reasons to use BaseDocTemplate:
#   - You need multiple frames on a page, like two columns.
#   - You need different page templates inside one document.
#   - You need portrait and landcape pages in the same document.
#   - You need special page callbacks or events handlers (e.g., Table of Contents)

# TODO: Two column layout or editorial layout


def form_letter():
    path = Path(__file__)
    output_file_path = path.parent / "output" / f"{path.stem}.pdf"
    doc = BaseDocTemplate(
        str(output_file_path),
        pagesize=letter,
        leftMargin=72,
        rightMargin=72,
        topMargin=72,
        bottomMargin=18,
    )
    frame = Frame(
        doc.leftMargin,
        doc.bottomMargin,
        doc.width,
        doc.height,
        id="normal",
    )
    doc.addPageTemplates([PageTemplate(id="main", frames=[frame])])

    flowables = []
    logo = path.parent.parent / "assets" / "python.png"
    magazine_name = "Pythonista"
    issue_number = 12
    sub_price = "99.00"
    limited_date = "03/05/2010"
    free_gift = "tin foil hat"

    formatted_time = datetime.now().strftime("%Y-%m-%d %I:%M%p")
    full_name = "Mike Driscoll"
    address_parts = ["411 State St.", "Waterloo, IA 50158"]

    img = Image(logo, 2 * inch, 2 * inch)
    flowables.append(img)

    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="BigNormal", parent=styles["Normal"], fontSize=12, leading=14
        )
    )
    styles.add(
        ParagraphStyle(name="Justify", parent=styles["BigNormal"], alignment=TA_JUSTIFY)
    )

    flowables.append(Paragraph(formatted_time, styles["BigNormal"]))
    flowables.append(Spacer(1, 12))

    flowables.append(Paragraph(f"Dear {full_name},", styles["BigNormal"]))

    for part in address_parts:
        flowables.append(Paragraph(part.strip(), styles["BigNormal"]))

    flowables.append(Spacer(1, 12))
    flowables.append(Paragraph(full_name.split()[0], styles["BigNormal"]))
    flowables.append(Spacer(1, 12))

    # Implicit String Literal Concatenation
    # Adjacent string literals are automatically joined by Python.
    body = (
        f"We would like to welcome you to our subscriber base for {magazine_name} Magazine! "
        f"You will receive {issue_number} issues at the excellent introductory price of ${sub_price}. "
        f"Please respond by {limited_date} to start receiving your subscription and get "
        f"the following free gift: {free_gift}"
    )

    flowables.append(Paragraph(body, styles["Justify"]))
    flowables.append(Spacer(1, 12))

    flowables.append(
        Paragraph(
            "Thank you very much and we look forward to serving you.", styles["Justify"]
        )
    )
    flowables.append(Spacer(1, 12))

    flowables.append(Paragraph("Sincerely,", styles["BigNormal"]))
    flowables.append(Spacer(1, 12))

    flowables.append(Paragraph("Miranda Priestly", styles["BigNormal"]))
    flowables.append(Spacer(1, 12))
    doc.build(flowables)


if __name__ == "__main__":
    form_letter()
