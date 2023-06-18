import os
from camera import motionCam
import telegram
from telegram import Update
from telegram.ext import CommandHandler, Application, CommandHandler, ContextTypes, MessageHandler, filters

BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

# Help message
helpMsg = '''
Hola, soy GatiCam, Raúl me ha diseñado con las siguientes funciones:

1. /foto, escribe este comando si quieres robarle un selfie al Puma desde la cámara\n

2. Cuando detecte movimiento pasaré fotos del Pumardo.
'''

# Help command
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(helpMsg)

# Command to take a photo
async def foto(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    ret, frame = motionCam.getVideo()
    motionCam.takePhoto("photo.jpeg", frame)

# Unknown commands filter
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Qué es ' + update.message.text + ' , no entiendo wasajasa.')

bot = telegram.Bot(BOT_TOKEN)

# Cyclic scan of the folder to send pictures (worked better than sending it right back when the picture is taken)
async def fileCheck():
    while (True):
        motion_exists = os.path.exists("motion.jpeg")
        photo_exists = os.path.exists("photo.jpeg")

        if (motion_exists):
            try:
                async with bot:
                    await bot.send_photo(CHAT_ID, open("motion.jpeg", "rb"))
                os.remove("motion.jpeg")
            except:
                pass

        elif (photo_exists):
            try:
                async with bot:
                    await bot.send_photo(CHAT_ID, open("photo.jpeg", "rb"))
                os.remove("photo.jpeg")
            except:
                pass

# Response to commands introduced in chat.
def start() -> None:
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("foto", foto))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, unknown))
    application.run_polling()