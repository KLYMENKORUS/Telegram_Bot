import telebot

bot = telebot.TeleBot('5705971115:AAEtv2mXiIqDyBBQsU6jOz0qdlVwvsV9rCU')


@bot.message_handler(commands=['start'])
def start(message):
    if message.from_user.last_name == None:
        message_user = f'Hello, <b>{message.from_user.first_name}</b>'
        bot.send_message(message.chat.id, message_user, parse_mode='html')
    else:
        message_user1 = f'Hello, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
        bot.send_message(message.chat.id, message_user1, parse_mode='html')


bot.polling(none_stop=True)
