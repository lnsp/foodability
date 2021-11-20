import random

import food_manager
import recipes_manager
from utils import load_from_pickle

def compute_score(plan, recipes, food):


def pack_bins(days, recipes, food):
    bins = [random.randrange(recipes) for _ in range(days)]
    

    print(bins)

if __name__ == "__main__":
    recipes = load_from_pickle(food_file="food.pickle")
    food_manager = food_manager.assemble()
