import spacy

# available languages : fr or en

class Nlp:

    def __init__(self, lang: str):
        if lang == 'fr':
            self.lang = spacy.load('fr_core_news_sm')
        elif lang == 'en':
            self.lang = spacy.load('en_core_web_sm')

    def french(self, sentence: str) -> []:
        fr = [(word.text, word.pos_) for word in self.lang(sentence)]
        return fr

    def english(self, sentence: str) -> []:
        en = [(word.text, word.pos_) for word in self.lang(sentence)]
        return en

    def get_index(self, sentence: str) -> str:
        treat = self.lang(sentence)
        token = treat[1]
        return token.text
