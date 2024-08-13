import requests
import time
from unidecode import unidecode
session = requests.session()

class Translator():
    def __init__(self):
        self.endpoint = "https://latin-words.com/cgi-bin/translate.cgi"

    def __main__(self):
        ...

    def latin_comparison(self,word1,word2):
        if len(word1) != len(word2):
            return False
        if word1==word2:
            return True
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                continue
            elif word1[i] == "i" and word2[i] == "j":
                continue
            elif word2[i] == "i" and word1[i] == "j":
                continue
            elif word1[i] == "u" and word2[i] == "v":
                continue
            elif word2[i] == "u" and word1[i] == "v":
                continue
            else:
                return False
        return True

    def get_term_and_definition(self,word,delay=0.1):

        # print(word)

        demacronized_word = unidecode(word.rstrip())            

        time.sleep(delay)

        try:
            req = session.get(self.endpoint,params={"query":demacronized_word})
        except req.json()["status"] != "ok":
            print(req.json()["status"])
            raise UserWarning
    
        lines = req.json()["message"].replace('.','').split("\n")
        for i in range(len(lines)):
            # print(i)
            # print(lines[i].split(' '))
            if self.latin_comparison(demacronized_word, lines[i].replace(',','').split(' ')[0]) and not self.latin_comparison(demacronized_word, lines[i+1].replace(',','').split(' ')[0]) and "[" in lines[i]:
                definition = lines[i+1].rstrip()
                print(session.post("https://www.latin-is-simple.com/api/vocabulary/macronize/",data={"vanilla_text":lines[i].split("[")[0]}).status)
                term = session.post("https://www.latin-is-simple.com/api/vocabulary/macronize/",data={"vanilla_text":lines[i].split("[")[0]}).json()["macronized_text"].replace(',','')
                return definition, term
            
        for i in range(len(lines)):
            # print(i)
            # print(lines[i].split(' '))
            if "[" in lines[i]:
                definition = lines[i+1].rstrip()
                term = session.post("https://www.latin-is-simple.com/api/vocabulary/macronize/",data={"vanilla_text":lines[i].split("[")[0]}).json()["macronized_text"].replace(',','')
                return definition, term
        
            

