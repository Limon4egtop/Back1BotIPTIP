from FakeDataBase import *
import telebot

bot = telebot.TeleBot("BOT TOKEN")


@bot.callback_query_handler(func=lambda call: call.data == "backToMenu")
def mainMenu(call):
    bot.send_message(call.message.chat.id, "Выберите комикс", reply_markup=generateMenuButton())


def startMenu(message):
    bot.send_message(message.chat.id, "Выберите комикс", reply_markup=generateMenuButton())

def generateMenuButton():
    markupInline = telebot.types.InlineKeyboardMarkup()
    markupInline.row(telebot.types.InlineKeyboardButton(text="Лисы 🦊", callback_data='comics1'))
    markupInline.row(telebot.types.InlineKeyboardButton(text="Снежное утро 🌅", callback_data='comics2'))
    markupInline.row(telebot.types.InlineKeyboardButton(text="Птицы 🐤", callback_data='comics3'))
    return markupInline

@bot.callback_query_handler(func=lambda call: call.data[:-1] == "comics")
def startComics(call):
    bot.send_photo(call.message.chat.id,
                   photo=getComicsPage(int(call.data[-1]) - 1, 0),
                   reply_markup=generateComicsMenu(call.data[-1], 0))

@bot.callback_query_handler(func=lambda call: call.data[:8] == "openPage")
def nextComicsPage(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)
    comicsId, pageId = map(int, call.data[8:].split("p"))
    bot.send_photo(call.message.chat.id,
                   photo=getComicsPage(comicsId-1, pageId),
                   reply_markup=generateComicsMenu(comicsId, pageId))

def generateComicsMenu(comicsId, pageNumber):
    markupInline = telebot.types.InlineKeyboardMarkup()
    if pageNumber != 0:
        firstButton = telebot.types.InlineKeyboardButton(text=f"❮ {str(pageNumber)}",
                                                            callback_data=f'openPage{str(comicsId)}p{str(pageNumber-1)}')
    else:
        firstButton = telebot.types.InlineKeyboardButton(text="|", callback_data="backToMenu")

    centerButton = telebot.types.InlineKeyboardButton(text=f"{str(pageNumber+1)} / {str(getComicsLen(comicsId))}",
        callback_data="Null")
    if pageNumber+1 != getComicsLen(comicsId):
        lastButton = telebot.types.InlineKeyboardButton(text=f"{str(pageNumber+2)} ❯",
                                                            callback_data=f"openPage{str(comicsId)}p{str(pageNumber+1)}")
    else:
        lastButton = telebot.types.InlineKeyboardButton(text="|", callback_data="backToMenu")
    markupInline.row(firstButton, centerButton, lastButton)
    markupInline.add(telebot.types.InlineKeyboardButton(text="В начало", callback_data='backToMenu'))
    return markupInline
