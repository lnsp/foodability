from food_manager import FoodManager, FoodItem
from food_manager import assemble
from recipes_manager import Recipe, remove_duplicate_recipes, remove_nonsense_recipes
from utils import load_from_pickle
from typing import List
from graph import Graph
import random
from bin_packing import pack_bins, calculate_ingredients, init_bins, calculate_waste
from recipe_preselector import RecipePreselector

def init_all():
    recipes = load_from_pickle(file="recipes.pickle")
    food = assemble(food_file="min_food.pickle")
    
    recipes = remove_duplicate_recipes(recipes)
    recipes = remove_nonsense_recipes(recipes)
    
    for r in recipes:
        r.cache_ingredients(food)

    food.filter_by_has_weight()
    return recipes, food, RecipePreselector(food, recipes)

def print_stats(recipes, food, bins):
    ingredient_list = {}
    for b in bins:
        calculate_ingredients(recipes[b], food, ingredient_list, True)
    
    print("Ingredient List")
    for ing, amt in ingredient_list.items():
        print(ing.name, ing.weight, amt)

    print("Recipes")
    for b in bins:
        print(recipes[b])

    print("total waste", calculate_waste(ingredient_list))

if __name__ == "__main__":
    recipes, food, selector = init_all()
    
    tags = ["broccoli"]

    selected_recipe_indices = selector.get_recipes(tags, k=20, size=10)
    selected_recipes = list(map(lambda i: recipes[i], selected_recipe_indices))
    bins = pack_bins(*init_bins(5, selected_recipes), selected_recipes, food)
    
    print_stats(selected_recipes, food, bins)
