# file operations
file_out = open("file.txt", "wt")
print("Oops, I created a file", file=file_out)
file_out.close()

poem = """There was a young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the previous night."""

file_out = open("file.txt", "wt")
file_out.write(poem)
file_out.close()

file_in = open("file.txt", "rt")
poem = file_in.read()
file_in.close()
print(poem)

poem = ""
file_in = open("file.txt", "rt")
chunk = 100

while True:
    fragment = file_in.read(chunk)
    if not fragment:
        break
    poem = poem + fragment

file_in.close()
print("SEPARATOR")
print(poem)

porm = ""
file_in = open("file.txt", "rt")

while True:
    line = file_in.readline()
    if not line:
        break
    poem = poem + line

file_in.close()
print(poem)

# binary files
binary_data = bytes(range(0, 256))

file_out = open("binary.txt", "wb")
file_out.write(binary_data)
file_out.close()

file_in = open("binary.txt", "rb")
data = file_in.read()
file_in.close()
print(data)

# context managers
with open("binary.txt", "rb") as file_in:
    data = file_in.read()
    print(data)

with open("binary.txt", "rb") as file_in:
    file_in.seek(255)
    data = file_in.read()
    print(data)
