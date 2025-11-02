from flask import Flask, jsonify, request
import redis

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379)

@app.route('/vote', methods=['POST'])
def vote():
    data = request.json
    item = data.get("item")
    if item:
        r.incr(item)
        return jsonify({"message": "Vote counted"}), 200
    return jsonify({"error": "No item selected"}), 400

@app.route('/results', methods=['GET'])
def results():
    keys = ["item1", "item2", "item3"]
    result = {key: int(r.get(key) or 0) for key in keys}
    return jsonify(result)

app.run(host='0.0.0.0', port=5000)
