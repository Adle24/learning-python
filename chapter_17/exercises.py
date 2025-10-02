import unicodedata
import re

# exercise 1
mystery = "\U0001f984"
print(f"{mystery=}")
print(f"mystery name: {unicodedata.name(mystery)}")

another_mystery = "\U0001f4a9"
print(f"{another_mystery=}")
print(f"mystery name: {unicodedata.name(another_mystery)}")

# exercise 2
pop_bytes = mystery.encode("utf-8")
print(f"{pop_bytes=}")

# exercise 3
pop_string = pop_bytes.decode("utf-8")
print(f"{pop_string=}")

# exercise 4
source = "my name is Askar Adilet"
print(re.findall(r"\bA\w*", source))
print(re.findall(r"\bc\w{3}\b", source))
print(re.findall(r"\b\w*r\b", source))
print(re.findall(r"\b\w*[aeiou]{3}[^aeiou\s]*\w*\b", source))
