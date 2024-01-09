# 1 задание из 2 блока (Бэкенд-разработка)

В данном проекте выполнено только 1 задание из 2 блока
## Задание #
> Написать телеграмм-бота, используя библиотеку `pyTelegramBotApi`, который отображает комикс для пользователя. Бот должен предлагать пользователю выбор одного из нескольких доступных комиксов (хотя бы 3 штуки). Каждый комикс должен содержать не менее 5 «слайдов» (1 слайд = 1 картинка). При открытии диалога с ботом, пользователь может запустить бота командой `/start`. При запуске бот сообщает пользователю информацию о доступных комиксах и предлагает выбор, какой из них пользователь хочет почитать. Выбор комикса происходит путём нажатия на кнопку выбора комикса. После выбора комикса бот присылает пользователю первую страницу и добавляет кнопки «вперёд», «назад» и «в начало». Кнопки «вперёд» и «назад» переключают страницу комикса. Кнопка «в начало» возвращает пользователя к этапу выбора.

## Запуск проекта #
В файле `funk.py` в 4 строке необходимо **указать токен** своего телеграм-бота

### Небольшое пояснение 
```python
@bot.message_handler(content_types=['text'])
def getTextMessages(message):
    if message.text.lower() == "/start":
        startMenu(message)
```
Команда `/start` была реализована намеренно через `content_types=['text']`, а не через `commands=['start']`.
