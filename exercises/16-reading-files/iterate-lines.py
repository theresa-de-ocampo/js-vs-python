from pathlib import Path

file_path = Path(__file__).parent / "files" / "movies.txt"

with open(file_path, "r") as f:
    for line in f:
        print(line, end="")
