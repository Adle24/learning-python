# exercise 1
def pointless(param: dict[str, int]) -> None:
    key = list(param.keys())[0].capitalize()
    value = list(param.values())[0] + 1

    print(key, value)

pointless({'key': 1})