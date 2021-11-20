import random
import math
import copy

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
        if food_item != None:
            #print(tags, food_item.name)
            q = quantity
            if (not is_pcs) and food_item.weight > 0:
                q /= food_item.weight
            
            ingredient_list.setdefault(food_item, 0)
            ingredient_list[food_item] += q
        else: 
            return False
    return True

def calculate_waste(ingredient_list):
    waste = 0
    for ing, q in ingredient_list.items():
        overshoot = math.ceil(q) - q
        waste += overshoot * ing.weight
    return waste

def compute_score(plan, recipes, food_manager):
    ingredient_list = {}
    for recipe_idx in plan:
        calculate_ingredients(recipes[recipe_idx], food_manager, ingredient_list)
    return calculate_waste(ingredient_list)

def pack_bins(days, recipes, food_manager):
    bins = [random.randrange(len(recipes)) for _ in range(days)]
    score = compute_score(bins, recipes, food_manager)

    for i in range(100):
        alter_idx = random.randrange(days)
        value = random.randrange(len(recipes))
        if not value in bins:
            bins_new = copy.copy(bins)
            bins_new[alter_idx] = value
            score_new = compute_score(bins_new, recipes, food_manager)

            if score_new < score:
                score = score_new
                bins = bins_new
                print(i)
                print(score)
    return bins

if __name__ == "__main__":
    recipes = load_from_pickle(file="recipes.pickle")
    food_manager = food_manager.assemble(food_file="food.pickle")
    food_manager.filter_by_has_weight()
    
    bins = pack_bins(3, recipes, food_manager)
    
    ingredient_list = {}
    for b in bins:
        calculate_ingredients(recipes[b], food_manager, ingredient_list)
        print(ingredient_list)
    

    for b in bins:
        print(recipes[b])