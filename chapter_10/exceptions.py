# error handling
my_list = [1, 2, 3]
position = 5

try:
    my_list[position]
except IndexError:
    print(f"Need a position between 0 and {len(my_list) - 1}, but got {position}")
except Exception as e:
    print(f"Something else went wrong, {e}")
finally:
    print("Got it!")


# custom exceptions
class UppercaseException(Exception):
    pass


words = ["hello", "world", "LOL"]

for word in words:
    if word.isupper():
        raise UppercaseException(word)
