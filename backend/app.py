import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from core.main import *
import math
from uuid import uuid4
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import time

if os.getenv('DOWNLOAD_PICKLE'):
    connect_str = os.getenv('AZURE_STORAGE_CONNECTION')
    container_str = os.getenv('AZURE_STORAGE_CONTAINER')

    print('Fetch pickle files from Azure Storage container', container_str)
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    for fpath in ['basics.pickle','food.pickle', 'min_food.pickle', 'recipes.pickle']:
        blob_client = blob_service_client.get_blob_client(container=container_str, blob=fpath)
        with open(fpath, "wb") as pickle_file:
            pickle_file.write(blob_client.download_blob().readall())
        print('Fetched %s from Azure Blob storage' % fpath)

recipes, food_manager, recipe_selector = init_all(food_pickle=os.getenv('FOOD_DATASET', default='min_food.pickle'))
app = Flask(__name__)
CORS(app)

@app.route("/")
def status():
    return jsonify({'status': 'ok'})

@app.route("/api/version")
def version():
    return jsonify({'version': os.getenv('GIT_COMMIT')})

user_recipes = {}

@app.route("/api/all-tags")
def tags():
    uid = str(uuid4())
    return jsonify({'tags': ['broccoli'], 'uid': uid})

@app.route('/api/waste', methods=['POST'])
def waste():
    recipes = request.json['recipes']
    uid = request.json['uid']

    current_recipes = list(filter(lambda x: x.title in recipes, user_recipes[uid]))
    ingredient_list = {}
    for recipe in current_recipes:
        calculate_ingredients(recipe, food_manager, ingredient_list, True)
    
    waste, total_amount = calculate_waste(ingredient_list)
    rel_waste = waste / total_amount

    print(waste, total_amount, rel_waste)

    plastic, metal, carton, glass = get_total_packaging(ingredient_list)
    return jsonify({
        'waste': {
            'absolute': '%.2f' % (waste / 1000),
            'relative': '%.0f' % (rel_waste * 100),
        },
        'packaging': {
            'plastic': '' if plastic == 0.0 else '%.2f' % plastic,
            'metal': '' if metal == 0.0 else '%.2f' % metal,
            'carton': '' if carton == 0.0 else '%.2f' % carton,
            'glass': '' if glass == 0.0 else '%.2f' % glass
        }
    })

@app.route("/api/plan", methods=['POST'])
def plan():
    tags = request.json['tags']
    uid = request.json['uid']
    days = int(request.json['days'])

    if uid not in user_recipes:
        predicted_recipe_indices = recipe_selector.get_recipes(tags, k=20, size=100)
        predicted_recipes = list(map(lambda i: recipes[i], predicted_recipe_indices))
        user_recipes[uid] = predicted_recipes
    
    # we can guarantee that user_recipes[uid] has been set
    excluded = set(map(lambda x: x, request.json['recipes']['excluded']))
    chosen = set(map(lambda x: x, request.json['recipes']['chosen'])) - excluded

    # print('days', days)
    # print('excluded', len(excluded), excluded)
    # print('chosen', len(chosen), chosen)

    current_recipes = list(filter(lambda x: x.title not in excluded, user_recipes[uid]))
    # print('number of current recipes', len(current_recipes))

    if len(chosen) > days:
        raise Exception("chosen can't be larger than number of days")

    fixed_bins = list(filter(lambda x: x.title in chosen, current_recipes))
    # print('fixed_bins', list(map(lambda x: x.title, fixed_bins)))

    unchosen_recipes = list(filter(lambda x: x.title not in chosen, current_recipes))
    print('number of unchosen recipes', len(unchosen_recipes))
    _, possible_bins = init_bins(days - len(chosen), unchosen_recipes)
    # print('possible_bins', list(map(lambda x: x.title, possible_bins)))

    new_possible_bins = pack_bins(fixed_bins, possible_bins, current_recipes, food_manager)
    json_recipes = list(map(lambda x: {'title': x.title, 'image': x.image}, fixed_bins + new_possible_bins))
    return jsonify({'recommended': tags, 'recipes': json_recipes})

def format_weight(weight):
    if weight > 1000:
        return '%.2f' % (weight/1000)
    elif weight < 1:
        return '%.0f' % (weight*1000)
    else:
        return '%.2f' % (weight)

def weight_unit(weight):
    if weight > 1000:
        return 'kg'
    elif weight < 1:
        return 'mg'
    else:
        return 'g'

@app.route("/api/shop", methods=['POST'])
def shopping_list():
    recipes = request.json['recipes']
    uid = request.json['uid']

    current_recipes = list(filter(lambda x: x.title in recipes, user_recipes[uid]))
    ingredient_list = {}
    for recipe in current_recipes:
        calculate_ingredients(recipe, food_manager, ingredient_list, True)
    
    recipes_with_url = []
    for recipe in current_recipes:
        recipes_with_url.append({
            'title': recipe.title,
            'url': recipe.url,
        })
    readable_ingredients = []
    for ing, amt in ingredient_list.items():
        units = math.ceil(amt[0])
        readable_ingredients.append({
            'unit': weight_unit(ing.weight * amt[0]),
            'weight': format_weight(amt[0] * ing.weight),
            'usedby': '' if amt[1] == 1 else 'used by %d' % amt[1],
            'name': ing.name,
            'units': '' if units > 3 else '%.0f unit%s' % (units, 's' if units > 1 else ''),
        })

    return jsonify({'shoppingList': readable_ingredients, 'recipes': recipes_with_url})


app.run(host='0.0.0.0', port=int(os.getenv('FLASK_PORT', default='9876')))
