# type hints
palindrome: str = "was it a car or a cat i saw"
nays: dict[str, str] = {"horse": "neigh", "pedant": "nay", "genealogist": "awee"}
myNumber: int | float = 3.14
quantumValue: float | None = None

print(myNumber)
print(palindrome)
print(nays)
print(quantumValue)


# function hints
def num_to_str(num: int) -> str:
    return str(num)


def no_return() -> None:
    print("Hey!")


print(num_to_str(myNumber))
no_return()


# docstrings
def echo(something: str) -> None:
    """
    fucntion for prinitng on console
    :param something: str
    :return: None
    """
    print(something)
