import unittest
from helloworld import Nlp
from match import Match
from semantic_similarity import semantic_similarities_docs


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
        self.assertEqual(treat[2], ['nsubj', 'ROOT', 'det', 'attr', 'punct'])
        self.assertEqual(treat[3], [True, True, True, True, False])
        self.assertEqual(treat[4], [False, False, False, False, True])
        self.assertEqual(treat[5], [False, False, False, False, False])

    def test_percentages(self):
        lang = Nlp('en')
        treat = lang.check_percentages('hello, 50%')
        self.assertEqual(treat, 'percentage : 50 %')

    def test_named_entities(self):
        lang = Nlp('en')
        treat = lang.named_entities('I work at Apple and Google')
        self.assertEqual(treat, [('Apple', 'ORG'), ('Google', 'ORG')])

    def test_semantic_similarity(self):
        process = semantic_similarities_docs("Hello i am a cat", "Hello i am a dog")
        self.assertEqual(process, 0.979388603073431)


class TestMatch(unittest.TestCase):

    def test_process_input(self):
        m = Match()
        process = m.process_pattern_on_input('Puppies belong to Elizabeth II', [{'TEXT': 'Elizabeth'}, {'TEXT': 'II'}])
        expect = 'Elizabeth II'
        self.assertEqual(process, expect)

if __name__ == '__main__':
    unittest.main()
