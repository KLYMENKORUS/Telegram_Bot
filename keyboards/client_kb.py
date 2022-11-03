from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_1 = KeyboardButton('Режим работы')
kb_2 = KeyboardButton('Расположение')
kb_3 = KeyboardButton('Меню')
# kb_4 = KeyboardButton('Поделиться номером', request_contact=True)
# kb_5 = KeyboardButton('Отправить где я', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.add(kb_1)
kb_client.row(kb_2, kb_3)
# kb_client.row(kb_4, kb_5)

