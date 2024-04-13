from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '7148468736:AAGjwGoJAfKZdBO_SpqX5koycYldnZL7qdc'
BOT_USERNAME: Final =  '@Al_FinnBot'

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hey there! I am a finance bot. Here are some of the commands: \n"
                                    "credc - for credit calculator\n"
                                    "depc - for deposit calculator\n"
                                    "game - for 52\n")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Just press start(or write '/start')")

def handle_response(text: str) -> str:
    prc: str = text.lower()
    if 'credc' in prc:
        return 'write your credit amount'
    if 'depc' in prc:
        return 'deposit ur moni pls'
    if 'game' in prc:
        return '52 52 52 52'

    return 'what?'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print (f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print (f'update {update} caused error {context.error}')

if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error)

    print('Polling...')
    app.run_polling(poll_interval=5)

'''
import logging
import time
from aiogram import Bot, Dispatcher, types
import Parser


def Bot():
    bot = Bot(token="7148468736:AAGjwGoJAfKZdBO_SpqX5koycYldnZL7qdc")  # Объект бота
    dp = Dispatcher(bot)  # Диспетчер

@dp.message_handler(commands=['start', 'help'])
async def process_start_command(message: types.Message):
    await message.reply("Тут ваш текст")

@dp.message_handler(commands=['command'])
async def process_start_command(message: types.Message):
    await message.reply("Тут еще что-то")
'''