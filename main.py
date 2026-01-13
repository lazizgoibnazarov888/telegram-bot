import telebot
import os

TOKEN = os.getenv("8321512442:AAGuqdF6y7FG8q9mpga3WfBDqLpt2tcOAmQ")
bot = telebot.TeleBot(TOKEN)

LINK = "https://u3.shortink.io/main?utm_campaign=797988&utm_source=affiliate&utm_medium=sr&a=NB8LBSuYJ5oitr&ac=invest&code=50START"

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "👋 Добро пожаловать!\n\n"
        "Чтобы начать:\n"
        "1️⃣ Зарегистрируйтесь по ссылке\n"
        "2️⃣ Пополните баланс\n"
        "3️⃣ Напишите «готово»\n\n"
        f"🔗 Ссылка:\n{LINK}"
    )

@bot.message_handler(func=lambda message: True)
def auto_reply(message):
    text = message.text.lower()

    if "готово" in text:
        bot.send_message(
            message.chat.id,
            "✅ Отлично! Ваша заявка принята.\nОжидайте дальнейших инструкций."
        )
    elif "помощь" in text:
        bot.send_message(
            message.chat.id,
            "ℹ️ Если есть вопросы — просто напишите их сюда."
        )
    else:
        bot.send_message(
            message.chat.id,
            "🤖 Я получил ваше сообщение.\n"
            "Напишите «готово» после регистрации."
        )

bot.polling(none_stop=True)

