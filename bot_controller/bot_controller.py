# ======================================================================================================================

# Author: BERKYT

# ======================================================================================================================

import logging
import socket
import asyncio
import aiohttp
import json

from aiogram import Bot, Dispatcher, executor, types
from other.config import TOKEN


client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)
client.connect(('127.0.0.1', 1234))

API_TOKEN = TOKEN

# Configure logging
logging.basicConfig(
    format='%(threadName)s %(name)s %(levelname)s: %(message)s',
    level=logging.INFO
)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler(command='off')
async def echo(message: types.Message):

    with open('personal.json', 'r', encoding='utf-8') as f:  # открыли файл
        text = json.load(f)  # загнали все из файла в переменную
        print(text)  # вывели результат на экран

    await message.answer(text['mode'])
    await message.answer(message.chat.id)


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)
    await message.answer(message.chat.id)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
