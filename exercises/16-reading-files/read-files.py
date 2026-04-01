from pathlib import Path

# The forward slash operator helps create child paths, like os.path.join()
# os.path.join() is cross-platform


# The forward slash is an operator overloaded by pathlib
# Even if you did something like:
# ```
# dirname = Path(__file__).parent
# file_path = dirname / "files" / "hello.txt"
# ```
# Python knows that dirname is a Path object.

file_path = Path(__file__).parent / "files" / "hello.txt"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
