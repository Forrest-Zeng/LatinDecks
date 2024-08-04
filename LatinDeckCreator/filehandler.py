class FileHandler():
    def __init__(self, path):
        self.path = path

    def read_text_lines(self, file="input.txt"):
        with open(f"{self.path}/{file}", "r") as r:
            return r.readlines()
    
    def write_text_lines(self, string, output="output.txt", append=False, delay=0.1):
        if not append:
            open(f'{self.path}/{output}', 'w').close()
        with open(f"{self.path}/{output}", "a") as w:
            w.write(string)
        
        print(f"Deck has been exported to {output}")
