from collections import namedtuple


Duck = namedtuple("Duck", "bill tail")
my_duck = Duck("wide orange", "long")
print(my_duck)
