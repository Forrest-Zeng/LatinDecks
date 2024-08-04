import json
from pywhitakers import Translator
import unidecode

class DeckCreator():
    def __init__(self, path):
        self.path = path
        self.TranslatorObject = Translator()
    # derivs = parse_derivatives()
    # print(get_derivative(derivs,"ager"))
    # print(derivs)

    def run_input(self, type,delay=0.1):
        with open(f"{self.path}/input.txt", "r") as r:
            lines = r.readlines()

        result = {}
        failed = []

        for line in lines:
            try:
                definition = self.TranslatorObject.get_term_and_definition(line.rstrip(),type,delay)
                result[definition[1]]=definition[0]
            except:
                print(line.rstrip())
                print("The above word didn't translate right, skipping.")
                failed.append(line.rstrip())

        json_object = json.dumps(result, indent=4)
        
        open(f'{self.path}/output.json', 'w').close()
        with open(f"{self.path}/output.json", "a") as w:
            w.write(json_object)

        print(failed)

    def load_total_dictionary(self):
        dictionary = {}
        names = ["Adjectives","Adverbs","Conjunctions","Exclamations","Interogatives","Nouns","Prepositions","Pronouns","Verbs","Numbers"]
        for i in range(len(names)):
            try:
                with open(f"{self.path}/NLVE{names[i]}.json") as w:
                    json_dictionary = json.load(w)
                    dictionary.update(json_dictionary)
            except:
                print(f'{names[i]} file not detectable')

        return dictionary

    def create_total_json(self, override_dict):
        open(f'{self.path}/output.json', 'w').close()
        with open(f"{self.path}/output.json", "a") as w:
            if override_dict:
                w.write(json.dumps(override_dict, indent=4))
            else:
                w.write(json.dumps(self.load_dictionary, indent=4))

    def create_total_deck(self, override_json="input.json"):
        with open(f"{self.path}/{override_json}") as w:
            vocab = json.load(w)
        words = sorted(vocab.keys())

        failed = []

        open(f'{self.path}/output.txt', 'w').close()
        with open(f"{self.path}/output.txt", "a") as w:
            w.write("#separator:colon\n")
            for word in words:
                try:
                    definition = vocab[word]
                    w.write(f"{definition}:{word}:{unidecode(word[0]).upper()}\n")
                except:
                    print(word.rstrip())
                    print("The above word didn't translate right, skipping.")
                    failed.append(word.rstrip())

        print(failed)

    # create_deck(