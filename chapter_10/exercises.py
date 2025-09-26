# exercise 1
def good():
    return ["Harry", "Ron", "Hermione"]


# exercise 2
def get_odds():
    for num in range(10):
        if num % 2 == 1:
            yield num


for index, num in enumerate(get_odds()):
    if index == 2:
        print(num)


# exercise 3
def test(func):
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result

    return wrapper


@test
def add(a, b):
    return a + b


print(add(1, 2))


# exercise 4
class OopsException(Exception):
    pass


try:
    print("Raising exception")
    raise OopsException
except OopsException:
    print("Caught an Oops")
