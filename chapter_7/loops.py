# while loop
count = 1

while count <= 5:
    print(count)
    count = count + 1

# break statement
while True:
    stuff = input("String to capitalize (type q to quit): ")
    if stuff.lower() == "q":
        break

    print(stuff.capitalize())

# continue statement
while True:
    value = input("Integer, please (q to quit): ")

    if value.lower() == "q":
        break

    number_to_square = int(value)

    if number_to_square % 2 == 0:
        continue

    print(f"{number_to_square} squared is {number_to_square**2}")

# else block in loops
numbers = [1, 3, 5]
position = 0

while position < len(numbers):
    result_number = numbers[position]

    if result_number % 2 == 0:
        print(f"Found even number {result_number}")
        break

    position = position + 1
else:
    print("No even number found")

# for loop
word = "thud"

for letter in word:
    print(letter)

for letter in word:
    if letter.lower() == "u":
        break

    print(letter)

for letter in word:
    if letter.lower() == "x":
        print("Eek! An x!")
        break

    print(letter)
else:
    print("No x there!")

# ranges
for num in range(0, 3):
    print(num)
