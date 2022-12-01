from aiogram import Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database.bot_db import sql_command_random
from keyboards.client_cb import start_markup
from config import bot, dp
from random import choice
from parser import animations


async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id, (
        f"Саламу алейкум {message.from_user.first_name}!"
    ))

async def mem(message: types.Message):
    mem1 = open("media/haha.webp", "rb")
    mem2 = open("media/ooo.webp", "rb")
    mem3 = open("media/mmeeemmms.webp", "rb")
    mems = [mem1, mem2, mem3]
    photo = choice(mems)
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)

async def quiz1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton("NEXT" ,callback_data="button1")
    markup.add(button1)
    question = "Year of release of the programming language Python?"
    answer = [
        "1885",
        "1991",
        "2002",
        "1981",
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type="quiz",
        correct_option_id=1,
        reply_markup=markup
    )

async def get_random_user(message: types.Message):
    await sql_command_random(message)

async def parser_projects(message: types.Message):
    items = animations.parser()
    for item in items:
        await message.answer(
            f"{item['link']}\n\n"
            f"{item['title']}\n"
            f"{item['info']}\n"
        )

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=["start"])
    dp.register_message_handler(mem, commands=["mem"])
    dp.register_message_handler(quiz1, commands=["quiz"])
    dp.register_message_handler(get_random_user, commands=['get'])
    dp.register_message_handler(parser_projects, commands=['parser'])
