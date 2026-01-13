import telebot

TOKEN = "8321512442:AAGuqdF6y7FG8q9mpga3WfBDqLpt2tcOAmQ"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Привет! 👋\n\n"
        "Вот ссылка на Pocket Option:\n"
        "https://u3.shortink.io/main?utm_campaign=797988&utm_source=affiliate&utm_medium=sr&a=NB8LBSuYJ5oitr&ac=invest&code=50START"
    )

bot.polling()
