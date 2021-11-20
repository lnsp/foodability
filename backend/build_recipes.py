import datetime
import json
import re
import requests
from recipe_scrapers import scrape_me
from tqdm import tqdm
import pickle

from core import recipes_manager
from core.hello_fresh import *

my_recipes = []

def add_recipes(links):
    global my_recipes
    print(links)
    for link in tqdm(links):
        recipe = recipes_manager.Recipe(link)
        my_recipes.append(recipe)

    my_recipes = list(set(my_recipes))
    with open("recipes.pickle", "wb") as file:
        pickle.dump(my_recipes, file)
    print("saved", len(my_recipes))

add_recipes(get_recipe_links7("https://sunbasket.com/menu"))
#add_recipes(get_recipe_links5("https://www.thekitchn.com/collection/salmon"))

for i in range(1, 3):
    add_recipes(get_recipe_links6("https://sweetpeasandsaffron.com/category/main-ingredient/lentils/page/",i))
    add_recipes(get_recipe_links6("https://sweetpeasandsaffron.com/category/main-ingredient/beans/page/",i))
    add_recipes(get_recipe_links6("https://sweetpeasandsaffron.com/category/main-ingredient/chicken/page/",i))
    add_recipes(get_recipe_links6("https://sweetpeasandsaffron.com/category/main-ingredient/seafood/page/",i))
for i in range(10):
    add_recipes(get_recipe_links4(i))
add_recipes(get_recipe_links3())
add_recipes(get_recipe_links2())
for i in range(10):
    add_recipes(get_recipe_links(i))
       
    