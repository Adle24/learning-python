import os


# exercise 1
print(os.listdir("./"))
print(os.listdir("../"))

# exercise 2
test_txt = "This is a test of the emergency text system"

with open("./exercise.txt", "wt") as f:
    f.write(test_txt)

with open("./exercise.txt", "rt") as f:
    test_txt = f.read()
    print(test_txt)
