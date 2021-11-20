import datetime
import json
import re
import requests
from recipe_scrapers import scrape_me
from tqdm import tqdm
import pickle

from core import recipes_manager
from core.hello_fresh import get_recipe_links, get_recipe_links2, get_recipe_links3, get_recipe_links4

my_recipes = []

def add_recipes(links):
    for link in tqdm(links):
        recipe = recipes_manager.Recipe(link)
        my_recipes.append(recipe)

    with open("recipes.pickle", "wb") as file:
        pickle.dump(my_recipes, file)
    print("saved")
        
for i in range(10):
    add_recipes(get_recipe_links4(i))
add_recipes(get_recipe_links3())
add_recipes(get_recipe_links2())
for i in range(10):
    add_recipes(get_recipe_links(i))
        
    