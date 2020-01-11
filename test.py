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
        self.assertEqual(treat, 'kitty cat')

    def test_attributes(self):
        lang = Nlp('en')
        treat = lang.attributes("I am a doggy !")
        self.assertIsInstance(treat, list)
        self.assertEqual(treat[0], [0, 1, 2, 3, 4])
        self.assertEqual(treat[1], ['I', 'am', 'a', 'doggy', '!'])
        self.assertEqual(treat[2], [True, True, True, True, False])
        self.assertEqual(treat[3], [False, False, False, False, True])
        self.assertEqual(treat[4], [False, False, False, False, False])

    def test_percentages(self):
        lang = Nlp('en')
        treat = lang.check_percentages('hello, 50%')
        self.assertEqual(treat, 'percentage : 50 %')

if __name__ == '__main__':
    unittest.main()
