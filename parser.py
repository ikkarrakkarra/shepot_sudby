from gigachat import GigaChat
from gigachat.models import Chat, Messages, MessagesRole

# ⚠️ ВСТАВЬ СЮДА СВОЙ КЛЮЧ ИЗ SBER STUDIO
# Найти: developers.sber.ru → Studio → проект → GigaChat API → Настройки API → Авторизационные данные
GIGACHAT_CREDENTIALS = "MDE5ZWVkZGItYTY4ZC03OWY2LTg4MzktZjQ5OWY0OTM1MmJmOjBkOWZiZDdmLTQwNjMtNDA5YS04MzA0LTQ4NmVjMDczMGMxZg=="

# Инициализация клиента с базовым адресом для физических лиц
client = GigaChat(
    base_url="https://api.giga.chat/v1",
    credentials=GIGACHAT_CREDENTIALS,
    scope="GIGACHAT_API_PERS",
    verify_ssl_certs=False,
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
    """Генерирует гороскоп через GigaChat Ultra 3.5."""
    sign_form = SIGN_MAP.get(sign_ru.lower(), sign_ru.capitalize())
    period_ru = period_map.get(period, 'сегодня')
    
    prompt = (
        f"Ты — опытный астролог. Напиши короткий, но глубокий гороскоп для знака {sign_form} "
        f"на {period_ru} на русском языке. Стиль: загадочный, доверительный, как 'Шёпот судьбы'. "
        "Текст должен быть уникальным, без общих фраз. Длина: 2-3 предложения. "
        "Дай конкретный совет или предсказание."
    )
    
    try:
        # Создаём объект Chat согласно официальному примеру
        chat = Chat(
            model="GigaChat-3-Ultra",
            messages=[Messages(role=MessagesRole.USER, content=prompt)],
        )
        
        # Отправляем запрос
        resp = client.chat(chat)
        
        # Извлекаем текст ответа
        horoscope = resp.choices[0].message.content.strip()
        return horoscope
        
    except Exception as e:
        print(f"Ошибка GigaChat: {e}")
        return f"✨ Звёзды сегодня шепчут: для знака {sign_form} наступает время перемен. Прислушайся к себе."

def getHoro(sign_ru, period='today'):
    text = generate_horoscope(sign_ru, period)
    return f"<b>☀️ Гороскоп на сегодня: {sign_ru.capitalize()}</b>\n\n💬 {text}"

def getHoroTodayAll():
    return "✨ Сегодня звёзды благосклонны ко всем знакам! Выбери свой знак ниже."
