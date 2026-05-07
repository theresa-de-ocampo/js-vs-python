# This code snippet is not that useful.
# Encodings are just important for old, T1 fonts.
# The encoding determines which glyph the font should use for that character code.

from pathlib import Path

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas


def standard_fonts():
    p = Path(__file__)
    output_path = p.parent / "output"

    for enc in ["MacRoman", "WinAnsi"]:
        c = canvas.Canvas(str(output_path / f"{p.stem}-{enc}.pdf"))
        c.setPageCompression(0)

        x = 0
        y = 744

        for face_name in pdfmetrics.standardFonts:
            if face_name in ["Symbol", "ZapfDingbats"]:
                enc_label = face_name + "Encoding"
            else:
                enc_label = enc + "Encoding"

            print(enc_label)

            font_name = face_name + "-" + enc_label
            pdfmetrics.registerFont(pdfmetrics.Font(font_name, face_name, enc_label))

            c.setFont("Times-Bold", 18)
            c.drawString(80, y, font_name)

            y -= 20

            alpha = "abcdefghijklmnopqrstuvwxyz"
            c.setFont(font_name, 14)
            c.drawString(x + 85, y, alpha)

            y -= 20

        c.save()


if __name__ == "__main__":
    standard_fonts()
