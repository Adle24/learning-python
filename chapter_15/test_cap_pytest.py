from string import capwords


def cap_function(text: str) -> str:
    return capwords(text)


def test_one_word():
    text = "duck"
    result = cap_function(text)
    assert result == "Duck"


def test_multiple_words():
    text = "a veritable flock of ducks"
    result = cap_function(text)
    assert result == "A Veritable Flock Of Ducks"


def test_words_with_apostrophes():
    text = "I'm fresh out of ideas"
    result = cap_function(text)
    assert result == "I'm Fresh Out Of Ideas"


def test_words_with_quotes():
    text = "'You're despicable!' said Daffy Duck"
    result = cap_function(text)
    assert result == "'You're Despicable!' Said Daffy Duck"
