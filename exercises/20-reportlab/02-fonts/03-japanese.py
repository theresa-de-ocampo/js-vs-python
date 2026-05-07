from pathlib import Path

from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics

# CID (Character Identifier) composite fonts are specialized PostScript font formats designed
# for large character sets, typically used for Asian languages (Chinese, Japanese, Korean).
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfgen import canvas


def asian_font_demo():
    p = Path(__file__)
    output_path = p.parent / "output" / f"{p.stem}.pdf"
    c = canvas.Canvas(str(output_path), pagesize=letter)

    pdfmetrics.registerFont(UnicodeCIDFont("HeiseiMin-W3"))
    c.setFont("HeiseiMin-W3", 16)

    # Google Translate from English to Japanese
    # Convert the Japanese character to unicode
    # https://r12a.github.io/app-conversion/
    # From the website above, use "Hex/UTF-32"
    # Append each section with \u
    uniqlo = "\u30e6\u30cb\u30af\u30ed"

    c.drawString(25, 730, uniqlo)

    # Python 3 supports Unicode out of the box.
    c.drawString(25, 700, "こんにちは")
    c.save()


if __name__ == "__main__":
    asian_font_demo()
