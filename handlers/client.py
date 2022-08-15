from bot_telegram.py import dp, bot

@dp.message_handler(commands=['start' , 'help']
async def command_start(message : type.Messsge):
    try:
        await bot.send_message(message.from_user.id, 'Добро пожаловать. \n Работа с ботом началась.'
        await message.delete()
    except:
        await message.reply('Вы не добавились к боту, напишите ему:\n https://t.me/tg_tests_1008_bot')
                               
@dp.message_handler(commands=['Режим работы'])
async def command_pizza_open(message : type.Message):
    await bot.send_message(message.from_user.id, 'Временно не работаем')
                           
@dp.message_handler(commands=['Расположение'])
async def command_pizza_open(message : type.Message):
    await bot.send_message(message.from_user.id, 'ул. Строителей 7')
