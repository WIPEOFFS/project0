import os
import logging
import telebot
from logger_setup import setup_logger
from nasa.nasa_api import fetch_nasa_apod

logger = setup_logger(__name__, log_level=logging.INFO)

# Используйте os для получения токена из переменных окружения
TOKEN = os.getenv('TOKEN')

if not TOKEN:
    logger.error("TOKEN is not set. Please set the TOKEN environment variable.")
    raise ValueError("TOKEN is not set.")

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['version'])
def send_version(message):
    bot.reply_to(message, 'created by WIPEOFFS')
    logger.info(f"User {message.from_user.username} ({message.from_user.id}) sent: {message.text}")


@bot.message_handler(commands=['apod'])
def send_apod(message):
    explanation, image_url, hd_image_url = fetch_nasa_apod()
    response = f"`{explanation}`\n\n[URL]({image_url})\n[HD URL]({hd_image_url})"
    bot.reply_to(message, response, parse_mode='Markdown')


@bot.message_handler(func=lambda message: True)
def log_message(message):
    logger.info(f"Received message from {message.from_user.username} ({message.from_user.id}): {message.text}")


if __name__ == '__main__':
    logger.info("Bot is starting...")
    bot.polling(none_stop=True)
