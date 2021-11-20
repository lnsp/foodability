import re
import pickle


def tokenize(s: str) -> list:
    """Returns a list of token for the given string"""
    sentence = re.sub('[^A-Za-z ]+', ' ', s.strip())
    sentence = sentence.lower()
    sentence = sentence.split()
    return sentence


def load_from_pickle(file="recipes.pickle"):
    with open("recipes.pickle", "rb") as file:
        l = pickle.load(file)
        return l


if __name__ == "__main__":
    s = tokenize("red tomato  - hallo - sdsdd - \n")