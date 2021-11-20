import re

def tokenize(s: str) -> list:
    """Returns a list of token for the given string"""
    sentence = re.sub('[^A-Za-z ]+', ' ', s.strip())
    sentence = sentence.lower()
    sentence = sentence.split()
    return sentence


if __name__ == "__main__":
    s = tokenize("red tomato  - hallo - sdsdd - \n")