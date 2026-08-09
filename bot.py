import os
import requests
from datetime import datetime, timezone

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHANNEL_ID = os.environ["CHANNEL_ID"]

url = (
    "https://api.coingecko.com/api/v3/simple/price"
    "?ids=the-open-network"
    "&vs_currencies=usd"
    "&include_24hr_change=true"
)

response = requests.get(url, timeout=20)
data = response.json()

ton = data["the-open-network"]["usd"]
change = data["the-open-network"]["usd_24h_change"]

time = datetime.now(timezone.utc).strftime("%H:%M UTC")

message = f"""💎 TON KURSI

💰 1 TON = ${ton:.4f}

📊 24 soatlik o‘zgarish: {change:+.2f}%

🕐 Yangilandi: {time}

🔄 Keyingi yangilanish: 5 daqiqadan keyin
"""

telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

requests.post(
    telegram_url,
    json={
        "chat_id": CHANNEL_ID,
        "text": message
    },
    timeout=20
)
