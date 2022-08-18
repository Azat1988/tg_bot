from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import os

storage = MemoryStorage()

#bot = Bot(token=os.getenv('TOKEN'), proxy=os.getenv('HTTP_PROXY_TG'))
bot = Bot(token=os.getenv('TOKEN'))
#bot = Bot(token='5562475997:AAE9ID-AKZDbbBMkQ9YYCGSvoIruwTXzMnA', proxy='http://10.22.1.135:3128')
dp = Dispatcher(bot, storage = storage)
