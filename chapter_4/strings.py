# string creation
single_quoted_string = "This is a single quoted string"
print(single_quoted_string)

double_quoted_string = "This is a double quoted string"
print(double_quoted_string)

raw_string = r"This is a raw string. You can\'t escape characters there"
print(raw_string)

raw_f_string = rf"{raw_string}"
print(raw_f_string)

sentence = "This is an f string"
f_string = f"{sentence}"
print(f_string)

mixed_string = "This is a double quoted string. But we can use 'single quotes' inside"
print(mixed_string)

multiline_string = """There was a Young Lady of Norway,
Who casually sat in a doorway;
When the door squeezed her flat,
She exclaimed, "What of that?"
This courageous Young Lady of Norway."""
print(multiline_string)

empty_string = ""
print(empty_string)

# string creation with str()
print(str(98.0))
print(str(-1))
print(str(True))

# string escaping
palindrome = "A man,\nA plan,\nA canal:\nPanama"
print(palindrome)

print("\ttab")

testimony = "'I did nothing' - he said."
print(testimony)

speech = "The backslash (\\) bends over backwards to please you."
print(speech)

# string combining and duplication
first_name = "Adilet"
last_name = "Askar"
full_name = first_name + " " + last_name
print(full_name)

start = "Na" * 4 + "\n"
middle = "Hey" * 3 + "\n"
end = "Goodbye"
print(start + start + middle + end)

# string indexing and slicing
letters = "abcdefghijklmnopqrstuvwxyz"
print(letters[0])
print(letters[-1])
print(letters[:])
print(letters[20:])
print(letters[12:15])
print(letters[-3:])
print(letters[18:-3])
print(letters[::7])
print(letters[:20:4])
print(letters[::-1])

# string methods
print(f"The length of letters: {len(letters)}")

tasks = "get gloves, get mask, give cat vitamins, call ambulance"
splitted_tasks = tasks.split(",")
print(splitted_tasks)

joined_string = ", ".join(splitted_tasks)
print(joined_string)

setup = "a duck goes into a bar."
replaced_setup = setup.replace("duck", "marmoset")
print(replaced_setup)

strange_word = "keepthemalive"
print(strange_word.startswith("ke"))
print(strange_word.endswith("e"))

without_prefix = strange_word.removeprefix("keep")
print(without_prefix)

without_suffix = strange_word.removesuffix("alive")
print(without_suffix)

world = " earth "
print(world.strip())

found_word = multiline_string.find("the")
print(found_word)
print(multiline_string.isalnum())

print(full_name.lower())
print(full_name.upper())
print(full_name.title())

print(setup.center(30))

# string formatting

# old-style
print("%s" % 42)
print("%d" % 42)
print("%x" % 42)
print("%o" % 42)

cat = "Chester"
weight = 28
print("My cat %s weighs %s pounds" % (cat, weight))

# new-style
thing = "woodchunk"
place = "lake"
print("The {} is in the {}.".format(thing, place))

# f-strings
name = "Askar Adilet"
age = 28
print(f"My name is {name}, and I am {age} years old.")
print(f"{name=}, {age=}")
