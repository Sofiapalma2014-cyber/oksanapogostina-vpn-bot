
import os
import telebot
from telebot import types

TOKEN = os.environ.get("BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("Не задан BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True
    )
    keyboard.row("🔌 Подключить VPN")
    keyboard.row("💎 Тарифы", "🆘 Поддержка")

    bot.send_message(
        message.chat.id,
        "💖 Добро пожаловать в Oksanapogostina VPN!\n\n"
        "✨ Выбери нужный пункт меню ниже.\n\n"
        "ℹ️ Демоверсия: VPN-подключение пока не настроено.",
        reply_markup=keyboard
    )


@bot.message_handler(func=lambda message: True)
def menu(message):
    if message.text == "💎 Тарифы":
        answer = "💎 Тарифы пока готовятся."
    elif message.text == "🆘 Поддержка":
        answer = "🆘 Поддержка скоро появится."
    elif message.text == "🔌 Подключить VPN":
        answer = "🔐 VPN-сервер пока не подключён."
    else:
        answer = "💖 Выбери пункт меню ниже."

    bot.reply_to(message, answer)


bot.infinity_polling()
