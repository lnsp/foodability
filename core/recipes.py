from recipe_scrapers import scrape_me
import get_numbers
import get_units
import get_ingredient
import hello_fresh
import pickle
from tqdm import tqdm

def build_ingredient(ingredient, yields):
    num = get_numbers.get_numbers(ingredient)
    unit = get_units.get_units(ingredient)
    if num == None:
        num = 1
    if unit == None:
        is_unit = True
    else:
        num = num * unit[0]
        is_unit = False
    tokens = get_ingredient.get_ingredient(ingredient)
    return num, tokens, is_unit

class Recipe:
    def __init__(self, url):
        self.url = url
        scraper = scrape_me(url, wild_mode=True)
        yields = get_numbers.get_numbers(scraper.yields())
        if yields == None or yields <= 0:
            yields = 1

        self.ingredients = [build_ingredient(ingredient, yields) for ingredient in scraper.ingredients()]
    def __str__(self):
        ret = "url: {0}\ningredients:".format(self.url)
        for ing in self.ingredients:
            ret += "\n" + str(ing)
        return ret + "\n"

def load_from_pickle(file="recipes.pickle"):
    with open("recipes.pickle", "rb") as file:
        l = pickle.load(file)
        return l
