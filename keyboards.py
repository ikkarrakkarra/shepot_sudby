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
    buttons = [types.InlineKeyboardButton(text=name, callback_data=f"{code}|today") for name, code in signs]
    markup.add(*buttons)
    return markup

def get_share_keyboard():
    """Кнопка 'Поделиться' через стандартную ссылку Telegram."""
    markup = types.InlineKeyboardMarkup()
    share_btn = types.InlineKeyboardButton(
        text="🔮 Поделиться с друзьями",
        url="https://t.me/share/url?url=https://t.me/shepotsudby_bot&text=Загляни в «Шёпот судьбы» — узнай свой гороскоп!"
    )
    markup.add(share_btn)
    return markup
