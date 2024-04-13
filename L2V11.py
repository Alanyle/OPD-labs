import logging
import time
from aiogram import Bot, Dispatcher, executor, types
import Parser


def Bot():
    bot = Bot(token="Ваш токен")  # Объект бота
    dp = Dispatcher(bot)  # Диспетчер

@dp.message_handler(commands=['start', 'help'])
async def process_start_command(message: types.Message):
    await message.reply("Тут ваш текст")

@dp.message_handler(commands=['command'])
async def process_start_command(message: types.Message):
    await message.reply("Тут еще что-то")