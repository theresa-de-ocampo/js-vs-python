from pathlib import Path

from reportlab.platypus import SimpleDocTemplate, Paragraph


def add_inline_image():
    path = Path(__file__)
    output_path = path.parent / "output" / f"{path.stem}.pdf"
    image_path = path.parent.parent / "assets" / "python.png"

    doc = SimpleDocTemplate(str(output_path))

    story = []
    story.append(
        Paragraph(
            f'Here is a picture: <img src="{image_path}" width=50 height=50 /> in the middle of our text.'
        )
    )

    doc.build(story)


if __name__ == "__main__":
    add_inline_image()
