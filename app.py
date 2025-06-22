from flask import Flask, request, jsonify, send_from_directory
import datetime
import os
from flask_cors import CORS

app = Flask(__name__, static_folder='../frontend', static_url_path='')
CORS(app)

@app.route("/")
def serve_index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").lower()

    if "hello" in user_message or "hi" in user_message:
        response = "Hello there! How can I help you?"
    elif "how are you" in user_message:
        response = "I'm doing great! How about you?"
    elif "your name" in user_message:
        response = "I'm OceanBot, your friendly assistant!"
    elif "time" in user_message:
        now = datetime.datetime.now()
        response = f"The time now is {now.strftime('%I:%M %p')}"
    elif "bye" in user_message:
        response = "Goodbye! Take care."
    else:
        response = "Hmm... I didn't understand that."

    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)
