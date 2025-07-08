from fastapi import FastAPI, Request
import requests
import os

app = FastAPI()

BOT_TOKEN = os.environ.get("BOT_TOKEN")   # Telegram Bot Token
CHAT_ID = os.environ.get("CHAT_ID")       # Telegram Chat ID

def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, json=payload)

@app.post("/signal/")
async def receive_signal(request: Request):
    data = await request.json()
    symbol = data.get("symbol")
    price = data.get("price")

    msg = f"🚨 SIGNAL ALERT 🚨\nSymbol: {symbol}\nPrice: ₹{price}"
    send_telegram_alert(msg)

    return {"status": "received"}

