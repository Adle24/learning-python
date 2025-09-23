# tuple creation
empty_tuple = ()
print(empty_tuple)

one_element_tuple = ("Groucho",)
print(one_element_tuple)

another_one_element_tuple = ("Groucho",)
print(another_one_element_tuple)

not_tuple = "Groucho"
print(not_tuple)

my_tuple = ("Groucho", "Chico", "Harpo")
print(my_tuple)

# tuple unpacking
first_name, second_name, third_name = my_tuple
print(first_name, second_name, third_name)

# variable swapping
password = "swordfish"
icecream = "tuttifrutti"
password, icecream = icecream, password
print(password)
print(icecream)

# conversion
my_list = ["Groucho", "Chico", "Harpo"]
print(tuple(my_list))
print(tuple("abc"))
print(tuple(b"\x01\x02\x03"))

# indexing
number_tuple = (1, 2, 3)
print(number_tuple[0])
print(number_tuple[-1])

# combining and repeating
print((1,) + (1, 2))
print((1, 3, 4) * 3)

# comparison
first_tuple = (7, 2)
second_tuple = (7, 2, 9)

print(first_tuple == second_tuple)
print(first_tuple < second_tuple)
print(first_tuple > second_tuple)

# iteration
words = ("fresh", "out", "of", "ideas")

for word in words:
    print(word)
