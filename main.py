import telebot
from persona_generator import generate_persona
from avatar_generator import generate_avatar
from config import TELEGRAM_TOKEN

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     "Привет! Я — EGO AI. Напиши, кем ты хочешь стать: \nНапример: Хочу стать уверенным миллионером")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_input = message.text
    persona = generate_persona(user_input)
    avatar_url = generate_avatar(user_input)

    response = f"\U0001F464 *Твой новый образ создан!*\n\n"                f"*Имя стиля:* {persona['title']}\n"                f"*Описание:* {persona['bio']}\n"                f"*Советы:* {persona['tips']}\n\n"                f"_Сгенерировано AI_"
    bot.send_photo(message.chat.id, avatar_url, caption=response, parse_mode='Markdown')

bot.polling()
