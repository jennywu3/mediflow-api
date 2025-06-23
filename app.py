from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

@app.route("/", methods=["GET"])
def hello():
    return "Hello from Python API test!"

@app.route("/get-id", methods=["POST"])
def get_id():
    data = request.get_json()
    user_id = data.get("id", None)
    if user_id is None:
        return jsonify({"error": "No ID provided"}), 400
    return jsonify({"result": f"Received ID: {user_id}"})

if __name__ == "__main__":
    app.run()
