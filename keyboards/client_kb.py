from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

btn_Opening_hour = KeyboardButton('/Режим_работы')
btn_Pizzeria_Location = KeyboardButton('/Расположение')
btn_Menu = KeyboardButton('/Меню')
btn_User_Phone_Number = KeyboardButton('Поделится номером', request_contact=True)
btn_User_Location = KeyboardButton('Отправить где я', request_location=True)
#btn_ = KeyboardButton('')

# ReplyKeyboardMarkup - класс замещает стандартную клавиатуру
# 	one_time_keyboard=True - параметр прячет клавиатуру, после нажатия на любую из кнопок и выводит стандартную
kb_Client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

# add - добавляет кнопку с новой строки
# insert - добавляет кнопки в свободое пространство
# row - добавляет кнопки в одну строку
#kb_Client.add(btn_Opening_hour).add(btn_Pizzeria_Location).add(btn_Menu)
#kb_Client.add(btn_Opening_hour).add(btn_Pizzeria_Location).insert(btn_Menu)
#kb_Client.row(btn_Opening_hour, btn_Pizzeria_Location, btn_Menu)
kb_Client.add(btn_Opening_hour).row(btn_Pizzeria_Location, btn_Menu).row(btn_User_Phone_Number,btn_User_Location)