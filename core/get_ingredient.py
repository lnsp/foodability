from recipe_scrapers import scrape_me
import nltk
import re

import get_units

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('universal_tagset')

def get_ingredient(ing):
    tokens = nltk.word_tokenize(ing)
    tagged = nltk.pos_tag(tokens, tagset='universal')
    words = []
    for x, y in tagged:
        if y in ['ADJ', 'NOUN']:
            if get_units.get_units(x) == None:
                if not re.search("[0-9]", x, re.IGNORECASE):
                    words.append(x)
    return words

if __name__ == "__main__":
    scraper = scrape_me('https://www.feastingathome.com/tomato-risotto/', wild_mode=True)
    ingredients = scraper.ingredients()
    for ing in ingredients:
        print(ing, get_ingredient(ing))