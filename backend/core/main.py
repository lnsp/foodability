from .food_manager import FoodManager, FoodItem
from .food_manager import assemble
from .recipes_manager import Recipe, remove_duplicate_recipes, remove_nonsense_recipes
from .utils import load_from_pickle
from typing import List
from .graph import Graph
import random
from .bin_packing import pack_bins, calculate_ingredients, init_bins, calculate_waste
from .recipe_preselector import RecipePreselector
from .bin_packing import get_total_packaging

def init_all(food_pickle="min_food.pickle", recipe_pickle="recipes.pickle"):
    recipes = load_from_pickle(file=recipe_pickle)
    food = assemble(food_file=food_pickle)
    
    recipes = remove_duplicate_recipes(recipes)
    recipes = remove_nonsense_recipes(recipes)
    
    for r in recipes:
        r.cache_ingredients(food)

    food.filter_by_has_weight()
    return recipes, food, RecipePreselector(food, recipes)

def print_stats(recipes, food, bins):
    ingredient_list = {}
    for b in bins:
        calculate_ingredients(b, food, ingredient_list, True)
    
    print("Ingredient List")
    for ing, amt in ingredient_list.items():
        print(ing.name, ing.weight, amt)

    print("Recipes")
    for b in bins:
        print(b)

    print("total waste", calculate_waste(ingredient_list))

    print(get_total_packaging(ingredient_list))
