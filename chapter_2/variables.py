# variable naming conventions
# - can contain lowercase letters
# - can contain uppercase letters
# - can contain underscores (_)
# - can contain digits
# - case-sensitive
# - cannot begin with digit, only letters or underscores
# - cannot be python reserved keyword
# list all python keywords
help("keywords")
# ----------------------------------------------------------------------------------------------------------------------


# python types
# Name           | Type     | Mutable | Example
# boolean        | bool     | no      | True, False
# integer        | int      | no      | 47, 25000, 25_000
# floating point | float    | no      | 3.14, 2.7e5
# complex        | complex  | no      | 3j, 5 + 5j
# text sttring   | str      | no      | "kitchen", 'cat', 'a'
# list           | list     | yes     | ["up", "right", "left", "bottom"]
# tuple          | tuple    | no      | (2, 4, 5)
# bytes          | bytes    | no      | b'ab\xff'
# bytearray      | bytearray| yes     | bytearray(...)
# set            | set      | yes     | set([3, 5, 7]), {1, 2, 3}
# frozen set     | frozenset| no      | frozenset(["Ellie", "Joel"])
# dictionary     | dict     | yes     | {"color": "red", "count": 1}
# ----------------------------------------------------------------------------------------------------------------------


# python is dynamically typed language
# variables is just labels for created objects
myNum = 5
print(myNum)
print(id(myNum))

myNum = 6
print(myNum)
print(id(myNum))

# variable deletion
del myNum
# print(myNum) this won't work since varible does not exist anymore
