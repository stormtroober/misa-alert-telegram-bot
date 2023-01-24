
"""
Simple bot to send message about levels of Misa river during the emergencies
"""
import DataRetriever as DataRetriever
import ReservedSettings
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
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, JobQueue

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)



# Define a few command handlers. These usually take the two arguments update and
# context.
# Best practice would be to replace context with an underscore,
# since context is an unused local variable.
# This being an example and not having context present confusing beginners,
# we decided to have it present as context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends explanation on how to use the bot."""
    await update.message.reply_text("Hi! Use /set <seconds> to set a timer")


async def alarm(context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send the alarm message."""
    job = context.job
    data = DataRetriever.RetrieveStationData()
    await context.bot.send_message(ReservedSettings.MyUserId, text=data)

def main() -> None:
    """Run bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(ReservedSettings.token).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler(["start", "help"], start))

    job_queue = application.job_queue
    job_minute = job_queue.run_repeating(alarm, interval=600, first=10)
    # Run the bot until the user presses Ctrl-C
    application.run_polling()
    
if __name__ == "__main__":
    main()