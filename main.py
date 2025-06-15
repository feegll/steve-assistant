from telethon import TelegramClient, events
from telethon.sessions import StringSession
import asyncio
import json
import os

from steve.handlers import register_handlers

CONFIG_FILE = "config.json"

# Завантажуємо конфіг
with open(CONFIG_FILE, "r", encoding="utf-8") as f:
    config = json.load(f)

api_id = config["api_id"]
api_hash = config["api_hash"]
session_string = config.get("session_string")  # None
group_id = config["group_id"]

    client = TelegramClient(StringSession(session_string), api_id, api_hash)

register_handlers(client, group_id)

if __name__ == "__main__":
    with client:
        print("[Steave запущен]")
        client.run_until_disconnected()
