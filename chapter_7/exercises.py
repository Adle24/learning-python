# exercise 1
for num in range(3, -1, -1):
    print(num)

# exercise 2
guess_me = 7
num = 7

while True:
    if num < guess_me:
        print("Too low")
    elif num > guess_me:
        print("Too high")
        break
    else:
        print("Found it")
        break

# exercise 3
guess_me = 5

for num in range(10):
    if num < guess_me:
        print("Too low")
    elif num > guess_me:
        print("Oops")
        break
    else:
        print("Found it")
        break
