# exercise 1
e2f = {
    "dog": "chien",
    "cat": "chat",
    "walrus": "morse",
}

print(f"French of walrus is {e2f['walrus']}")

f2e = {}

for k, v in e2f.items():
    f2e[v] = k

print(f"French ton english dictionary is {f2e}")
print(f"English of chien is {f2e['chien']}")
print(f"English words are {list(e2f.keys())}")

# exercise 2
life = {
    "animals": {
        "cats": ["Henri", "Grumpy", "Lucy"],
        "octopi": {},
        "emus": {},
    },
    "plants": {},
    "others": {},
}

print(f"Top level keys of life: {list(life.keys())}")
print(f"Keys of life[animals]: {list(life["animals"].keys())}")
print(f"Values of life[animals][cats]: {list(life["animals"]["cats"])}")

# exercise 3
squares = {num: num ** 2 for num in range(10)}
print(squares)

# exercise 4
odds = {num for num in range(10) if num % 2 == 1}
print(odds)

# exercise 5
my_gen_comprehension = (f"Got {number}" for number in range(10))

for number in my_gen_comprehension:
    print(number)

# exercise 6
key_tuple = ("optimist", "pessimist", "troll")
value_tuple = ("'The glass is half full", "The glass is half empty", "How did you get a glass?")

print(dict(zip(key_tuple, value_tuple)))

# exercise 7
titles = ['Creature of Habit', 'Crewel Fate', 'Sharks On a Plane']
plots = ['A nun turns into a monster', 'A haunted yarn shop', 'Check your exits']

print(dict(zip(titles, plots)))
