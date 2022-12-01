import aioschedule
from aiogram import types, Dispatcher
from config import bot
import asyncio

async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await message.answer('Ok!')

async def progulka():
    await bot.send_message(chat_id=chat_id, text="Go for a walk bro!")

async def sleep():
    photo = open('media/sleep.webp', 'rb')
    await bot.send_photo(chat_id=chat_id, photo=photo, caption="Good night bro!")

async def shade():
    aioschedule.every().day.at('19:00').do(progulka)
    aioschedule.every().day.at('23:00').do(sleep)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)

def register_handlers_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id, lambda word: 'remind' in word.text)