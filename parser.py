import random
from gigachat import GigaChat

# ⚠️ ВСТАВЬ СЮДА СВОЙ КЛЮЧ ИЗ SBER STUDIO
# Найти его: developers.sber.ru → Studio → твой проект → GigaChat API → Настройки API → Авторизационные данные
GIGACHAT_CREDENTIALS = "ТВОЙ_КЛЮЧ_GIGACHAT"

giga = GigaChat(
    credentials=GIGACHAT_CREDENTIALS,
    verify_ssl_certs=False,
    scope="GIGACHAT_API_PERS"
)

TAROT_CARDS = [
    "Шут", "Маг", "Верховная Жрица", "Императрица", "Император",
    "Иерофант", "Влюблённые", "Колесница", "Сила", "Отшельник",
    "Колесо Фортуны", "Справедливость", "Повешенный", "Смерть",
    "Умеренность", "Дьявол", "Башня", "Звезда", "Луна", "Солнце",
    "Суд", "Мир"
]

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
    """Генерирует гороскоп через GigaChat."""
    sign_form = SIGN_MAP.get(sign_ru.lower(), sign_ru.capitalize())
    period_ru = period_map.get(period, 'сегодня')
    
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
        print(f"Ошибка GigaChat (гороскоп): {e}")
        return f"✨ Звёзды сегодня шепчут: для знака {sign_form} наступает время перемен. Прислушайся к себе."

def generate_tarot_reading(question=""):
    """Генерирует расклад Таро через GigaChat."""
    card = random.choice(TAROT_CARDS)
    
    prompt = (
        f"Ты — опытный таролог. Пользователь вытянул карту Таро: '{card}'. "
        f"Вопрос пользователя: '{question}'. "
        "Дай короткую, но глубокую интерпретацию этой карты в контексте вопроса. "
        "Стиль: загадочный, мистический, но полезный. Длина: 2-3 предложения."
    )
    
    try:
        response = giga.chat(prompt)
        reading = response.choices[0].message.content.strip()
        return card, reading
    except Exception as e:
        print(f"Ошибка GigaChat (Таро): {e}")
        return card, "Карта сегодня молчит, но её энергия уже рядом. Прислушайся к своему внутреннему голосу."

def getHoro(sign_ru, period='today'):
    text = generate_horoscope(sign_ru, period)
    return f"<b>☀️ Гороскоп на сегодня: {sign_ru.capitalize()}</b>\n\n💬 {text}"

def getHoroTodayAll():
    return "✨ Сегодня звёзды благосклонны ко всем знакам! Выбери свой знак ниже."
