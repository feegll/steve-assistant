from telethon import events
from .core import build_reply
from .utils import extract_context
from .log import load_log, save_log

def register_handlers(client, group_id):
    @client.on(events.NewMessage(chats=group_id))
    async def handler(event):
        text = event.raw_text.strip()
        lines = text.split("\n")
        if len(lines) < 5:
            return

        context = extract_context(lines)
        log = load_log()
        phone = context.get("phone")

        if phone in log:
            return

        reply = build_reply(context)

        try:
            if context.get("username") and context["username"].startswith("@"):
                await client.send_message(context["username"], reply)
            else:
                entity = await client.get_input_entity(phone)
                await client.send_message(entity, reply)

            log[phone] = True
            save_log(log)
        except Exception as e:
            print(f"[Ошибка отправки]: {e}")
