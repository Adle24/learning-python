import os
import pathlib


print(os.path.realpath("./file.txt"))
file_path = pathlib.Path("eek") / "urk" / "snort.txt"
print(file_path)
