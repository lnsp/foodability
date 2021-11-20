from food_manager import FoodManager
from recipes import Recipe
from utils import load_from_pickle


def get_recipes():
    return load_from_pickle(file="recipes.pickle")

def get_food_items():
    return load_from_pickle(file="food.pickle")