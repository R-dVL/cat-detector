import config
import telegram
from telegram import Update
from telegram.ext import CommandHandler, Application, CommandHandler, ContextTypes, MessageHandler, filters
from camera import motionCam

helpMsg = '''
Hola, soy PumuCam, Raúl me ha diseñado con las siguientes funciones:

1. /foto1, escribe este comando si quieres robarle un selfie al Puma desde la cámara 1.\n
/foto2 si quieres hacerlo desde la cámara 2.

2. Si vas a esta dirección http://192.168.1.142:5000 me encontraras retransmitiendo en directo (si no estas en casa tendrás que activar la VPN).

3. Cuando detecte movimiento pasaré fotos del Pumardo.
'''

# Send picture method
def send_photo(path):
    #bot.send_photo(config.CHAT_ID, photo=open(path, 'rb'))
    print('photo')

# Send message method
def send_message(text):
	#bot.sendMessage(config.CHAT_ID, text)
    print('msg')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(helpMsg)

# Command to take a photo and send it back
async def foto(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    ret, frame = motionCam.cap.read()
    motionCam.take_picture("/home/rdvl/PumuCam/app/data/foto.jpeg", frame)
    await send_photo("/home/rdvl/PumuCam/app/data/foto.jpeg")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
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