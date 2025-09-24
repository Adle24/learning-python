# set creation
empty_set = set()
print(f"Empty set is: {empty_set}")

evens_set = {0, 2, 4, 6, 8}
print(f"Evens set is: {evens_set}")

my_set = set("letters")
print(f"My set is: {my_set}")

# length of set
print(f"The length of the set is: {len(my_set)}")

# adding elements
my_set.add("m")
print(f"My set is: {my_set}")

# removing elements
my_set.remove("m")
print(f"My set is: {my_set}")

# combining sets
first_set = {1, 3, 5}
second_set = {2, 4, 6}

print(first_set | second_set)

# iteration
for item in my_set:
    print(item)

# test for inclusion
drinks = {
    "martini": {"vodka", "vermouth"},
    "black russian": {"vodka", "kahlua"},
    "white russian": {"cream", "kahlua", "vodka"},
    "manhattan": {"rye", "vermouth", "bitters"},
    "screwdriver": {"orange juice", "vodka"},
}

for name, contents in drinks.items():
    if "vodka" in contents:
        print(name)

# set operations
for name, contents in drinks.items():
    if contents & {"vermouth", "orange juice"}:
        print(name)

a_set = {1, 2, 3}
b_set = {2, 3}

print(a_set & b_set)
print(a_set | b_set)
print(a_set - b_set)
print(a_set ^ b_set)

print(a_set.issubset(b_set))
print(a_set.issuperset(b_set))

# set comprehensions
test_set = {number for number in range(1, 6) if number % 3 == 1}
print(test_set)

# immutable sets
immutable_set = frozenset({1, 2, 3})
print(immutable_set)
