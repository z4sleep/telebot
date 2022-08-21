#! /usr/bin/env python3
# -*- coding: utf-8 -*
import telebot;
from datetime import datetime;
from env import token;
bot = telebot.TeleBot(token);
@bot.message_handler(content_types=['text'])#@bot.message_handler(content_types=['text', 'document', 'audio'])
def get_text_messages(message):
    #current_date = datetime.now().date();
    #current_time = datetime.now().time();
    if message.text.lower() in ["привет","hi","hi","hello","здарова","шалом"]:
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text.lower() == "/help":
        bot.send_message(message.from_user.id, "Поздаровайся или спроси меня то что я знаю! Например время, дату или ...")
    elif message.text.lower() in ["дурак","дебил","осел","тормоз","идиот"]:
        bot.send_message(message.from_user.id, f"Сам {message.text}!!!")
    elif message.text.lower() in ["сколько времени","сколько время","который час","время","назови время","скажи время","time","current time"]:
        bot.send_message(message.from_user.id, f"На вопрос - {message.text} я отвечу {datetime.now().time()}")
    elif message.text.lower() in ["какое число","какое сегодня число","дата","назови дату","скажи дату","date","current data"]:
        bot.send_message(message.from_user.id, f"На вопрос - {message.text} я отвечу {datetime.now().date()}")
    else:
        bot.send_message(message.from_user.id, f"Я не понимаю что значит - {message.text} \nНапиши /help")


bot.polling(none_stop=True, interval=0)