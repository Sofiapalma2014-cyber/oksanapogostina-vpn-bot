
import os
import telebot
from telebot import types

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True
    )
    keyboard.row("🔌 Подключить VPN", "⛔ Отключить VPN")
    keyboard.row("💎 Тарифы", "🆘 Поддержка")

    bot.send_message(
        message.chat.id,
        "💗 Добро пожаловать в Oksanapogostina VPN!\n\n"
        "Меню готово. Настоящее VPN-подключение "
        "пока не настроено.",
        reply_markup=keyboard
    )

@bot.message_handler(func=lambda message: True)
def menu(message):
    bot.reply_to(
        message,
        "Эта функция пока не подключена. 💗"
    )

bot.infinity_polling()
