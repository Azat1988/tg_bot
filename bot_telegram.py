from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os

bot = Bot(token=os.getenv('TOKEN'), proxy=os.getenv('HTTP_PROXY_TG'))
#bot = Bot(token='5562475997:AAE9ID-AKZDbbBMkQ9YYCGSvoIruwTXzMnA', proxy='http://10.22.1.135:3128')
dp = Dispatcher(bot)

@dp.message_handler()
async def echo_send(message : types.Message):
    # ответ туда куда было написано сообщение
    #await message.answer (message.text)
    # ответ с указанием сообщения на которое отвечаем
    #await message.reply (message.text)
    # ответ в личку
    await bot.send_message(message.from_user.id, message.text)

executor.start_polling(dp, skip_updates=True)
