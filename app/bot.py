import config
from camera import motionCam
import telegram
from telegram import Update
from telegram.ext import CommandHandler, Application, CommandHandler, ContextTypes, MessageHandler, filters

bot = telegram.Bot(config.BOT_TOKEN)

async def send_photo(path) -> None:
    await bot.send_photo(config.CHAT_ID, open(path, "rb"))

helpMsg = '''
Hola, soy PumuCam, Raúl me ha diseñado con las siguientes funciones:

1. /foto, escribe este comando si quieres robarle un selfie al Puma desde la cámara 1.\n

2. Si vas a esta dirección http://192.168.1.142:5000 me encontraras retransmitiendo en directo (si no estas en casa tendrás que activar la VPN).

3. Cuando detecte movimiento pasaré fotos del Pumardo.
'''
# Help command
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(helpMsg)

# Command to take a photo and send it back
async def foto(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    ret, frame = motionCam.cap.read()
    motionCam.take_picture("/home/rdvl/Proyectos/cat-detector/data/foto.jpeg", frame)
    await bot.send_photo(config.CHAT_ID, open("/home/rdvl/Proyectos/cat-detector/data/foto.jpeg", "rb"))

# Unknown commands filter
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Qué es ' + update.message.text + ' , no entiendo wasajasa.')

# Response to commands introduced in chat.
def start():
    application = Application.builder().token(config.BOT_TOKEN).build()
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("foto", foto))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.run_polling()

if __name__ == ("__main__"):
    start()
    print("Puma arrancando motores...")