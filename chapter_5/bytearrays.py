# bytearray is like byte but they are mutable
empty_bytearray = bytearray()
print(empty_bytearray)

my_list = [1,2,3,255]
my_bytearray = bytearray(my_list)
print(my_bytearray)

my_tuple = (4, 5, 6)
another_bytearray = bytearray(my_tuple)
print(another_bytearray)

zeroed_bytearray = bytearray(5)
print(zeroed_bytearray)

string_bytearray = bytearray('abc', 'ascii')
print(string_bytearray)

# indexing and slicing
test_bytearray = bytearray(b'\xff\x01abcdef')
print(test_bytearray[2])
print(test_bytearray[4:6])

test_bytearray[1] = 127
print(test_bytearray)

test_bytearray = test_bytearray.replace(b'\xff\x7f', b'XYZ')
print(test_bytearray)

test_bytearray.insert(-1, 3)
print(test_bytearray)

test_bytearray.append(42)
print(test_bytearray)

test_bytearray.extend(b'!!!')
print(test_bytearray)