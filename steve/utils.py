def extract_context(lines):
    """
    Преобразует строки из Telegram в структуру данных.
    """
    context = {
        "first_name": lines[0].strip(),
        "birth_date": lines[1].strip(),
        "phone": lines[2].strip(),
        "start_date": lines[3].strip(),
        "shift": lines[4].strip(),
        "username": lines[5].strip() if len(lines) >= 6 else None,
    }
    return context
