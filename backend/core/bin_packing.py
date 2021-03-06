import random
import math
import copy

from . import food_manager
from . import recipes_manager
from .food_manager import FoodItem
from .recipes_manager import Recipe
from .utils import load_from_pickle

def calculate_ingredients(recipe, food_manager, ingredient_list, print_=False):
    """
    Adds to ingredient_list the needed ingredients and their quantities
    """
    for ing in recipe.ingredient_cache:
        quantity, food_item, is_pcs = ing
        if food_item != None:
            #print(tags, food_item.name)
            q = quantity
            if (not is_pcs) and food_item.weight > 0:
                q /= food_item.weight
            
            ingredient_list.setdefault(food_item, [0,0])
            ingredient_list[food_item][0] += q
            ingredient_list[food_item][1] += 1

def calculate_waste(ingredient_list):
    waste = 0
    total = 0
    for ing, q in ingredient_list.items():
        q = q[0]
        overshoot = math.ceil(q) - q
        waste += overshoot * ing.weight
        total += q * ing.weight
    return waste, total

def compute_score(bins_fixed, bins, recipes, food_manager):
    ingredient_list = {}
    for r in bins:
        calculate_ingredients(r, food_manager, ingredient_list)
    for r in bins_fixed:
        calculate_ingredients(r, food_manager, ingredient_list)
    waste, total = calculate_waste(ingredient_list)
    plastic, metal, carton, glass = get_total_packaging(ingredient_list)
    return waste + (plastic + 0.5*carton + 0.5*metal) * 100

def pack_bins(bins_fixed, bins, recipes, food_manager):
    if len(bins) == 0:
        return bins
    score = compute_score(bins_fixed, bins, recipes, food_manager)
    for i in range(1000):
        alter_idx = random.randrange(len(bins))
        value = random.randrange(len(recipes))
        value = recipes[value]
        if not value in (bins + bins_fixed):
            bins_new = copy.copy(bins)
            bins_new[alter_idx] = value
            score_new = compute_score(bins_fixed, bins_new, recipes, food_manager)

            if score_new < score+random.uniform(0., 0.03):
                score = score_new
                bins = bins_new
    return bins

def init_bins(days, recipes):
    random.shuffle(recipes)
    return [], recipes[:min(days, len(recipes))]

def get_total_packaging(ingredient_list):
    plastic, metal, carton, glass = 0,0,0,0
    for ing, amt in ingredient_list.items():
        amt = amt[0]
        plastic_, metal_, carton_, glass_ = ing.get_packaging(amt)
        plastic += plastic_
        metal += metal_
        carton += carton_
        glass += glass_
    return plastic, metal, carton, glass


if __name__ == "__main__":
    recipes = load_from_pickle(file="recipes.pickle")
    food_manager = food_manager.assemble(food_file="min_food.pickle")
    
    recipes = recipes_manager.remove_duplicate_recipes(recipes)
    recipes = recipes_manager.remove_nonsense_recipes(recipes)
    
    for r in recipes:
        r.cache_ingredients(food_manager)

    food_manager.filter_by_has_weight()
    
    bins = pack_bins(*init_bins(3), recipes, food_manager)
    
    print(bins, len(recipes))
    
    ingredient_list = {}
    for b in bins:
        calculate_ingredients(recipes[b], food_manager, ingredient_list, True)
    
    print("ingredient_list")
    for ing, amt in ingredient_list.items():
        print(ing.name, ing.weight, amt)

    for b in bins:
        print(recipes[b])