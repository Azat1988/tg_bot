from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_Client
from aiogram.types import ReplyKeyboardRemove
from db import sqlite_db

#@dp.message_handler(commands=['start' , 'help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Добро пожаловать.\nРабота с ботом началась.', reply_markup=kb_Client)
        await message.delete()
    except:
        await message.reply('Вы не добавились к боту, напишите ему:\nhttps://t.me/tg_tests_1008_bot')
                               
#@dp.message_handler(commands=['Режим_работы'])
async def command_pizza_open(message : types.Message):
    await bot.send_message(message.from_user.id, 'Временно не работаем')
                           
#@dp.message_handler(commands=['Расположение'])
# ReplyKeyboardRemove() -удаляет клавиатуру созданную нами
async def command_pizza_place(message : types.Message):
    await bot.send_message(message.from_user.id, 'ул. Строителей 7', reply_markup=ReplyKeyboardRemove())

#@dp.message_handler(commands=['Меню'])
async def command_menu(message : types.Message):
    await sqlite_db.sql_read(message)
	

def register_handlers_client(dp : Dispatcher):
	dp.register_message_handler(command_start, commands=['start' , 'help'])
	dp.register_message_handler(command_pizza_open, commands=['Режим_работы'])
	dp.register_message_handler(command_pizza_place, commands=['Расположение'])
	dp.register_message_handler(command_menu, commands=['Меню'])
