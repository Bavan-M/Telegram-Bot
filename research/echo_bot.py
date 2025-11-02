import logging
from aiogram import Bot,Dispatcher,executor,types
from dotenv import load_dotenv
import os

load_dotenv()
TELEGRAM_BOT_TOKEN=os.getenv("TELEGRAM_BOT_TOKEN")
#print(TELEGRAM_BOT_TOKEN)

logging.basicConfig(level=logging.INFO)

bot=Bot(token=TELEGRAM_BOT_TOKEN)
dp=Dispatcher(bot)

@dp.message_handler(commands=['start','help'])
async def command_start_handler(message:types.Message):
    await message.reply("Hi\nI am Echo bot!\nPowered by aiogram")

if __name__=="__main__":
    executor.start_polling(dispatcher=dp,skip_updates=True)