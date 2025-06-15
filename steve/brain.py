from steve.core import build_reply

def decide_action(context):
    """
    Принимает решение на основе контекста:
    - генерирует текст для ответа
    - возвращает действие: 'message', 'call', 'wait' и т.д.
    """
    # Простейшая логика для старта — потом расширим
    reply = build_reply(context)

    if context.get("username"):
        action = "message"
    elif context.get("phone"):
        action = "message_by_phone"
    else:
        action = "wait"

    return {
        "action": action,
        "reply": reply
    }
