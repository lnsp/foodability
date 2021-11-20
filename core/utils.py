import re
import pickle
from food_manager import FoodItem
from recipes_manager import Recipe

def tokenize(s: str) -> list:
    """Returns a list of token for the given string"""
    sentence = re.sub('[^A-Za-z ]+', ' ', s.strip())
    sentence = sentence.lower()
    sentence = sentence.split()
    return sentence


def load_from_pickle(file="recipes.pickle"):
    with open(file, "rb") as f:
        l = pickle.load(f)
        return l


if __name__ == "__main__":
    s = tokenize("red tomato  - hallo - sdsdd - \n")