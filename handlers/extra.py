from aiogram import Dispatcher, types
from config import bot, dp
from random import choice

async def game_stepen_echo(message: types.Message):
    emoji = choice('⚽,''🏀,''🎲,''🎯,''🎳,''🎰')
    try:
        if message.text.startswith("game"):
            await bot.send_dice(message.chat.id, emoji=emoji)
        else:
            a = int(message.text)**2
            await bot.send_message(message.from_user.id, str(a))
    except:
        await bot.send_message(message.from_user.id, message.text)
    

# async def echo(message: types.Message):
#     try:
#         a = int(message.text)**2
#         await bot.send_message(message.from_user.id, str(a))
#     except:
#         await bot.send_message(message.from_user.id, message.text)

def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(game_stepen_echo)
    # dp.register_message_handler(echo)