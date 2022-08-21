#! /usr/bin/env python3
# -*- coding: utf-8 -*
import telebot;
from env import token;
bot = telebot.TeleBot(token);
@bot.message_handler(content_types=['text'])#@bot.message_handler(content_types=['text', 'document', 'audio'])
def get_text_messages(message):
    if message.text.lower() == "привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text.lower() == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    elif message.text.lower() == "дурак":
        bot.send_message(message.from_user.id, "Сам дурак!!!")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=0)