import copy
from itertools import zip_longest

# list creation
empty_list = []
print(empty_list)

weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
print(weekdays)

another_empty_list = list()
print(another_empty_list)

string_list = list("cart")
print(string_list)

# conversion
my_tuple = (1, 2, 3)
converted_list = list(my_tuple)
print(converted_list)

talk_like_pirate = "9/19/2024"
splitted_list = talk_like_pirate.split("/")
print(splitted_list)

# indexing and slicing
marxes = ["Groucho", "Chico", "Harpo"]
print(marxes[0])
print(marxes[-1])
print(marxes[:-1])
print(marxes[::-1])

# list methods
marxes.reverse()
print(marxes)

marxes.append("Zeppo")
print(marxes)

marxes.insert(2, "Gummo")
print(marxes)

print(["blah"] * 4)

other = ["Karl"]
marxes.extend(other)
print(marxes)

marxes[2] = "Wanda"
print(marxes)

del marxes[-1]
print(marxes)

marxes.remove("Wanda")
print(marxes)

chico = marxes.pop(1)
print(chico)
print(marxes)

test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test_list.clear()
print(test_list)

harpo_index = marxes.index("Harpo")
print(harpo_index)

if "Groucho" in marxes:
    print("Groucho is out brother")

zeppo_count = marxes.count("Zeppo")
print(zeppo_count)

sorted_marxes = sorted(marxes)
print(marxes)
print(sorted_marxes)

marxes.sort()
print(marxes)

print(len(marxes))

# copying a list
numbers = [1, 2, 3]
numbers_copy = numbers.copy()
another_numbers_copy = numbers[:]
yet_another_numbers_copy = list(numbers)
deep_copy_numbers = copy.deepcopy(numbers)

numbers[0] = -1
print(numbers)
print(another_numbers_copy)
print(yet_another_numbers_copy)
print(numbers_copy)
print(deep_copy_numbers)

# iteration
cheeses = ["brie", "gjetost", "havarti"]

for cheese in cheeses:
    print(cheese)

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
fruits = ["apple", "banana", "orange"]
drinks = ["coffee", "milk", "tea"]

for day, fruit, drink in zip(days, fruits, drinks):
    print(f"{day}: drink {drink} - eat {fruit}!")

for day, fruit, drink in zip_longest(days, fruits, drinks, fillvalue="TBD"):
    print(f"{day}: drink {drink} - eat {fruit}!")

english = "Monday", "Tuesday", "Wednesday"
french = "Lundi", "Mardi", "Mercred"

word_dictionary = zip(english, french)
print(dict(word_dictionary))

# list comprehensions
list_comp = [number for number in range(1, 6)]
print(list_comp)

odd_numbers = [number for number in range(1, 11) if number % 2 != 0]
print(odd_numbers)
