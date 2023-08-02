from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

button1 = KeyboardButton("/help")
button2 = KeyboardButton("/work_time")
button3 = KeyboardButton("/location")
button4 = KeyboardButton("Поделиться номером", request_contact=True)
button5 = KeyboardButton("Отправить мое местоположение", request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.add(button1).add(button2).add(button3).row(button4).row(button5)
