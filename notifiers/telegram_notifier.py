from dotenv import load_dotenv
import os
from telegram import Bot

load_dotenv()

async def send_notification( message ):
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    token   = os.getenv("TELEGRAM_TOKEN")
    bot     = Bot(token=token)

    await bot.send_message(chat_id=chat_id, text=message)