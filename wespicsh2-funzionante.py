# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 21:33:00 2020

@author: david
"""

import requests
from bs4 import BeautifulSoup
#import scraper as sc

import logging

from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)

TOKEN = '1231697784:AAEu6I6yRyaEFg3NCROtXsHXWaZpRgLX-SA'

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

Wespicsh_base_knowledge = "\nOra che mi hai avviato con /start, ti dico che non sempre dò aiuto con /help.\nMa con /item dico un paio di cose."
"""
PREZZO = range(1)

reply_keyboard = [
    ['Prezzo'],
    ['Done'],
]

markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
"""

def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Ciaone a te!' + Wespicsh_base_knowledge)


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Aiutati da solo')


def item(update: Update, context: CallbackContext) -> str:
    """Nome e prezzo articolo messo su scraper"""
    URL = 'https://www.amazon.it/Microsoft-WS2-00010-Tastiera-di-Design/dp/B072LQSNJH/ref=nav_ya_signin?__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2X3S702VMGCU9&dchild=1&keywords=surface+keyboard&qid=1608551836&sprefix=surface+key%2Caps%2C385&sr=8-1&'
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id='productTitle').get_text()
    price = soup.find(id='price_inside_buybox').get_text()
    p = price.replace('\n','')
    p1 = p.replace('\xa0','')

    update.message.reply_text(f'Nome item: {title.strip()}\nPrezzo: {p1}\nLink: {URL}') #, reply_markup=markup,)


'''
def done(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        "ciao"
    )

    return ConversationHandler.END
'''
'''
def unknown(update, context):
    answer = "Dai su, t'ho detto cosa puoi fare..."
    context.bot.send_message(chat_id=update.effective_chat.id, text=answer)
'''

def main():
    """Start the bot."""
    updater = Updater("1231697784:AAEu6I6yRyaEFg3NCROtXsHXWaZpRgLX-SA", use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher
 
    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    #dispatcher.add_handler(MessageHandler(Filters.command, unknown))
    dispatcher.add_handler(CommandHandler("item", item))
    #dispatcher.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
