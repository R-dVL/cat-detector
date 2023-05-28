import motion
import bot
import threading

class Thread_1(threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
      
   def run(self):
      motion.start()
      
MotionThread = Thread_1(1, "Motion Detector", 1)

class Thread_2(threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
      
   def run(self):
      bot.start()
      
BotThread = Thread_2(2, "Telegram Bot", 2)

if __name__ == "__main__":
   BotThread.start()
   print("Bot arrancando..")
   bot.send_message("PumuCam arrancando motores...\n Escribe /help si necesitas ayuda.")
   
   MotionThread.start()
   print("Detectando Pumas..")