from aiogram import types, Dispatcher
from create_bot import dp

import json, string

#@dp.message_handler()
async def echo_send(message : types.Message):
#Проверка собщения по какому-либо словарю. В данном случаем проверка на мат.
    if {i.lower().translate(str.maketrans('','',string.punctuation)) for i in message.text.split(' ')}\
       .intersection(set(json.load(open('dict/cenz_dict.json')))) != set():
        await message.reply('Маты запрещены')
        await message.delete()
	
    # ответ туда куда было написано сообщение
    #await message.answer (message.text)
    # ответ с указанием сообщения на которое отвечаем
    #await message.reply (message.text)
    # ответ в личку
    #await bot.send_message(message.from_user.id, message.text)

def register_handlers_other(dp : Dispatcher):
	dp.register_message_handler(echo_send)
