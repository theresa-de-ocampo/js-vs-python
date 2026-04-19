from pathlib import Path

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def create_form(filename, date, amount, receiver):
    c = canvas.Canvas(filename, pagesize=letter)
    c.setLineWidth(0.3)
    c.setFont("Helvetica", 12)

    c.drawString(30, 750, "OFFICIAL COMMUNIQUE")
    c.drawString(30, 735, "OF ACME INDUSTRIES")

    c.drawString(500, 750, date)
    c.line(480, 747, 580, 747)

    c.drawString(275, 725, "AMOUNT OWED: ")
    c.drawString(500, 725, amount)
    c.line(378, 723, 580, 723)

    c.drawString(30, 703, "RECEIVED BY: ")
    c.line(120, 700, 580, 700)
    c.drawString(120, 703, receiver)

    c.save()


if __name__ == "__main__":
    p = Path(__file__)
    file_path = p.parent / "output" / f"{p.stem}.pdf"
    create_form(str(file_path), "2026-04-16", "$1.99", "Mike")
