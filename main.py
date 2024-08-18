from flask import Flask, request, render_template, send_file

app = Flask(__name__)

import sys

sys.path.append('.')

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

    ID = random.randint(1, 100000)
    lines = request.form['terms'].split('\n')

    internal_deck = DeckClient.create_deck_internal(lines)
    DeckClient.FileHandlerObject.write_text_lines(internal_deck[0],
                                                  output=f'{ID}.txt')

    return render_template("download.html", ID=ID, failed=internal_deck[1], duplicates=[item for item, count in collections.Counter(lines).items() if count > 1])


@app.route('/download', methods=['GET'])
def download_file():
    ID = request.args['id']
    return send_file(f"outputs/{ID}.txt", as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
