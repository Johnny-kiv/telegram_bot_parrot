import analizator
from main import bot, dp
from analizator import *
from aiogram.types import Message
from config import admin_id

async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text="Бот запущен")

@dp.message_handler()
async def echo(message: Message):
    """print(message)
    new_text=""
    l="?!.,@#$%^&*()\"\'№;:<>+={}]["
    b="АБВГДЕЁЖЗИЙКЛМНОПРСТУХФЦЧШЩЬЫЪЭЮЯABCDEFGHIJKLMNOPQRSTUVWXZY"
    var=""
    global text
    for leter in message.text:
        if leter not in l:
            new_text +=  leter
        elif leter in l:
            var = leter

    text = "Сам, "+new_text.lower() + ", профессор"+var"""
    text=analizator.jhn_analizator(message.text)
    await bot.send_message(chat_id=message.from_user.id, text=text)