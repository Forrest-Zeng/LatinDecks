import requests
import time
import random
from unidecode import unidecode
session = requests.session()
import urllib.request
import urllib.parse

class Translator():
    def __init__(self):
        self.endpoint = "https://latin-words.com/cgi-bin/translate.cgi"
        self.header_choices = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.2420.81",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 14.4; rv:124.0) Gecko/20100101 Firefox/124.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 14_4_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Safari/605.1.15",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 14_4_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
"Mozilla/5.0 (X11; Linux i686; rv:124.0) Gecko/20100101 Firefox/124.0"
        ]


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

        headers = {'User-Agent':random.choice(self.header_choices),
                # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                # 'Accept-Language': 'en-US,en;q=0.5'
                #    'authority':'www.google.com',
                   'accept':'*/*',
                   'Connection': 'keep-alive',
                   }

        # print(headers)

        try:
            req = session.get(self.endpoint,headers=headers,params={"query":demacronized_word}).json()
            print(type(req))
            print(req)
                                       
        except req["status"] != "ok" or req["status"] != "200":
            print("req didn't return ok status")
            print(req["status"])
            raise UserWarning
    
        lines = req["message"].replace('.','').split("\n")
        for i in range(len(lines)):
            # print(i)
            # print(lines[i].split(' '))
            if self.latin_comparison(demacronized_word, lines[i].replace(',','').split(' ')[0]) and not self.latin_comparison(demacronized_word, lines[i+1].replace(',','').split(' ')[0]) and "[" in lines[i]:
                definition = lines[i+1].rstrip()
                try:
                    data = urllib.parse.urlencode({"vanilla_text":lines[i].split("[")[0]}).encode()
                    t_request = urllib.request.Request(url="https://www.latin-is-simple.com/api/vocabulary/macronize/",headers=headers,data=data)
                    term_request = eval(urllib.request.urlopen(t_request).read().decode('utf-8'))
                    # term_request = session.post("https://www.latin-is-simple.com/api/vocabulary/macronize/",data={"vanilla_text":lines[i].split("[")[0]},headers=headers)
                    term = term_request["macronized_text"].replace(',','')
                except:
                    print("Macronization unavailable")
                    term = lines[i].split("[")[0]
                
                return definition, term
            
        for i in range(len(lines)):
            # print(i)
            # print(lines[i].split(' '))
            if "[" in lines[i]:
                definition = lines[i+1].rstrip()
                try:
                    data = urllib.parse.urlencode({"vanilla_text":lines[i].split("[")[0]}).encode()
                    t_request = urllib.request.Request(url="https://www.latin-is-simple.com/api/vocabulary/macronize/",headers=headers,data=data)
                    term_request = eval(urllib.request.urlopen(t_request).read().decode('utf-8'))
                    # term_request = session.post("https://www.latin-is-simple.com/api/vocabulary/macronize/",data={"vanilla_text":lines[i].split("[")[0]},headers=headers)
                    term = term_request["macronized_text"].replace(',','')
                except:
                    print("Macronization unavailable")
                    term = lines[i].split("[")[0]
                return definition, term
        
            

