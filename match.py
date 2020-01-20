import spacy
from spacy.matcher import Matcher


class Match:
    """Class uses spacy.matcher()"""

    def __init__(self):
        self.match_lang = spacy.load('en_core_web_sm')
        self.matcher = Matcher(self.match_lang.vocab)

    def process_pattern_on_input(self, sentence: str, pattern: list) -> str:
        self.matcher.add('PATTERN', None, pattern)
        doc = self.match_lang(sentence)
        matches = self.matcher(doc)

        for span_id, start, end in matches:
            span = doc[start:end]
            print(span.text)
            return span.text
