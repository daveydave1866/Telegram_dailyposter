import requests
import os

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHANNEL_ID = os.environ["CHANNEL_ID"]
MESSAGE = os.environ["MESSAGE"]

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
payload = {
    "chat_id": CHANNEL_ID,
    "text": MESSAGE
}

response = requests.post(url, data=payload)
print(response.json())
