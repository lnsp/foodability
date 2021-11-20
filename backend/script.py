from core.main import *

if __name__ == "__main__":
    recipes, food, selector = init_all()
    
    tags = ["broccoli"]

    selected_recipe_indices = selector.get_recipes(tags, k=20, size=10)
    selected_recipes = list(map(lambda i: recipes[i], selected_recipe_indices))
    bins = pack_bins(*init_bins(5, selected_recipes), selected_recipes, food)
    
    print_stats(selected_recipes, food, bins)