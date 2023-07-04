import logging
from telegram import __version__ as TG_VER
try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]
if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from terCode import dollarParser
import authentication

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_text(f"Hi {user.first_name}!\nSend /parse to get the current dollar price in rials.")

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Available Commands:\n /parse - To get the current dollar price in rials.")

async def get_dollar(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
	"""Send a message when the command /parse is issued."""
	message = dollarParser()
	await update.message.reply_text(message)

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text("I didn't understand your message :(\nTry again.")


def main() -> None:
	"""Start the bot."""
	# Create the Application and pass it your bot's token.
	API_TOKEN = authentication.API_TOKEN
	application = Application.builder().token(API_TOKEN).build()

    # on different commands - answer in Telegram
	application.add_handler(CommandHandler("start", start))
	application.add_handler(CommandHandler("help", help))
	application.add_handler(CommandHandler("parse", get_dollar))

    # on non command i.e message - echo the message on Telegram
	application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, unknown))

    # Run the bot until the user presses Ctrl-C
	application.run_polling()


if __name__ == "__main__":
    main()
