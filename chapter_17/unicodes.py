import unicodedata
import html


# unicode characters
def unicode_test(value):
    name = unicodedata.name(value)
    val = unicodedata.lookup(name)
    print(f"{value=}, {name=}, {val=}")


unicode_test("A")
unicode_test("$")
unicode_test("\u20ac")
unicode_test("\u2603")

# encoding
snowman = "\u2603"
print(f"Len of snowman: {len(snowman)}")

encoded = snowman.encode("utf-8")
print(f"Encoded snowman: {encoded}")

# decoding
place = "caf\u00e9"
print(f"Place: {place}")

place_bytes = place.encode("utf-8")
print(f"Place: {place_bytes}")

decoded = place_bytes.decode("utf-8")
print(f"Decoded place: {decoded}")

# html entities
print(html.unescape("&egrave;"))
