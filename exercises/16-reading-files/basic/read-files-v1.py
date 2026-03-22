# from pathlib import Path

# file_path = Path(__file__).with_name("files/hello.txt")

# with file_path.open("r") as file:
#     print(file.read())

a = open("files/hello.txt", "r")
print("***** Read All *****")
print(a.read())
a.close()

print("\n***** Read First 10 Chars *****")
b = open("files/hello.txt", "r")
print(b.read(10))
b.close()


print("\n***** Read First 2 Lines *****")
c = open("files/hello.txt", "r")
print(c.readline(), end="")
print(c.readline())
c.close()

print("\n***** readlines - keeps \\n *****")
d = open("files/hello.txt", "r")
print(d.readlines())
d.close()

print("\n***** splitlines - removes \\n *****")
e = open("files/hello.txt", "r")
print(e.read().splitlines())
e.close()
