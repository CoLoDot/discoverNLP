import unittest
from helloworld import Nlp


class TestNlp(unittest.TestCase):
    """Test Nlp class"""

    def test_french(self):
        """Test Nlp.french() returns a list"""
        lang = Nlp('fr')
        french = lang.french('Coucou, ça va ?')
        self.assertIsInstance(french, list)

    def test_english(self):
        """Test Nlp.english() returns a list"""
        lang = Nlp('en')
        en = lang.english('hello, whats up ?')
        self.assertIsInstance(en, list)

    def test_get_index(self):
        """Test Nlp.get_index() returns str"""
        lang = Nlp('en')
        treat = lang.get_index('hi i am a kitty')
        self.assertIsInstance(treat, str)

    def test_get_slice(self):
        """Test Nlp.get_slice() returns str"""
        lang = Nlp('en')
        treat = lang.get_slice('Hello kitty cat', 1, 4)
        self.assertIsInstance(treat, str)

if __name__ == '__main__':
    unittest.main()
