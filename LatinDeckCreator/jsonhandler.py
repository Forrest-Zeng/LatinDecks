import json

class JsonHandler():
    def __init__(self, path):
        self.path = path
    
    def create_json(self, dict):
        open(f'{self.path}/output.json', 'w').close()
        with open(f"{self.path}/output.json", "a") as w:
            w.write(json.dumps(dict, indent=4))

    def load_dictionary_json(self, file="input.json"):
        with open(f"{self.path}/{file}") as w:
            return json.load(w)
        