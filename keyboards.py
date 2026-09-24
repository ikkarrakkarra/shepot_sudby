from telebot import types

def get_zodiac_keyboard():
    """Клавиатура для выбора знака зодиака."""
    markup = types.InlineKeyboardMarkup(row_width=3)
    signs = [
        ("♈ Овен", "овен"), ("♉ Телец", "телец"), ("♊ Близнецы", "близнецы"),
        ("♋ Рак", "рак"), ("♌ Лев", "лев"), ("♍ Дева", "дева"),
        ("♎ Весы", "весы"), ("♏ Скорпион", "скорпион"), ("♐ Стрелец", "стрелец"),
        ("♑ Козерог", "козерог"), ("♒ Водолей", "водолей"), ("♓ Рыбы", "рыбы")
    ]
    buttons = []
    for name, code in signs:
        btn = types.InlineKeyboardButton(text=name, callback_data=f"{code}|today")
        buttons.append(btn)
    markup.add(*buttons)
    return markup


def get_share_keyboard():
    """Кнопка 'Поделиться' с непустым текстом (это важно!)."""
    markup = types.InlineKeyboardMarkup()
    share_btn = types.InlineKeyboardButton(
        text="🔮 Поделиться с друзьями",
        switch_inline_query="Загляни в «Шёпот судьбы» — узнай свой гороскоп! 🔮"
    )
    markup.add(share_btn)
    return markup
