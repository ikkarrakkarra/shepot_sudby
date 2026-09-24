import telebot
from telebot import types
from parser import getHoro, getHoroTodayAll, generate_tarot_reading, period_map
from keyboards import get_main_keyboard, get_zodiac_keyboard, get_share_keyboard

# ⚠️ ВСТАВЬ СЮДА СВОЙ ТОКЕН ОТ @BotFather
TOKEN = "ТВОЙ_ТОКЕН_ОТ_BOTFATHER"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "🌙 *«Тсс... Слушай. Судьба не кричит — она шепчет.»*\n\n"
        "Я — твой проводник в мире звёзд и карт Таро. "
        "Выбери, что тебя интересует:"
    )
    bot.send_message(message.chat.id, welcome_text, parse_mode='Markdown', reply_markup=get_main_keyboard())

@bot.message_handler(func=lambda message: message.text == "🔮 Гороскоп")
def horoscope_menu(message):
    text = getHoroTodayAll() + "\n\n⚛️ Выбери свой знак зодиака:"
    bot.send_message(message.chat.id, text, reply_markup=get_zodiac_keyboard())

@bot.message_handler(func=lambda message: message.text == "🃏 Таро")
def tarot_menu(message):
    text = (
        "🃏 *Таро-расклад*\n\n"
        "Задай свой вопрос (или просто напиши что-нибудь), и я вытяну для тебя карту."
    )
    bot.send_message(message.chat.id, text, parse_mode='Markdown')
    bot.register_next_step_handler(message, process_tarot_question)

def process_tarot_question(message):
    question = message.text
    card, reading = generate_tarot_reading(question)
    
    response_text = (
        f"🃏 *Твоя карта:* {card}\n\n"
        f"💬 *Толкование:*\n{reading}"
    )
    bot.send_message(message.chat.id, response_text, parse_mode='Markdown', reply_markup=get_share_keyboard())

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if "|" in call.data:
        el = call.data.split("|")
        sign = el[0]
        period = el[1]
        horoscope = getHoro(sign, period_map.get(period, 'today'))
        
        bot.send_message(
            call.message.chat.id,
            horoscope,
            parse_mode="html",
            disable_web_page_preview=True,
            reply_markup=get_share_keyboard()
        )

if __name__ == '__main__':
    bot.infinity_polling(interval=0)
