from funk import *

@bot.message_handler(content_types=['text'])
def getTextMessages(message):
    if message.text.lower() == "/start":
        startMenu(message)


bot.polling(none_stop=True, interval=0)