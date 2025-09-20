myInteger = 5
zeroInteger = 0
prefixedInteger = +123
negativeInteger = -123
separatedInteger = 1_000_000

print(myInteger)
print(zeroInteger)
print(prefixedInteger)
print(negativeInteger)
print(separatedInteger)

# operations
print(1 + 2)
print(1 - 2)
print(2 * 5)
print(3 / 2)
print(3 // 2)
print(7 % 3)
print(2**10)

# assignment
myNum = 2
print(myNum + 3)

myNum += 3
print(myNum)

myNum -= 4
print(myNum)

myNum *= 2
print(myNum)

# contrling precedence with ()
print(2 + 3 * 4)
print((2 + 4) * 4)

# base literals
print(f"Decimal: {10}")
print(f"Binary: {0b10}")
print(f"Octal: {0o10}")
print(f"Hexadecimal: {0x10}")

print(bin(73))
print(oct(73))
print(hex(73))

# type conversions
print(int(True))
print(int(False))
print(int(67.3))
print(int(-56.4))
print(int("-28"))
print(int("1_000_000"))
print(True + 2)
