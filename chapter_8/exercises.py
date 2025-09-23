# exercise 1
years_list = [1996, 1997, 1998, 1999, 2000, 2001]

print(f"My third birhday was in {years_list[3]}")
print(f"I was oldest in {years_list[-1]}")

# exercise 2
things = ["mozzarella", "cinderella", "salmonella"]
things[1] = things[1].capitalize()
print(things)

things[0] = things[0].upper()
print(things)

things.remove("salmonella")
print(things)

# exercise 3
surprise = ["Groucho", "Chico", "Harpo"]
surprise[-1] = surprise[-1].lower()[::-1].capitalize()
print(surprise)

# exercise 4
evens = [number for number in range(10) if number % 2 == 0]
print(evens)

# exercise 5
start1 = ["fee", "fie", "foe"]
rhymes = [
    ("flop", "get a mop"),
    ("fope", "turn the rope"),
    ("fa", "get your ma"),
    ("fudge", "call the judge"),
    ("fat", "pet the cat"),
    ("fog", "walk the dog"),
    ("fun", "say we're done"),
]
start2 = "Someone better"

start1_caps = " ".join([word.capitalize() + "!" for word in start1])

for first, second in rhymes:
    print(f"{start1_caps} {first.capitalize()}!")
    print(f"{start2} {second}.")

# exercise 6
questions = [
    "We don't serve strings around here. Are you a string?",
    "What is said on Father's Day in the forest?",
    "What makes the sound 'Sis! Boom! Bah!'?",
]

answers = ["An exploding sheep.", "No, I'm a frayed knot.", "'Pop!' goes the weasel."]

q_a = ((0, 1), (1, 2), (2, 0))

for q, a in q_a:
    print("Q:", questions[q])
    print("A:", answers[a])
    print()
