import motion
import bot
import threading
import asyncio

class Thread_1(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
      
    def run(self):
        motion.start()
      
motionThread = Thread_1(1, "Motion Detector", 1)

class Thread_2(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
      
    def run(self):
        asyncio.run(bot.file_check())
      
fileCheckerThread = Thread_2(2, "File Checker", 2)

if __name__ == "__main__":
    motionThread.start()
    fileCheckerThread.start()
    bot.send_message("GatiCam arrancando motores...")
    bot.start()