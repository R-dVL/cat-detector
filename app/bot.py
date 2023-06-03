import config
import os
from camera import motionCam
import telegram
from telegram import Update
from telegram.ext import CommandHandler, Application, CommandHandler, ContextTypes, MessageHandler, filters

bot = telegram.Bot(config.BOT_TOKEN)

# Help message
helpMsg = '''
Hola, soy PumuCam, Raúl me ha diseñado con las siguientes funciones:

1. /foto, escribe este comando si quieres robarle un selfie al Puma desde la cámara\n

2. Cuando detecte movimiento pasaré fotos del Pumardo.
'''

# Help command
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(helpMsg)

# Command to take a photo
async def foto(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    ret, frame = motionCam.readCap()
    motionCam.take_picture("photo.jpeg", frame)

# Unknown commands filter
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Qué es ' + update.message.text + ' , no entiendo wasajasa.')

# Escaneo cíclico en búsqueda de la foto de movimiento
async def file_check():
    while (True):
        motion_exists = os.path.exists("motion.jpeg")
        photo_exists = os.path.exists("photo.jpeg")

        if (motion_exists):
            try:
                async with bot:
                    await bot.send_photo(config.CHAT_ID, open("motion.jpeg", "rb"))
                os.remove("motion.jpeg")
            except:
                print("Error sending photo")

        elif (photo_exists):
            try:
                async with bot:
                    await bot.send_photo(config.CHAT_ID, open("photo.jpeg", "rb"))
                os.remove("photo.jpeg")
            except:
                print("Error sending photo")

async def send_message(text):
    try:
        async with bot:
            await bot.send_message(config.CHAT_ID, text)
    except:
        print("Error sending message")

# Response to commands introduced in chat.
def start() -> None:
    application = Application.builder().token(config.BOT_TOKEN).build()
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("foto", foto))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, unknown))
    application.run_polling()