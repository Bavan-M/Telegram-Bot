from dotenv import load_dotenv
import os
from aiogram import Bot,Dispatcher,executor,types
import openai
import sys

load_dotenv()
openai.api_key=os.getenv("OPENAI_API_KEY")
TELEGRAM_BOT_TOKEN=os.getenv("TELEGRAM_BOT_TOKEN")

class Reference:
    def __init__(self)->None:
        self.response=""

refernce=Reference()
model_name="gpt-3.5-turbo"

bot=Bot(token=TELEGRAM_BOT_TOKEN)
dispatcher=Dispatcher(bot=bot)

def clear_past():
    refernce.response=""

@dispatcher.message_handler(commands=['clear'])
async def clear(message:types.Message):
    clear_past()
    await message.reply("i have cleared the past conversaton and context")

@dispatcher.message_handler(commands=['help'])
async def helper(message:types.Message):
    help_command="""
        Hi ,I am Tele bot ! Please follow the command
        /start - to start the conversation
        /clear - to clear the past conversation and context
        /help - to get this help menu
    """
    await message.reply(help_command)

@dispatcher.message_handler(commands=['start'])
async def welcome(messages:types.Message):
    await messages.reply("Hi\n I am Tele Bot\nHow can i assisit you ?")

@dispatcher.message_handler()
async def chatgpt(message:types.Message):
    print(f">> User : \n\t{message.text}")
    response=openai.ChatCompletion.create(
        model=model_name,
        messages=[
            {"role":"assistant","content":refernce.response},
            {"role":"user","content":message.text}
        ]
    )
    refernce.response=response['choices'][0]['message']['content']
    print(f">>> chatGPT : \n\t{refernce.response}")
    await bot.send_message(chat_id=message.chat.id,text=refernce.response)

if __name__=="__main__":
    executor.start_polling(dispatcher=dispatcher,skip_updates=True)