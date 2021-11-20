import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from core.main import *
from uuid import uuid4

recipes, food_manager, recipe_selector = init_all()
app = Flask(__name__)
CORS(app)

@app.route("/")
def status():
    return jsonify({'status': 'ok'})

user_recipes = {}

@app.route("/api/all-tags")
def tags():
    uid = str(uuid4())
    return jsonify({'tags': ['broccoli'], 'uid': uid})

@app.route("/api/plan", methods=['POST'])
def plan():
    tags = request.json['tags']
    uid = request.json['uid']
    days = request.json['days']

    if uid not in user_recipes:
        predicted_recipe_indices = recipe_selector.get_recipes(tags, k=20, size=20)
        predicted_recipes = list(map(lambda i: recipes[i], predicted_recipe_indices))
        user_recipes[uid] = predicted_recipes
    
    # we can guarantee that user_recipes[uid] has been set
    excluded = set(map(lambda x: x, request.json['recipes']['excluded']))
    chosen = set(map(lambda x: x, request.json['recipes']['chosen']))
    current_recipes = list(filter(lambda x: x.title not in excluded, user_recipes[uid]))

    if len(chosen) > days:
        raise Exception("chosen can't be larger than number of days")

    fixed_bins = list(filter(lambda x: x.title in chosen, current_recipes))
    _, possible_bins = init_bins(days - len(chosen), list(filter(lambda x: x.title not in chosen, current_recipes)))

    new_possible_bins = pack_bins(fixed_bins, possible_bins, current_recipes, food_manager)
    json_recipes = list(map(lambda x: {'title': x.title }, fixed_bins + new_possible_bins))
    return jsonify({'recommended': tags, 'recipes': json_recipes})


@app.route("/api/shop", methods=['POST'])
def shopping_list():
    return jsonify({'shoppingList': [
         "500g flour",
        "25g backing powder",
        "100g salt",
        "250g sugar",
        "1 liter milk",
        "6 eggs",
        "100g butter",
    ], 'recipes': []})


app.run(host='0.0.0.0', port=int(os.getenv('FLASK_PORT', default='9876')))
