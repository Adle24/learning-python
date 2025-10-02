import re
import string


result = re.match("You", "Young Frankenstein")
print(bool(result))

another_result = re.search("Frank", "Young Frankenstein")
print(bool(another_result))

yet_another_result = re.findall("n", "Young Frankenstein")
print(yet_another_result)

splitted = re.split("n", "Young Frankenstein")
print(splitted)

replaced = re.sub("n", "?", "Young Frankenstein")
print(replaced)

# regex patterns
printable = string.printable
digits = re.findall("\d", printable)
print(digits)

letters = re.findall("\w", printable)
print(letters)

source = "I wish I may, I wish I might Have a dish of fish tonight."
print(re.findall("wish", source))
