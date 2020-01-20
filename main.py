from helloworld import Nlp
from match import Match

if __name__ == '__main__':
    # init class with english or french language
    # 'fr' or 'en'
    nlp = Nlp(lang='en')
    nlp_matcher = Match()

    if nlp.lang == 'fr':
        print(nlp.french('Bonjour, je suis un chaton'))
        print(nlp.get_index("Chaton très mignon !"))
        print(nlp.get_slice("Chaton très mignon !", 1, 4))
    else:
        print(nlp.english('Hi ! Im Abd'))
        print(nlp.get_index("Cute Kitten !"))
        print(nlp.get_slice("Cute Kitten !", 1, 4))
        print(nlp.attributes("I am a doggy !"))
        print(nlp.check_percentages('There is 90% of population that...'))
        print(nlp.named_entities('I work at Google'))

        nlp_matcher.process_pattern_on_input('Hello, I love to listen to Nina Simone !', [{'TEXT': 'Nina'}, {'TEXT': 'Simone'}])