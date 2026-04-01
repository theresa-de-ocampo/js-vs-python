from pathlib import Path


def get_output_path():
    output_dir = Path(__file__).parent / "output"
    output_dir.mkdir(exist_ok=True)

    file_path = output_dir / f"{Path(__file__).stem}.pdf"

    return str(file_path)
