import datetime
import json
import re
import requests
from recipe_scrapers import scrape_me
from tqdm import tqdm
import pickle

from core import recipes_manager
from core.hello_fresh import get_recipe_links

my_recipes = []

for i in range(1):
    links = get_recipe_links(i)
    for link in tqdm(links):
        recipe = recipes_manager.Recipe(link)
        my_recipes.append(recipe)
        
    with open("recipes.pickle", "wb") as file:
        pickle.dump(my_recipes, file)
    print("saved", i, "pages")