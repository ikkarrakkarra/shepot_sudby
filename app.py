import telebot
from telebot import types
from parser import getHoro, getHoroTodayAll, period_map
from keyboards import get_zodiac_keyboard

# ⚠️ ВСТАВЬ СЮДА СВОЙ ТОКЕН ОТ @BotFather
TOKEN = "8910242289:AAHA58NR6EB-0IIQy6vx9GNRKId1x4f3l7U"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "🌙 *«Тсс... Слушай. Судьба не кричит — она шепчет.»*\n\n"
        "Я — твой астрологический проводник. "
        "Выбери свой знак зодиака, и я расскажу, что звёзды приготовили для тебя сегодня.\n\n"
        "⚛️ Выбери свой знак зодиака:"
    )
    bot.send_message(
        message.chat.id,
        welcome_text,
        parse_mode='Markdown',
        reply_markup=get_zodiac_keyboard()
    )

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    bot.answer_callback_query(call.id)
    
    if "|" in call.data:
        el = call.data.split("|")
        sign = el[0]
        period = el[1]
        
        horoscope = getHoro(sign, period_map.get(period, 'сегодня'))
        
        bot.send_message(
            call.message.chat.id,
            horoscope,
            parse_mode="html",
            disable_web_page_preview=True
        )

if __name__ == '__main__':
    print("=== БОТ ЗАПУЩЕН ===")
    bot.infinity_polling(interval=0)
