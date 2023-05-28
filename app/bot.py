import telegram
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from app.camera import motionCam, streamCam

helpMsg = '''
Hola, soy PumuCam, Raúl me ha diseñado con las siguientes funciones:

1. /foto1, escribe este comando si quieres robarle un selfie al Puma desde la cámara 1.\n
/foto2 si quieres hacerlo desde la cámara 2.

2. Si vas a esta dirección http://192.168.1.142:5000 me encontraras retransmitiendo en directo (si no estas en casa tendrás que activar la VPN).
   
3. Cuando detecte movimiento pasaré fotos del Pumardo.
'''

# Setup
def obtainCHAT_ID():
    with open("/home/rdvl/PumuCam/app/data/CHAT_ID") as f:
        CHAT_ID = f.read()
        f.close()
    return CHAT_ID
    
def obtainTOKEN():
    with open("/home/rdvl/PumuCam/app/data/TOKEN") as f:
        TOKEN = f.read()
        f.close()
    return TOKEN
    
bot = telegram.Bot(obtainTOKEN())
updater = Updater(obtainTOKEN(), use_context=True)

# Send picture method
def send_photo(path):
    bot.send_photo(obtainCHAT_ID(), photo=open(path, 'rb'))
    
# Send message method
def send_message(text):
	bot.sendMessage(obtainCHAT_ID(), text)
 
def help(update: Update, context: CallbackContext):
    update.message.reply_text(helpMsg)

# Command to take a photo and send it back
def foto(update: Update, context: CallbackContext):
    ret, frame = motionCam.cap.read()
    motionCam.take_picture("/home/rdvl/PumuCam/app/data/foto.jpeg", frame)
    send_photo("/home/rdvl/PumuCam/app/data/foto1.jpeg")
    
# Response to unknown commands (filters every /"text" introduced in the chat).
def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Que es'%s', no entiendo wasajasa" % update.message.text)

# Response to commands introduced in chat.
def start():
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(CommandHandler('foto1', foto1))
    updater.dispatcher.add_handler(CommandHandler('foto2', foto2))
    updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))
    updater.start_polling()
    
if __name__ == ("__main__"):
    start()