# Вставьте ваш токен, полученный у BotFather
BOT_TOKEN = '5622410166:AAHh6OVhMyDuMkbMwyNmKRlsNbUGpJqJo6A'
# URL вашего mini app
WEBAPP_URL = 'https://denis-bez.github.io/vanilla-js-boilerplate/'

import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Открыть Mini App", web_app=WebAppInfo(url=WEBAPP_URL)))
    
    bot.reply_to(message, "Привет! Нажми на кнопку ниже, чтобы открыть Mini App:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Используйте команду /start для запуска Mini App.")

if __name__ == "__main__":
    bot.polling(none_stop=True)

