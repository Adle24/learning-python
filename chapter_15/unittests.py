import unittest
from string import capwords


def cap_function(text: str) -> str:
    return capwords(text)


class TestCapitalization(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_one_word(self):
        text = "duck"
        result = cap_function(text)
        self.assertEqual(result, "Duck")

    def test_multiple_words(self):
        text = "a veritable flock of ducks"
        result = cap_function(text)
        self.assertEqual(result, "A Veritable Flock Of Ducks")

    def test_words_with_apostrophe(self):
        text = "I'm fresh out of ideas"
        result = cap_function(text)
        self.assertEqual(result, "I'm Fresh Out Of Ideas")


if __name__ == "__main__":
    unittest.main()
