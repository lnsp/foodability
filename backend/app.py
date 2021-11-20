from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def status():
    return jsonify({ 'status': 'ok' })

@app.route("/api/all-tags")
def tags():
    return jsonify({ 'tags': [] })

@app.route("/api/plan", methods=['POST'])
def plan():
    excluded = request.json
    # handle excluded recipes, make tag and recipe recommendations
    return jsonify({ 'recommended': [], 'recipes': [] })

@app.route("/api/shop", methods=['POST'])
def shopping_list():
    return jsonify({ 'shoppingList': [], 'recipes': [] })

app.run(host='0.0.0.0')
