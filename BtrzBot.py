#!/usr/bin/env python
# coding: utf-8

import os
import telebot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Inicia o bot do Telegram
bot = telebot.TeleBot(os.environ['BOT_API_TOKEN'])


def bot_conversa(message):
    chatbot = ChatBot("Beatriz", trainer = "chatterbot.trainers.ChatterBot.CorpusTrainer")
    resposta = chatbot.get_response(message)
    resposta = str(resposta)
    bot.reply_to(message, resposta)
    
    msgs = open("resposta.txt", "w")
    msgs.write(resposta)
    msgs.close()


#Mensagem inicial
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, u"Olá! A Beatriz não quer falar com você no momento e me desenvolveu para te responder. Se contente com isso. Mas e ai, o que tu quer?")


#Qualquer mensagem
@bot.message_handler(func=lambda message:True)
def msg(message):
    bot_conversa(message.text)
    resposta = open("resposta.txt", "r")
    resposta = resposta.read()
    bot.reply_to(message, resposta)


bot.polling()
