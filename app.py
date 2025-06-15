from flask import Flask, render_template, request, jsonify
from responses import get_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["GET"])
def chatbot_response():
    user_input = request.args.get('msg')
    response = get_response(user_input)
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
