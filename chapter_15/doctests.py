import doctest
from string import capwords


def cap_function(text: str) -> str:
    return capwords(text)


if __name__ == "__main__":
    doctest.testmod()
