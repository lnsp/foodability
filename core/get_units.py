from recipe_scrapers import scrape_me
import re

def get_units(s):
    if re.search("gram", s, re.IGNORECASE):
        return (1., "w")
    if re.search("kilo", s, re.IGNORECASE):
        return (1000., "w")
    if re.search("lb", s, re.IGNORECASE):
        return (453.59, "w")
    if re.search("pound", s, re.IGNORECASE):
        return (453.59, "w")
    if re.search("oz", s, re.IGNORECASE):
        return (28.35, "w")
    if re.search("ounce", s, re.IGNORECASE):
        return (28.35, "w")
    if re.search(" g ", s, re.IGNORECASE):
        return (1., "w")
    if re.search("[0-9]g", s):
        return (1., "w")
    if re.search("pinch", s):
        return (1., "w")

    if re.search("litre", s, re.IGNORECASE):
        return (1000., "v")
    if re.search("[0-9][ ]*ml", s, re.IGNORECASE):
        return (1., "v")
    if re.search("pint", s, re.IGNORECASE):
        return (473.176473, "v")
    if re.search("gallon", s, re.IGNORECASE):
        return (3785.41178, "v")
    if re.search("tbsp", s, re.IGNORECASE):
        return (14.7868, "v")
    if re.search("table[ ]?spoon", s, re.IGNORECASE):
        return (14,7868, "v")
    if re.search("tea[ ]?spoon", s, re.IGNORECASE):
        return (4.92892, "v")
    if re.search("tsp", s, re.IGNORECASE):
        return (4.92892, "v")
    if re.search("cup", s, re.IGNORECASE):
        return (236.588, "v")
    return None

if __name__ == "__main__":
    scraper = scrape_me('https://www.feastingathome.com/tomato-risotto/', wild_mode=True)
    ingredients = scraper.ingredients()
    for ing in ingredients:
        print(ing, get_units(ing))

    print(ing, get_units(ing))