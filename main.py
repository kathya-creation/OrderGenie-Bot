from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "OrderGenie Bot is Live!"

@app.route("/message", methods=["POST"])
def message():
    user_input = request.json.get("message", "").lower()
    response = "Default reply"

    if "like" in user_input or "likes" in user_input:
        if "1k" in user_input or "1000" in user_input:
            response = "1k Likes = ₹15
Post ka link bhejo 🔗"
        elif "2k" in user_input:
            response = "2k Likes = ₹30
Post ka link bhejo 🔗"
        else:
            response = "Likes ke liye ₹15 per 1k ka rate hai.
Post link bhejo."

    elif "follower" in user_input or "followers" in user_input:
        if "1k" in user_input or "1000" in user_input:
            response = "1k Followers = ₹249
Account username bhejo 📱"
        else:
            response = "Followers ₹249 per 1k hain.
Account username bhejo."

    elif "view" in user_input or "views" in user_input:
        response = "1k Views = ₹20
Video link bhejo 🎥"

    elif "pay" in user_input or "payment" in user_input:
        response = "Pay karo is UPI pe: paytm.s1gh93w@pty
Phir screenshot bhejo 📸"

    elif "done" in user_input or "screenshot" in user_input:
        response = "Order Done ✅
Delivery jaldi start ho jayegi ⏳"

    elif "panel" in user_input:
        response = "Panel ka link: https://wholesmm.com
But order yahin kara do, fast ho jaayega!"

    return {"reply": response}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
