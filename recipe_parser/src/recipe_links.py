import requests
import json
import datetime
import re

def get_recipe_links_hello_fresh(pages):
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
    for i in range(pages):
        url = "https://www.hellofresh.com/recipes/search/?page=" + str(i)
        raw = session.get(url, headers=headers).text
        match = re.finditer(r'"(https://www.hellofresh.com/recipes/[^"]*)"', raw)
        for m in match:
            s = m.group(1)
            if not(s[:-1] == url[:-1] or s in blacklist):
                found.append(s)
    return found


if __name__ == "__main__":
    print(get_recipe_links_hello_fresh(30))