from telethon import TelegramClient, events
from telethon.sessions import StringSession
import asyncio
import json
import os

CONFIG_FILE = "config.json"

# Завантажуємо конфіг
with open(CONFIG_FILE, "r", encoding="utf-8") as f:
    config = json.load(f)

api_id = config["api_id"]
api_hash = config["api_hash"]
session_string = config.get("session_string")  # None
group_id = config["group_id"]


if not session_string:
    with TelegramClient(StringSession(), api_id, api_hash) as client:
        print("Введіть код підтвердження з Telegram...")
        client.start()
        session_string = client.session.save()

        config["session_string"] = session_string
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
        print("Session string збережено до config.json")
else:
    client = TelegramClient(StringSession(session_string), api_id, api_hash)


# Путь к логам
LOG_PATH = "log_sent.json"
if not os.path.exists(LOG_PATH):
    with open(LOG_PATH, "w") as f:
        json.dump({}, f)

def load_log():
    with open(LOG_PATH, "r") as f:
        return json.load(f)

def save_log(log):
    with open(LOG_PATH, "w") as f:
        json.dump(log, f)

@client.on(events.NewMessage(chats=group_id))
async def handler(event):
    text = event.raw_text.strip()
    lines = text.split("\n")
    if len(lines) < 5:
        return

    fio = lines[0].strip()
    birth_date = lines[1].strip()
    phone = lines[2].strip()
    start_date = lines[3].strip()
    shift = lines[4].strip()
    username = lines[5].strip() if len(lines) >= 6 else None

    log = load_log()
    if phone in log:
        return

    message = (
        f"Привет, меня зовут Steave, я ассистент администратора!\n"
        f"HR менеджер передал мне твои контакты и сказал, что тебя заинтересовала наша вакансия 'менеджер чата'.\n"
        f"Как указано, ты хотел бы приступить к обучению {start_date}, верно?"
    )

    try:
        if username and username.startswith("@"):  # пишем по юзернейму
            await client.send_message(username, message)
        else:  # fallback по номеру телефона
            entity = await client.get_input_entity(phone)
            await client.send_message(entity, message)

        log[phone] = True
        save_log(log)

    except Exception as e:
        print(f"Ошибка при отправке: {e}")

if __name__ == "__main__":
    with client:
        print("[Steave запущен]")
        client.run_until_disconnected() 
