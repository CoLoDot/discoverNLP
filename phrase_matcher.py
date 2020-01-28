import spacy
from spacy.matcher import PhraseMatcher


def matcher_golden_retriever(sentence: str):
    nlp = spacy.load("en_core_web_sm")
    matcher = PhraseMatcher(nlp.vocab)
    pattern = nlp("Golden Retriever")
    matcher.add('DOG', None, pattern)
    doc = nlp(sentence)

    for match_id, start, end in matcher(doc):
        span = doc[start:end]
        print("Match : ", span.text)
        return span.text


if __name__ == '__main__':
    matcher_golden_retriever('I love Golden Retriever !')
