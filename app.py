from flask import Flask, render_template, jsonify, request
import random
riddles = [
  {
    "question": "What has to be broken before you can use it?",
  "answer": "egg",
  },
  {
    "question": "I’m tall when I’m young, and I’m short when I’m old. What am I?",
  "answer": "candle",
  },
  {
    "question": "What is full of holes but still holds water?",
  "answer": "sponge",
  },
  {
    "question":"I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I? ",
  "answer": "map",
  },
  {
    "question":" I am weightless, but you can see me. Put me in a bucket, and I'll make it lighter. What am I? ",
  "answer": "hole",
  },
]

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get-story")
def getRiddles():
    return jsonify({
        "status":"success",
        "story":random.choice(riddles)
    })

if __name__ == "__main__":
    app.run(debug=True)