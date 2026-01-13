import telebot
import os
import random

TOKEN = os.getenv("8321512442:AAGuqdF6y7FG8q9mpga3WfBDqLpt2tcOAmQ")
bot = telebot.TeleBot(TOKEN)

# ТВОЙ Telegram ID
ADMIN_ID = 123456789  # ← ОБЯЗАТЕЛЬНО замени на свой

# Одобренные пользователи
approved_users = set()

# Валютные пары OTC
PAIRS = [
    "EUR/USD OTC",
    "GBP/USD OTC",
    "USD/JPY OTC",
    "AUD/USD OTC",
    "USD/CHF OTC"
]

# Таймфреймы
TIMEFRAMES = ["5s", "10s", "15s", "30s", "1m", "2m", "3m", "5m"]

DIRECTIONS = ["⬆️ BUY", "⬇️ SELL"]

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "👋 Добро пожаловать!\n\n"
        "📌 Чтобы получить сигналы:\n"
        "1️⃣ Зарегистрируйтесь по ссылке:\n"
        "https://u3.shortink.io/main?utm_campaign=797988&utm_source=affiliate&utm_medium=sr&a=NB8LBSuYJ5oitr&ac=invest&code=50START\n\n"
        "2️⃣ Пополните баланс от 30$\n"
        "3️⃣ Отправьте свой Pocket Option ID\n\n"
        "❗ Без регистрации и депозита сигналы не выдаются."
    )

@bot.message_handler(func=lambda m: m.text.isdigit())
def receive_id(message):
    bot.send_message(
        message.chat.id,
        "✅ ID получен.\n"
        "⏳ Ожидайте проверки."
    )

    bot.send_message(
        ADMIN_ID,
        f"🔔 НОВЫЙ ПОЛЬЗОВАТЕЛЬ\n\n"
        f"👤 @{message.from_user.username}\n"
        f"📱 Telegram ID: {message.chat.id}\n"
        f"🆔 Pocket ID: {message.text}"
    )

@bot.message_handler(commands=['signal'])
def send_signal(message):
    if message.chat.id not in approved_users:
        bot.send_message(
            message.chat.id,
            "⛔ Доступ закрыт.\n"
            "Сначала регистрация и депозит от 30$."
        )
        return

    pair = random.choice(PAIRS)
    timeframe = random.choice(TIMEFRAMES)
    direction = random.choice(DIRECTIONS)

    bot.send_message(
        message.chat.id,
        f"📊 СИГНАЛ\n\n"
        f"📈 Пара: {pair}\n"
        f"⏱ Таймфрейм: {timeframe}\n"
        f"🎯 Направление: {direction}\n\n"
        f"⏰ Вход: СЕЙЧАС"
    )

@bot.message_handler(commands=['approve'])
def approve_user(message):
    if message.chat.id != ADMIN_ID:
        return

    try:
        user_id = int(message.text.split()[1])
        approved_users.add(user_id)

        bot.send_message(
            user_id,
            "✅ Доступ подтверждён!\n"
            "Теперь вы можете получать сигналы.\n\n"
            "📌 Команда: /signal"
        )

        bot.send_message(message.chat.id, "✅ Пользователь одобрен.")
    except:
        bot.send_message(
            message.chat.id,
            "❌ Ошибка.\n"
            "Используй формат:\n"
            "/approve TELEGRAM_ID"
        )

bot.polling()

 

