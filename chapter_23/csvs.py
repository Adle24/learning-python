import csv


villains = [
    ["Doctor", "No"],
    ["Rosa", "Klebb"],
    ["Mister", "Big"],
    ["Auric", "Goldfinger"],
    ["Ernst", "Blogeld"],
]

with open("villains", "wt") as file:
    csvout = csv.writer(file, lineterminator="\n")
    csvout.writerows(villains)

with open("villains", "rt") as file:
    cin = csv.reader(file)
    villains = [row for row in cin]
    print(villains)

with open("villains", "rt") as file:
    cin = csv.DictReader(file, fieldnames=["first", "last"])
    villains = [row for row in cin]
    print(villains)
