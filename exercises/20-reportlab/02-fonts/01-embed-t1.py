from pathlib import Path

# This load the package initializer only.
# It doesn't import every submodule (from reportlab import *)
import reportlab
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas


def embedded_font_demo():
    p = Path(__file__)
    file_path = p.parent / "output" / f"{p.stem}.pdf"
    c = canvas.Canvas(str(file_path), pagesize=letter)
    reportlab_folder = Path(reportlab.__file__).parent
    fonts_folder = reportlab_folder / "fonts"
    print(f"ReportLab font folder is located at {fonts_folder}")

    # afm = fonts_folder / "DarkGardenMK.afm"
    # pfb = fonts_folder / "DarkGardenMK.pfb"

    # font_face = pdfmetrics.EmbeddedType1Face(afm, pfb)
    # pdfmetrics.registerTypeFace(font_face)

    face_name = "DarkGardenMK"
    font = pdfmetrics.Font("Horror Font", face_name, "WinAnsiEncoding")
    pdfmetrics.registerFont(font)

    # If you used DarkGardenMK instead, ReportLab automatically registers it.
    c.setFont("Horror Font", 40)
    c.drawString(10, 730, "The DarkGardenMK Font")
    c.save()


if __name__ == "__main__":
    embedded_font_demo()
