from recipe_scrapers import scrape_me
import get_numbers
import get_units
import get_ingredient
import hello_fresh
import pickle
import food_manager
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
        scraper = scrape_me(url, wild_mode=False)
        yields = get_numbers.get_numbers(scraper.yields())
        if yields == None or yields <= 0:
            yields = 1
        self.ingredients = [build_ingredient(ingredient, yields) for ingredient in scraper.ingredients()]
        try:
            self.title = scraper.title()
        except:
            self.title = "Untitled Recipe"
        self.total_time = scraper.total_time()
        
    def __str__(self):
        ret = "url: {0}\ningredients:".format(self.url)
        if hasattr(self, "ingredient_cache"):
            for ing in self.ingredient_cache:
                quantity, food_item, is_pcs = ing
                ret += "\n" + food_item.name + " " + str(quantity)
        else:
            for ing in self.ingredients:
                ret += "\n" + str(ing)
        return ret + "\n"
    
    def cache_ingredients(self, fm):
        self.ingredient_cache = []
        for num, tokens, is_unit in self.ingredients:
            food = fm.get_food_item_by_tag(tokens)
            if food != None:
                self.ingredient_cache.append((num, food, is_unit))
    
    def __eq__(self, other):
        return self.url == other.url

    def __hash__(self):
        return hash(self.url)

def load_from_pickle(file="recipes.pickle"):
    with open("recipes.pickle", "rb") as file:
        l = pickle.load(file)
        return l

def remove_duplicate_recipes(recipes):
    return list(set(recipes))

def remove_nonsense_recipes(recipes):
    ret = []
    for r in recipes:
        if len(r.ingredients) > 3:
            ret.append(r)
    return ret