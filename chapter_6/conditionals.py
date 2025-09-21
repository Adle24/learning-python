# this is a comment

# if-else conditional
disaster = True

if disaster:
    print("Woe!")
else:
    print("Whee!")

# nested conditionals
furry = True
large = True

if furry:
    if large:
        print("It is a yeti.")
    else:
        print("It is a cat.")
else:
    if large:
        print("It is a whale.")
    else:
        print("It is a human. Or a hairless cat.")

# elif conditionals
color = "mauve"

if color == "red":
    print("It is a tomato")
elif color == "grren":
    print("It is a green pepper")
elif color == "bee purple":
    print("I do not know what it is, but only bees can see it.")
else:
    print(f"I have never heard of the color {color}")

# boolean expressions
my_num = 7
print(my_num == 5)
print(my_num < 8)
print(my_num <= 7)
print(my_num > 10)
print(my_num >= 1)
print(my_num != 3)
print((my_num < 10) and (my_num > 3))
print((my_num > 10) or (my_num < 1))
print(not (my_num > 10))
print(4 < my_num < 10)

# falsy values
print(bool(False))
print(bool(None))
print(bool(""))
print(bool(0))
print(bool(0.0))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(set()))

some_list = []

if some_list:
    print("There is something here")
else:
    print("It is empty")

# membership operator
vowels = "aeiou"
letter = "o"

if letter in vowels:
    print(f"{letter} is a vowel")

# walrus operator
post_limit = 300
post_string = "Blah" * 50

if (diff := post_limit - len(post_string)) >= 0:
    print("A fitting post")
else:
    print(f"Went over by {abs(diff)}")

# match expressions
superhero = "Spiderman"

match superhero:
    case "Superman":
        secret_identity = "Clark Kent"
    case "Batman":
        secret_identity = "Bruce Wayne"
    case "Spiderman":
        secret_identity = "Peter Parker"
    case _:
        secret_identity = "?"

print(secret_identity)

subject = [3, 5]

match subject:
    case x, y if y > 6:
        print("y > 6")
    case 2, 5:
        print("2, 5")
    case x, 5:
        print(f"{x=}, {y=}")
    case 3, 5:
        print("3, 5")
    case _:
        print(f"no match for {subject}")
