from food_manager import FoodManager, FoodItem
from recipes_manager import Recipe
from utils import load_from_pickle
from typing import List
from graph import Graph
import random
from bin_packing import pack_bins

def get_recipes():
    return load_from_pickle(file="recipes.pickle")

def get_food_items():
    return load_from_pickle(file="min_food.pickle")


class RecipePreselector:

    def __init__(self, manager: FoodManager, recipes: List[Recipe]) -> None:
        self.manager = manager
        self.recipes = recipes
        self.selected_recipes = []

    def compute_initial_recipes_(self, tags, k=20):
        recipe_to_occ = {}
        for r_idx, r in enumerate(self.recipes):
            for tag in tags:
                if tag.lower().strip() in [token.lower().strip() for elem in r.ingredients for token in elem[1]]:
                    recipe_to_occ.setdefault(r_idx, 0)
                    recipe_to_occ[r_idx] += 1
        l = [e[0] for e in sorted(recipe_to_occ.items(), key=lambda x: x[1])[-k:]]
        return l[-k:]

    def get_related_recipes(self, r_idx: int, k=20):
        """Returns a list of related recipes based on their ingredients. Recipe index is given. The first item is the list is
        the most related recipe"""
        recipe_to_count = {}
        ingredients = [token.lower().strip() for elem in self.recipes[r_idx].ingredients for token in elem[1]]
        for r_idx, r in enumerate(self.recipes):
            ing = [token.lower().strip() for elem in r.ingredients for token in elem[1]]
            recipe_to_count[r_idx] = len(set(ingredients).intersection(set(ing)))
        l = [e[0] for e in sorted(recipe_to_count.items(), key=lambda x: x[1])[-k:]]
        l = [e for e in l if recipe_to_count[e] > 0 and e != r_idx]
        l.reverse()
        return l

    def get_recipes(self, tags, k=100, size=50):
        self.selected_recipes = self.compute_initial_recipes_(tags, k=k)
        if len(self.selected_recipes) > size or len(self.selected_recipes) == 0:
            return self.selected_recipes
        for _ in range(size - len(self.selected_recipes)):
            r_idx = self.selected_recipes[random.randint(0, len(self.selected_recipes)-1)]
            succs = self.get_related_recipes(r_idx)
            for succ in [s for s in succs if s not in self.selected_recipes]:
                self.selected_recipes.append(succ)
                break
            
        return self.selected_recipes

if __name__ == "__main__":
    manager = FoodManager(get_food_items())
    recipes = get_recipes()
    tags = ["broccoli"]
    selector = RecipePreselector(manager, recipes)
    l = selector.get_recipes(tags, k=20, size=10)

    bins = pack_bins(5, [recipes[idx] for idx in l], manager)

    for e in bins:
        print(recipes[l[e]].url)

