# Older ReportLab Style
# The <font> tag is not HTML for a browser.
# Paragraph in ReportLab accepts a small XML-like markup language inside the text string.
# Paragraph supports tags like:
#     <b>bold</b>
#     <i>italic</i>
#     <u>underline</u>
#     <font size="12" name="Helvetica">Helvetica Font</font>
#     <br />
# But the cleaner approach is to put those in the paragraph style instead.
# The inline tags are only useful when only a part of the paragraph needs different formatting.

import time
from pathlib import Path

from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch


def form_letter():
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

    flowables = []
    logo = path.parent.parent / "assets" / "python.png"
    magazine_name = "Pythonista"
    issue_number = 12
    sub_price = "99.00"
    limited_date = "03/05/2010"
    free_gift = "tin foil hat"

    formatted_time = time.ctime()
    full_name = "Mike Driscoll"
    address_parts = ["411 State St.", "Waterloo, IA 50158"]

    img = Image(logo, 2 * inch, 2 * inch)
    flowables.append(img)

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="Justify", alignment=TA_JUSTIFY))
    text = f"<font size=12>{formatted_time}</font>"

    flowables.append(Paragraph(text, styles["Normal"]))
    flowables.append(Spacer(1, 12))

    text = f"<font size=12>{full_name}</font>"
    flowables.append(Paragraph(text, styles["Normal"]))

    for part in address_parts:
        text = f"<font size=12>{part.strip()}</font>"
        flowables.append(Paragraph(text, styles["Normal"]))

    flowables.append(Spacer(1, 12))
    text = f"<font size=12>Dear {full_name.split()[0]},</font>"
    flowables.append(Paragraph(text, styles["Normal"]))
    flowables.append(Spacer(1, 12))

    text = f"""
    <font size=12>We would like to welcome you to our subscriber base for {magazine_name} Magazine!
    You will receive {issue_number} issues at the excellent introductory price of ${sub_price}.
    Please respond by {limited_date} to start receiving your subscription and get the following free gift: {free_gift}</font>
    """

    flowables.append(Paragraph(text, styles["Justify"]))
    flowables.append(Spacer(1, 12))

    text = (
        f"<font size=12>Thank you very much and we look forward to serving you.</font>"
    )

    flowables.append(Paragraph(text, styles["Justify"]))
    flowables.append(Spacer(1, 12))
    text = "<font size=12>Sincerely,</font>"
    flowables.append(Paragraph(text, styles["Normal"]))
    flowables.append(Spacer(1, 48))
    text = "<font size=12>Miranda Priestly</font>"
    flowables.append(Paragraph(text, styles["Normal"]))
    flowables.append(Spacer(1, 12))
    doc.build(flowables)


if __name__ == "__main__":
    form_letter()
