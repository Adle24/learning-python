# exercise 1
my_bytes = bytes((1, 2, 3, 4, 5))
print(f"The length of my_bytes: {len(my_bytes)}")

# exercise 2
my_bytearray = bytearray((1, 2, 3, 4, 5))
print(f"The length of my_bytearray: {len(my_bytearray)}")

# exercise 3
my_bytes = my_bytearray
print(my_bytes)

my_bytearray = my_bytes
print(my_bytearray)

# exercise 4
print(my_bytearray * 2)
print(my_bytes * 2)
