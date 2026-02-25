from flask import Flask, jsonify, request
from model.scoring_model import score_proposal

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Public Goods Allocation API Running"

@app.route("/score", methods=["POST"])
def score():
    data = request.json
    result = score_proposal(data)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
