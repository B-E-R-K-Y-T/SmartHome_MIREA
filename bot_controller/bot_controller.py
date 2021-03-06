# ======================================================================================================================

# Author: BERKYT

# ======================================================================================================================

import logging
import code.client.base_client as base_client
import code.server.base_server as base_server


from aiogram import Bot, Dispatcher, executor, types
from other.config import TOKEN


# sensor = base_client.Client('127.0.0.1', 2323).get_client()
base_server.Server('127.0.0.1', 8888)

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


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)
    await message.answer(message.chat.id)

    # client.send(message.text.encode('utf-8'))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
