import Parser

from telebot import TeleBot, types

bot = TeleBot('7148468736:AAGjwGoJAfKZdBO_SpqX5koycYldnZL7qdc')

@bot.message_handler(commands=['start'])
def send_welcome(message: types.Message):
    bot.send_message(chat_id=message.chat.id, text="Hey there! I am a finance bot. Here are some of the commands: \n"
                                                    "/credcalc - for credit calculator\n"
                                                    "/depcalc - for deposit calculator\n"
                                                    "/game - for 52\n")
@bot.message_handler(commands=['credcalc'])
def credc(message: types.Message):
    print(message.text)
    bot.send_message(chat_id=message.chat.id, text=f'Enter your credit amount')
    bot.register_next_step_handler(message, credc2)
def credc2(message: types.Message):
    print(message.text)
    crm = int(message.text)
    bot.send_message(chat_id=message.chat.id, text=f'Enter your credit time in months')
    bot.register_next_step_handler(message, credc3, crm)
def credc3(message: types.Message, crm):
    print(message.text)
    crt = int(message.text)
    bot.send_message(chat_id=message.chat.id, text=f'Enter your credit percentage')
    bot.register_next_step_handler(message, credc4, crm, crt)
def credc4(message: types.Message, crm, crt):
    print(message.text)
    crp = int(message.text)/12000
    print(crp)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("1. Count without early repayment")
    btn2 = types.KeyboardButton("2. Enter data for early repayment")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, 'Will you do early repayments?\n'
                                      '1. Count without early repayment\n'
                                      '2. Enter data for early repayment\n', reply_markup=markup)
    bot.register_next_step_handler(message, credc5, crm, crt, crp)
    '''    markup = types.InlineKeyboardMarkup(row_width=2)
    item = types.InlineKeyboardButton('1. Count without early repayment', callback_data='c_1')
    item2 = types.InlineKeyboardButton('2. Enter data for early repayment', callback_data='c_2')
    markup.add(item, item2)
    bot.send_message(message.chat.id, 'Will you do early repayments?', reply_markup=markup)
    bot.register_next_step_handler(message, credc5)'''
def credc5(message: types.Message, crm, crt, crp):
    msg = message.text
    if (msg.count('1')):
        #crn= crm*(crp+ (crp/(1+crp)*crt-1))
        crn=crm*(crp+((crp*(1+crp)**crt)/(((1+crp)**crt)-1)))
        bot.send_message(message.chat.id, text= "Your monthly payment is = " + str(crn))
    elif (msg.count('2')):
        bot.send_message(chat_id=message.chat.id, text=f'Enter your repayment amount')
        bot.register_next_step_handler(message, credc51, crm, crt, crp)
def credc51(message: types.Message, crm, crt, crp):
    print(message.text)
    crem = message.text
    bot.send_message(chat_id=message.chat.id, text=f'Enter your repayment month')
    bot.register_next_step_handler(message, credc52, crm, crt, crp, crem)
def credc52(message: types.Message, crm, crt, crp, crem):
    print(message.text)
    cret = int(message.text)
    crn=crm*(crp+((crp*(1+crp)**cret)/(((1+crp)**cret)-1)))
    crm-=crn*cret
    crt-=cret
    crl=crm*(crp+((crp*(1+crp)**crn)/(((1+crp)**crn)-1)))
    bot.send_message(chat_id=message.chat.id, text=f'Your monthly payment for the first ' + str(cret) + ' months is = ' + str(crn)+ (' \n'
                                                    'then it will be ' + str(crl)))
    bot.register_next_step_handler(message, credc52, crm, crt, crp, crem, cret)

@bot.message_handler(commands=['depcalc'])
def depc(message: types.Message):
    print(message.text)
    bot.send_message(chat_id=message.chat.id, text=f'Enter your first deposit amount')
    bot.register_next_step_handler(message, depc2)
def depc2(message: types.Message):
    print(message.text)
    dem = int(message.text)
    bot.send_message(chat_id=message.chat.id, text=f'Enter your deposit percentage')
    bot.register_next_step_handler(message, depc3, dem)
def depc3(message: types.Message, dem):
    print(message.text)
    dep = int(message.text)/12000
    bot.send_message(chat_id=message.chat.id, text=f'Enter your period of deposit in months')
    bot.register_next_step_handler(message, depc4, dem, dep)
def depc4(message: types.Message, dem, dep):
    det = int(message.text)
    den=dem*(1+dep)**det
    bot.send_message(message.chat.id, text= "Your amount of money in deposit in " + str(det) + " months is = " + str(den))


@bot.message_handler(commands=['game'])
def gm(message: types.Message):
    print(message.text)
    bot.send_message(chat_id=message.chat.id, text=f'Enter your lowest savings')
    bot.register_next_step_handler(message, gm2)
def gm2(message: types.Message):
    print(message.text)
    gm = int(message.text)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("52")
    markup.add(btn1)
    bot.send_message(message.chat.id, 'Enter your period of savings', reply_markup=markup)
    bot.register_next_step_handler(message, gm3, gm)
def gm3(message: types.Message, gm):
    print(message.text)
    gp = int(message.text)
    gx = gm*gp
    gf = (gx+gm)*gp/2
    bot.send_message(chat_id=message.chat.id, text=f'You will save for yourself ' + str(gf))

bot.infinity_polling(skip_pending=True)

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
#t='abcdefghijklmnopqrstuvwxyz'
#print(t[1:11] + '2' + t[11:-2])
