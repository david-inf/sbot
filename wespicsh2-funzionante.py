# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 21:33:00 2020

@author: david
"""


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

Wespicsh_base_knowledge = "\nOra che mi hai avviato con /start, ti dico che non sempre dò aiuto con /help."


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Ciaone a te!' + Wespicsh_base_knowledge)


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Aiutati da solo')


def unknown(update, context):
    answer = "Dai su, t'ho detto cosa puoi fare..."
    context.bot.send_message(chat_id=update.effective_chat.id, text=answer)


def main():
    """Start the bot."""
    updater = Updater("1231697784:AAEu6I6yRyaEFg3NCROtXsHXWaZpRgLX-SA", use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher
    
    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(MessageHandler(Filters.command, unknown))
    dispatcher.add_handler(CommandHandler("item", item))
    dispatcher.add_handler(conv_handler)
    
    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher
    
    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()  # fai def main()
