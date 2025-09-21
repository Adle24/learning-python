# exercise 1
secret = 6
guess = 6

if guess < secret:
    print("too low")
elif guess > secret:
    print("too high")
else:
    print("just right")

# exercise 2
small = True
green = False

if small:
    if green:
        print("pea")
    else:
        print("cherry")
else:
    if green:
        print("watermelon")
    else:
        print("pumpkin")
