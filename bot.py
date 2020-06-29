import telebot
import config

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Данный бот определяет отправили ему текст или фотографию")


@bot.message_handler(content_types=['text'])
def echo_text(message):
    bot.reply_to(message, 'Это текст')


@bot.message_handler(content_types=['photo'])
def echo_img(message):
    bot.reply_to(message, 'Это картинка')


@bot.message_handler(content_types=['document'])
def echo_document(message):
    bot.reply_to(message, 'Это документ')


bot.polling()
