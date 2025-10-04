import binascii
import struct


# exercise 1
gif = binascii.unhexlify(
    b"47494638396101000100800000000000ffffff21f90401000000002c000000000100010000020144003b"
)
print(gif)

# exercise 2
width, height = struct.unpack("<hh", gif[6:10])
print(width, height)
