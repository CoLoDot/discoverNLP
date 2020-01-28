import spacy

class Nlp:
    """'Nlp' is for Natural Language Processing.
    AVAILABLE LANGUAGES : french or english"""

    def __init__(self, lang: str):
        """Nlp.__init__() constructs
        an object by loading the
        choosen language : 'fr' or 'en'"""
        if lang == 'fr':
            self.lang = spacy.load('fr_core_news_sm')
        elif lang == 'en':
            self.lang = spacy.load('en_core_web_md')

    def french(self, sentence: str) -> []:
        """Nlp.french() takes an str obj and returns a list"""
        fr = [(word.text, word.pos_) for word in self.lang(sentence)]
        return fr

    def english(self, sentence: str) -> []:
        """Nlp.english() takes an str obj and returns a list"""
        en = [(word.text, word.pos_) for word in self.lang(sentence)]
        return en

    def get_index(self, sentence: str) -> str:
        """Nlp.get_index() takes an str obj and returns a str"""
        treat = self.lang(sentence)
        token = treat[1]
        return token.text

    def get_slice(self, sentence: str, from_: int, to_: int) -> str:
        """Nlp.get_slice() takes an str obj and return a slice of it int str"""
        treat = self.lang(sentence)
        spaning = treat[int(from_):int(to_)]
        return spaning.text

    def attributes(self, sentence: str) -> []:
        treat = self.lang(sentence)
        treat_id = [token.i for token in treat]
        treat_text = [token.text for token in treat]
        treat_dependency = [token.dep_ for token in treat]
        treat_is_alpha = [token.is_alpha for token in treat]
        treat_is_punct = [token.is_punct for token in treat]
        treat_like_num = [token.like_num for token in treat]
        return [treat_id, treat_text, treat_dependency, treat_is_alpha, treat_is_punct, treat_like_num]

    def check_percentages(self, sentence: str) -> str:
        treat = self.lang(sentence)
        for element in treat:
            if element.like_num:
                next_elm = treat[element.i + 1]
                if next_elm.text == '%':
                    return "percentage : " + element.text + " %"

    def named_entities(self, sentence: str) -> []:
        treat = self.lang(sentence)
        return [(t.text, t.label_) for t in treat.ents]

    def semantic_similarities_docs(self, doc_1: str, doc_2: str) -> float:
        process_1 = self.lang(doc_1)
        process_2 = self.lang(doc_2)
        return process_1.similarity(process_2)