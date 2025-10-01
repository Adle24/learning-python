from pprint import pprint
from typing import OrderedDict
import logging


# assertions
my_number = 6

assert my_number == 6
assert my_number > 5
# assert my_number < 2, "Is it true?"


# printing
def func(*args, **kwargs):
    print(vars())


func(1, 2, 3, 4, 5)
func([1, 2, 3])

# f-strings
my_var = "thing"
print(f"{my_var = }")
print(f"{10 / 2 = }")

# pretty print
quotes = OrderedDict(
    [
        ("Moe", "A wise guy, huh?"),
        ("Larry", "Ow!"),
        ("Curly", "Nyuk nyuk!"),
    ]
)

print(quotes)
pprint(quotes)

# logging
logging.debug("looks like rain")
logging.info("and hail")
logging.warning("did i hear a thunder")
logging.error("did i hear a roar")
logging.critical("stop fencing bullshit")


# python debugger
def process_cities(filename):
    with open(filename, "rt") as file:
        for line in file:
            line = line.strip()
            if "quit" in line.lower():
                return
            country, city = line.split(",")
            city = city.strip()
            country = country.strip()
            print(city.title(), country.title(), sep=",")
