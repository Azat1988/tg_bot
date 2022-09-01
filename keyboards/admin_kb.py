from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


btn_load = KeyboardButton('/Загрузить')
btn_delete = KeyboardButton('/Удалить')

kb_admin = ReplyKeyboardMarkup(resize_keyboard=True).insert(btn_load).insert(btn_delete)