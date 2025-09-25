# function declaration
def do_nothing():
    pass


def make_sound():
    print("quack")


def agree():
    return True


def echo(anything):
    return anything + " " + anything


def commentary(color):
    if color == "red":
        return "It's a tomato"
    elif color == "green":
        return "It's a pepper"
    elif color == "bee purple":
        return "I don't know what it is, but only bees can see it"
    else:
        return f"I have never heard of the color {color}"


do_nothing()
make_sound()

is_agreed = agree()
print(f"Is he agreed: {is_agreed}")

print(echo("Adilet"))
print(commentary("violet"))


# None is absence of value
def whatis(thing):
    if thing is None:
        print("None")
    elif thing:
        print("True")
    else:
        print("False")


whatis(None)
whatis([])
whatis([""])
whatis("None")


# arguments
def menu(wine, entree, dessert="pudding"):
    return {
        "wine": wine,
        "entree": entree,
        "dessert": dessert,
    }


print(menu("chardonnay", "chicken", "cake"))
print(menu(entree="beef", dessert="cheese cake", wine="bordeaux"))
print(menu("frontenac", dessert="flan", entree="fish"))
print(menu(wine="chardonay", entree="chicken"))


# packing and unpacking
def print_args(*args):
    print(f"Positional tuple: {args}")


def print_kwargs(**kwargs):
    print(f"Keyword dictionary: {kwargs}")


def print_data(data, /, start=0, end=100):
    for value in data[start:end]:
        print(value)


my_data = ["a", "b", "c", "d", "e", "f"]
print_args(1, 2, 3)
print_kwargs(a=1, b=2, c=3)
print_data(my_data, 2, 4)

# mutablity
my_list = ["a", "b", "c", "d", "e", "f"]


def modify_list(data):
    data[1] = "x"


modify_list(my_list)
print(my_list)


# docstrings
def my_function(anything):
    """
    prints argument of function
    :param anything:
    :return: None
    """

    print(anything)


help(my_function)
print(my_function.__doc__)


# functions are first class citizens
def answer():
    print(42)


def run_function(func):
    func()


def add_args(arg1, arg2):
    print(arg1 + arg2)


def run_with_args(func, arg1, arg2):
    func(arg1, arg2)


run_function(answer)
run_with_args(add_args, 1, 2)

print(type(run_function))


# inner functions
def outer(a, b):
    def inner(c, d):
        return c + d

    return inner(a, b)


print(outer(1, 2))

# lambda functions
stairs = ["thud", "meow", "thud", "hiss"]


def edit_story(words, func):
    for word in words:
        print(func(word))


edit_story(stairs, lambda word: word.capitalize())


# generators
def my_range(first=0, last=10, step=1):
    number = first

    while number < last:
        yield number
        number += step


ranger = my_range(1, 3)
print(ranger.__next__())
print(ranger.__next__())


# decorators
def document_it(func):
    def new_function(*args, **kwargs):
        print("Running function:", func.__name__)
        print("Positional arguments:", args)
        print("Keyword arguments:", kwargs)
        result = func(*args, **kwargs)
        print("Result:", result)
        return result

    return new_function


@document_it
def add_ints(num_1, num_2):
    return num_1 + num_2


add_ints(1, 2)

# namespaces
animal = "fruitbat"


def change_and_print_global():
    global animal
    animal = "wombat"
    print(f"Inside change_and_print_global: {animal}")


change_and_print_global()
print(animal)


# recursion
def flatten(lol):
    for item in lol:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item


lols = [1, 2, [3, 4, 5], [6, [7, 8, 9], []]]
print(list(flatten(lols)))
