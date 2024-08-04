import sys
sys.path.append(".")

from pywhitakers import Translator

class DeckWriter():
    def __init__(self, path):
        self.path = path
        self.TranslatorObject = Translator()
    # derivs = parse_derivatives()
    # print(get_derivative(derivs,"ager"))
    # print(derivs)    

    def translate_list(self, lines, delay=0.1):

        result = {}
        failed = []

        for line in lines:
            try:
                definition = self.TranslatorObject.get_term_and_definition(line.rstrip(),delay)
                result[definition[1]]=definition[0]
            except:
                print(line.rstrip())
                print("The above word didn't translate right, skipping.")
                failed.append(line.rstrip())
        print(failed)
        return result,failed

    def return_deck(self, words, delay=0.1):
        translated_tuple = self.translate_list(words,delay)
        word_dictionary = translated_tuple[0]
        terms = sorted(word_dictionary.keys())

        string = ''
        for term in terms:
            definition = word_dictionary[term].rstrip()
            # print(term)
            # print(definition)
            string+=f'{definition}:{term}\n'

        return string,translated_tuple[1]
    



