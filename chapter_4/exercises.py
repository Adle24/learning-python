# exercise 1
song = """When an eel grabs your arm,
And it causes great harm,
That's - a moray!"""

upper_letter = song[-6].upper()
changed_song = song[:-6] + upper_letter + song[-5:]
print(changed_song)

# exercise 2
poem = """My kitty cat likes %s,
My kitty cat likes %s,
My kitty cat fell on his %s
And now thinks he's a %s."""

print(poem % ("roast", "beef", "ham", "head"))

# exercise 3
letter = """
Dear {salutation} {name},
Thank you for your letter. We are sorry that our {product}
{verbed} in your {room}. Please note that it should never
be used in a {room}, especially near any {animals}.
Send us your receipt and {amount} for shipping and handling.
We will send you another {product} that, in our tests,
is {percent}% less likely to have {verbed}.
Thank you for your support.
Sincerely,
{spokesman}
{job_title}
""".format(
    salutation="Mr",
    name="Askar Adilet",
    product="PyCharm",
    verbed="appeared",
    room="Room",
    animals="animals",
    amount="amount",
    percent="20",
    spokesman="spokesman",
    job_title="Job Title",
)

print(letter)

# exercise 4
names = ["duck", "gourd", "spitz"]
for name in names:
    cap_name = name.capitalize()
    print("%sy Mc%sface" % (cap_name, cap_name))

print()
for name in names:
    print("{}y Mc{}face".format(name.capitalize(), name.capitalize()))

print()
for name in names:
    print(f"{name.capitalize()}y Mc{name.capitalize()}face")