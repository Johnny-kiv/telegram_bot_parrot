import analizator
from main import bot, dp
from analizator import *
from aiogram.types import Message
from config import admin_id

async def send_to_admin(dp):
    await Message.reply("Бот запущен")

@dp.message_handler()
async def echo(message: Message):
    text=analizator.jhn_analizator(message.text)
    await message.reply(text)