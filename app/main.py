import motion
import bot
import stream
import threading
import asyncio

# Motion detector Thread
class motionDetectorThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        motion.start()

motionThread_1 = motionDetectorThread(1, "Motion Detector", 1)

# File check thread
class fileCheckThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        asyncio.run(bot.fileCheck())

fileCheckerThread_1 = fileCheckThread(2, "File Check", 1)

class streamingThread(threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter

   def run(self):
      stream.start()

StreamThread_1 = streamingThread(3, "Streaming", 1)

if __name__ == "__main__":
    motionThread_1.start()
    fileCheckerThread_1.start()
    StreamThread_1.start()
    # Not using a separated thread for bot polling since async gave me some problems with it
    bot.start()