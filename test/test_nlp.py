import pytest
from helloworld import Nlp
from semantic_similarity import semantic_similarities_docs
from phrase_matcher import matcher_golden_retriever

class TestNlp:
    """Test Nlp class"""

    def test_french(self):
        """Test Nlp.french() returns a list"""
        lang = Nlp('fr')
        french = lang.french('Coucou, ça va ?')
        assert isinstance(french, list)

    def test_english(self):
        """Test Nlp.english() returns a list"""
        lang = Nlp('en')
        en = lang.english('hello, whats up ?')
        assert isinstance(en, list)

    def test_get_index(self):
        """Test Nlp.get_index() returns str"""
        lang = Nlp('en')
        treat = lang.get_index('hi i am a kitty')
        assert isinstance(treat, str)

    def test_get_slice(self):
        """Test Nlp.get_slice() returns str"""
        lang = Nlp('en')
        treat = lang.get_slice('Hello kitty cat', 1, 4)
        assert isinstance(treat, str)
        assert treat == 'kitty cat'

    def test_attributes(self):
        lang = Nlp('en')
        treat = lang.attributes("I am a doggy !")
        assert isinstance(treat, list)
        assert treat[0] == [0, 1, 2, 3, 4]
        assert treat[1] == ['I', 'am', 'a', 'doggy', '!']
        assert treat[2] == ['nsubj', 'ROOT', 'det', 'attr', 'punct']
        assert treat[3] == [True, True, True, True, False]
        assert treat[4] == [False, False, False, False, True]
        assert treat[5] == [False, False, False, False, False]

    def test_percentages(self):
        lang = Nlp('en')
        treat = lang.check_percentages('hello, 50%')
        assert treat == 'percentage : 50 %'

    def test_named_entities(self):
        lang = Nlp('en')
        treat = lang.named_entities('I work at Apple and Google')
        assert treat == [('Apple', 'ORG'), ('Google', 'ORG')]

    def test_semantic_similarity(self):
        process = semantic_similarities_docs("Hello i am a cat", "Hello i am a dog")
        assert process == 0.979388603073431

    def test_phrase_matcher(self):
        process = matcher_golden_retriever("Cute Golden Retriever !!")
        assert process == "Golden Retriever"
