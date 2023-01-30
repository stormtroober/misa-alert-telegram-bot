
"""
Simple bot to send message about levels of Misa river during the emergencies
"""
import DataRetriever as DataRetriever
import ReservedSettings
import logging
from Settings import loop_time
from Resources import NoPrintCode, ErrorCode

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
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, JobQueue, MessageHandler, filters

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

async def tresholdChange(update: Update, _) -> None:
    if(checkAllUserIds(update.message.from_user.id)):
        try:
            splittedMessage = update.message.text.replace(',', '.').split()
            if(len(splittedMessage) > 1 and len(splittedMessage) < 3):
                try:
                    value = float(splittedMessage[1])
                except Exception as ex:
                    print("EXCEPTION " + ex)
                    await update.message.reply_text("Uso: /setSogliaAllarme <1.5>")
                else:
                    DataRetriever.getDataFilter().changeTreshold(value)
                    await update.message.reply_text("Certo " + update.message.from_user.name + ', soglia cambiata a ' + str(value) + ' metri')
            else:
                await update.message.reply_text("Uso: /setSogliaAllarme <1.5>")

        except Exception as ex:
            print(ex)
            await update.message.reply_text("Uso: /setSogliaAllarme <1.5>")
    else:
        await update.message.reply_text(update.message.from_user.name + ' non sei autorizzato a fare questo cambiamento!')
    
def checkAllUserIds(from_user_id):
    tests = []
    for id in ReservedSettings.whiteListedUserIds:
        tests.append(from_user_id == id)
    return any(tests)

async def ping(update: Update, _) -> None:
    await update.message.reply_text("Ci sono!")

async def alarm(context: ContextTypes.DEFAULT_TYPE) -> None:
    dataFilteredAndFormatted = DataRetriever.RetrieveStationData()
    #DEBUG COMANDI
    #dataFilteredAndFormatted = ErrorCode
    if(dataFilteredAndFormatted != ErrorCode):
        if dataFilteredAndFormatted != NoPrintCode:
            await context.bot.send_message(ReservedSettings.DefaultChatId, 
                                        #    message_thread_id=ReservedSettings.DefaultTopicId, 
                                           text=dataFilteredAndFormatted)
    else:
        print('Cannot get Data from the host.')


def main() -> None:
    """Run bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(ReservedSettings.token).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler(["setSogliaAllarme"], tresholdChange))
    echo_handler = MessageHandler(filters.TEXT, ping)
    application.add_handler(echo_handler)

    keyboard = [[InlineKeyboardButton("Option 1", callback_data='1'),
             InlineKeyboardButton("Option 2", callback_data='2')]]
    

    reply_markup = InlineKeyboardMarkup(keyboard)
    # await application.bot.send_message(chat_id='YOUR_CHAT_ID', text='Choose an option:', reply_markup=reply_markup)

    job_queue = application.job_queue
    job_alarm = job_queue.run_repeating(alarm, interval=loop_time, first=1)
    # Run the bot until the user presses Ctrl-C
    application.run_polling()
    
if __name__ == "__main__":
    main()