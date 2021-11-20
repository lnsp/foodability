import datetime
import json
import re

import requests
from recipe_scrapers import scrape_me
from tqdm import tqdm
import recipes_manager
import pickle


def get_recipe_links(page):
    today = datetime.datetime.today()
    session = requests.session()

    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:71.0) Gecko/20100101 Firefox/71.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}

    blacklist = [
        'https://www.hellofresh.com/recipes/quick-meals',
        'https://www.hellofresh.com/recipes/mexican-recipes',
        'https://www.hellofresh.com/recipes/italian-recipes',
        'https://www.hellofresh.com/recipes/pasta-recipes',
        'https://www.hellofresh.com/recipes/mexican-recipes/tacos',
        'https://www.hellofresh.com/recipes/easy-recipes',
    ]

    found = []

    url = "https://www.hellofresh.com/recipes/search/?page=" + str(page)
    raw = session.get(url, headers=headers).text
    match = re.finditer(r'"(https://www.hellofresh.com/recipes/[^"]*)"', raw)
    for m in match:
        s = m.group(1)
        if not(s[:-1] == url[:-1] or s in blacklist):
            found.append(s)

    return found


if __name__ == "__main__":
    my_recipes = []
    
    for i in range(10):
        links = get_recipe_links(i)
        for link in tqdm(links):
            recipe = recipes_manager.Recipe(link)
            my_recipes.append(recipe)
        if i % 5 == 4:
            with open("recipes.pickle", "wb") as file:
                pickle.dump(my_recipes, file)
            print("saved", i, "pages")