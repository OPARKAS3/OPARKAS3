from flask import Flask, request
import requests

app = Flask(__name__)

# ✅ Home route
@app.route("/")
def home():
    return "✅ Scalper Bot is Live!!"

# ✅ Signal route
@app.route("/signal", methods=["POST"])
def signal():
    data = request.json
    symbol = data.get("symbol", "NIFTY")
    price = data.get("price", "UNKNOWN")
    msg = f"📈 Signal: {symbol} at ₹{price}"

    # Telegram alert
    send_telegram(msg)
    return {"status": "Signal sent"}, 200

# ✅ Telegram function
def send_telegram(message):
    bot_token = "6171234567:AAEXAMPLExyz..."  # ✅ replace with your token

    chat_id = "1274012617"
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print("Telegram Error:", e)

# ✅ Run app
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
