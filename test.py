import unittest
from helloworld import Nlp


class MyTestCase(unittest.TestCase):
    def test_french(self):
        lang = Nlp('fr')
        french = lang.french('Coucou, ça va ?')
        self.assertIsInstance(french, list)

    def test_english(self):
        lang = Nlp('en')
        en = lang.english('hello, whats up ?')
        self.assertIsInstance(en, list)

    def test_get_index(self):
        lang = Nlp('en')
        treat = lang.get_index('hi i am a kitty')
        self.assertIsInstance(treat, str)

if __name__ == '__main__':
    unittest.main()
