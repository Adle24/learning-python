# bytes are immutable
my_byte = b"ABC\x01\x02\x03\x41\x42"
print(my_byte)

# conversion
my_list = [1, 2, 3, 255]
the_bytes = bytes(my_list)
print(the_bytes)

print(bytes(range(0, 256)))

hex_string = "FF01616263646566"
from_hex_string = bytes.fromhex(hex_string)
print(from_hex_string)
print(from_hex_string.hex())

# indexing and slicing bytes
print(from_hex_string[0])
print(from_hex_string[3:])

# appending bytes
first_byte = bytes((1, 2, 3))
second_byte = bytes((4, 5, 6))
first_byte += second_byte
print(first_byte)

# repeating bytes
example_byte = bytes((1, 2, 3))
example_byte *= 2
print(example_byte)
