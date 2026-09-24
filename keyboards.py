from telebot import types

def get_main_keyboard():
    """Главная клавиатура с выбором раздела."""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn_horoscope = types.KeyboardButton("🔮 Гороскоп")
    btn_tarot = types.KeyboardButton("🃏 Таро")
    markup.add(btn_horoscope, btn_tarot)
    return markup

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
    """Кнопка 'Поделиться'."""
    markup = types.InlineKeyboardMarkup()
    share_btn = types.InlineKeyboardButton("🔮 Поделиться с друзьями", switch_inline_query="")
    markup.add(share_btn)
    return markup
