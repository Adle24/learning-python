import copy

from chapter_6.conditionals import vowels

# dictionary creation
empty_dict = {}
print(f"This is an empty dictionary: {empty_dict}")

bierce_dict = {
    "day": "A period of twenty-four hours, mostly misspent",
    "positive": "Mistaken at the top of one's voice",
    "misfortune": "The kind of fortune that never misses",
}

print(f"Bierce Dictionary: {bierce_dict}")

acme_customer = dict(first="Wile", middle="E", last="Coyote")
print(f"Acme Customer: {acme_customer}")

# conversion to dict
lol = [["a", "b"], ["c", "d"], ["e", "f"]]
converted_dict = dict(lol)
print(f"Converted Dictionary: {converted_dict}")

# accessing dictionary elements
pythons = {
    "Chapman": "Graham",
    "Cleese": "John",
    "Idle": "Eric",
    "Jones": "Terry",
    "Palin": "Michael",
    "Gilliam": "Terry",
}

print(f"Pythonistas: {pythons}")
print(f"Cleese's firstname: {pythons['Cleese']}")
print(f"Idle's firstname: {pythons.get('Idle')}")
print(f"Askar's firstname: {pythons.get('Askar', 'No such Pythonista')}")

# dictionary iteration
accusation = {"room": "ballroom", "weapon": "lead pipe", "person": "Col. Mustard"}

for card in accusation:
    print(card)

for card in accusation.keys():
    print(card)

for value in accusation.values():
    print(value)

for card, value in accusation.items():
    print(f"{card} has value: {value}")

# dictionary methods
test_dict = {"color": "red", "quantity": 4, "size": "large"}

print(f"The length of test_dict is: {len(test_dict)}")

additional_dict = {"has_price": True, "angle": "acute"}
final_dict = {**test_dict, **additional_dict}
union_dict = test_dict | additional_dict

test_dict.update(additional_dict)

print(f"Updated test_dict is: {test_dict}")
print(f"Final dictionary is: {final_dict}")
print(f"Union dictionary is: {union_dict}")

del test_dict["color"]
print(f"Updated test_dict is: {test_dict}")

test_dict.pop("quantity")
print(f"Updated test_dict is: {test_dict}")

test_dict.clear()
print(f"Updated test_dict is: {test_dict}")

print(f"Is Adilet Pythonista: {'Adilet' in pythons}")

# copying dictionaries
signals = {"green": "go", "yellow": "go faster", "red": "smile for the camera"}

copied_signals = signals
another_signals = signals.copy()
deep_signals_copy = copy.deepcopy(signals)

signals["blue"] = "confuse everyone"

print(f"Original signlas: {signals}")
print(f"Copied signals: {copied_signals}")
print(f"Another copied signals: {another_signals}")
print(f"Deep copied signals: {deep_signals_copy}")

# dictionary comparison (works only == and !=)
first_dict = {1: 1, 2: 2, 3: 3}
second_dict = {4: 4, 5: 5, 6: 6}
third_dict = {1: 1, 2: 2, 3: 3}

print(first_dict == second_dict)
print(first_dict == third_dict)

# dictionary comprehensions
word = "letters"

letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)

me_vowels = "aeiou"
word = "onomatopoeia"

vowel_counts = {letter: word.count(letter) for letter in word if letter in vowels}
print(vowel_counts)
