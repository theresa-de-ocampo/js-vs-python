from pathlib import Path

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.rl_config import defaultPageSize


def first_page(c: canvas.Canvas, document: SimpleDocTemplate):
    title = "PLATYPUS Demo"
    PAGE_WIDTH, PAGE_HEIGHT = defaultPageSize
    c.saveState()
    c.setFont("Times-Bold", 18)
    c.drawCentredString(PAGE_WIDTH / 2, PAGE_HEIGHT - 100, title)

    c.setFont("Times-Roman", 10)
    c.drawString(inch, inch * 10, "Welcome to the First PLATYPUS Page!")
    c.restoreState()


def later_pages(c: canvas.Canvas, document: SimpleDocTemplate):
    c.saveState()
    c.setFont("Helvetica", 10)
    c.drawString(7 * inch, 0.5 * inch, f"Page {document.page}")
    c.restoreState()


def create_document():
    path = Path(__file__)
    output_path = path.parent / "output" / f"{path.stem}.pdf"
    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=letter,
        leftMargin=72,
        rightMargin=72,
        topMargin=72,
        bottomMargin=18,
    )
    styles = getSampleStyleSheet()
    flowables = []
    spacer = Spacer(1, 0.25 * inch)

    for i in range(50):
        text = f"Paragraph #{i}"
        p = Paragraph(text, styles["Normal"])
        flowables.append(p)
        flowables.append(spacer)

    doc.build(flowables, onFirstPage=first_page, onLaterPages=later_pages)


if __name__ == "__main__":
    create_document()
