from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "OrderGenie Bot is Running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    message = data.get("message", "").lower()

    if "like" in message or "1k like" in message:
        response = "1k Likes = ₹15"
    elif "follower" in message or "1k follower" in message:
        response = "1k Followers = ₹249"
    elif "view" in message or "1k view" in message:
        response = "1k Views = ₹20"
    else:
        response = "Likes, Followers or Views — kya chahiye aapko?\n\n📌 Price Chart:\n1k Likes = ₹15\n1k Followers = ₹249\n1k Views = ₹20"

    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
