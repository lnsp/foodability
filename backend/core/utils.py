import re
import pickle

def tokenize(s: str) -> list:
    """Returns a list of token for the given string"""
    sentence = re.sub('[^A-Za-z ]+', ' ', s.strip())
    sentence = sentence.lower()
    sentence = sentence.split()
    return sentence

class RenameUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        renamed_module = module
        if module == "recipes_manager":
            renamed_module = "core.recipes_manager"
        elif module == "food_manager":
            renamed_module = "core.food_manager"

        return super(RenameUnpickler, self).find_class(renamed_module, name)


def load_from_pickle(file="recipes.pickle"):
    with open(file, "rb") as f:
        l = RenameUnpickler(f).load()
        return l


if __name__ == "__main__":
    s = tokenize("red tomato  - hallo - sdsdd - \n")