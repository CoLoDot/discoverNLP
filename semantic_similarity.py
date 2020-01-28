import spacy

nlp = spacy.load('en_core_web_md')

def semantic_similarities_docs(doc_1: str, doc_2: str) -> float:
    process_1 = nlp(doc_1)
    process_2 = nlp(doc_2)
    return process_1.similarity(process_2)

def dimensional_vector(doc: str) -> []:
    d = nlp(doc)
    print(d[2])
    return d[2].vector

if __name__ == '__main__':
    print(semantic_similarities_docs("Hello i am a cat", "Hello i am a dog"))
    print(dimensional_vector("I love strawberries"))