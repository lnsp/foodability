import datetime
import json
import re

import requests
from recipe_scrapers import scrape_me
from tqdm import tqdm
from . import recipes_manager
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


def get_recipe_links2():
    today = datetime.datetime.today()
    session = requests.session()

    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:71.0) Gecko/20100101 Firefox/71.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}

    blacklist = [
    ]

    found = []

    url = "https://www.myrecipes.com/search?q="
    raw = session.get(url, headers=headers).text
    match = re.finditer(r'"(https://www.myrecipes.com/recipe[^"]*)"', raw)
    for m in match:
        s = m.group(1)
        if not(s[:-1] == url[:-1] or s in blacklist):
            found.append(s)

    return found



def get_recipe_links3():
    today = datetime.datetime.today()
    session = requests.session()

    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:71.0) Gecko/20100101 Firefox/71.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}

    blacklist = [
        'https://www.jamieoliver.com/recipes/category/course/meals-for-one/', 'https://www.jamieoliver.com/recipes/category/tesco-community-cookery-school/', 'https://www.jamieoliver.com/recipes/category/occasion/dinner-party/', 'https://www.jamieoliver.com/recipes/category/books/together/', 'https://www.jamieoliver.com/recipes/category/books/jamies-keep-cooking-family-favourites/', 'https://www.jamieoliver.com/recipes/category/books/7-ways/', 'https://www.jamieoliver.com/recipes/category/books/veg/', 'https://www.jamieoliver.com/recipes/category/tesco-community-cookery-school/','https://www.jamieoliver.com/recipes/vegetables-recipes/?rec-page=2','https://www.jamieoliver.com/recipes/category/special-diets/vegan/', 'https://www.jamieoliver.com/recipes/butternut-squash-recipes/'
    ]

    found = []

    url = "https://www.jamieoliver.com/recipes/vegetables-recipes/"
    raw = session.get(url, headers=headers).text
    match = re.finditer(r'"(https://www.jamieoliver.com/recipes/[^"]*)"', raw)
    for m in match:
        s = m.group(1)
        if not(s[:-1] == url[:-1] or s in blacklist):
            found.append(s)

    return found


def get_recipe_links4(idx):
    today = datetime.datetime.today()
    session = requests.session()

    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:71.0) Gecko/20100101 Firefox/71.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}

    blacklist = [
    ]

    found = []

    url = "https://www.justataste.com/recipes/?_recipe_categories=30-minute-meals&_paged=" + str(idx)
    raw = session.get(url, headers=headers).text
    match = re.finditer(r'summary"><div class="post-summary__image"><a href="(https://www.justataste.com/[^"]*)"', raw)
    for m in match:
        s = m.group(1)
        if not(s[:-1] == url[:-1] or s in blacklist):
            found.append(s)
    return found


def get_recipe_links5(idx):
    today = datetime.datetime.today()
    session = requests.session()

    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:71.0) Gecko/20100101 Firefox/71.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}

    blacklist = [
    ]

    found = []

    url = "https://vanillaandbean.com/recipe-index/" + str(idx)
    raw = session.get(url, headers=headers).text
    match = re.finditer(r'summary"><div class="post-summary__image"><a href="(https://www.justataste.com/[^"]*)"', raw)
    for m in match:
        s = m.group(1)
        if not(s[:-1] == url[:-1] or s in blacklist):
            found.append(s)
    return found

    
