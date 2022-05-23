#simple echo bot
import telebot

#
bot = telebot.TeleBot('5130328485:AAH3afeOqvZAXHvgoNeC2zstEQRdbEuAaNk')

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Online')

@bot.message_handler(content_types=["text"])
def handler_text(message):
    bot.send_message(message.chat.id, 'echo: ' + message.text)

bot.polling(none_stop=True, interval=1)
