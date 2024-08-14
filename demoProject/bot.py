
import telebot

# Ваш токен, полученный от BotFather
TOKEN = '7254319323:AAGu_wTsQoA5xLvqto6RewJqfSwlku-zdo4'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['version'])
def send_version(message):
    bot.reply_to(message, 'created by WIPEOFFS')


if __name__ == '__main__':
    bot.polling(none_stop=True)