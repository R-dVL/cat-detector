import config
import os
import asyncio
import telegram

bot = telegram.Bot(config.BOT_TOKEN)

async def start():
    while (True):
        file_exists = os.path.exists("/home/rdvl/Proyectos/cat-detector/data/motion.jpeg")
        if (file_exists):
            async with bot:
                await bot.send_photo(config.CHAT_ID, open("/home/rdvl/Proyectos/cat-detector/data/motion.jpeg", "rb"))
            os.remove("/home/rdvl/Proyectos/cat-detector/data/motion.jpeg")

if __name__ == ("__main__"):
    asyncio.run(start())