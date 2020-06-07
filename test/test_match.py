import pytest
from helloworld import Nlp
from match import Match

class TestMatch:

    def test_process_input(self):
        m = Match()
        process = m.process_pattern_on_input('Puppies belong to Elizabeth II', [{'TEXT': 'Elizabeth'}, {'TEXT': 'II'}])
        expect = 'Elizabeth II'
        assert process == expect