from flask import Flask, request, render_template, send_file
import sys

sys.path.append('.')
app = Flask(__name__)

from LatinDeckCreator import DeckCreator

DeckClient = DeckCreator("outputs")

import random
import os
import collections

@app.route('/')
@app.route('/index.html')
def home():
    return render_template("index.html")


@app.route('/create_deck', methods=['POST'])
def create_deck():
    list_of_files = os.listdir('outputs')
    full_path = ["outputs/{0}".format(x) for x in list_of_files]

    if len(list_of_files) >= 10:
        oldest_file = min(full_path, key=os.path.getctime)
        os.remove(oldest_file)

    lines = request.form['terms'].split('\n')
    print(request.form)
    software = request.form['software']
    print(software)

    internal_deck = DeckClient.create_deck_internal(lines)
    if software == "Quizlet":
        return render_template("copy.html", deck=internal_deck[0], failed=internal_deck[1],duplicates=[item for item, count in collections.Counter(lines).items() if count > 1])
    else:
        ID = random.randint(1, 100000)
        DeckClient.FileHandlerObject.write_text_lines(internal_deck[0],
                                                  output=f'{ID}.txt')

        return render_template("download.html", ID=ID, software=software, failed=internal_deck[1], duplicates=[item for item, count in collections.Counter(lines).items() if count > 1])


@app.route('/download', methods=['GET'])
def download_file():
    ID = request.args['id']
    return send_file(f'outputs/{ID}.txt', as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
