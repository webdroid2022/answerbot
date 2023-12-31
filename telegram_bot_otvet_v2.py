import telebot
import os

bot_token = os.getenv("BOT_TOKEN")
GROUP_CHAT_ID = os.getenv("GROUP_CHAT_ID")  # Замініть на ID групового чату

bot = telebot.TeleBot(bot_token)

# обробка команди /start
@bot.message_handler(commands=["start"])
def handle_start(message):
    bot.send_message(message.chat.id, 'Чим я можу допомогти?')

# обробка текстових повідомлень
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.chat.id == GROUP_CHAT_ID:  # Повідомлення від групи - відповідь
        if message.reply_to_message:  # Це відповідь на повідомлення
            user_id = message.reply_to_message.forward_from.id
            bot.send_message(user_id, message.text)
    else:  # Повідомлення від користувача - запит
        bot.forward_message(GROUP_CHAT_ID, message.chat.id, message.message_id)
