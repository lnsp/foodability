import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def status():
    return jsonify({'status': 'ok'})


@app.route("/api/all-tags")
def tags():
    return jsonify({'tags': ['banana', 'apple', 'pizza', 'burger', 'chicken', 'steak']})


@app.route("/api/plan", methods=['POST'])
def plan():
    tags = request.json['tags']
    excluded = set(map(lambda x: x, request.json['recipes']['excluded']))
    # handle excluded recipes, make tag and recipe recommendations
    recipes = [
        {
            'title': 'Chicago-style pizza',
            'image': '',
        },
        {
            'title': 'Egg omelett',
            'image': '',
        },
        {
            'title': 'Ass',
            'image': ''
        }]
    # delete all excluded from recipes
    recipes = list(filter(lambda x: x['title'] not in excluded, recipes))
    return jsonify({'recommended': tags, 'recipes': recipes})


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
