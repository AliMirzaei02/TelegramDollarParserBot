from telegram.ext import Updater
from telegram._update import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import filters
import authentication
import terCode

API_TOKEN = authentication.API_TOKEN
updater = Updater(API_TOKEN, use_context=True)


def start(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Hi there. Here you can be aware of the current dollar price in rials.")

def help(update: Update, context: CallbackContext):
	update.message.reply_text("Available Commands:\n /parse - To get the current dollar price in rials")

def parse(update: Update, context: CallbackContext):
	update.message.reply_text(terCode.dollarParser())

def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)

def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('parse', parse))
updater.dispatcher.add_handler(MessageHandler(filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
	# Filters out unknown commands
	filters.command, unknown))

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(filters.text, unknown_text))
