import sys
sys.path.append(".")
from LatinDeckCreator import DeckCreator

test = DeckCreator("LatinDeckCreator/test_path")

print(test.create_deck_textfile())