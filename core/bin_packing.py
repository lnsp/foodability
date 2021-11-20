import random
import math

import food_manager
import recipes_manager
from food_manager import FoodItem
from recipes_manager import Recipe
from utils import load_from_pickle

def calculate_ingredients(recipe, food_manager, ingredient_list):
    """
    Adds to ingredient_list the needed ingredients and their quantities
    """
    for ing in recipe.ingredients:
        quantity, tags, is_pcs = ing
        food_item = food_manager.get_food_item_by_tag(tags)
        
        q = quantity
        if (not is_pcs) and food_item.weight > 0:
            q /= food_item.weight
        
        ingredient_list.setdefault(food_item, 0)
        ingredient_list[food_item] += q
    


def compute_score(plan, recipes, food_manager):
    ingredient_list = {}
    for recipe_idx in plan:
        calculate_ingredients(recipes[recipe_idx], food_manager, ingredient_list)
    
    for ing, amt in ingredient_list.items():
        print(ing.name, ing.weight, amt, ing.image_url)



def pack_bins(days, recipes, food_manager):
    bins = [random.randrange(recipes) for _ in range(days)]
    print(bins)

if __name__ == "__main__":
    recipes = load_from_pickle(file="recipes.pickle")
    food_manager = food_manager.assemble(food_file="food.pickle")
    compute_score([0,1,2], recipes, food_manager)