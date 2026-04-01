from pathlib import Path

file_path = Path(__file__).resolve().parent.parent / "files" / "hello.txt"

a = open(file_path, "r")
print("***** Read All *****")
print(a.read())
a.close()

print("\n***** Read First 10 Chars *****")
b = open(file_path, "r")
print(b.read(10))
b.close()


print("\n***** Read First 2 Lines *****")
c = open(file_path, "r")
print(c.readline(), end="")
print(c.readline())
c.close()

print("\n***** readlines - keeps \\n *****")
d = open(file_path, "r")
print(d.readlines())
d.close()

print("\n***** splitlines - removes \\n *****")
e = open(file_path, "r")
print(e.read().splitlines())
e.close()
