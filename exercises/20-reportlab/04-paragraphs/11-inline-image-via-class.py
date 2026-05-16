from pathlib import Path

from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Table

# Image class is a flowable, not true inline paragraph content.
# So it cannot be inserted inside a Paragraph sentence the same way the <img> tag can.
# The closest approach would be to lay it out using a one-row Table.


def add_inline_image():
    path = Path(__file__)
    output_path = path.parent / "output" / f"{path.stem}.pdf"
    image_path = path.parent.parent / "assets" / "python.png"

    doc = SimpleDocTemplate(str(output_path))

    story = []
    inline_image = Image(str(image_path), width=50, height=50)
    story.append(
        Table(
            [
                [
                    Paragraph("Here is a picture:"),
                    inline_image,
                    Paragraph("in the middle of our text."),
                ]
            ]
        )
    )

    doc.build(story)


if __name__ == "__main__":
    add_inline_image()
