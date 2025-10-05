import os
import shutil


print(os.path.exists("./file.txt"))
print(os.path.isfile("./file.txt"))
print(os.path.isdir("./file.txt"))
print(
    os.path.isabs(
        "C:\\Users\\adlep\\PycharmProjects\\learning-python\\chapter_20\\file.txt"
    )
)
shutil.copy("./file.txt", "./fily.txt")
os.rename("./fily.txt", "./fil.txt")
os.remove("./fil.txt")
