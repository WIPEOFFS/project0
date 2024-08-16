import logging
import os

import telebot

from logger_setup import setup_logger

logger = setup_logger(__name__, log_level=logging.INFO)

TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['version'])
def send_version(message):
    bot.reply_to(message, 'created by WIPEOFFS')
    logger.info(f"User {message.from_user.username} ({message.from_user.id}) sent: {message.text}")


@bot.message_handler(func=lambda message: True)
def log_message(message):
    logger.info(f"Received message from {message.from_user.username} ({message.from_user.id}): {message.text}")


if __name__ == '__main__':
    logger.info("Bot is starting...")
    bot.polling(none_stop=True)
