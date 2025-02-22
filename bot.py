from config import TOKEN

import telebot
from telebot import types

bot = telebot.TeleBot(TOKEN)

cmd1 = 'Ищу то'
cmd2 = 'Ищу сё'

lastMsgId = ''

@bot.message_handler(commands=['start'])
def start(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1   = types.KeyboardButton(cmd1)
        btn2   = types.KeyboardButton(cmd2)
        markup.add(btn1).add(btn2)
        msg    = f'Добро пожаловать, {message.from_user.first_name}'
        lastMsgId = bot.send_message(message.from_user.id, msg, reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
        if message.text == cmd1:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1   = types.KeyboardButton('я тоже ищу то. Давай искать вместе')
                btn2   = types.KeyboardButton('в меню')
                markup.add(btn1).add(btn2)
                msg    = f'Поможем с то'
                lastMsgId = bot.send_message(message.from_user.id, msg, reply_markup=markup)
                bot.delete_message(message.chat.id, lastMsgId.message_id-1)

        elif message.text == cmd2:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1   = types.KeyboardButton('я уже нашел сё. Давай покажу')
                btn2   = types.KeyboardButton('в меню')
                markup.add(btn1).add(btn2)
                msg    = f'Поможем с сё'
                lastMsgId = bot.send_message(message.from_user.id, msg, reply_markup=markup)
                bot.delete_message(message.chat.id, lastMsgId.message_id-1)

        else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1   = types.KeyboardButton(cmd1)
                btn2   = types.KeyboardButton(cmd2)
                markup.add(btn1).add(btn2)
                msg    = f'Добро пожаловать, {message.from_user.first_name}'
                lastMsgId = bot.send_message(message.from_user.id, msg, reply_markup=markup)
                bot.delete_message(message.chat.id, lastMsgId.message_id-1)

        bot.delete_message(message.chat.id, lastMsgId.message_id-2)


bot.polling(none_stop=True, interval=0)