from flask import Flask, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app)

openai.api_key = os.getenv("OPENAI_API_KEY")

PROMPT = '''
Write a short satirical article in the style of the Harvard Lampoon.
It should be absurd, witty, and not exceed 300 words.
Include a fake title, author, and publication section.
'''

@app.route("/generate_article", methods=["GET"])
def generate_article():
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": PROMPT}]
        )
        article = response["choices"][0]["message"]["content"]
        return jsonify({"article": article})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/", methods=["GET"])
def home():
    return "Backend is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
