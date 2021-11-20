from food_manager import FoodManager, FoodItem
from recipes import Recipe
from utils import load_from_pickle
from typing import List



def get_recipes():
    return load_from_pickle(file="recipes.pickle")

def get_food_items():
    return load_from_pickle(file="min_food.pickle")


class RecipePreselector:

    def __init__(self, manager: FoodManager, recipes: List[Recipe]) -> None:
        self.manager = manager
        self.recipes = recipes
        self.selected_recipes = []

    def compute_initial_recipes(self, tags, k=20):
        recipe_to_occ = {}
        for r_idx, r in enumerate(self.recipes):
            for tag in tags:
                if tag in r.ingredients:
                    recipe_to_occ.setdefault(r_idx, 0)
                    recipe_to_occ[r_idx] += 1
        l = sorted(recipe_to_occ.items(), key=lambda x: x)


if __name__ == "__main__":
    manager = FoodManager(get_food_items())
    recipes = get_recipes()
    tags = ["tomato"]

