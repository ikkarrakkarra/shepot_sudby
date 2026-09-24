from gigachat import GigaChat

# ⚠️ ВСТАВЬ СЮДА СВОЙ КЛЮЧ ИЗ SBER STUDIO
GIGACHAT_CREDENTIALS = "MDE5ZWVkZGItYTY4ZC03OWY2LTg4MzktZjQ5OWY0OTM1MmJmOjBkOWZiZDdmLTQwNjMtNDA5YS04MzA0LTQ4NmVjMDczMGMxZg=="

# === РЕЖИМ ОТЛАДКИ ===
# True = используем заглушку (для теста callback'ов)
# False = используем реальный GigaChat
DEBUG_MODE = True

giga = GigaChat(
    credentials=GIGACHAT_CREDENTIALS,
    verify_ssl_certs=False,
    scope="GIGACHAT_API_PERS"
)

SIGN_MAP = {
    'овен': 'Овнов', 'телец': 'Тельцов', 'близнецы': 'Близнецов',
    'рак': 'Раков', 'лев': 'Львов', 'дева': 'Дев',
    'весы': 'Весов', 'скорпион': 'Скорпионов', 'стрелец': 'Стрельцов',
    'козерог': 'Козерогов', 'водолей': 'Водолеев', 'рыбы': 'Рыб'
}

period_map = {
    'today': 'сегодня',
    'tomorrow': 'завтра',
    'week': 'на неделю'
}

def generate_horoscope(sign_ru, period='today'):
    """Генерирует гороскоп через GigaChat (или заглушку в режиме отладки)."""
    sign_form = SIGN_MAP.get(sign_ru.lower(), sign_ru.capitalize())
    period_ru = period_map.get(period, 'сегодня')
    
    # Режим отладки: возвращаем тестовый гороскоп
    if DEBUG_MODE:
        return f"🔮 Тестовый гороскоп для знака {sign_form} на {period_ru}. Если ты видишь это сообщение — callback работает корректно!"
    
    # Реальный режим: запрос к GigaChat
    prompt = (
        f"Ты — опытный астролог. Напиши короткий, но глубокий гороскоп для знака {sign_form} "
        f"на {period_ru} на русском языке. Стиль: загадочный, доверительный, как 'Шёпот судьбы'. "
        "Текст должен быть уникальным, без общих фраз. Длина: 2-3 предложения. "
        "Дай конкретный совет или предсказание."
    )
    
    try:
        response = giga.chat(prompt)
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Ошибка GigaChat: {e}")
        return f"✨ Звёзды сегодня шепчут: для знака {sign_form} наступает время перемен. Прислушайся к себе."

def getHoro(sign_ru, period='today'):
    text = generate_horoscope(sign_ru, period)
    return f"<b>☀️ Гороскоп на сегодня: {sign_ru.capitalize()}</b>\n\n💬 {text}"

def getHoroTodayAll():
    return "✨ Сегодня звёзды благосклонны ко всем знакам! Выбери свой знак ниже."
