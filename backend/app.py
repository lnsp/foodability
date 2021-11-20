from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api")
def status():
    return jsonify({ 'status': 'ok' })

app.run(host='0.0.0.0')
