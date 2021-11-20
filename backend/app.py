from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def status():
    return jsonify({ 'status': 'ok' })

@app.route("/api/tags")
def status():
    return jsonify({ 'tags': [] })

@app.route("/api/recipes", methods=['POST'])
def status():
    return jsonify({ 'recipes': [] })

@app.route("/api/shopping-list", methods=['POST'])
def status():
    return jsonify({ 'items': [] })

app.run(host='0.0.0.0')
