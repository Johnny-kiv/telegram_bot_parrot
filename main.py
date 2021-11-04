"""import requests


API_link = "https://api.telegram.org/bot2020365693:AAFu6n7mmnUtxU0thHz2S8APTbUXdeDZ8Mg"
updates = requests.get(API_link + "/getUpdates?offset=-1").json()

print(updates)

message=updates["result"][-1]["message"]

chat_id = message["from"]["id"]


send_message = requests.get(API_link+f"/sendMessage?chat_id=1776334853&text=🍑👢")"""

import asyncio

from aiogram import Bot, Dispatcher, executor
from config import bot_token

loop = asyncio.get_event_loop()
bot = Bot(bot_token, parse_mode="HTML")
dp = Dispatcher(bot,loop=loop)

if __name__ == "__main__":
    from handlers import dp, send_to_admin
    executor.start_polling(dp, on_startup=send_to_admin)


