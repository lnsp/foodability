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
    excluded = request.json
    # handle excluded recipes, make tag and recipe recommendations
    return jsonify({'recommended': ['pizza', 'egg', 'chicken'], 'recipes': [
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
        }
    ]})


@app.route("/api/shop", methods=['POST'])
def shopping_list():
    return jsonify({'shoppingList': [], 'recipes': []})


app.run(host='0.0.0.0', port=int(os.getenv('FLASK_PORT', default='9876')))
