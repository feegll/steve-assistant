from telethon import TelegramClient
import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION_STRING = os.getenv("SESSION_STRING")

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

def start_userbot():
    @client.on(events.NewMessage(pattern="/ping"))
    async def handler(event):
        await event.reply("✅ Я жив, братан!")

    print("✅ Стив запущен как userbot.")
    client.start()
    client.run_until_disconnected()
