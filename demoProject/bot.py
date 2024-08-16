import os
import telebot

TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['version'])
def send_version(message):
    bot.reply_to(message, 'created by WIPEOFFS')


if __name__ == '__main__':
    bot.polling(none_stop=True)
