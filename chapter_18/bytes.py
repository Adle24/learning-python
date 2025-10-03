import struct
import binascii


valid_png_header = b"\x89PNG\r\n\x1a\n"
data = b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00\xc0"

if data[:8] == valid_png_header:
    width, height = struct.unpack(">LL", data[16:24])
    print(f"Valid PNG, width: {width}, height: {height}")
else:
    print("Invalid PNG")


# byte conversion
print(binascii.hexlify(valid_png_header))
print(binascii.unhexlify(b"89504e470d0a1a0a"))

# bit operators
print(1 & 3)
print(1 | 3)
print(1 ^ 3)
print(~1)
print(1 << 1)
print(2 >> 1)