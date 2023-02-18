import requests
import json
from telegram.ext import Updater, CommandHandler, MessageHandler, filters
updater = Updater(token = '1862942603:AAEzW9QN8u09zBK79PdcUBk2AI2bml1TWaM', use_context=True)
dispatcher = updater.dispatcher
def hello(update,context):
    context.bot.send_message(chat_id = update.effective_chat.id,text='hello world')
hello_Handler=CommandHandler('hello', hello)
dispatcher.add_handler(hello_Handler)
updater.start_polling()